from django.shortcuts import render,redirect
from .models import Medicine
from .forms import MedicineForm,RegisterUserForm


# Home Page
def Main(request):
    return render(request,'main.html')


# Listing All the Products
def All_Products(request):
    products = Medicine.objects.all()
    context = {
        'products' : products
    }
    return render(request,'base/All_Products.html',context)

# Creating New Products
def creat_product(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('All-Products')
    else:
        form = MedicineForm()    
    return render(request,'base/Create_Product.html',{'form':form})


# Deleting Product
def delete_product(request,pk):
    product = Medicine.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('All-Products')
    return render(request,'base/delete_product.html',{})



# Register User View
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'base/Register_Page.html', {'form': form})

# Login User

