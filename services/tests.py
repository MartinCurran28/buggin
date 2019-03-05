from django.test import TestCase
from .models import Service

class ServiceTest(TestCase):
    """
    Here we'll define the tests
    that run against our product models
    """
    
    def test_str(self):
        test_name = Service(name = 'A Service')
        self.assertEqual(str(test_name), 'A Service')
        
        

