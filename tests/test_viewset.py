import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'igmsm.settings')   
import django
django.setup()
from rest_framework import test

class EmployerTest(test.APITestCase):
    def test_viewset_EmployeeListViewset_with_admin_token(self):
        headers = {'Authorization': "Token b79a7b34eb29b3472c53de47113c7743c9d60e11"}
        response = self.client.get("http://127.0.0.1:8000/api/v1/admin/employee/", headers=headers )
        self.assertEqual(
            response.status_code, 200
        )
    def test_viewset_EmployeeListViewset_without_token(self):
        response = self.client.get("http://127.0.0.1:8000/api/v1/admin/employee/" )
        self.assertEqual(
            response.status_code, 401
        )
    def test_get_viewset_EmployeeViewset_with_admin_token(self):
        headers = {'Authorization': "Token b79a7b34eb29b3472c53de47113c7743c9d60e11"}
        response = self.client.get("http://127.0.0.1:8000/api/v1/public/employeelist/", headers=headers )
        self.assertEqual(
            response.status_code, 200
        )
    def test_get_viewset_EmployeeViewset_without_token(self):
        response = self.client.get("http://127.0.0.1:8000/api/v1/public/employeelist/" )
        self.assertEqual(
            response.status_code, 200
        )