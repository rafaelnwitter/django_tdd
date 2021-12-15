from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTesTCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'   
        )

    def test_cadastro(self):
        """Teste que verifica se o animal foi cadastrado com suas respectivas caracteristicas"""
        self.assertEqual(self.animal.nome_animal, 'Leão')