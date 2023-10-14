from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        firstname =  request.POST.get('firstname')
        lastname =  request.POST.get('lastname')
        nomer =  request.POST.get('nomer')
        mail =  request.POST.get('mail')
        message =  request.POST.get('message')

        # Cохранить заявку от пользователя
    
    return render(request, "contact.html")
