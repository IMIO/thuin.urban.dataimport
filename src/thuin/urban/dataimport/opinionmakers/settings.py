# -*- coding: utf-8 -*-

from thuin.urban.dataimport.opinionmakers.importer import OpinionMakersImporter
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class OpinionMakersImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=OpinionMakersImporter):
        """
        """
        super(OpinionMakersImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the access file to read.
        """
        settings = super(OpinionMakersImporterFromImportSettings, self).get_importer_settings()

        access_settings = {
            'db_name': 'tab_urba_97.mdb',
            'table_name': 'CONSUL',
            'key_column': 'Sigle',
        }

        settings.update(access_settings)

        return settings
