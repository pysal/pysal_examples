from setuptools import setup
import os
import glob

dirs = glob.glob("pysal_examples/*")
files = []
for d in dirs:
    files.extend(glob.glob(d+"/*"))
files = [f.replace("pysal_examples/", "") for f in files]
setup(name='pysal_examples',
            version='1.0.0',
            description='Example data sets for PySAL',
            url='https://github.com/pysal/pysal_examples',
            author='Serge Rey',
            author_email='sjsrey@gmail.com',
            license='3-Clause BSD',
            packages=['pysal_examples'],
            package_data={'pysal_examples': files},
            zip_safe=False)
