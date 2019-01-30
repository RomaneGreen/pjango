import sys
sys.path.append("..")

from django.contrib.auth.models import User
from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from .models import TokenTransfer,UserProfile
from renmoproj import views

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'I am not part of the homepage.')

class AddTokenPageTests(SimpleTestCase):

    def test_add_token_status_code(self):
        response = self.client.get('/account/token/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('add_token'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('add_token'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_token.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/account/token/')
        self.assertContains(response, 'Add Tokens')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/account/token/')
        self.assertNotContains(
            response, 'I am not part of the add token page.')

class SendTokenPageTests(SimpleTestCase):

    def test_send_token_status_code(self):
        response = self.client.get('send_tokens')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
         response = self.client.get(reverse('transfer_token'))
         self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('send_token/'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_token.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('send_token/')
        self.assertContains(response, 'Send Tokens')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('send_token/')
        self.assertNotContains(
            response, 'I am not part of the send token page.')



class UserProfileTests(TestCase):

    def setUp(self):
        use = User.objects.create(username='Jay',email="jay@aol.com",password="jjjjjjjjj")
        

    def test_profile_view(self):
         response = self.client.get(reverse('profile'))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'Profile')
         self.assertTemplateUsed(response, 'registration/profile.html')

    def test_profile_content(self):
        use = UserProfile.objects.get(id=1)
        expected_object_name = f'{use.name}'
        self.assertEquals(expected_object_name, '')


class TokenTransferTests(TestCase):

    def setUp(self):

        Mark = UserProfile.objects.create(name='Mark',about="jay@aol.com",tokens="5")
        tok = TokenTransfer.objects.create(sender=Mark,message="jay@aol.com",reciever="Sean",tokens='5')
        

    def test_token_transfer_view(self):
         response = self.client.get(reverse('transfer_token'))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'Profile')
         self.assertTemplateUsed(response, 'send_token.html')

  