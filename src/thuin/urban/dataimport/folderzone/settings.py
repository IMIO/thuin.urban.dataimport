# -*- coding: utf-8 -*-

from thuin.urban.dataimport.folderzone.importer import FolderZonesImporter
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class FolderZonesImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=FolderZonesImporter):
        """
        """
        super(FolderZonesImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the mdb file to read.
        """
        settings = super(FolderZonesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'tab_urba 97.mdb',
            'table_name': 'ZONEGEO',
            'key_column': 'Type_Zone',
        }

        settings.update(db_settings)

        return settings
