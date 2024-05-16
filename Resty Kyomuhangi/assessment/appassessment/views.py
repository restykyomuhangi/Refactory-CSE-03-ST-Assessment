from django.shortcuts import render
from .models import *


# Create your views here.
def registrationform(request):
    message = None
    if request.method == 'POST':
        
        instance = request.POST
        reg = Registration(
            firstname=instance.get('firstname'),
            lastname=instance.get('lastname'),
            course=instance.get('course'),
            entryscheme=instance.get('entryscheme'),
            intake=instance.get('intake'),
            sponsorship=instance.get('sponsorship'),
            gender=instance.get('gender'),
            dob=instance.get('dob'),
            residence=instance.get('residence'),
        )
        reg.save()
        message = "Form has been Submitted successfully !"
    context = {'message':message}   
    return render(request,'appassessment/registrationform.html', context)


