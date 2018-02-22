from setuptools import setup, find_packages
from helga_{{ cookiecutter.plugin_package }} import __version__ as version


setup(
    name="{{ cookiecutter.plugin_name }}",
    version=version,
    description=('{{ cookiecutter.plugin_description }}'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='{{ cookiecutter.plugin_name }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    test_suite='tests/test_{{ cookiecutter.plugin_package }}',
)
