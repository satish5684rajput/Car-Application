from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
import json
import datetime

from car_sales.models import SalesRecords, Customer
from car_sales.utils import return_response, getMonthlyRecords


class HomePageView(View):
	"""
    This is home page view and this is for rendering home page template
	"""
	def get(self, request):	
		records = [SalesRecords.objects.first()]
		customers = Customer.objects.all()
		return render(request, 'home.html', {'records': records, 'customers':customers})

class SaleRecord(View):
	def get(self, request):
		try:
			records = SalesRecords.objects.select_related('customer').filter(
											Q(pk=request.GET.get('id')) | 
											Q(customer=request.GET.get('id')))
			if not records:
				message = "No Record Found"
			else:
				message = str(len(records))+" Records Found"
			return return_response(success=True, message=message, data=records)
		except:
			return return_response(success=False, message="Something Went Wrong")

	def post(self, request):		
		form_data = request.POST
		if int(form_data.get('selling_price')) > 1000000:
			return return_response(success=False, 
					message="Selling Price Should Not Be More Than 1 Million")
		else:
			try:
				record = SalesRecords.objects.create(
				date_of_purchase=datetime.datetime.strptime(form_data.get('purchase_date'), '%Y-%m-%d'), 
				customer=Customer.objects.get(pk=form_data.get('customer_id')), 
				fuel=form_data.get('fuel'),
				vehicle_segment=form_data.get('vehicle_segment'),
				selling_price=form_data.get('selling_price'), 
				power_steering=form_data.get('power_steering'),
				air_bugs=form_data.get('air_bugs'),
				sun_roof=form_data.get('sun_roof'),
				Matt_finish=form_data.get('matt_finish'),
				music_system=form_data.get('music_system'))
				return return_response(success=True, message="Record Created Successfully", data=[record])
			except:
				return return_response(success=False, message="Record Not Created Successfully")

class CustomerRecord(View):
	def post(self, request):
		if Customer.objects.filter(pk=request.POST.get('customer_id')).count() > 0:
			return return_response(success=False, message="Customer Id Already Exist")
		else:
			try:
				Customer.objects.create(
					customer_id=request.POST.get('customer_id'),
					customer_gender=request.POST.get('customer_gender'),
					customer_income_group=request.POST.get('customer_income_group'),
					customer_region=request.POST.get('customer_region'),
					customer_marital_status=request.POST.get('customer_marital_status'))
				return return_response(success=True, 
										message="Customer Created Successfully")
			except:
				return return_response(success=False, message="Customer Not Created Successfully")

class UpdateSaleRecord(View):

	def post(self, request):
		form_data = request.POST
		if int(form_data.get('selling_price')) > 1000000:
			return return_response(success=False, 
					message="Selling Price should not be more than 1 million")
		records = SalesRecords.objects.filter(sales_id=form_data.get('sales_id'))
		if records.exists():
			try:
				records.update(
					customer=form_data.get('customer_id'), 
					fuel=form_data.get('fuel'),
					vehicle_segment=form_data.get('vehicle_segment'),
					selling_price=form_data.get('selling_price'), 
					power_steering=form_data.get('power_steering'),
					air_bugs=form_data.get('air_bugs'),
					sun_roof=form_data.get('sun_roof'),
					Matt_finish=form_data.get('matt_finish'),
					music_system=form_data.get('music_system'))
				return return_response(success=True, message="Record Updated successfully", data=records)
			except:
				return return_response(success=False, message="Record Not Updated")
		else:
			return return_response(success=False, message="Record Not Found")

class DeleteSaleRecord(View):

	def get(self, request):
		post_data = request.GET
		records = SalesRecords.objects.filter(sales_id=post_data.get('sales_id'))
		if records.exists():
			try:
				records.delete()
				return return_response(success=True, message="Record Deleted successfully", data=records)
			except:
				return return_response(success=False, message="Record Not Deleted")
		else:
			return return_response(success=False, message="Record Not Found")

class GraphRecords(View):
	def get(self, request):
		post_data = request.GET
		try:
			label = 'label'
			data = getMonthlyRecords()
			from django.http import HttpResponse
			response = {'success': True, 'message': "", 'records': data}
			return HttpResponse(json.dumps(response), content_type='application/json')
		except:
			return return_response(success=False, message="No Record Found")
		else:
			return return_response(success=False, message="Record Not Found")

