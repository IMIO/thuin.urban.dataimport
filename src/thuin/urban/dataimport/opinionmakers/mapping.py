# -*- coding: utf-8 -*-

from thuin.urban.dataimport.opinionmakers.mappers import DefaultValuesMapper
from thuin.urban.dataimport.opinionmakers.mappers import OpinionMakerFactory
from thuin.urban.dataimport.opinionmakers.mappers import TitleMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper


OBJECTS_NESTING = [
    (
        'OPINION MAKER', [],
    ),
]

FIELDS_MAPPINGS = {
    'OPINION MAKER':
    {
        'factory': [OpinionMakerFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Sigle',
                    'to': 'id',
                },
                {
                    'from': 'Libelle',
                    'to': 'extraValue',
                },
            ),

            TitleMapper: {
                'from': 'Libelle',
                'to': 'title',
            },

            DefaultValuesMapper: {
                'from': 'Sigle',
                'to': ('TALCondition', 'activatedFields', 'eventTypeType',),
            },
        },
    },
}
