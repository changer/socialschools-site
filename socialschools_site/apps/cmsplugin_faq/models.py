from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class faq(CMSPlugin):

  question = models.CharField(_("Question"), max_length=150)
  collapselink = models.CharField(_("Collapselink"), max_length=20)
  answer  = models.TextField(_("Answer"))
  image = models.ImageField(_("Image"), upload_to=CMSPlugin.get_media_path, blank=True)


