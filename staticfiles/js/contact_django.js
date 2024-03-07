$(document).ready(function () {
    $('#contactForm').submit(function (event) {
        var form = $(this);
        event.preventDefault(); // Formun varsayılan gönderimini engelle
        $.ajax({
            type: "POST",
            url: form.attr('action'),
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                if (response.success) {
                    $('#success').modal('show'); // Başarılı durumda success modal'ını aç
                } else {
                    // Başarısız durumda bir şey yapma
                }
                },
            error: function (xhr, errmsg, err) {
                // Hata durumunda bir şey yapma
            }
        });
    });
});