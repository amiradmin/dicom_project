from django.db import models


class DicomFile(models.Model):
    """
    Model representing a DICOM file with associated metadata.

    Attributes:
        file (FileField): The uploaded DICOM file.
        uploaded_at (DateTimeField): The timestamp when the file was uploaded.
        patient_id (CharField): The ID of the patient.
        modality (CharField): The imaging modality (e.g., CT, MRI).
        series_instance_uid (CharField): The unique identifier for the series instance.
        study_instance_uid (CharField): The unique identifier for the study instance.
        doctype (CharField): The type of document.
    """
    file = models.FileField(upload_to='dicom_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    patient_id = models.CharField(max_length=100)
    modality = models.CharField(max_length=50)
    series_instance_uid = models.CharField(max_length=100)
    study_instance_uid = models.CharField(max_length=100)
    doctype = models.CharField(max_length=50)

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Modality: {self.modality}, Doctype: {self.doctype}"
