from django.test import TestCase, RequestFactory
from .views import index
class FaceCropTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def testViews():
        with open('/home/kien/Downloads/birthday2.jpg', 'rb') as img:
            r = self.factory.post('/facecrop/',{'img':img})
            resp = index(r)
