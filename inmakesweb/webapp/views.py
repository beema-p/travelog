from django.shortcuts import render

from .models import Place

from .models import People


# Create your views here.
def display(request):
    obj = Place.objects.all()
    ppl = People.objects.all()
    return render(request, 'index.html', {'res': obj, 'result': ppl})
