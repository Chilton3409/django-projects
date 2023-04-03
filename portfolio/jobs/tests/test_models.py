from django.test import TestCase
from ..models import Expenses
import uuid


#create tests below

class ExpensesTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        #set up non modified objects
        Expenses.objects.create(id=1, expenses='a', amount=100, date='1992-02-02')

    def test_expenses_label(self):
        expense = Expenses.objects.get(id=1)
        field_label = expense._meta.get_field('expenses').verbose_name
        self.assertEqual(field_label, 'expenses')

    def test_amount_label(self):
        expense = Expenses.objects.get(id=1)
        field_label = expense._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    
    def test_get_absolute(self):
        expenses = Expenses.objects.get(expenses='a')
        self.assertEqual(expenses.get_absolute_url(), '/jobs/expensesDetail/00000000-0000-0000-0000-000000000001/details/')

    