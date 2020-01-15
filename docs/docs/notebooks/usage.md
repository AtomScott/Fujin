---
title: Sample Notebook
layout: post
nav_order: 1
parent: Notebooks
---
# Sample Notebook


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


This notebook assumes that the following packages are already imported.


```python
from fujin import Fujin
from jinja2 import Environment, FileSystemLoader
```

Check whether the current working directory is correct.


```python
import os

if os.path.basename(os.getcwd())!='Fujin':
    os.chdir('../')
assert os.path.basename(os.getcwd())=='Fujin', os.getcwd()
```


```python
package_dirs = ['fujin']
foo = Fujin(package_dirs, '', 'docs/docs/API-Reference')

# print discovered modules
print(foo.get_modules())

# print discovered members (functions and classes)
print(foo.get_members(['fujin.fujin']))

# print discovered objs as doc objs
print(foo.docs)
```

    ['fujin.example', 'fujin.fujin']
    ['fujin.fujin.Fujin', 'fujin.fujin.parse_args', 'fujin.fujin.tester_func']
    [<numpydoc.docscrape.FunctionDoc object at 0x7fab15b9f400>, <numpydoc.docscrape.ClassDoc object at 0x7fab046f4cc0>, <numpydoc.docscrape.FunctionDoc object at 0x7fab0471dc88>, <numpydoc.docscrape.FunctionDoc object at 0x7fab042e76a0>]


