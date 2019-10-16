from django.http import HttpResponse
import json

from car_sales.models import SalesRecords, Customer


def return_response(success=True, message=None, data=None, status_code=200):
	if data:
		data = convert_into_json(data)
	else:
		data = []
	response = {'success': success, 'message': message, 'records': data}
	return HttpResponse(json.dumps(response), content_type='application/json', 
						status= status_code)

def convert_into_json(records):
	json_records = []
	for record in records:
		row = {'sales_id': record.sales_id,
			'date_of_purchase': str(record.date_of_purchase.date()),
			'customer_id': record.customer_id,
			'fuel': record.fuel,
			'power_steering': record.power_steering,
			'vehicle_segment': record.vehicle_segment,
			'selling_price': record.selling_price,
			'air_bugs': record.air_bugs,
			'sun_roof': record.sun_roof,
			'Matt_finish': record.Matt_finish,
			'music_system': record.music_system,
			'customer_marital_status': marital_status(record.customer.customer_marital_status),
			'customer_income_group': record.customer.get_customer_income_group_display(),
			'customer_region': record.customer.get_customer_region_display(),
			'customer_gender': record.customer.get_customer_gender_display()
			}
		json_records.append(row)
	return json_records

def marital_status(status):
	data = {1: 'Married', 0: 'Un-Married'}
	return data.get(int(status))

def getMonthlyRecords():
	records = SalesRecords.objects.values('date_of_purchase')
	month_mapping = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "June", 7: "July", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 11: "Dec"}
	month_records = {}
	for record in records:
		month = month_mapping.get(record['date_of_purchase'].month)
		if month_records.get(month):
			month_records[month] = month_records.get(month)+1
		else:
			month_records[month] = 1
	monthly_result = []
	for month in month_mapping.values():
		monthly_result.append({'y': month_records.get(month), 'label': month})
	return monthly_result


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