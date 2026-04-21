# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Publications(models.Model):

    #__Publications_FIELDS__
    last_updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    url = models.CharField(max_length=255, null=True, blank=True)
    file_name = models.CharField(max_length=255, null=True, blank=True)
    inserted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    title = models.CharField(max_length=255, null=True, blank=True)
    organisation = models.CharField(max_length=255, null=True, blank=True)

    #__Publications_FIELDS__END

    class Meta:
        verbose_name        = _("Publications")
        verbose_name_plural = _("Publications")


class Web_Tech(models.Model):

    #__Web_Tech_FIELDS__
    organisation = models.CharField(max_length=255, null=True, blank=True)
    cms = models.CharField(max_length=255, null=True, blank=True)
    database = models.CharField(max_length=255, null=True, blank=True)
    programming_language = models.CharField(max_length=255, null=True, blank=True)
    inserted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Web_Tech_FIELDS__END

    class Meta:
        verbose_name        = _("Web_Tech")
        verbose_name_plural = _("Web_Tech")


class Social_Media(models.Model):

    #__Social_Media_FIELDS__
    organisation = models.CharField(max_length=255, null=True, blank=True)
    network = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    profile = models.CharField(max_length=255, null=True, blank=True)
    inserted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Social_Media_FIELDS__END

    class Meta:
        verbose_name        = _("Social_Media")
        verbose_name_plural = _("Social_Media")



#__MODELS__END
