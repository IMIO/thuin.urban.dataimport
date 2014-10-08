# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from thuin.urban.dataimport.interfaces import IThuinDataImporter


class ThuinDataImporter(UrbawebDataImporter):
    """ """

    implements(IThuinDataImporter)
