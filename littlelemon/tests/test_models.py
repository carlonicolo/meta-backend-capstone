from django.test import TestCase
from datetime import date

from restaurant.models import Menu, Booking


# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="TestMenuItem", price=80, inventory=100)
        self.assertEqual(str(item), "TestMenuItem: 80")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="TestBookingName", no_of_guests=2, booking_date=date.today())
        booking_date = date.today()
        self.assertEqual(str(item), f"TestBookingName for date: {booking_date}")
