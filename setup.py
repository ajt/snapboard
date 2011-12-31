from setuptools import setup, find_packages

version = '.01'

setup(
    name='snapboard',
    version=version,
    description="snapboard",
    long_description="",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='snapboard,forums,django',
    author='ajt',
    author_email='',
    url='',
    license='',
    packages=find_packages(),
    package_data = {
        'snapboard': [
            'templates/snapboard/*.html',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
