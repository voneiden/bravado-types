import os.path

from setuptools import setup

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='bravado-types',
    use_scm_version=True,
    license="MIT License",
    description="Library for generating type stubs for Swagger clients "
                "generated by Bravado",
    author="Nicholas Gaya",
    url="https://github.com/nickgaya/bravado-types",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["bravado_types"],
    package_data={
        'bravado_types': ['py.typed', 'templates/*.mako'],
    },
    # According to the documentation, this is needed to ensure MyPy can
    # detect the py.typed file. See
    # https://mypy.readthedocs.io/en/latest/installed_packages.html
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'bravado',
        'bravado-core',
        # Template rendering library
        'mako',
        # Used for accessing package resources
        'setuptools',
    ],
)
