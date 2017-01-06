# -*- coding: utf-8 -*-

from thuin.urban.dataimport.folderzone.mappers import FolderZoneFactory

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper


OBJECTS_NESTING = [
    ('FOLDERZONE', [],),
]

FIELDS_MAPPINGS = {
    'FOLDERZONE':
    {
        'factory': [FolderZoneFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Type_Zone',
                    'to': 'id',
                },
                {
                    'from': 'Libelle',
                    'to': 'title',
                },
            ),
        },
    },
}
