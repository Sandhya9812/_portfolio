from django.shortcuts import render
from .models import Certificate  # make sure model name is 'Certificate'

def certificates_list(request):  # fix function name spelling
    certificates = Certificate.objects.all()  # model name starts with capital C
    return render(request, 'certificates.html', {'certificates': certificates})
