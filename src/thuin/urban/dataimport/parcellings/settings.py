# -*- coding: utf-8 -*-

from thuin.urban.dataimport.parcellings.importer import ParcellingsImporter
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class ParcellingsImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=ParcellingsImporter):
        """
        """
        super(ParcellingsImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the access file to read.
        """
        settings = super(ParcellingsImporterFromImportSettings, self).get_importer_settings()

        access_settings = {
            'db_name': 'tab_urba 97.mdb',
            'table_name': 'LOTISSEM',
            'key_column': 'Cle_Lot',
        }

        settings.update(access_settings)

        return settings
