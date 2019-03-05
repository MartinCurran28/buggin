from django.shortcuts import render
from .models import Service

def all_services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})
    
    
    
