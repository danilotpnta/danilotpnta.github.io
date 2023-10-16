---
title: "How to embed ML application?"
description: "Example how to add ml application from gradio.app"
date: "2023-10-06"
categories: [All, TAGS]
number-sections: true
toc: false
---

## Adding the script

```html
<script type="module"
src="https://gradio.s3-us-west-2.amazonaws.com/3.36.1/gradio.js">
</script>
<gradio-app space="ForBo7/FloodDetector"></gradio-app>
```

## Styling
To avoid lines surrounding, add to `theme-light.scss` 
```css
.info.svelte-1kyws56.svelte-1kyws56 {
    display: none !important;
}

.embed-container.svelte-1kyws56.svelte-1kyws56 {
    border: none !important;
}
```