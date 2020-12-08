from django.shortcuts import render
import random 	                # import the random module

# Create your views here.
def index(request):

    return render(request,"index.html")



def number_guesser(request):
    print("Got Post Info....................")
    name_from_form = int(request.POST['number'])
 
    if name_from_form != 79:
        name_from_form = "your number isnt here"
    context = {
        "name_from_form" : name_from_form,
    
    
        }
    return render(request,"win.html",context)



