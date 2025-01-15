from django.contrib import admin



# Register your models here.
from elect.models import servicee,rev,contact
admin.site.register(servicee)
admin.site.register(rev)
admin.site.register(contact)

