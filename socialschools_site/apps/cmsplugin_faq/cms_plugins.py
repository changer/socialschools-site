from cms.plugin_base import  CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


from models import faq

class faqPlugin(CMSPluginBase):
	model = faq
	name = _("FAQ Plugin")
	render_template = "cmsplugin_faq/faq_item.html"

	def render(self, context, instance, placeholder):
		context.update({
			'object': instance
			})
		return context

plugin_pool.register_plugin(faqPlugin)
