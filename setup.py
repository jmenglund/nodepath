from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='nodepath',
    version=0.1,
    description=(
        'A Python package for working with tree data in pandas'),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    packages=find_packages(exclude=['docs', 'tests*']),
    py_modules=['nodepath'],
    install_requires=['pandas>=0.16', 'numpy'],
    author='Markus Englund',
    author_email='jan.markus.englund@gmail.com',
    url='https://github.com/jmenglund/nodepath',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['pandas'],
)
