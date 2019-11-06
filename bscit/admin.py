from django.contrib import admin


# Register your models here.
from . models import question
from .models import Events
from .models import notice
from .models import profile


admin.site.register(question)
admin.site.register(Events)
admin.site.register(notice)

admin.site.register(profile)

admin.site.site_header = 'Administration'
admin.site.site_title = 'Administration'