from setuptools import setup, find_packages
import os
import re
import codecs

NAME = 'NSMAXIMALES'
META_PATH = os.path.join(NAME,' __init__.py')
REQUIREMENTS =  ["ete3","pandas","scipy","numpy","scipy"]
CLASSIFIERS = ['Development Status :: 4 - Beta',
                                 'Intended Audience :: Developers',
                                 'Intended Audience :: Data Analysts',
                                 'License :: OSI Approved :: MIT License',
                                 'Natural Languaje :: Spanish',
                                 'Operating System :: Microsoft :: Windows',
                                 'Programming Language :: Python',
                                 'Topic :: Data Analytics',
                                 'Topic :: Topology']
HERE = os.path.abspath(os.path.dirname(__name__))

if __name__ == "__main__": setup(name="NsMaximales", 
                                description="NsMaximales se encarga de calcular los n-subárboles maximales y apartir de ellos obtener una base topológica",
                                license="MIT",
                                url="https://github.com/Gennifer2001/tesis/blob/main/T%C3%A9sisjeje2_1xd.ipynb",version="0.1",
                                author="Yeimi Rodriguez y Genifer Montaño",
                                author_email="gennifermontanorodriguez@gmail.com o yeimir0000@gmail.com",
                                long_description=open("README.md").read(),
                                packages=find_packages(),
                                zip_safe= False,
                                install_requires = REQUIREMENTS,
                                classifiers= CLASSIFIERS)
