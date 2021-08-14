from django.contrib import admin
from .models import Collage

class COllageName(admin.ModelAdmin):
    list_display = ('id','Firstname','Lastname', 'email', 'mob')
# Register your models here.
admin.site.register(Collage, COllageName)
