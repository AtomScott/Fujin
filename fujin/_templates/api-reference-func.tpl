---
title: {{ module }}.{{ name }}
layout: default
parent: API Reference
nav_order: 1
---

# {{ name }}

## *Function* {{ module }}.{{ name }}
{{ data['Signature'] }}


{% for section in sections %}{% set param_list = data[section] %}
{% if param_list|length > 0 %}
| {{ section }} |   |   |
| - | - | - | - |
{% for param in param_list %}
|   | {{ param.name }} : {{ param.int }} | {{ '.'.join(param.desc) }} |
{% endfor %}   
{% endif %}{% endfor %}

{% if data['See also'] > 0 %}
<div>
**See also**
{{ '.'.join(data['See also']) }}
</div>
{% endif %}

{% if data['Warning'] > 0 %}
<div>
**See also**
{{ '\n'.join(data['Warning']) }}
</div>
{% endif %}


{% for note in notes %}{% set note_list = data[note] %}
{% if note_list|length > 0 %}
### {{ note }}
---
{{ '.'.join(note_list) }}
{% endif %}{% endfor %}

{% if data['Examples'] > 0 %}
### Examples
---
{% for text, code in data['Examples'] %}
{{ text }}
```python
{{ code }}
```
{% endfor %}
{% endif %}