from django.test import TestCase
import datetime


# Create your tests here.
object = datetime.datetime.now()
hora = str(object)
x = slice(19)
hora = hora[x]

print(hora)