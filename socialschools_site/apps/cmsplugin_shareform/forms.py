from django import forms
from django.utils.translation import ugettext_lazy as _
#import settings
from nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm


class ShareForm(forms.Form):
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'placeholder': _('Your email address*'), 'class':'form-control'}))
    schoolname = forms.CharField(label=_("Schoolname"), widget=forms.TextInput(attrs={'placeholder': _('Schoolname*'), 'class':'form-control'}))

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
