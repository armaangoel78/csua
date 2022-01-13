import setuptools

from pathlib import Path

setuptools.setup(
    name="csuayyy",
    version="0.0.7",
    author="Armaan Goel",
    author_email="armaangoel78@gmail.com",
    description="CLI for easily interfacing with Berkeley CSUA",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    project_urls={
        'Github': 'https://github.com/armaangoel78/csua/',
    },
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
    		'csuayyy=csuayyy.src.main:main',
    		'csua=csuayyy.src.main:main'
    	]
    },        
    python_requires='>=3.6',
    install_requires=['pexpect', 'termcolor']
)