A Function/Class doc object contains all the information that can be found in the respective function/class docstring. Please note that the docstring must be written in [Numpy Style](https://numpydoc.readthedocs.io/en/latest/format.html). 

Let's print a sample of the docs below.


```python
doc_obj = foo.docs[0]
print(doc_obj)
```

    .. function:: foo
        
    
    foo(var1, var2, long_var_name='hi')
    
    Summarize the function in one line.
    
    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.
    
    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    
    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.
    type_without_description
    
    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation
    common_parameters_listed_above : type
        Explanation
    
    Raises
    ------
    BadException
        Because you shouldn't have done that.
    
    See Also
    --------
    
    :func:`numpy.array`
        Relationship (optional).
    :func:`numpy.ndarray`
        Relationship (optional), which could be fairly long, in which case the line wraps here.
    :func:`numpy.dot`, :func:`numpy.linalg.norm`, :func:`numpy.eye`
        ..
    
    Notes
    -----
    Notes about the implementation algorithm (if needed).
    
    This can have multiple paragraphs.
    
    You may include some math:
    
    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
    
    And even use a Greek symbol like :math:`\omega` inline.
    
    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.
    
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.
    
    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.
    
    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b
    


Numpy doc parses this data into a dictionary for us automatically. It is stored in `doc._parsed_data`.


```python
doc_obj._parsed_data
```




    {'Signature': "foo(var1, var2, long_var_name='hi')",
     'Summary': ['Summarize the function in one line.'],
     'Extended Summary': ['Several sentences providing an extended description. Refer to',
      'variables using back-ticks, e.g. `var`.'],
     'Parameters': [Parameter(name='var1', type='array_like', desc=['Array_like means all those objects -- lists, nested lists, etc. --', 'that can be converted to an array.  We can also refer to', 'variables like `var1`.']),
      Parameter(name='var2', type='int', desc=['The type above can either refer to an actual Python type', '(e.g. ``int``), or describe the type of the variable in more', 'detail, e.g. ``(N,) ndarray`` or ``array_like``.']),
      Parameter(name='long_var_name', type="{'hi', 'ho'}, optional", desc=['Choices in brackets, default first when optional.'])],
     'Returns': [Parameter(name='', type='type', desc=['Explanation of anonymous return value of type ``type``.']),
      Parameter(name='describe', type='type', desc=['Explanation of return value named `describe`.']),
      Parameter(name='out', type='type', desc=['Explanation of `out`.']),
      Parameter(name='', type='type_without_description', desc=[])],
     'Yields': [],
     'Receives': [],
     'Raises': [Parameter(name='', type='BadException', desc=["Because you shouldn't have done that."])],
     'Warns': [],
     'Other Parameters': [Parameter(name='only_seldom_used_keywords', type='type', desc=['Explanation']),
      Parameter(name='common_parameters_listed_above', type='type', desc=['Explanation'])],
     'Attributes': [],
     'Methods': [],
     'See Also': [([('numpy.array', None)], ['Relationship (optional).']),
      ([('numpy.ndarray', None)],
       ['Relationship (optional), which could be fairly long, in',
        'which case the line wraps here.']),
      ([('numpy.dot', None), ('numpy.linalg.norm', None), ('numpy.eye', None)],
       [])],
     'Notes': ['Notes about the implementation algorithm (if needed).',
      '',
      'This can have multiple paragraphs.',
      '',
      'You may include some math:',
      '',
      '.. math:: X(e^{j\\omega } ) = x(n)e^{ - j\\omega n}',
      '',
      'And even use a Greek symbol like :math:`\\omega` inline.'],
     'Warnings': [],
     'References': ['Cite the relevant literature, e.g. [1]_.  You may also cite these',
      'references in the notes section above.',
      '',
      '.. [1] O. McNoleg, "The integration of GIS, remote sensing,',
      '   expert systems and adaptive co-kriging for environmental habitat',
      '   modelling of the Highland Haggis using object-oriented, fuzzy-logic',
      '   and neural-network techniques," Computers & Geosciences, vol. 22,',
      '   pp. 585-588, 1996.'],
     'Examples': ['These are written in doctest format, and should illustrate how to',
      'use the function.',
      '',
      '>>> a = [1, 2, 3]',
      '>>> print([x + 3 for x in a])',
      '[4, 5, 6]',
      '>>> print("a\\nb")',
      'a',
      'b'],
     'index': {}}




```python
# print(doc_obj.get_class())
dir(doc_obj), doc_obj.methods
```




    (['__abstractmethods__',
      '__class__',
      '__contains__',
      '__delattr__',
      '__dict__',
      '__dir__',
      '__doc__',
      '__eq__',
      '__format__',
      '__ge__',
      '__getattribute__',
      '__getitem__',
      '__gt__',
      '__hash__',
      '__init__',
      '__init_subclass__',
      '__iter__',
      '__le__',
      '__len__',
      '__lt__',
      '__module__',
      '__ne__',
      '__new__',
      '__reduce__',
      '__reduce_ex__',
      '__repr__',
      '__reversed__',
      '__setattr__',
      '__setitem__',
      '__sizeof__',
      '__slots__',
      '__str__',
      '__subclasshook__',
      '__weakref__',
      '_abc_impl',
      '_cls',
      '_description',
      '_doc',
      '_error_location',
      '_func_rgx',
      '_funcbacktick',
      '_funcname',
      '_funcnamenext',
      '_funcplain',
      '_is_at_section',
      '_is_show_member',
      '_line_rgx',
      '_mod',
      '_parse',
      '_parse_index',
      '_parse_param_list',
      '_parse_see_also',
      '_parse_summary',
      '_parsed_data',
      '_read_sections',
      '_read_to_next_section',
      '_role',
      '_str_extended_summary',
      '_str_header',
      '_str_indent',
      '_str_index',
      '_str_param_list',
      '_str_section',
      '_str_see_also',
      '_str_signature',
      '_str_summary',
      '_strip',
      'empty_description',
      'extra_public_methods',
      'get',
      'items',
      'keys',
      'methods',
      'properties',
      'sections',
      'show_inherited_members',
      'values'],
     ['generate_docs',
      'get_docs',
      'get_doctext',
      'get_members',
      'get_modules',
      'get_text',
      'get_yaml',
      'ismember',
      'parse_block',
      'parse_color_block',
      'parse_methods',
      'parse_section',
      'parse_signature',
      'parse_text'])




```python
file_loader = FileSystemLoader('fujin/_templates')
env = Environment(
    loader=file_loader,
    trim_blocks=True,
    lstrip_blocks=True
)
template = env.get_template(
    'api-reference-func.tpl', 
    )
output = template.render(
    name=doc_obj.get_func()[1],
    module=doc_obj.get_func()[0].__module__,
    data=doc_obj,
    sections=['Parameters', 'Returns', 'Yields', 'Receives', 'Raises', 'Warns', 'Other Parameters']
    )

with open("./docs/docs/API-Reference/Output.md", "w+") as f:
    f.write(output)
```


```python
# List of paths packages
args = parse_args()
package_dirs = args.input_dirs
out_dir = args.out_dir

assert args.overwrite == os.path.exists(out_dir), \
    "{0}".format('Path does not exist' if args.overwrite else 'Not given permission to overwrite')

if args.overwrite: shutil.rmtree(out_dir)        
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-82-6dec234c90ab> in <module>()
          1 # List of paths packages
    ----> 2 args = parse_args()
          3 package_dirs = args.input_dirs
          4 out_dir = args.out_dir
          5 


    NameError: name 'parse_args' is not defined



```python
for module in get_package_contents(package_dirs):
    print(str(module))
    
    file_path = os.path.join(out_dir, args.prefix + module + args.suffix + '.md')
    os.makedirs(out_dir, exist_ok=True)

    

    
        intro_txt = 'Writing to path {0}'.format(file_path)
        bars = '-' * len(intro_txt)
        print('\t'+bars)
        print('\t'+intro_txt)
        # write module details
        module = importlib.import_module(module)

        
        
        for name, obj in get_module_contents(module):
            print('\t {0}'.format(name))

            if isfunction(obj):
                doc = FunctionDoc(obj)
            elif isclass(obj):
                doc = ClassDoc(obj)

            # f.write(str(doc))

            s = []
            for key, item in doc._parsed_data.items():
                if item: # filter for empty collections and None
                    try: 
                        txt = generate_text(key, item)
                    except NotImplementedError as e:
                        print('\t\t Error: {0} autodoc has not been implemented yet'.format(key))
                    except KeyError as e:
                        print('\t\t Error: {0} is not Numpy style docstring'.format(key))
                    s.append(txt)
            
            s.insert(1,'<div class=\'desc\' markdown="1">')
            s += ['---','</div>']
            f.write('\n'.join(s))
        print('\t'+bars)

```
