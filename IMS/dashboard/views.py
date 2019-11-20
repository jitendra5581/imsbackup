from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return(render(request,'index.html'))
    

def purchase_view(request):
    
    return(render(request,'purchase.html'))
    


def measures_view(request):
    return(render(request,'measures.html'))
    

def product_view(request):
    return(render(request,'product.html'))
    

def inventory_product_view(request):
    return(render(request,'inventoryproduct.html'))
    

def sales_view(request):
    return(render(request,'index.html'))
    


def sales_by_inv_view(request):
    return(render(request,'index.html'))
    

def inventory_calculation_view(request):
    return(render(request,'index.html'))


def change_pwd_view(request):
    return(render(request,'index.html'))
            
def logout_view(request):
    return(render(request,'index.html'))

