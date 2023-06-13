from django.contrib import admin
from .models import ContactPerson

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','facebook', 'whatsapp']

admin.site.register(ContactPerson, ContactAdmin)