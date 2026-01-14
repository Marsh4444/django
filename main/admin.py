from django.contrib import admin
from .models import Project, About, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    search_fields = ['name', 'description']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']
    search_fields = ['name', 'email']
    list_filter = ['submitted_at']