# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.interfaces import IAccessImporter

from plone.theme.interfaces import IDefaultPloneLayer


class IThuinDataImporter(IAccessImporter):
    """ marker interface for Thuin Agorawin importer """


class IThuinUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""
