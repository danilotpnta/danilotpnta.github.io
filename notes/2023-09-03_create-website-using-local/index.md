---
title: "Create Website using Local"
description: "Description of this Note"
date: "2023-09-03"
categories: [All, TAGS]
number-sections: true
toc: false
---

## Setting up the Terminal

First you need to have an idea to control the terminal. Look at the following link

> [Environments](/Users/datoapanta/Desktop/Notes/Environments.md)

1. Create an environment  called `web`  with python
   
   ```bash
   conda create -n web python=3.7
   ```

2. To activate the new environment
   
   ```bash
   conda activate web
   ```

3. To move terminal to website folder in Desktop:
   
   ```bash
   cd /Users/datoapanta/Desktop/website
   ```

---

## Setting up Next.js

> [Installation Guide](https://nextjs.org/learn/basics/create-nextjs-app/setup)

To kills a port

```
npx kill-port 3000
```


