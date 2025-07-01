from django.contrib import admin
from .models import ContactSubmission, Project, Client, NewsletterSubscription
from django.utils.html import format_html
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'submitted_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display     = ('name', 'short_description', 'preview') 
    search_fields    = ('name',)                       
    list_per_page    = 20                               
    readonly_fields  = ('preview',)                     

    def short_description(self, obj):
        return obj.description[:50] + '…' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px; border-radius:4px;" />',
                obj.image.url
            )
        return '–'
    preview.short_description = 'Thumbnail'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'preview')
    search_fields = ('name', 'designation')

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:40px; height:40px; border-radius:50%;" />',
                obj.image.url
            )
        return '–'
    preview.short_description = 'Photo'

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display  = ('email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)