---
title: "How to generate a Project Directory Tree"
description: "Description of this Note"
date: "2024-06-09T14:28:19"
categories: [All, TAGS]
year: "2024"
toc: false
---
Expected outcome:

```bash 
.
├── environmet.yml
├── README.md
├── .gitignore
└── src
    ├── datasets
    │   └── constants.py
    ├── train.py
    └── utils
        ├── CLIP_encoder.py
        └── __init__.py

5 directories, 5 files
```

To accomplish this

```bash
brew install tree
cd project/
```

To print the working directory with specific depth:

```bash
tree -L 2
```

To avoid some directories being printed
```bash
tree -I 'venv|node_modules'
```


