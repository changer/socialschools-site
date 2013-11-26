from cms.plugin_base import  CMSPluginBase
from cms.plugin_pool import plugin_pool 
from django.utils.translation import ugettext_lazy as _


from models import Feature

class FeaturePlugin(CMSPluginBase):
	model =  Feature
	name = _("Feature Plugin")
	render_template = "cmsplugin_feature/feature.html"

	def render(self, context, instance, placeholder):
		context.update({
			'object': instance
			})
		return context

plugin_pool.register_plugin(FeaturePlugin)