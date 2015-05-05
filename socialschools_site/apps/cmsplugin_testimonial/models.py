from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models

LEFT = "left"
RIGHT = "right"
FLOAT_CHOICES = ((LEFT, _("left")),
                (RIGHT, _("right")),
)

class Testimonial(CMSPlugin):

	float = models.CharField(_("Image placement"), max_length=10, blank=True, null=True,
        choices=FLOAT_CHOICES, help_text=_("Move image left, right or center."))
	image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
	big_header  = models.TextField(_("Quotation"),null=True, max_length=150)
	name = models.CharField(_("Name of Recommending person"), max_length=150)
	detail = models.CharField(_("School detail"), max_length=200)

	def __unicode__(self):
		return u'{0}'.format(self.name)