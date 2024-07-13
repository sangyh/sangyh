---
author: "Sangy"
title: "It took me 5 mins to launch this site!"
draft: false
date: "2024-07-13"
description: "using Hugo, PaperMod and Netlify."
tags: ["hugo", "blog", "netlify"]
categories: ["blog", "hugo"]
series: ["Tech"]
aliases: ["quick-blogging-stack"]
cover:
  image: images/image.png
  caption: "laptop"
---

I share how I launched this Hugo site in 5 mins, invariably for my future self when I get around to doing it again after having forgetten it.

#### Setting up the blog

1. Install Hugo.
To install Hugo on macOS, I ran:
```
brew install hugo
```
For reference, here is Hugo's [quick start guide](https://gohugo.io/getting-started/quick-start/).

2. Start a new site with a yaml config using
```
hugo new site my-blog --format yaml
```

I ran this in a www folder in my root directory. This command created a new folder called my-blog with a default config.yaml file.
3. The Next step is to pick a theme. I found that PaperMod was the most popular as seen [here](https://themes.gohugo.io/themes/hugo-papermod/). I cloned the theme into my my-blog folder.
```
git clone https://github.com/nanxiaobei/hugo-paper mod
```
4. Theme installation instructions are on the github wiki page. I followed the submodule method recommended on the [wiki](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation).

5. The last step is to update the config.yaml to include the theme.
```
theme: [PaperMod] 
```
Now, running `hugo server` in the terminal will start a local server at http://localhost:1313/.

#### Deploying the blog

The first step is to create a Github repository and push the code to it.
For hosting the site, I opted for Netlify as it's free, easy to use, and automatically deploys updates with every push to the main branch.

The steps are fairly straightforward on the Netlify UI.
1. Create a new site using an existing project from Github.Authorize Netlify to access Github.
2. Next, Netlify will recognize the Hugo site and update the Build command: `hugo`
3. I had to add an environment variable for the HUGO_VERSION. This is the version of Hugo that Netlify will use to build the site. Not having this was throwing an error as it was trying to use an older version of Hugo.
4. Click deploy. 

That's it, we have a blog!  


### Next steps

- Add favicon 
These files need to be in the static folder. I placed them under static/assets/ and updated the config.yaml to include them.
```
assets:
    disableHLJS: true
    favicon: "/assets/favicon.ico"
    favicon16x16: "/assets/favicon-16x16.ico"
    favicon32x32: "/assets/favicon-32x32.ico"
    apple_touch_icon: "/assets/apple-touch-icon.png"
```
- Add a custom domain [pending]
- Add analytics [pending]
- Search engine optimization [pending]