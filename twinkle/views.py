from django.shortcuts import render
from django.http import HttpResponse
from twinkle.models import parents,children,payments
from twinkle.forms import parentForm , childrenForm ,payments_form
from django.views.generic import TemplateView, ListView

#from twinkle.forms import payment_form
# Create your views here.

def index(request):
    context_dict = {'boldmessage':"We grow ,We laugh ,We learn"}

    return render(request,'twinkle/index.html',context=context_dict)

def about(request):
    context_dict = {'ceo':"CHIEF EXECUTIVE OFFICER - KYOMUHENDO BETTY CONTACT 0787006984"}

    return render(request,'twinkle/about.html',context=context_dict)

def view_parent(request):

    parent_list = parents.objects.order_by('-father_firstname')
    context_dict = {'parents' : parent_list}

    return render(request,'twinkle/parents.html',context_dict)


def view_children(request):

    #######
    child_list = children.objects.order_by('-firstname')
    context_dict = {'children':child_list}

    return render(request,'twinkle/children.html',context_dict)


def register(request):
    #we create a boolean variable to help us to continue with the logic or not
    print("i have reached")

    registered = False
    
    if request.method == 'POST':
        parent_form = parentForm(data=request.POST)

        children_form = childrenForm(data=request.POST)
       
        if parent_form.is_valid() and children_form.is_valid():

            parent = parent_form.save()

            parent.save()

            children = children_form.save()

            children.parent = parent

            children.save()

            registered = True
            print("Registration successful")
        else:
            print(parent_form.errors, children_form.errors)
    else:
        parent_form = parentForm()

        children_form = childrenForm()

    return render(request,'twinkle/register.html',{'parent_form':parent_form,'children_form':children_form,registered:'registered'})



def view_payments(request):
    query = request.GET.get('child')
    kid = children.objects.filter(firstname=query)
    return render(request,'twinkle/addpayments.html',{'kid':kid})

def show_payment_history(request):
    query = request.GET.get('child')
    payment = payments.objects.filter(child=query)
    if payment:
        available = True
    else:
        available = False
    return render(request,'twinkle/show_payment_history.html',{'payment':payment})
  
def add_payments(request):
  
    if request.method =='POST':
        payments_form_one = payments_form(data=request.POST)
        if payments_form_one.is_valid():
            payments = payments_form_one.save()
            payments.save()
        else:
            print(payments_form_one.errors)
    else:
        payments_form_one = payments_form()

    return render(request,'twinkle/payments.html',{'payments_form_one':payments_form_one})
