try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

setup(
    name="ply-2",
    description="Python Lex & Yacc - second version",
    long_description = """
PLY is yet another implementation of lex and yacc for Python. Some notable
features include the fact that its implemented entirely in Python and it
uses LALR(1) parsing which is efficient and well suited for larger grammars.

PLY provides most of the standard lex/yacc features including support for empty 
productions, precedence rules, error recovery, and support for ambiguous grammars. 

PLY is extremely easy to use and provides very extensive error checking. 
It is compatible with both Python 2 and Python 3.

This is a refactored and updated version. The origical is called ply and was
written by David Beazley <dave@dabeaz.com>.
""",
    license="BSD",
    version="0.1",
    author="Hercinger Viktor",
    author_email="hercinger.viktor@gmail.com",
    maintainer="Hercinger Viktor",
    maintainer_email="hercinger.viktor@gmail.com",
    url="http://www.dabeaz.com/ply/",
    packages=['ply', 'ply.lex', 'ply.yacc'],
)
