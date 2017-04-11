from django.contrib import admin

# Register your models here.
from .models import Patent
from .models import Keywords
from .models import Uspc

admin.site.register(Patent)
admin.site.register(Keywords)
admin.site.register(Uspc)