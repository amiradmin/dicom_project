from django.contrib import admin
from .models import DicomFile


class DicomFileAdmin(admin.ModelAdmin):
    """
    Admin interface options for DicomFile model.

    Customizes the list display and search fields for the DicomFile model in the admin interface.
    """
    list_display = ('patient_id', 'modality', 'series_instance_uid', 'study_instance_uid', 'doctype', 'uploaded_at')
    search_fields = ('patient_id', 'modality', 'series_instance_uid', 'study_instance_uid', 'doctype')
    list_filter = ('modality', 'uploaded_at', 'doctype')


admin.site.register(DicomFile, DicomFileAdmin)
