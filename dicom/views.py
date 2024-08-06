import os
from django.conf import settings
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DicomFile
from .serializers import DicomFileSerializer
import pydicom


class DicomFileUploadView(APIView):
    """
    View to handle the upload of DICOM files.

    Uses MultiPartParser and FormParser to handle file uploads.
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for uploading DICOM files.

        Extract metadata using pydicom and save it along with the file.

        Args:
            request: The HTTP request containing the file and metadata.

        Returns:
            Response: HTTP response indicating success or failure.
        """
        file_obj = request.FILES['file']
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'dicom_files')

        # Create the directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file_obj.name)

        # Save the uploaded file
        with open(file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        # Read the DICOM file to extract metadata
        dicom_data = pydicom.dcmread(file_path)
        patient_id = dicom_data.PatientID
        modality = dicom_data.Modality
        series_instance_uid = dicom_data.SeriesInstanceUID
        study_instance_uid = dicom_data.StudyInstanceUID

        data = {
            'file': file_obj,
            'patient_id': patient_id,
            'modality': modality,
            'series_instance_uid': series_instance_uid,
            'study_instance_uid': study_instance_uid,
            'doctype': request.data.get('doctype')
        }

        file_serializer = DicomFileSerializer(data=data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
