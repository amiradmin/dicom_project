from rest_framework import serializers
from .models import DicomFile

class DicomFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DicomFile
        fields = ('id', 'file', 'uploaded_at', 'patient_id', 'modality', 'series_instance_uid', 'study_instance_uid')
