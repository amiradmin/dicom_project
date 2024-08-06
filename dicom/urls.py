from django.urls import path
from .views import DicomFileUploadView

urlpatterns = [
    path('upload/', DicomFileUploadView.as_view(), name='dicom-file-upload'),
]