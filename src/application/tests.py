from django.test import TestCase

# Create your tests here.
def prueba(**kwargs):
    print(kwargs['prueba'])

prueba(prueba='hola')

