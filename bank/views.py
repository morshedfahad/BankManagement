from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def staff_home(request):
    return render(request,'staff_home.html')

@login_required
def register_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        nid = request.POST['nid']
        f_name = request.POST['f_name']
        m_name = request.POST['m_name']
        occupation = request.POST['occupation']
        email = request.POST['email']
        gender = request.POST['gender']
        acc_no = request.POST['acc_no']
        acc_type = request.POST['acc_type']
        mobile_no = request.POST['mobile_no']
        city = request.POST['city']
        customer = Customer(name=name, dob=dob, nid=nid, f_name=f_name, m_name=m_name, occupation=occupation, email=email, gender=gender, account_number=acc_no, acc_type=acc_type, mobile_no=mobile_no,
        city=city, balance=0 )
        customer.save()
        return redirect('staff_home')
    else:
        return render(request,'register_customer.html')


def deposit(request):
    if request.method =='POST':
        name = request.POST.get('name')
        acc_no = request.POST.get('acc_no')
        amount = int(request.POST.get('deposit_amount'))
    
        customer = Customer.objects.filter(name=name,account_number=acc_no)[0]

        customer.balance += amount
        customer.save()
        return render(request,'deposit.html',{'customer':customer})
        
    else:
        return render(request,'deposit.html')

def withdraw(request):
    if request.method =='POST':
        name = request.POST.get('name')
        acc_no = request.POST.get('acc_no')
        amount = int(request.POST.get('withdraw_amount'))
        
        customer = Customer.objects.filter(name=name,account_number=acc_no)[0]

        customer.balance -= amount
        customer.save()
        return render(request,'withdraw.html',{'customer':customer})
        
    else:
        return render(request,'withdraw.html')

def transfer_money(request):
    if request.method =='POST':
        from_name = request.POST.get('from_name')
        to_name = request.POST.get('to_name')
        from_acc_no = request.POST.get('from_acc_no')
        to_acc_no = request.POST.get('to_acc_no')
        amount = int(request.POST.get('transfer_amount'))
    
        from_customer = Customer.objects.filter(name=from_name,account_number=from_acc_no)[0]
        to_customer = Customer.objects.filter(name=to_name,account_number=to_acc_no)[0]

        from_customer.balance -= amount
        to_customer.balance += amount
        from_customer.save()
        to_customer.save()
        return render(request,'transfer_money.html',{'from_customer':from_customer, 'to_customer':to_customer})
        
    else:
        return render(request,'transfer_money.html')


def statement(request):
    if request.method =='POST':
        #name = request.POST.get('name')
        acc_no = request.POST.get('acc_no')
        amount = (request.POST.get('deposit_amount'))
        #f_date = request.POST.get('f_date')
        #t_date = request.POST.get('t_date')
        nm = request.POST.get('c_name')
        customer = Customer.objects.filter(account_number=acc_no)[0]
        customer.name == nm
        customer.balance == amount
        
        return render(request,'statement.html',{'customer':customer})
        
    else:
        return render(request,'statement.html')




# def statement(request):

#     if request.method=='POST':
#         acc_no = request.POST.get('acc_no')
#         amount = int(request.POST('amount')) 

#         # acc_type = request.POST.get['acc_type']
#         # f_date = request.POST.get['f_date']
#         # t_date = request.POST.get['t_date']
       

#         Customer = Customer.objects.filter(acc_no="acc_no").order_by("date")
#         Customer.balance = amount
#         Customer.save()
    
#         return render(request,'statement.html',{'customer':Customer,})
#     else: 

#         return render(request,'statement.html') 