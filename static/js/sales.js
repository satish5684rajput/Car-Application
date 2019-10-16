function searchRecord() {
	id = document.getElementById("search_text").value;
	$.ajax({
		type: 'GET',
		url: "sale_record/",
		data: {'id': id},
		success: function(response){
			if(response.success && (response.records.length > 0)) {
				alert(response.message)
				putRecordInTable(response.records);
			}
			else {
				alert(response.message);
				putRecordInTable([]);
			}
		}
	});
	return false;
}

function createCustomer() {
	form_data = $('#feature_req_form').serialize();
	$.ajax({
		type: 'POST',
		url: "/customer/",
		data: form_data,
		success: function(response) {
			alert(response.message)
			$('#customerRegistrationModel').modal('toggle');
			$('.customer_form_field').filter(function() { return this.value = ''});
		}
	});	
	return false;
}

function createNewRecord() {
	form_data = $('#create_sale_form').serialize();
	$('.sale_form_field').filter(function() { return this.value = ''});
	$.ajax({
		type: 'POST',
		url: "/sale_record/",
		data: form_data,
		success: function(response){
			if(response.success && (response.records.length > 0)) {
				alert(response.message);
				$('#createSaleForm').modal('toggle');
				putRecordInTable(response.records);
			}
			else {
				alert(response.message);
			}
		}
	});
	return false;
}

function openUpdateForm(record_id) {
	record_no = 'record_no_'+record_id;
	var empty = $('.customer_update_form').filter(function() { return this.value = ''});
	$('#updateSaleRecord').modal();
	var rowData = $('#'+record_no).children("td").map(function () {
        return $(this).text();
    }).get();
    $("#sales_id").val(record_id);
    $('#customer_id').val(rowData[2]);
    $('#fuel').val(rowData[3]);
    $('#vehicle_segment').val(rowData[4]);
    $('#selling_price').val(rowData[5]);  
    $('#power_steering').val(rowData[6]);
    $('#air_bugs').val(rowData[7]);
    $('#sun_roof').val(rowData[8]);
    $('#matt_finish').val(rowData[9]);
    $('#music_system').val(rowData[10]);
    
}

function updateRecord() {
	form_data = $('#update_sale_form').serialize();
	$('#updateSaleRecord').modal('toggle');
	$.ajax("/update_sale_record/", {
		type: 'POST',
		data: form_data,
		success: function(response){
			if(response.success && (response.records.length > 0)) {
				alert(response.message);
				putRecordInTable(response.records);
			}
			else {
				alert(response.message);
			}
		}
	});
	return false;
}

function deleteRecord(record_id) {
	table_record_no = '#record_no_'+record_id;
	data = {'sales_id': record_id}
	$.ajax("/delete_record/", {
		type: 'GET',
		data: data,
		success: function(response){
			if(response.success) {
				alert(response.message);
				$(table_record_no).remove();
			}
			else {
				alert(response.message);
			}
		}
	});
	return false;
}

function putRecordInTable(records) {
	$('#sales_records').empty();
	for (i = 0; i < records.length; i++) {
		record = records[i];
		record_id = record.sales_id;
		edit_button = '<button type="button" class="btn btn-default" onclick="openUpdateForm('+record_id+')">Edit</button>';
		delete_button = '<button type="button" class="btn btn-default" onclick="deleteRecord('+record_id+')">Delete</button>';
		row = '<tr id="record_no_'+record_id+'">'+
		'<td class="record_sales_id">'+record_id+'</td>'+
		'<td calss="record_date_of_purchase">'+record.date_of_purchase+'</td>'+
		'<td>'+record.customer_id+'</td>'+
		'<td>'+record.fuel+'</td>'+
		'<td>'+record.vehicle_segment+'</td>'+
		'<td>'+record.selling_price+'</td>'+
		'<td>'+record.power_steering+'</td>'+
		'<td>'+record.air_bugs+'</td>'+
		'<td>'+record.sun_roof+'</td>'+
		'<td>'+record.Matt_finish+'</td>'+
		'<td>'+record.music_system+'</td>'+
		'<td>'+record.customer_gender+'</td>'+
		'<td>'+record.customer_income_group+'</td>'+
		'<td>'+record.customer_region+'</td>'+
		'<td>'+record.customer_marital_status+'</td>'+
		'<td>'+edit_button+'</td>'+
		'<td>'+delete_button+'</td></tr>'
		$('#sales_records').append(row);
	}
}

function openCreaterRcordForm() {
	var empty = $('.create_sale_field').filter(function() { return this.value = ''});
}

function getGraphRecords() {
	$.ajax("/get_graph_records/", {
		type: 'GET',
		data: {},
		success: function(response){
			if(response.success) {
				showGraph(response.records)
			}
			else {
				alert(response.message);
			}
		}
	});
	return false;
}

function showGraph(records) {

		// Construct options first and then pass it as a parameter
		var options1 = {
			animationEnabled: true,
			title: {
				text: "Car Sales"
			},
			data: [{
				type: "column", //change it to line, area, bar, pie, etc
				legendText: "",
				showInLegend: true,
				dataPoints: records
				}]
		};

		$("#resizable").resizable({
			create: function (event, ui) {
				//Create chart.
				$("#chartContainer1").CanvasJSChart(options1);
			},
			resize: function (event, ui) {
				//Update chart size according to its container size.
				$("#chartContainer1").CanvasJSChart().render();
			}
		});
		$('#graphModal').modal();
		
}

$(".graph_close_btn").on('click', function(event){
    location.reload();
});
