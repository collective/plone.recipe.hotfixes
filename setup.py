# -*- coding: utf-8 -*-
"""
This module contains the tool of plone.recipe.hotfixes
"""
from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0.dev0'

long_description = '\n\n'.join([
    read('README.rst'),
    read('CONTRIBUTORS.rst'),
    read('CHANGES.rst'),
])

entry_point = 'plone.recipe.hotfixes:Recipe'
entry_points = {
    'zc.buildout': [
        'default = {0:s}'.format(entry_point)
    ]
}

setup(name='plone.recipe.hotfixes',
      version=version,
      description='Automatic hotfix management for Plone.',
      long_description=long_description,
      # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Buildout',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python',
          'Topic :: Software Development :: Build Tools',
      ],
      keywords='',
      author='René Jochum',
      author_email='rene@webmeisterei.com',
      url='http://github.com/collective/plone.recipe.hotfixes/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
          'zc.recipe.egg',
      ],
      extras_require={
          'test': [
              'testfixtures',
              'zc.buildout [test]',
              'zope.testing',
          ],
      },
      test_suite='plone.recipe.hotfixes.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
