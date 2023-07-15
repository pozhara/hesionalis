from django.contrib import admin
from .models import Artist, Design, Appointment, Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'skills', 'gender')
    search_fields = ('name', 'skills', 'gender')
    list_filter = ('name', 'skills', 'gender')


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('category', 'artist')
    search_fields = ('category', 'artist')
    list_filter = ('category', 'artist')


@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):
    list_display = ('user', 'appointment_at', 'tattoo_category', 'artist', 'status')
    list_filter = ('status', 'artist', 'created_on')
    search_fields = ('user', 'artist', 'tattoo_category')
    summernote_fields = ('comment')
    actions = ['accept_appointment', 'reject_appointment']

    def accept_appointment(self, request, queryset):
        queryset.update(status=1)

    def reject_appointment(self, request, queryset):
        queryset.update(status=2)


admin.site.register(Profile)
