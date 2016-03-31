try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    'Django>=1.8.0',
    'jsonfield>=1.0.3',
    'bleach>=1.4.1',
    'six>=1.9.0'
]

with open('README.rst') as f:
    readme = f.read()


setup(
    name='bleachfields',
    version='1.0.6',
    packages=['bleachfields'],
    license='MIT',
    description='Tools for bleaching text and JSON of HTML',
    long_description=readme,
    author='Alex Francis',
    author_email='afrancis@betterworks.com',
    install_requires=install_requires,
    url="https://github.com/BetterWorks/django-bleachfields/",
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
