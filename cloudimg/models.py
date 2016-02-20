# -*- coding: utf-8 -*-
from django.db import models
import settings
class Image(models.Model):
	sub_dirs = settings.UPLOAD_IMAGE_DIR.split() #Get the last sub-dir
	docfile = models.FileField(upload_to=sub_dirs[-1])

