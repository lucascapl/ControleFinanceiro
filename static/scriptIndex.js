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
    var status = '{{ status }}';
    console.log(status);
    if (status === 'success') {
        alert("Dados enviados com sucesso");
    } else if (status === 'error') {
        alert("Dados inválidos! Tente novamente");
        window.location.href = "\main";
    }
});