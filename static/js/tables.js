$(document).ready(function() {
   $('#datatableetl').dataTable( {
    "language": {
        "url": "/static/js/es.es.lang"
    }
    } );

    $( ".consultaapibtn" ).click(function() {
        var texto_buscar=$("#consulta").val();
        if (texto_buscar == ''){
            alert('Ingrese el codigo de proceso a Buscar');
            $( "#consulta" ).focus();
        }else{
            window.open('http://181.49.210.130:9000/api/procesos/'+texto_buscar+'/', '_blank');
        }
    });
} );