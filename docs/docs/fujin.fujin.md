---
layout: post
title: fujin.fujin
description: >
 
Create simple docs with minimal requirements.

---





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

















#### **parse_args(** **  **)** {#signature}

Parse args From the command line#### **tester_func(** *a, b, c*  **)** {#signature}

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
