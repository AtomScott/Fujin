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

import warnings
warnings.filterwarnings("ignore")

class Fujin():
    def __init__(self, package_dirs, out_dir, args=defaultdict(lambda: '')):
        self.package_dirs = package_dirs
        self.modules = self.get_modules()
        self.members = self.get_members()
        self.docs = self.get_docs()
        self.args = args
        self.out_dir = out_dir

    def generate_docs(self):
        for module in self.modules:
            out_path = os.path.join(self.out_dir, self.args['prefix'] + module + self.args['suffix'] + '.md')
            with open(out_path,"w+") as f:
                f.write(self.get_yaml(module))
                for doc in self.docs:
                    f.write(self.get_doctext(doc))


    def get_text(self, key, item):
        if key == 'Signature':
            return self.parse_signature(key, item)
        if key in ['Summary', 'Extended Summary']: 
            return self.parse_text(item)
        if key in ['Parameters', 'Returns', 'Yields', 'Receives', 'Raises', 'Warns', 'Other Parameters']:
            return self.parse_section(key, item)
        if key in ['Notes', 'Warnings', 'References', 'Examples']:
            return self.parse_block(key, item)
        if key == 'See Also': 
            return self.parse_color_block(key, item)
        if key == 'Methods': 
            return self.parse_methods(key, item)
        if key == 'index': 
            raise NotImplementedError(key, item)
        else:
            raise KeyError(key, item)

    def get_doctext(self, doc):
        doctext = []
        for key, item in doc._parsed_data.items():
            if item: # filter for empty collections and None
                try: 
                    txt = self.get_text(key, item)
                except NotImplementedError as e:
                    txt = ''
                    print('\t\t Error: {0} autodoc has not been implemented yet'.format(key))
                except KeyError as e:
                    txt = ''
                    print('\t\t Error : {0} is not Numpy style docstring'.format(key))
                doctext.append(txt)
        return '\n'.join(doctext)


    def parse_signature(self, key, item):
        match = re.match(r"(.*)\((.*)\)" ,item)
        if match:
            name, so = match.groups()
            return '#### **{0}(** *{1}*  **)** {{#signature}}\n'.format(name, so)
        else:
            return '\n'

    def parse_text(self, item, sep='\n'):
        # if >>> is code block
        # if .. math:: or :math: is math 
        for i, s in enumerate(item):
            if s.startswith('>>>'): 
                item.insert(i, '~~~python')
                item.append('~~~')
                break
            elif s.startswith('.. math::'):
                item[i] = item[i].replace('.. math::', '$$\n')
                while True:
                    i += 1
                    if i >= len(item): break
                    if not item[i].startswith('\t'): break
                item.insert(i, '$$')
            math = re.match(r"(.*):math:`(.*)`(.*)" ,s)
            if math:
                item[i] = '$$'.join(math.groups())
        
        return sep.join(item)

    def parse_section(self, key, item):
        s = ['##### {0} {{#section}}\n'.format(key), '<dl>']
        for p in item: 
            # p[0] param name, p[1] param type, p[2] param desc
            s.append('<dt markdown=\'1\'>' + '`{0}` : *{1}*'.format(p[0] if p[1] else " ", p[1]) + '\n</dt>')
            s += ["\t<dd markdown=\'1\'> {0} \n</dd>\n".format(''.join(p[2]))]
        s.append('</dl>')
        s.append('')
        return '\n'.join(s)

    def parse_block(self, key, item):
        s = ['##### {0} {{#block-header}}'.format(key)]
        s.append(self.parse_text(item))
        return '\n'.join(s)

    def parse_color_block(self, key, item):
        s = ['##### **{0}**'.format(key)]
        for lst, desc in item:
            names = ', '.join([name for name, _ in lst])
            s.append(': '.join([names, self.parse_text(desc, ' ')]))
        return '<div class=\'color-block\' markdown=\'1\'>'+'\n'.join(s)+'\n</div>'

    def parse_methods(self, key, item):
        s = []
        for name, _, lst in item:
            doc = NumpyDocString('\n'.join(lst))
            doc._parsed_data['Signature'] = name
            s.append(self.get_doctext(doc))
        return '\n'.join(s)

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
                        objs.append(FunctionDoc(obj))
                    elif isclass(obj):
                        objs.append(ClassDoc(obj))
        return objs


    def get_yaml(self, mod):
        mod = importlib.import_module(mod)
        yam = '\n'.join([ \
            '---',
            'layout: post',
            'title: {0}'.format(mod.__name__),
            'description: >',
            ' '+mod.__doc__,
            '---', '\n'])
        return yam

        # yam += '# ' +  '{0}'.format(mod.__name__) + '\n'

        # if short_desc != ' ':
        #     yam += '\n'.join([
        #         '## Description', 
        #         '{0}'.format(mod.__doc__)])

        # yam += '---\n'
    def ismember(self, obj):
        return isfunction(obj) or isclass(obj)


def parse_args():
    """Parse args From the command line
    """        
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-o','--out_dir', default='./docs')
    parser.add_argument('-i','--input_dirs', nargs='+', help='<Required> Set flag', required=True)
    parser.add_argument('-x','--overwrite', action='store_true', default=False)
    parser.add_argument('-p','--prefix', default='./docs')
    parser.add_argument('-s','--suffix', default='')
    args = parser.parse_args()
    return args


def tester_func(a,b,c):
    """Func to test fujin functionality
    
    Parameters
    ----------
    a : int
        variable a
    b : int
        variable b
    c : int
        variable c
    
    Returns
    -------
    hey
        a+b+c
    """    
    return a+b+c


            
            

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
