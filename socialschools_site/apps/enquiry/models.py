from django.db import models
from django.utils.translation import ugettext_lazy as _


class DemoRequest(models.Model):
    first_preference = models.DatetimeField(verbose_name=_(u'First Preference'))
    second_preference = models.DatetimeField(blank=True, null=True, verbose_name=_(u'Second Preference'))
    name = models.CharField(max_length=250, verbose_name=_(u'Name'))
    phone = models.CharField(max_length=50, verbose_name=_(u'Phone'))
    email = models.EmailField(verbose_name=_(u'Email'))
    schoolname = models.CharField(max_length=250, verbose_name=_(u'School Name'))
    remarks = models.CharField(blank=True, verbose_name=_(u'Remarks'))

    def __unicode__(self):
        return u'%s' % self.school

class Cost(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'Name'))
    phone = models.CharField(max_length=50, verbose_name=_(u'Phone'), blank=True, null=True)
    email = models.EmailField(verbose_name=_(u'Email'))
    number_of_students = models.IntegerField(verbose_name=_(u'Number of Students'))
    schoolname = models.CharField(max_length=250, verbose_name=_(u'School Name'))
    remarks = models.CharField(blank=True, verbose_name=_(u'Remarks'))

    def __unicode__(self):
        return u'%s' % self.school

class Support(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'Name'))
    phone = models.CharField(max_length=50, verbose_name=_(u'Phone'), blank=True, null=True)
    email = models.EmailField(verbose_name=_(u'Email'))
    question = models.CharField(verbose_name=_(u'Question'))

    def __unicode__(self):
        return u'%s' % self.school


