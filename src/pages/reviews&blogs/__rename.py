import os
import re

def sanitize_title(title):
    """Sanitizes a title to be used as a filename or URL slug."""
    title = title.lower()
    title = re.sub(r'\s+', '-', title)
    title = re.sub(r'[^\w\-]', '', title)
    return title

def rename_mdx_files():
    """Renames all the .mdx files in the current folder based on the title parameter in each file."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        mdx_files = [f for f in os.listdir(current_dir) if f.endswith('.mdx')]

        for mdx_file in mdx_files:
            mdx_file_path = os.path.join(current_dir, mdx_file)

            # Read the contents of the Markdown file
            with open(mdx_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Extract the title parameter from the header
            match = re.search(r"title:\s*'(.+?)'", content)
            if match:
                title_param = match.group(1)
                sanitized_title = sanitize_title(title_param)
                
                # Rename the Markdown file
                new_file_name = f"{sanitized_title}.mdx"
                new_file_path = os.path.join(current_dir, new_file_name)
                os.rename(mdx_file_path, new_file_path)
                print(f"Markdown file '{mdx_file}' renamed to '{new_file_path}' successfully.")
            else:
                print(f"Failed to find title parameter in '{mdx_file}'.")

    except Exception as e:
        print(f"Error renaming Markdown files: {e}")

if __name__ == "__main__":
    rename_mdx_files()
