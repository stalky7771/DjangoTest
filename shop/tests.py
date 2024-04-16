from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.
def index(requesty):
    return HttpResponse("Hello from the Shop app")