from setuptools import setup

setup(name='fujin',
      version='0.1',
      description='create simple docs from .py and .ipynb',
      url='https://github.com/AtomScott/Fujin',
      author='Atom Scott',
      author_email='atom.james.scott@gmail.com',
      license='MIT',
      packages=['fujin'],
      install_requires=[
          'numpydoc',
      ],
      scripts=[
        'bin/fujin',
        'bin/fujin-nbconvert',
      ],
      zip_safe=False)
