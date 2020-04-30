from django.db import models

# Create your models here.

class Customer(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("OTHER", "Other")
    ]

    INCOME_GROUP = [
        ("L", "0- $25K"),
        ("M", "$25-$70K"),
        ("U", ">$70K")
    ]

    REGION_CHOICES = [
        ("N", "North"),
        ("S", "South"),
        ("E", "East"),
        ("W", "West")
    ]

    MARITAL_STATUS = [
        (1, "Yes"),
        (0, "No")
    ]

    customer_id = models.IntegerField(primary_key=True, unique=True)
    customer_gender = models.CharField(choices=GENDER_CHOICES, max_length=500)
    customer_income_group = models.CharField(choices=INCOME_GROUP, max_length=100)
    customer_region = models.CharField(choices=REGION_CHOICES, max_length=100)
    customer_marital_status = models.CharField(choices=MARITAL_STATUS, max_length=100)


class SalesRecords(models.Model):

    FUEL_CHOICES = [
        ("C", "CNG"),
        ("P", "Petrol"),
        ("D", "Diesel")
    ]

    BOOLEAN_CHOICES = [
        ('Yes', 1),
        ('No', 0)
    ]

    sales_id = models.AutoField(primary_key=True, unique=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    fuel = models.CharField(choices=FUEL_CHOICES, max_length=100, blank=True, null=True)
    vehicle_segment = models.CharField(max_length=100, blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    power_steering = models.CharField(choices=BOOLEAN_CHOICES, max_length=100, blank=True, null=True)
    air_bugs = models.CharField(choices=BOOLEAN_CHOICES, max_length=100, blank=True, null=True)
    sun_roof = models.CharField(choices=BOOLEAN_CHOICES, max_length=100, blank=True, null=True)
    Matt_finish = models.CharField(choices=BOOLEAN_CHOICES, max_length=100, blank=True, null=True)
    music_system = models.CharField(choices=BOOLEAN_CHOICES, max_length=100, blank=True, null=True)

# from car_sales.models import Customer, SalesRecords
# import datetime
# import csv
# ok = 0
# with open('C:\\Users\\satish.rajput\\Desktop\\projects\\Car Application\\Car Sales\\Data.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         if ok:
#             create_record(row)
#         else:
#             ok=1


# fuel = {"CNG": "C", "Petrol": "P", "Diesel": "D"}
# def create_record(row):
#     SalesRecords.objects.create(pk=int(row[0]), 
#         date_of_purchase=datetime.datetime.strptime(row[1], '%m/%d/%Y'), 
#         customer=get_customer(row), fuel=fuel.get(row[3]),
#         vehicle_segment=row[4],
#         selling_price=row[5], 
#         power_steering=int(row[6]),air_bugs=int(row[7]),
#         sun_roof=int(row[8]),
#         Matt_finish=int(row[9]),
#         music_system=int(row[10]))


# gender={"Male": "M", "Female": "F", "Other": "O"}
# income={"0- $25K": "L", "$25-$70K": "M", ">$70K": "U"}
# region ={"North": "N", "South": "S", "East":"E", "West": "W"}
# def get_customer(row):
#     if Customer.objects.filter(pk=int(row[2])).count() > 0:
#         ok =  Customer.objects.get(pk=int(row[2]))
#     else:
#         ok = Customer.objects.create(pk=int(row[2]), 
#                                 customer_gender=gender.get(row[11]), 
#                                 customer_income_group=income.get(row[12]), 
#                                 customer_region=region.get(row[13]), 
#                                 customer_marital_status=int(row[14]))
#     return ok
# form_data = request.POST
# SalesRecords.objects.create(pk='123456', 
#         date_of_purchase=datetime.datetime.strptime(form_data.get('purchaseDate'), '%Y-%m-%d'), 
#         customer=Customer.objects.get(pk=form_data.get('customer_id')), 
#         fuel=form_data.get('fuel'),
#         vehicle_segment=form_data.get('vehicle_segment'),
#         selling_price=form_data.get('selling_price'), 
#         power_steering=form_data.get('power_steering'),
#         air_bugs=form_data.get('air_bugs'),
#         sun_roof=form_data.get('sun_roof'),
#         Matt_finish=form_data.get('Matt_finish'),
#         music_system=form_data.get('music_system'))