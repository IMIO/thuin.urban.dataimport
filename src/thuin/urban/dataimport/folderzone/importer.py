# -*- coding: utf-8 -*-

from thuin.urban.dataimport.folderzone import mapping
from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class FolderZonesImporter(AccessDataImporter):
    """ """


class FolderZonesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class FolderZonesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return
