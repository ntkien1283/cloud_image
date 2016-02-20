from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from models import Image
from forms import ImageForm
import settings
import face_detection
import os
import ipdb
def index(request):
    ipdb.set_trace()
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Image(docfile = request.FILES['docfile'])
            newdoc.save()
            face_detection.detect_batch(settings.UPLOAD_IMAGE_DIR, settings.FACE_CROP_MARGIN,settings.FACE_CROP_IMAGE_DIR)
            # Redirect to the document list after POST
            return HttpResponse('Upload success')#HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = ImageForm() # A empty, unbound form

    # Load documents for the list page
    images = Image.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        "list.html",
        {'documents': images, 'form': form},
        context_instance=RequestContext(request)
    )
