$(document).ready( function () {
    $('#table').DataTable( {
        'scrollX': true,
        'scrollCollapse': true,
        'autoWidth': false,
        'columnDefs': [
            { width: '100px', targets: 0 }
        ],
        'order': [[0, 'desc']]
    } );
} );