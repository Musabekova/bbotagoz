from django.contrib import admin

# Register your models here.
from .models import Coach, Dancer


class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','awards','date_of_birth')
    fields = ['first_name', 'last_name','awards',('date_of_birth')]
#admin.site.register(Teacher)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Dancer)