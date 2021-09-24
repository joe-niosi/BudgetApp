from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .utils import get_plot

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    qs = ExpenseItem.objects.all()
    x = [x.title for x in qs]
    y = [y.expense for y in qs]
    chart = get_plot(x,y)
    user = User.objects.get(id = request.session['user_id'])
    all_expenses = ExpenseItem.objects.all()
    expenses =  ExpenseItem.objects.filter()
    
    context = {
        'user':user,
        'all_expenses': all_expenses,
        'chart': chart
    }
    return render(request, 'home.html', context)



def add_expense(request):
    if 'user_id' not in request.session:
        messages.error(request, "Access Denied, must be logged in!")
        return redirect('/')
    errors = ExpenseItem.objects.ExpenseItem_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')

    else:
        user = User.objects.get(id = request.session['user_id'])
        income = ExpenseItem.objects.create(
            title = request.POST['title'],
            expense = request.POST['expense'],
            user = User.objects.get(id = request.session['user_id'])   
        )
    return redirect('/home')

def delete_expense(request, expense_id ):
    if 'user_id' not in request.session:
        messages.error(request, "Access Denied, must be logged in!")
        return redirect('/')
    expense_to_delete = ExpenseItem.objects.get(id = expense_id)
    expense_to_delete.delete()
    return redirect('/home')

def edit_expense(request, expense_id):
    one_expense = ExpenseItem.objects.get(id = expense_id)
    context = {
        'expense': one_expense
    }
    return render(request, "edit.html", context)

def update_expense(request, expense_id):
    errors = ExpenseItem.objects.ExpenseItem_validator(request.POST)
    if errors:
        for(key, value) in errors.items():
            messages.error(request, value)
            return redirect('/home')
    expense_to_update = ExpenseItem.objects.get(id = expense_id)
    expense_to_update.title = request.POST['title']
    expense_to_update.expense = request.POST['expense']
    expense_to_update.save()
    return redirect('/home')