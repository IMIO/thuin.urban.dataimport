# -*- coding: utf-8 -*-

from thuin.urban.dataimport.opinionmakers import mapping
from thuin.urban.dataimport.opinionmakers import valuesmapping

from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping

from Products.urban.utils import moveElementAfter


class OpinionMakersImporter(AccessDataImporter):
    """ """

    def post_creation_process(self, urban_object, container):
        """
        Reorder OpinionRequestEventType objects at the right position.
        """
        ORET_ids = container.objectIds('OpinionRequestEventType')
        last_ORET_id = len(ORET_ids) > 1 and ORET_ids[-2] or 'config-opinion-request'
        moveElementAfter(urban_object, container, 'id', last_ORET_id)


class OpinionMakersMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class OpinionMakersValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
