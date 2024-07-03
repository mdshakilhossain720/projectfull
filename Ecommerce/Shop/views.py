from django.shortcuts import render
from.models import Product
from django.views import View
from .forms import CustomeRegestion
from django.contrib import messages
from.forms import loginForm


# Create your views here.
class ProductView(View):
     def get(self,request):
      genpant=Product.objects.filter(categorty='Gp')
      tshart=Product.objects.filter(categorty='Sh')
      laptop=Product.objects.filter(categorty='Lp')


      return render(request, 'Shop/home.html',{'genpant':genpant,'tshart':tshart,'laptop':laptop})

class ProductDetails(View):
 def get(self,request,pk):
   product=Product.objects.get(pk=pk)
   return render(request, 'Shop/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request,data=None):
 if data ==None:
   lehengas =Product.objects.filter(categorty='L')
 elif data == 'lubnan' or data == 'infinity':
   lehengas =Product.objects.filter(categorty='L').filter(brand=data)
 elif data =='below':
   lehengas =Product.objects.filter(categorty='L').filter(discount_prices__gt=20000)
 
 elif data =='above':
   lehengas =Product.objects.filter(categorty='L').filter(discount_prices__lt=20000)

   
   
 return render(request, 'Shop/lehenga.html',{'lehengas':lehengas})

def login(request):
     return render(request, 'Shop/login.html')

class CustomerRegistrationView(View):
  def get(self,request):
   form=CustomeRegestion()
   return render(request, 'Shop/customerregistration.html',{'form':form})
  
  def post(self,request):
    form=CustomeRegestion()
    if form.is_valid():
      messages.success(request,'Congrations Regestions Done')
      form.save()
    return render(request, 'Shop/customerregistration.html',{'form':form})
    

def checkout(request):
 return render(request, 'Shop/checkout.html')
