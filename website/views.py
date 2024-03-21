from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting
# Create your views here.
def welcome(request): 
    if request.user.is_authenticated:
        context = {"meetings":Meeting.objects.all()}
    else:
        context = {}
        
    return render(request, template_name="website/welcome.html",
                  context=context)

def about(request):
    return HttpResponse("Hola me llamo Pedro, y estoy aprendiendo Django")