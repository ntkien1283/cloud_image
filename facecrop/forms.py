from django import forms
from utils.multi_file_field import MultiFileField
class ImageForm(forms.Form):
    #docfile = forms.FileField(label='Select a file',)
    files = MultiFileField(min_num=1, max_num=1000, max_file_size = 5000*5000*5)

