from django import forms
from django.utils.translation import ugettext_lazy as _
#import settings
from nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm

class NotcampaignForm(forms.Form):
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'placeholder': _('Your email address*'), 'class':'form-control'}))
    vision = forms.CharField(label=_("Your vision"), widget=forms.Textarea(attrs={'placeholder': _('Your vision*'), 'class':'form-control'}))

    template = "cmsplugin_notcampaign/vision.html"

class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None


class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
