$(function(){

	$('#dataTables-example').DataTable({
                responsive: true
        });


	
	$('#static-age').click(function(){
		//window.alert('fuck this shit');
		$('.static-age-modal').modal('show');
	});

	$('.filter-age').click(function(){
		//filter age
	});
	$('#static-dept').click(function(){
		//window.alert('fuck this shit');
		$('.static-dept-modal').modal('show');
	});

	$('.filter-dept').click(function(){
		//filter department
	});
})