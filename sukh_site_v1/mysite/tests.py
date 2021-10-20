from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from . import views


# Create your tests here.
class MySiteTestCases(TestCase):
    def test_index_view(self):
        '''Ensures index view is reachable.'''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index_function(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_hobbies_view(self):
        '''Ensures hobbies view is reachable.'''
        response = self.client.get('/thingsIlike')
        self.assertEqual(response.status_code, 200)
    
    def test_hobbies_function(self):
        found = resolve('/thingsIlike')
        self.assertEqual(found.func, views.hobbies)
    
    def test_projects_view(self):
        '''Ensures projects view is reachable.'''
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)

    def test_projects_function(self):
        found = resolve('/projects')
        self.assertEqual(found.func, views.projects)

    def test_calculator_view(self):
        '''Ensures post view is reachable.'''
        response = self.client.post('/calculator')
        self.assertEqual(response.status_code, 200)
    

