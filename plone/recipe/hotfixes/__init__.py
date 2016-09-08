# -*- coding: utf-8 -*-
import os


class Recipe(object):
    """zc.buildout recipe"""

    buildout = None
    name = None
    options = None

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        self.options.setdefault(
            'base_url',
            ('https://raw.githubusercontent.com' +
             '/collective/plone.recipe.hotfixes/hotfixes/')
        )

        self.options.setdefault('configs', ('base',))

        # What files are tracked by this recipe
        self.files = [
            os.path.join(
                self.buildout['buildout']['bin-directory'], self.name
            )
        ]

    def install(self):
        self.options.setdefault(
            'plone_version',
            self.buildout.versions['Products.CMFPlone']
        )

        return self.files

    def update(self):
        return self.install()
