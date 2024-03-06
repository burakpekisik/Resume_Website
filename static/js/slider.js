var slideIndex = -1;
var slideTimer; // otomatik geçiş zamanlayıcısı

showSlides();

function plusSlides(n) {
    clearTimeout(slideTimer); // slayt değiştiğinde zamanlayıcıyı sıfırla
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    clearTimeout(slideTimer); // slayt değiştiğinde zamanlayıcıyı sıfırla
    showSlides(slideIndex = n - 1); // index 0'dan başladığı için n - 1 olarak ayarlayın
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");

    // Eğer n verilmediyse veya n undefined ise, slideIndex'i bir arttır.
    if (n === undefined) {
        slideIndex++;
    } else {
        slideIndex = n;
    }

    // slideIndex, sıfır ise, en son slayda gitmek için slides.length'e ayarla.
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    }
    // slideIndex negatif ise, en son slayda gitmek için slides.length - 1'e ayarla.
    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }

    // Tüm slaytları gizle
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // Aktif noktayı kaldır
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    // Aktif slaydı göster
    slides[slideIndex].style.display = "block";
    dots[slideIndex].className += " active";

    // Otomatik olarak slaydı değiştir
    slideTimer = setTimeout(showSlides, 5000);
}
