# -*- coding: utf-8 -*-
from django.db import models
import cloudimg.settings as settings
import os
class Image(models.Model):
	sub_dirs = settings.UPLOAD_IMAGE_DIR.split(os.sep) #Get the last sub-dir
	docfile = models.FileField(upload_to=sub_dirs[-1])

