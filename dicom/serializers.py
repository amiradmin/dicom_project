from rest_framework import serializers
from .models import DicomFile
import os


class DicomFileSerializer(serializers.ModelSerializer):
    """
    Serializer for DicomFile model.

    Serializes all fields in the DicomFile model and validates the file type.
    """

    class Meta:
        model = DicomFile
        fields = ('id', 'file', 'uploaded_at', 'patient_id', 'modality',
                  'series_instance_uid', 'study_instance_uid', 'doctype')

    def validate_file(self, value):
        """
        Validate the uploaded file to ensure it's a DICOM file.

        Args:
            value: The uploaded file.

        Raises:
            serializers.ValidationError: If the file type is not supported.

        Returns:
            The validated file.
        """
        valid_extensions = ['.dcm']
        ext = os.path.splitext(value.name)[1]  # Get the file extension

        if ext.lower() not in valid_extensions:
            raise serializers.ValidationError("Unsupported file type. Please upload a DICOM file.")

        return value

