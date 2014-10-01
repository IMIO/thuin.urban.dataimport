# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from thuin.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of thuin.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if thuin.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('thuin.dataimport'))

    def test_uninstall(self):
        """Test if thuin.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['thuin.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('thuin.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IThuinDataimportLayer is registered."""
        from thuin.dataimport.interfaces import IThuinDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IThuinDataimportLayer in utils.registered_layers())
