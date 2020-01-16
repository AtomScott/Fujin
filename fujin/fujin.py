"""
Create simple docs with minimal requirements.
"""

import os, sys
import importlib, inspect
import argparse, shutil
from collections import defaultdict
from numpydoc.docscrape import FunctionDoc, NumpyDocString, ClassDoc
from inspect import getmembers, isfunction, isclass
from pkgutil import walk_packages
import re

from jinja2 import Environment, FileSystemLoader

from .base import Funky, Classy

import warnings
warnings.filterwarnings("ignore")

class Fujin():
    """Fujin Base class

    The Fujin class handles the nits and bits to parse Numpy Style Docstrings.
    
    Fujin does the following things for us.

    - Finds all the modules defined in a package.
    - Parses the Numpy style docstrings using the NumpyDoc package.
    - Generates a dictionaries that contain parsed docstring information.
    - Generates markdown files for each class and function with Jinja2 templates.
    
    Attributes
    ----------
    modules : 
        List of modules found in the package
    members : 
        list of members found in the package
    docs : 
        list of Numpy style docstrings found in the package

    Returns
    -------
    [type]
        [description]
    
    Raises
    ------
    NotImplementedError
        [description]
    KeyError
        [description]
    """
    def __init__(self, package_dirs, out_dir, args=defaultdict(lambda: '')):
        self.package_dirs = package_dirs
        self.modules = self.get_modules()
        self.members = self.get_members()
        self.docs = self.get_docs()
        self.args = args
        self.out_dir = out_dir

        file_loader = FileSystemLoader('fujin/_templates')
        self.env = Environment(
            loader=file_loader,
            trim_blocks=True,
            lstrip_blocks=True
        )

    def generate_docs(self):
        """Generate markdown files
        """
        for module in self.modules:
            for doc in self.docs:
                out_path = os.path.join(self.out_dir, self.args['prefix'] + module + self.args['suffix'] + '.md') # TODO
                if doc.type == 'class':
                    template = env.get_template('api-reference-class.tpl')
                elif doc.type == 'function':
                    template = env.get_template('api-reference-func.tpl')
                else:
                    raise KeyError(doc.type)
                doc.write(out_path, template)

    def get_modules(self):
        """Returns the modules in a Fujin obj.
        
        Finds the modules found in a given list of directories. 
        
        Parameters
        ----------
        package_list : List
            A list of paths to each package.
            Insert `None` to find all modules in the current working directory.

        Returns
        -------
        List
            A list of module paths, joined by a '.' instead of `os.sep`.

        Examples
        --------
        >>> foo = fujin.Fujin(['fujin'])
        >>> print(foo.get_modules())
        ['fujin.fujin']
        """

        module_list = ['.'.join([fileFinder.path,modName]) for fileFinder , modName, _ in walk_packages(self.package_dirs)]

        return module_list

    def get_members(self, modules=None):
        """Returns the path of members of the modules in a Fujin obj
        
        Parameters
        ----------
        modules : list
            A list of modules to 
        Returns
        -------
        lst
            A list of paths. paths are joined by a '.' instead of `os.sep`.
        """        
        if modules is None:
            modules = self.modules

        members = []
        for module in modules:
            module = importlib.import_module(module)
            for name, obj in getmembers(module):
                if self.ismember(obj) and obj.__module__ == module.__name__:
                    members.append('.'.join((module.__name__, name)))
        return members

    def get_docs(self, modules=None):
        """Returns the obj of members of the modules in a Fujin obj
        
        Parameters
        ----------
        modules : list
            A list of modules to 
        Returns
        -------
        lst
            A list of objs.
        """        
        if modules is None:
            modules = self.modules

        objs = []
        for module in modules:
            module = importlib.import_module(module)
            for name, obj in getmembers(module):
                if self.ismember(obj) and obj.__module__ == module.__name__:
                    if isfunction(obj):
                        objs.append(Funky(obj))
                    elif isclass(obj):
                        objs.append(Classy(obj))
        return objs

    def ismember(self, obj):
        return isfunction(obj) or isclass(obj)


# def parse_args():
#     """Parse args From the command line
#     """        
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('-o','--out_dir', default='./docs')
#     parser.add_argument('-i','--input_dirs', nargs='+', help='<Required> Set flag', required=True)
#     parser.add_argument('-x','--overwrite', action='store_true', default=False)
#     parser.add_argument('-p','--prefix', default='./docs')
#     parser.add_argument('-s','--suffix', default='')
#     args = parser.parse_args()
#     return args


# def tester_func(a,b,c):
#     """Func to test fujin functionality
    
#     Parameters
#     ----------
#     a : int
#         variable a
#     b : int
#         variable b
#     c : int
#         variable c
    
#     Returns
#     -------
#     hey
#         a+b+c
#     """    
#     return a+b+c


            
            

    #     # print(f'\t\t{inspect.getdoc(module)}')

    #     # for fname in file_list:
    #     #     if fname.endswith('.py'):   
    #     #         print(f'\t{fname}')

    #     #         module = importlib.import_module('.'.join([dir_name, fname.replace('.py', '')]))
    #     #         print(dir(module))
    #     #         if 'foo' in dir(module):
    #     #             doc = FunctionDoc(module.foo)
    #     #             print(doc._parsed_data)
    #             # print(inspect.getmembers(module, predicate=inspect.ismethod))

    #             # doc = FunctionDoc(dir(module))
    #             # print(f'\t{doc}')

    #         # doc = FunctionDoc()
    #     # Remove the first entry in the list of sub-directories
    #     # if there are any sub-directories present
    #     # if len(subdirList) > 0:
    #     #     del subdirList[0]
