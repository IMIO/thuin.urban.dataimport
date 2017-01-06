# -*- coding: utf-8 -*-

from imio.urban.dataimport.factory import BaseFactory


# Factory
class FolderZoneFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.portal_urban.folderzones

    def getPortalType(self, container, **kwargs):
        return 'UrbanVocabularyTerm'
