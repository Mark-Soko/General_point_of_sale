from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def add_category(request):
    category_name= request.POST['category_name']
    category_description = request.POST['category_description']

    category1 = category(categ_name = category_name, categ_desc= category_description) 
    category1.save()
    return render(request,'dashboard.html')


def add_product(request):
    prod_name= request.POST['prod_name']
    buy_price= request.POST['buy_price']
    sell_price= request.POST['sell_price']
    prod_category= request.POST['prod_category']
    quantity= request.POST['quantity']
    
    product1 = product(prod_name =prod_name , Sell_price = sell_price ,buy_price = buy_price , prod_category = prod_category ,number_of_units = quantity) 
    product1.save()
    return render(request,'dashboard.html')


def add_customer(request):
    phone_number= request.POST['phone_number']
    cust_id = request.POST['cust_id']
    fname = request.POST['fname']
    lname = request.POST['lname']
    address = request.POST['address']

    customer1 = credited_customer(cust_contact = phone_number,cust_id = cust_id,fname = fname,lname = lname,address = address)
    customer1.save()
    return render(request,'dashboard.html')
