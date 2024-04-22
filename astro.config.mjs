import { defineConfig } from 'astro/config';

// In astro.config.mjs or where you configure routes
import mdx from "@astrojs/mdx";

// https://astro.build/config
export default defineConfig({

  // Other configurations...
  routes: [{
    // Define dynamic route for news pagination
    pattern: '/nieuws/page/:page'
    // Your specific setup here...
  }, {
    pattern: '/reviews&blogs/page/:page'
  }],
  integrations: [mdx()]
});