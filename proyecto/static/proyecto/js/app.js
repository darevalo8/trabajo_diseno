$(document).ready(function){
	//$('#example').DataTable( );

	$('#example').dataTable( {
		"columnDefs": [
			{
				"targets": [2],
				"visible": false,
				"searchable": false
			},
			{
				"targets": [3],
				"visible": false
			}
		]
	});

	var table = $('#example').DataTable( );

	$('a.toggle-vis').on('click', function (e) {
		e.preventDefault();

		var column = table.column( $(this).attr('data-column'));

		column.visible( ! column.visible());
	});

	$('#example tfoot th').each( function () {
		var title = $('#example thead th').eq( $(this).index() ).text();
		$(this).html('<input type="text" placeholder="search '+title+'" />');
	});

	table.columns().eq(0).each( function (colIdx ){
		$('input', table.column(colIdx).footer()).on('keyup change', function () {
			table
				.column(colIdx)
				.search(this.value)
				.draw();
		});
	});
		
};

