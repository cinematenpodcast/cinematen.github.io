// Import necessary packages
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import pagefind from "astro-pagefind";

// Export the combined configuration
export default defineConfig({

  // Define routes for dynamic pagination
  routes: [
    {
      // Define dynamic route for news pagination
      pattern: '/nieuws/page/:page',
      // Add any specific setup if needed
    },
    {
      // Define dynamic route for reviews & blogs pagination
      pattern: '/reviews&blogs/page/:page',
      // Add any specific setup if needed
    }
  ],

  // Integrations section
  integrations: [
    mdx(),
    pagefind(),
  ],
});