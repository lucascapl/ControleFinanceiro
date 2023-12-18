document.addEventListener('DOMContentLoaded', function() {
    // Obter a data atual
    var dataAtual = new Date();

    var dia = ('0' + dataAtual.getDate()).slice(-2);
    var mes = ('0' + (dataAtual.getMonth() + 1)).slice(-2);
    var ano = dataAtual.getFullYear();
    var dataFormatada = dia + '/' + mes + '/' + ano;

    $('.datepickerElement').val(dataFormatada);
    // Inicialize o Datepicker
    $('.datepickerElement').datepicker({
        format: 'dd/mm/yyyy',  // Formato desejado da data
        orientation: 'bottom',
        autoclose: true
    });
});