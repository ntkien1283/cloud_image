from django.test import TestCase, RequestFactory
from facecrop.views import index
class FaceCropTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def testViews(self):
        with open('/home/kien/Downloads/birthday2.jpg', 'rb') as img:
            result = self.factory.post('/facecrop/',{'img':img})
            resp = index(result)
            print(resp)
