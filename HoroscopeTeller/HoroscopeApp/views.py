from django.shortcuts import render, HttpResponse, redirect
import zodiac
# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        print(dob)
        print(type(dob))
        z=zodiac.calculate_zodiac_sign(dob)

        dic={"z":z}


        return render(request,'page2.html',dic)
    return render(request,'index.html')