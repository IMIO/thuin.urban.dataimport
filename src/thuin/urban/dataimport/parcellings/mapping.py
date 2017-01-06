# -*- coding: utf-8 -*-

from thuin.urban.dataimport.parcellings.mappers import IdMapper
from thuin.urban.dataimport.parcellings.mappers import ParcellingFactory

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper


OBJECTS_NESTING = [
    (
        'PARCELLING', [],
    ),
]

FIELDS_MAPPINGS = {
    'PARCELLING':
    {
        'factory': [ParcellingFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Autorise',
                    'to': 'authorizationDate',
                },
                {
                    'from': 'NBL',
                    'to': 'numberOfParcels',
                },
                {
                    'from': 'Rem_Lotis',
                    'to': 'changesDescription',
                },
                {
                    'from': 'Lotis',
                    'to': 'subdividerName',
                },
            ),

            IdMapper: {
                'from': ('Cle_Lot', 'Lotis', 'Autorise'),
                'to': 'id',
            },
        },
    },
}
