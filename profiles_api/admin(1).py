# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from profiles_api.models import UserProfile, ProfileFeedItem


# admin.site.register(UserProfileManager)
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
