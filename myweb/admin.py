from django.contrib import admin
from .models import *
from .models import Destination

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Oxestype)
admin.site.register(Oxes)
admin.site.register(Destination)