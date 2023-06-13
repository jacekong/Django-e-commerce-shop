from django.shortcuts import render
from .models import ContactPerson

# Create your views here.
def contact(request):
    contacts = ContactPerson.objects.all()
    
    context = {
        'contacts': contacts
    }
    return render(request, 'contact.html', context)