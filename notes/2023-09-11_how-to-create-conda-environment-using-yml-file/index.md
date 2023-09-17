---
title: "How to create Conda environment using YML file?"
description: "Description of this Note"
date: "2023-09-11"
categories: [All, Environment, TAGS, Conda]
number-sections: true
toc: false
---

## Define YML requirements
For instance the following file: `environment.yml`

```yml
name: cv1
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.7
  - pip=21.3.1
  - pip:
    - numpy==1.19.5
    - opencv-contrib-python==3.4.2.17
    - matplotlib==3.3.4
    - jupyter==1.0.0
    - scikit-learn==0.23.0
    - scipy==1.5.4
```

## Create Conda ENV from terminal 

```bash
conda env create -f path/to/environment.yml

```

