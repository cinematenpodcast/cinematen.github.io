import os
import re

def process_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Replace "+++" with "---"
    content = content.replace("+++", "---")
    
    # Replace " = " with ": "
    content = content.replace(" = ", ": ")
    
    # Replace "slug= " with "slug: "
    content = content.replace("slug=", "slug:")
    
    # Remove image at the top of the file
    lines = content.split('\n')
    new_content = ""
    found_image = False
    for line in lines:
        if line.strip().startswith("![") and line.strip().endswith(")"):
            found_image = True
        elif found_image:
            found_image = False
        else:
            new_content += line + "\n"
    
    # Delete the draft property from the headings
    new_content = re.sub(r'^#+ .*draft: (true|false)', lambda m: m.group(0).replace("draft: true", "").replace("draft: false", ""), new_content, flags=re.MULTILINE)
    
    # Add layout property below the first "---"
    layout_line = "layout: ../../layouts/NieuwsLayout.astro\n"
    new_content = re.sub(r'(?<=---\n)', layout_line, new_content, count=1)
    
    with open(file_path, 'w') as file:
        file.write(new_content)

def main():
    folder_path = "."  # Change this to the path of your folder if it's not the current directory
    
    # Get all .md files in the folder
    md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]
    
    # Process each .md file
    for md_file in md_files:
        file_path = os.path.join(folder_path, md_file)
        process_md_file(file_path)

if __name__ == "__main__":
    main()
