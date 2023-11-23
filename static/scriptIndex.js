document.addEventListener('DOMContentLoaded', function() {
    // Inicialize o Datepicker
    $('.datepickerElement').datepicker({
        format: 'dd/mm/yyyy',  // Formato desejado da data
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