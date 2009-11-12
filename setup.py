from distutils.core import setup

import pycompletion

setup(
    name='pycompletion',
    version=pycompletion.__version__,
    description='A lib to collect command line completion scripts of Python packages',
    author='Arthur Koziel, Jannis Leidel',
    author_email='arthur@arthurkoziel.com, jannis@leidel.info',
    url='http://github.com/jezdez/pycompletion/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    packages=['pycompletion'],
    package_data={'pycompletion': ['*/*']},
    scripts=['scripts/pycompletion'],
    zip_safe=False,
),
