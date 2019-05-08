from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

# Register your models here.
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    save_as = True
    
    fieldsets = (
        ('Title/date', {
            "fields": (
                "publish",
            ),
        }),
        ('Content', {
            "fields": (
                "title",
                "descriptions"
            ),
        }),
    )

admin.site.register(Blog,BlogAdmin)