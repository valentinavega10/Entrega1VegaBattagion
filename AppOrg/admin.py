from django.contrib import admin
from AppOrg.models import Expositor, Oyente

from AppOrg.views import expositores, oyentes

# Register your models here.

admin.site.register(Expositor)
admin.site.register(Oyente)