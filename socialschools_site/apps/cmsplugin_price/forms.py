from django import forms
from django.utils.translation import ugettext_lazy as _
#import settings
from nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm

CHOICES=[('1', _('Morning')),
         ('2', _('Evening')),
         ('3', _('No preference'))]


class PriceForm(forms.Form):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'placeholder': _('Your name*'), 'class':'form-control'}))
    phone = forms.CharField(label=_("Phone"), widget=forms.TextInput(attrs={'placeholder': _('Phone number'), 'class':'form-control'}), required=False)
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'placeholder': _('Your email address*'), 'class':'form-control'}))
    number_of_students = forms.IntegerField(label=_("number of students"), widget=forms.TextInput(attrs={'placeholder': _('Number of students*'), 'class':'form-control'}))
    schoolname = forms.CharField(label=_("Schoolname"), widget=forms.TextInput(attrs={'placeholder': _('Schoolname*'), 'class':'form-control'}))
    remarks = forms.CharField(label=_("Remarks"), widget=forms.Textarea(attrs={'placeholder': _('Remarks'), 'class':'form-control'}), required=False)
    template = "cmsplugin_price/contact.html"

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
