from django.db import models
from django.db.models.fields import CharField
from apps.loginRegApp.models import User
import re

# Create your models here.

# Budget Validator
# class BudgetManager(models.Manager):
#     def budget_validator(self, postData):
#         errors = {}
#         if len(postData['income_title']) < 3:
#             errors["income_title"] = "Income title must be at least 3 characters!"

#         income_regex = re.compile(r'^(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])|[1-9][0-9][0-9][0-9][0-9])$') 
#         if not income_regex.match(postData['income']):
#             errors["income"] = ("Invalid budget amount, must be in range of $1-99,999")
#         return errors

# Expense Item Validator
class ExpenseItemManager(models.Manager):
    def ExpenseItem_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "Expense item title must be at least 3 characters!"

        expense_regex = re.compile(r'^(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])|[1-9][0-9][0-9][0-9][0-9])$') 
        if not expense_regex.match(postData['expense']):
            errors["expense"] = ("Invalid expense amount, must be in range of $1-99,999")

        return errors

# class Budget(models.Model):
#     income_title = models.CharField(max_length=255)
#     income = models.IntegerField() #this will be the baseline for our budget amount that expenses withdraw from
#     user = models.ForeignKey(User, related_name='budgets', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = BudgetManager()

    
class ExpenseItem(models.Model):
    title = CharField(max_length=255)
    expense = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_info', on_delete=models.CASCADE)
    objects = ExpenseItemManager()