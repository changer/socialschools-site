from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from os.path import basename

LEFT = "left"
RIGHT = "right"
FLOAT_CHOICES = ((LEFT, _("left")),
                (RIGHT, _("right")),
)

class Feature(CMSPlugin):

	float = models.CharField(_("Image placement"), max_length=10, blank=True, null=True,
        choices=FLOAT_CHOICES, help_text=_("Move image left, right or center."))
	image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
	blue_header  = models.CharField(_("Blue part of title"), max_length=150)
	green_header = models.CharField(_("Green part of the tile"), max_length=150)
	black_header = models.CharField(_("Black part of the tile"), max_length=150)
	description = models.CharField(_("Remarks"), max_length=150)

	def __unicode__(self):
		if self.image:
			try:
				return u"%s" % basename(self.image.path)
			except:
				pass
		return "<empty>"