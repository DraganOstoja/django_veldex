from django.test import TestCase
from django.shortcuts import reverse
from django.contrib import auth
from kupoprodaja.models import User

class LandingPageTest(TestCase):
    
    def test_get(self):
        response= self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")

class UpdateViewTest(TestCase):
    
    def test_get(self):
        response= self.client.get(reverse("kupoprodaja:izmjena-ugovora"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "izmjena_ugovora.html")

