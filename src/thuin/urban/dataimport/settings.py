# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm


class ThuinImporterSettingsForm(ImporterSettingsForm):
    """ """


class ThuinImporterSettings(ImporterSettings):
    """ """
    form = ThuinImporterSettingsForm


class ThuinImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = ThuinImporterSettings
