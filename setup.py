from distutils.core import setup

setup(
    name = 'nit_dpi_validator',
    packages = ['nit_dpi_validator'], # this must be the same as the name above
    version = '0.1',
    description = 'Validador NIT, DPI Guatemala',
    author = 'Mario Monroy Canizales',
    author_email = 'm.monroyc22@hotmail.com',
    license='LGPL',
    url = 'https://github.com/monroy95/nit_dpi_validator', # use the URL to the github repo
    download_url = 'https://github.com/monroy95/nit_dpi_validator/tags',
    keywords = ['dpi', 'nit', 'Validador NIT Guatemala', 'NIT Guatemala'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License '
        '(LGPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
