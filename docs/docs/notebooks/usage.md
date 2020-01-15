---
layout: post
nav_order: 2
parent: notebooks
---

# Sample Notebook


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload



```python
from fujin import Fujin
```


```python
package_dirs = ['fujin']
foo = Fujin(package_dirs, '', 'docs/docs')

# print discovered modules
print(foo.get_modules())

# print discovered members (functions and classes)
print(foo.get_members(['fujin.fujin']))

# print discovered objs as doc objs
print(foo.get_docs())
print(foo.docs)
```

    ['fujin.fujin']
    ['fujin.fujin.Fujin', 'fujin.fujin.parse_args', 'fujin.fujin.tester_func']
    [<numpydoc.docscrape.ClassDoc object at 0x7f4ad0da8a90>, <numpydoc.docscrape.FunctionDoc object at 0x7f4ad0da85c0>, <numpydoc.docscrape.FunctionDoc object at 0x7f4ad0da8710>]
    [<numpydoc.docscrape.ClassDoc object at 0x7f4ad0db2668>, <numpydoc.docscrape.FunctionDoc object at 0x7f4ad0da84e0>, <numpydoc.docscrape.FunctionDoc object at 0x7f4ad0dbcb38>]



```python
# print members of fujin.fujin
print(foo.get_members(['fujin.fujin']))
```

    ['fujin.fujin.Fujin', 'fujin.fujin.parse_args', 'fujin.fujin.tester_func']



```python
print(foo.get_doctext(foo.docs[0]))
```

    
    
    
    
    Returns the obj of members of the modules in a Fujin obj
    ##### Parameters {#section}
    
    <dl>
    <dt markdown='1'>`modules` : *list*
    </dt>
    	<dd markdown='1'> A list of modules to  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'>  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'>  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'> A list of objs. 
    </dd>
    
    </dl>
    
    
    
    
    
    Returns the path of members of the modules in a Fujin obj
    ##### Parameters {#section}
    
    <dl>
    <dt markdown='1'>`modules` : *list*
    </dt>
    	<dd markdown='1'> A list of modules to  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'>  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'>  
    </dd>
    
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'> A list of paths. paths are joined by a '.' instead of `os.sep`. 
    </dd>
    
    </dl>
    
    
    
    Returns the modules in a Fujin obj.
    Finds the modules found in a given list of directories. 
    ##### Parameters {#section}
    
    <dl>
    <dt markdown='1'>`package_list` : *List*
    </dt>
    	<dd markdown='1'> A list of paths to each package.Insert `None` to find all modules in the current working directory. 
    </dd>
    
    </dl>
    
    ##### Returns {#section}
    
    <dl>
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'> A list of module paths, joined by a '.' instead of `os.sep`. 
    </dd>
    
    </dl>
    
    ##### Examples {#block-header}
    ~~~python
    >>> foo = fujin.Fujin(['fujin'])
    >>> print(foo.get_modules())
    ['fujin.fujin']
    ~~~
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



```python
print(foo.get_doctext(foo.docs[1]))
```

    #### **parse_args(** **  **)** {#signature}
    
    Parse args From the command line



```python
print(foo.get_doctext(foo.docs[2]))
```

    #### **tester_func(** *a, b, c*  **)** {#signature}
    
    Func to test fujin functionality
    ##### Parameters {#section}
    
    <dl>
    <dt markdown='1'>`a` : *int*
    </dt>
    	<dd markdown='1'> variable a 
    </dd>
    
    <dt markdown='1'>`b` : *int*
    </dt>
    	<dd markdown='1'> variable b 
    </dd>
    
    <dt markdown='1'>`c` : *int*
    </dt>
    	<dd markdown='1'> variable c 
    </dd>
    
    </dl>
    
    ##### Returns {#section}
    
    <dl>
    <dt markdown='1'>` ` : **
    </dt>
    	<dd markdown='1'> a+b+c 
    </dd>
    
    </dl>
    



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
