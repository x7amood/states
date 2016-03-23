from django.contrib import admin
from main.models import State, StateCapital,City

class StateAdmin(admin.ModelAdmin):
	list_display= ('name','abbreviation')
	search_fields = ['name']


# Register your models here.
admin.site.register(State, StateAdmin)
admin.site.register(StateCapital)
admin.site.register(City)