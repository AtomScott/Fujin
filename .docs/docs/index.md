---
layout: post
title: Home
nav_order: 1
---

# Fujin (*foo-jin*)

## Introduction

Fujin is a helper package written in python, to help me make simple docs and project pages from python **packages** and **jupyter notebooks**.


## Motivation
After a few years of programming with python, I found myself in need making repos the following style:
(Disclaimer: I mostly do data science work)---
layout: post
title: Home

---


```
+-- Root
|   +-- my_pkg
|       +-- __init__.py
|       +-- module1.py
|       +-- sub_pkg
|       +-- etc.
|   +-- notebooks
|       +-- notebook1.ipynb
|       +-- etc.
|   +-- tests
|   +-- docs
|   +-- data
```

Where my_pkg consists of large blocks of "good" code I use in repeatedly in jupyter notebooks. The jupyter notebooks is where I do most of the research and exploratory programming. I use %autoreload a lot.

Since I don't document the tests, if there was a solution to make nice documents from just `my_pkg` and `notebooks`, I thought it would be very useful.

Thats what Fujin is suposed to take care of. 

Have a look in the docs folder of Fujin on github. You might be suprised of how little there is. There is very little code in docs directory because we levarge github pages. With github pages, we can make beautifully themed webpages by simply adding `remote_theme: owner/name` to `_config.yml`.

It's super minimal, so there is a lot you can control!

## What does it do?

Run 

```
fujin -i Fujin notebooks -o docs/docs
```

This coverts all docstrings in the .py files (exlcuding `__init__.py` etc.) found under ./Fujin into .md files and all .ipynb files found under ./notebooks into .md files.

It's just super simple!

## Customization

Add additional styles into docs to get to change colors and stuff if you want.

## Todo

- [ ] automatically add links to docs.