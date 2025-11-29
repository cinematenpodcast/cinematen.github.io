---
layout: ../layouts/WatermarkLayout.astro
title: "Watermark Workaround Tutorial"
slug: watermark_remover
date: 2024-03-15
summary: "Tutorial on how to remove watermarks."
thumbnail: ""
---

# How to remove the Nano Banana watermark star

_Please use this information ethically and responsibly. Note that removing visible watermarks does not remove embedded metadata or technologies like SynthID, AI provenance is maintained for transparency reasons._

### Step 1

Go to [aistudio.google.com](https://aistudio.google.com) and login using a google account.

![aistudio UI](https://www.cinematen.be/images/watermark_remover/aistudio-screenshot.webp)


### Step 2

Generate an image using Nano Banana. This is our BEFORE example. As you can see there is a little white star watermark in the corner. You could now download that image and use Photoshop te try and remove it. Or you can be smart and just continue this tutorial!

![A generated image](https://www.cinematen.be/images/watermark_remover/nano-banana-screenshot-1.webp)

_To use the PRO version you have to have a Google Cloud Project with Billing enabled. But the normal version is still free off charge and has no generation limits._


### Step 3

Go to [Requestly.com](https://requestly.com/). There you can choose to install it as an extension on Chrome or install it systemwide.


### Step 4

When installed, open the [Requestly dashboard.](https://app.requestly.io/)
There click the **Rules** tab.

![Click the Rules tab](https://www.cinematen.be/images/watermark_remover/requestly-screenshot-1.webp)

### Step 5

Let's add a **New Rule**.

![Click New Rule](https://www.cinematen.be/images/watermark_remover/requestly-screenshot-2.webp)


### Step 6

Add a **Cancel Request** rule.

![Click Cancel Request rule categorie](https://www.cinematen.be/images/watermark_remover/requestly-screenshot-3.webp)


### Step 7

Here fill in the url: https://www.gstatic.com/aistudio/watermark/watermark_v4.png

Then click **Save Rule**.

![Add URL and Save Rule](https://www.cinematen.be/images/watermark_remover/requestly-screenshot-4.webp)


### Step 8

And that's it! You're done.

Restart your browser and go have a look at the previously generated image. As you can see the little white star is now gone.

![The watermark is gone](https://www.cinematen.be/images/watermark_remover/nano-banana-screenshot-2.webp)

