{% extends 'markdown.tpl'%}

{%- block header -%}
---
title: {{ nb.cells[0]['source'][2:] }}
layout: default
nav_order: 2
parent: Notebooks
---
{%- endblock header -%}    
