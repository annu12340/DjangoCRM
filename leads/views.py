from django.shortcuts import render
from . models import Lead
# Create your views here.
def home_page(request):
    leads=Lead.objects.all()
    return render(request,'leads/home_page.html',{'lead_data':leads})