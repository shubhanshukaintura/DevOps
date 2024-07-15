from django.test import TestCase
from myapp.models import MyModel

class MyModelTest(TestCase):
    def test_str(self):
        my_model = MyModel(name='Test Model')
        self.assertEqual(str(my_model), 'Test Model')
