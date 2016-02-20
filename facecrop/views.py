from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from models import Image
from forms import ImageForm
import cloudimg.settings as settings
import face_detection
import os
import ipdb
def index(request):
    ipdb.set_trace()
    # Handle file upload
    face_img_urls = []
    face_dir = settings.FACE_CROP_IMAGE_DIR.split(os.sep)[-1]

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        current_images = Image.objects.all()
        new_id = len(current_images) + 1
#       newdoc = Image(docfile = request.FILES['docfile'])
        files = request.FILES.getlist('img')
        for file_i in range(len(files)):
            newdoc = Image(docfile = files[file_i])
            new_file_name = str(new_id + file_i) + os.path.splitext(f.name)[1]
            newdoc.docfile.name =  new_file_name 
            newdoc.save()
            face_file_paths = face_detection.detect_one_img(settings.UPLOAD_IMAGE_DIR + os.sep + new_file_name, settings.FACE_CROP_MARGIN,settings.FACE_CROP_IMAGE_DIR)
            face_urls = []
            for face_name in face_file_paths:
                face_name = face_name.split(os.sep)
                _url = settings.MEDIA_URL + face_dir + os.sep + face_name[-1]
                face_urls.append(_url)
            face_img_urls.append(face_urls)
        # Load documents for the list page
    else:
        form = ImageForm() # A empty, unbound form

    return render_to_response(
        "list.html",
        {'face_img_urls': face_img_urls, 'form': form},
        context_instance=RequestContext(request)
    )
#        #images = Image.objects.all()
#        face_file_names = next(os.walk(settings.FACE_CROP_IMAGE_DIR))[2]
#        face_dir = settings.FACE_CROP_IMAGE_DIR.split(os.sep)[-1]
#        for face_name in face_file_names:
#            face_name = face_name.split(os.sep)
#            _url = settings.MEDIA_URL + face_dir + os.sep + face_name[-1]
#            face_file_url.append(_url)
#        # Render list page with the documents and the form
#
