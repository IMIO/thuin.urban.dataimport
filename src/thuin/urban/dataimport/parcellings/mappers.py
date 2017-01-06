# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.exceptions import NoObjectToCreateException
from imio.urban.dataimport.factory import BaseFactory


# Factory
class ParcellingFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.parcellings

    def getPortalType(self, container, **kwargs):
        return 'ParcellingTerm'


class IdMapper(Mapper):

    def mapId(self, line):
        create = self.getData('Lotis') or self.getData('Autorise')
        if not create:
            raise NoObjectToCreateException

        return self.getData('Cle_Lot')
