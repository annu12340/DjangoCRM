from django.shortcuts import render
from . models import Lead
# Create your views here.

def lead_list(request):
    leads=Lead.objects.all()
    return render(request,'leads/lead_list.html',{'lead_data':leads})

def lead_detail(request,pk):
    print(pk)
    lead=Lead.objects.get(id=pk)
    return render(request, 'leads/lead_list.html', {'lead_data': lead})
