from django.test import TestCase

from django.urls import reverse
import random
import uuid
from ..models import Expenses

class ExpensesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_expenses = 13

        for expense_id in range(number_of_expenses):
            Expenses.objects.create(id=uuid.uuid1(), amount=100, date='1992-09-08')
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/jobs/jobs')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get('jobs/jobs/')
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('/jobs/jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/jobs_list.html')
       

    