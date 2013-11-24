from django.db import models
from django.conf import settings

# Create your models here.
class FileUpload(models.Model):
    SYLLABUS = 'syllabus'
    CURRICULUM = 'curriculum'
    ACTIVITIES = 'activities'
    FILE_TYPES = (
        (SYLLABUS, 'Syllabus'),
        (CURRICULUM, 'Curriculum'),
        (ACTIVITIES, 'Activities'),
    )
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="uploaded_by")
    file_type = models.CharField(max_length=100, choices=FILE_TYPES)
    file_field = models.FileField(upload_to='file/%Y/%m/%d')
