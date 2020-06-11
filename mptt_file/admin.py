from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from mptt_file.models import FileObject

admin.site.register(FileObject, MPTTModelAdmin)
