# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.factory import BaseFactory


# Factory
class OpinionMakerFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        licence_types = [
            'BuildLicence', 'Article127', 'ParcelOutLicence',
            'UrbanCertificateTwo', 'MiscDemand', 'EnvClassOne', 'EnvClassTwo',
        ]
        portal_urban = self.site.portal_urban
        creation_places = [getattr(portal_urban, t.lower()).urbaneventtypes for t in licence_types]
        return creation_places

    def getPortalType(self, container, **kwargs):
        return 'OpinionRequestEventType'


class TitleMapper(Mapper):

    def mapTitle(self, line):
        raw_title = self.getData('Libelle')
        title = "Demande d'avis ({})".format(raw_title)
        return title


class DefaultValuesMapper(Mapper):

    def mapTalcondition(self, line):
        raw_id = self.getData('Sigle')
        tal_condition = "python: here.mayAddOpinionRequestEvent('{}')".format(raw_id)
        return tal_condition

    def mapEventtypetype(self, line):
        return 'Products.urban.interfaces.IOpinionRequestEvent'

    def mapActivatedfields(self, line):
        activated_fields = [
            'transmitDate',
            'receiptDate',
            'receivedDocumentReference',
            'adviceAgreementLevel',
            'externalDecision'
        ]
        return activated_fields
