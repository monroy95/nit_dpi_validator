import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'nit_dpi_validator',
    packages = ['nit_dpi_validator'], # this must be the same as the name above
    version = '0.1',
    description = 'Validador NIT, DPI Guatemala',
    author = 'Mario Monroy Canizales',
    author_email = 'm.monroyc22@hotmail.com',
    license='LGPL',
    url = 'https://github.com/monroy95/nit_dpi_validator', # use the URL to the github repo
    keywords = ['dpi', 'nit', 'Validador NIT Guatemala', 'NIT Guatemala'],
    long_description=long_description,
    python_requires='>=2.7',
)
