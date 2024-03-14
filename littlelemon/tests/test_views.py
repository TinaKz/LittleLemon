from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        for i in range(3):
            Menu.objects.create(Title = f"Menu{i}",
        Price = i,
        Inventory = i
    )
            
    def test_getall(self):
        self.assertEqual(Menu.objects.count(), 3)