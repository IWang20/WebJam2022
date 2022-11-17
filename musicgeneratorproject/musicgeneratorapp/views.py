from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Song
from django.template import loader

# Create your views here.


def musicgenerator(request):
    # paginator = Paginator(Songs.objects.all(), 1)
    # page_number = request.GET.get('page')
    #                     #get details, get page name
    # page_obj = paginator.get_page(page_number)
    # context = {"page_obj": page_obj}
    # return render(request, "index.html", context)
    
    #return render(request, 'path from template to the file', {'Song': Song})
    return HttpResponse("Hello world!")

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())