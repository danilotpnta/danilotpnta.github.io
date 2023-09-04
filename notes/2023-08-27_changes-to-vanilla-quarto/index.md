---
title: "Changes to Vanilla Quarto"
description: "Description of this Note"
date: "2023-08-27"
categories: [All, TAGS]
number-sections: true
toc: false
---

## Find Styles Code Highlighting
- Pandoc highlight styles: `/Applications/quarto/share/pandoc/highlight-styles`

## Changes the moon icon

- Change toggle-icons: `/Applications/quarto/share/formats/html/bootstrap/\_bootstrap-rules.scss`
- `/Users/datoapanta/Desktop/danilotpnta.github.io/docs/site_libs/bootstrap/bootstrap-dark.min.css`
- I change the SVG from this site: `https://icons.getbootstrap.com/icons/moon/`


<details>
<summary>Copy this</summary>

```css
// .navbar .quarto-color-scheme-toggle:not(.alternate) .bi::before {
//   background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#{colorToRGBA($navbar-light-color)}" class="bi bi-toggle-off" viewBox="0 0 16 16"><path d="M11 4a4 4 0 0 1 0 8H8a4.992 4.992 0 0 0 2-4 4.992 4.992 0 0 0-2-4h3zm-6 8a4 4 0 1 1 0-8 4 4 0 0 1 0 8zM0 8a5 5 0 0 0 5 5h6a5 5 0 0 0 0-10H5a5 5 0 0 0-5 5z"/></svg>');
// }

// Toggle MOON
.navbar .quarto-color-scheme-toggle:not(.alternate) .bi::before {
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#{colorToRGBA($navbar-light-color)}" class="bi bi-toggle-off" viewBox="0 0 16 16"><path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278zM4.858 1.311A7.269 7.269 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.316 7.316 0 0 0 5.205-2.162c-.337.042-.68.063-1.029.063-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286z"/></svg>');
}

// Toggle MOON filled
// .navbar .quarto-color-scheme-toggle.alternate .bi::before {
//   background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#{colorToRGBA($navbar-light-color)}" class="bi bi-toggle-on" viewBox="0 0 16 16"><path d="M5 3a5 5 0 0 0 0 10h6a5 5 0 0 0 0-10H5zm6 9a4 4 0 1 1 0-8 4 4 0 0 1 0 8z"/></svg>');
// }

.navbar .quarto-color-scheme-toggle.alternate .bi::before {
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#{colorToRGBA($navbar-light-color)}" class="bi bi-toggle-on" viewBox="0 0 16 16"><path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"/></svg>');
}
```

</details>


## Changes title of "Categories" to "All Categories" 

- `/Applications/quarto/bin/quarto.js`

Copy this:

```js
// headingEl.innerText = localizedString(format, kListingPageFieldCategories);
headingEl.innerText = "All Categories";
```

## Remove the "All" from "Categories" Sidebar

- `/Applications/quarto/bin/quarto.js`

Copy this:

```js
const allCategory = localizedString(format, kListingPageCategoryAll);
// const allEl = categoryElement(doc, allCategory, formatFn(allCategory, totalCategories), "");
```

## Adds extra feature to the headerOffset function 

- If the header is absolute then the header.height will be zero to fix the TOC
- `/Applications/quarto/share/projects/website/navigation/quarto-nav.js`


<details>
<summary>Copy this</summary>


```js
// function headerOffset() {
//   // Set an offset if there is are fixed top navbar
//   const headerEl = window.document.querySelector("header.fixed-top");
//   if (headerEl) {
//     return headerEl.clientHeight;
//   } else {
//     return 0;
//   }
// }

function headerOffset() {
  // Set an offset if there is are fixed top navbar
  const headerEl = window.document.querySelector("header.fixed-top");
  if (headerEl) {
    // If the page is a blog post then return the height as 0
    const blogSection = window.document.querySelector("header.blog-page");
    if (blogSection) {
      // Add extra padding to display well the navbar
      document.getElementById(
        "quarto-content"
      ).style.paddingTop = `${headerEl.clientHeight}px`;
      // returns 0 to fix the TOC where it displays the section
      return 0;
    } else {
      return headerEl.clientHeight;
    }
  } else {
    return 0;
  }
}
```

</details>
