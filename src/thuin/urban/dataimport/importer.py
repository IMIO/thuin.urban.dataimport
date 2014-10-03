# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ValuesMapping, ObjectsMapping
from thuin.urban.dataimport.interfaces import IThuinDataImporter
from thuin.urban.dataimport import objectsmapping, valuesmapping


class ThuinDataImporter(AccessDataImporter):
    """ """

    implements(IThuinDataImporter)

    def __init__(self, context, db_name, table_name='URBA', key_column='Cle_Urba'):
        super(ThuinDataImporter, self).__init__(context, db_name, table_name, key_column)


class ThuinMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class ThuinValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name, None)


def importThuinUrbaweb(context, db_name='tab_urba_97.mdb'):
    if context.readDataFile('thuinurbandataimport_marker.txt') is None:
        return

    db = context.openDataFile(db_name)
    db_filepath = db.name
    Thuin_dataimporter = ThuinDataImporter(context, db_filepath)

    # Thuin_dataimporter.setSavePoint(10)

    Thuin_dataimporter.importData(start=1, end=10)

    Thuin_dataimporter.picklesErrorLog(filename='thuin_aihm-log')
