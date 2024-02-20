from django.shortcuts import render
from .models import Info

def index(request):
     if request.method == "POST":
         name = request.POST['name']
         email = request.POST['email']
         subject = request.POST['subject']
         message = request.POST['message']
         print(name)
         query = Info(name = name , email = email,subject = subject,message = message)
         query.save()
         
     return render(request,'index.html')
def portfolio_details(request):
    return render(request,'portfilo.html')
#def blog(request):
   # return render(request,"blog-single.html")
     
     
     