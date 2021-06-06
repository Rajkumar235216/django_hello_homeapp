from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from homeapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("This is home app main page")
    context = {
        "variable1": "this is value 1",
        "variable2": "this is value 2",
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")
    """   return HttpResponse("This is about page") """

def services(request):
    return render(request, "services.html")
    """ return HttpResponse("This is services page") """

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email") 
        phone = request.POST.get("phone") 
        description = request.POST.get("description") 
        contact = Contact(name=name, email=email, phone=phone, description=description, date=datetime.today())
        contact.save()
        messages.success(request, "Your Data has been saved!")
        
    return render(request, "contact.html")
    """ return HttpResponse("This is contact page") """
