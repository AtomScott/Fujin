from numpydoc.docscrape import FunctionDoc, NumpyDocString, ClassDoc

class FujinBase():
    def __init__(self, doc_obj):
        pass

    def write(out_path):
        pass

    def parse_item(self, key, item):
        if key == 'Signature':
            return self.parse_signature(item)
        if key in ['Summary', 'Extended Summary']: 
            return self.parse_text(item)
        if key in ['Parameters', 'Returns', 'Yields', 'Receives', 'Raises', 'Warns', 'Other Parameters']:
            return self.parse_section(item)
        if key in ['Notes', 'Warnings', 'References']:
            return self.parse_block(item)
        if key == 'See Also': 
            return self.parse_color_block(item)
        if key == 'Examples':
            return self.parse_examples(item)
        if key == 'Methods': 
            return self.parse_methods(item)
        if key == 'index': 
            raise NotImplementedError(key, item)
        else:
            raise KeyError(key, item)

    def parse_signature(self, item):
        return item

    def parse_text(self, item):
        return '\n'.join(item)
        # if >>> is code block
        # if .. math:: or :math: is math 
        # for i, s in enumerate(item):
        #     if s.startswith('>>>'): 
        #         item.insert(i, '~~~python')
        #         item.append('~~~')
        #         break
        #     elif s.startswith('.. math::'):
        #         item[i] = item[i].replace('.. math::', '$$\n')
        #         while True:
        #             i += 1
        #             if i >= len(item): break
        #             if not item[i].startswith('\t'): break
        #         item.insert(i, '$$')
        #     math = re.match(r"(.*):math:`(.*)`(.*)" ,s)
        #     if math:
        #         item[i] = '$$'.join(math.groups())
        
        # return sep.join(item)

    def parse_section(self, item):
        return item

    def parse_block(self, item):
        return item

    def parse_color_block(self, item):
        return item

    def parse_methods(self, key, item):
        # todo
        s = []
        for name, _, lst in item:
            doc = NumpyDocString('\n'.join(lst))
            doc._parsed_data['Signature'] = name
            s.append(self.get_doctext(doc))
        return '\n'.join(s)

    def parse_examples(self, item):
        pass #todo

class Classy(FujinBase, ClassDoc):
    def __init__(self, doc_obj):
        super().__init__(doc_obj)
        self.dict = {key: self.parse_item(item) for key, item in self._parsed_data}
        self.dict['name'] = self.get_func()[1]
        self.dict['module'] = self.get_func()[0].__module__

    def write(output):
        template = env.get_template('api-reference-class.tpl')
        output = template.render(self.dict)
        with open(out_path,"w+") as f:
            f.write()

class Funky(FujinBase, FunctionDoc):
    def __init__(self, doc_obj):
        super().__init__(doc_obj)
        self.dict = {key: self.parse_item(item) for key, item in self._parsed_data}
        self.dict['name'] = self.get_func()[1]
        self.dict['module'] = self.get_func()[0].__module__

    def write(output):
        template = env.get_template('api-reference-func.tpl')
        output = template.render(self.dict)
        with open(out_path,"w+") as f:
            f.write()



    # def get_doctext(self, doc):
    #     doctext = []
    #     for key, item in doc._parsed_data.items():
    #         if item: # filter for empty collections and None
    #             try: 
    #                 txt = self.get_text(key, item)
    #             except NotImplementedError as e:
    #                 txt = ''
    #                 print('\t\t Error: {0} autodoc has not been implemented yet'.format(key))
    #             except KeyError as e:
    #                 txt = ''
    #                 print('\t\t Error : {0} is not Numpy style docstring'.format(key))
    #             doctext.append(txt)
    #     return '\n'.join(doctext)


    # def parse_signature(self, key, item):
    #     match = re.match(r"(.*)\((.*)\)" ,item)
    #     if match:
    #         name, so = match.groups()
    #         return '#### **{0}(** *{1}*  **)** {{#signature}}\n'.format(name, so)
    #     else:
    #         return '\n'

    # def parse_text(self, item, sep='\n'):
    #     # if >>> is code block
    #     # if .. math:: or :math: is math 
    #     for i, s in enumerate(item):
    #         if s.startswith('>>>'): 
    #             item.insert(i, '~~~python')
    #             item.append('~~~')
    #             break
    #         elif s.startswith('.. math::'):
    #             item[i] = item[i].replace('.. math::', '$$\n')
    #             while True:
    #                 i += 1
    #                 if i >= len(item): break
    #                 if not item[i].startswith('\t'): break
    #             item.insert(i, '$$')
    #         math = re.match(r"(.*):math:`(.*)`(.*)" ,s)
    #         if math:
    #             item[i] = '$$'.join(math.groups())
        
    #     return sep.join(item)

    # def parse_section(self, key, item):
    #     s = ['##### {0} {{#section}}\n'.format(key), '<dl>']
    #     for p in item: 
    #         # p[0] param name, p[1] param type, p[2] param desc
    #         s.append('<dt markdown=\'1\'>' + '`{0}` : *{1}*'.format(p[0] if p[1] else " ", p[1]) + '\n</dt>')
    #         s += ["\t<dd markdown=\'1\'> {0} \n</dd>\n".format(''.join(p[2]))]
    #     s.append('</dl>')
    #     s.append('')
    #     return '\n'.join(s)

    # def parse_block(self, key, item):
    #     s = ['##### {0} {{#block-header}}'.format(key)]
    #     s.append(self.parse_text(item))
    #     return '\n'.join(s)

    # def parse_color_block(self, key, item):
    #     s = ['##### **{0}**'.format(key)]
    #     for lst, desc in item:
    #         names = ', '.join([name for name, _ in lst])
    #         s.append(': '.join([names, self.parse_text(desc, ' ')]))
    #     return '<div class=\'color-block\' markdown=\'1\'>'+'\n'.join(s)+'\n</div>'

    # def parse_methods(self, key, item):
    #     s = []
    #     for name, _, lst in item:
    #         doc = NumpyDocString('\n'.join(lst))
    #         doc._parsed_data['Signature'] = name
    #         s.append(self.get_doctext(doc))
    #     return '\n'.join(s)



    # def get_yaml(self, mod):
    #     mod = importlib.import_module(mod)
    #     yam = '\n'.join([ \
    #         '---',
    #         'layout: post',
    #         'title: {0}'.format(mod.__name__),
    #         'description: >',
    #         ' '+mod.__doc__,
    #         '---', '\n'])
    #     return yam
