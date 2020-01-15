---
title: {{ module }}.{{ name }}
layout: post
parent: API Reference
nav_order: 1
---

# {{ name }}

## *Function* {{ module }}.{{ name }}
{{ data['Signature'] }}

<table>
{% for section in sections %}
{% set param_list = data[section] %}
{% if param_list|length > 1 %}
<tr>
    <th rowspan={{param_list|length}}>{{ section }}</th>
</tr>
{% for param in param_list %}
<tr>
    <th>{{ param.name }} : {{ param.int }}</th>
    <td>
        <dl>
            <dd>
            <div markdown='1'>
            {{ '.'.join(param.desc) }}
            </div>
            </dd>
        </dl>
    </td>
</tr>
{% endfor %}   
{% endif %}
{% endfor %}
</table>  
