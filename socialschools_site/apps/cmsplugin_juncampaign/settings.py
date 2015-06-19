# coding=utf-8
from django.utils.translation import ugettext_lazy as _

from django.conf import settings as project_settings

CMSPLUGIN_JUNCAMPAIGN_FORMS = getattr(project_settings, "CMSPLUGIN_JUNCAMPAIGN_FORMS", (
        ('socialschools_site.apps.cmsplugin_juncampaign.forms.JuncampaignForm', _('default')),
    )
)
