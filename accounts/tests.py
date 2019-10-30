from django.test import TestCase
from django.apps import apps
from .apps import AccountsConfig
from .models import Profile

class TestAccountsConfig(TestCase):
    def test_accounts_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)
        
class TestViews(TestCase):
    def test_login_page(self):
        page = self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_signup_page(self):
        page = self.client.get("/accounts/signup")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "signup.html")
        
class ProfileTests(TestCase):
    
    def test_str(self):
        test_name = Profile.user(username="A profile")
        self.assertEqual(str(test_name), 'An profile')