from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """
        Teste da home page
        """
        req = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            res = index(req)
            self.assertEqual(res.status_code, 200)