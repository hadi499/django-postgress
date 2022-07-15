from ast import Return
from django.http import HttpResponse


def home(request):
    return HttpResponse('Testing PostgersSql on django.')
