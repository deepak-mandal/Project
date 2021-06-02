from django.contrib import admin

# Register your models here.

#To make the App apps modificable in the admin portal
#from .models import Question
#admin.site.register(Question)

from .models import Allcourses, details
admin.site.register(Allcourses)
admin.site.register(details)