import setuptools

setuptools.setup(
    name="csuayyy",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Armaan Goel",                     # Full name of the author
    author_email="armaangoel78@gmail.com",
    description="CLI for easily interfacing with Berkeley CSUA",
    packages=setuptools.find_packages(),    # List of all python modules to be installed     
    entry_points={
        'console_scripts': [
    		'csuayyy=csuayyy.src.main:main',
    		'csua=csuayyy.src.main:main'
    	]
    },                               # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=['pexpect', 'docopt']                     # Install other dependencies if any
)