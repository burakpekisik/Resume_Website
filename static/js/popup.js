document.querySelectorAll('.mySlides').forEach(slide => {
    slide.onclick = () => {
        document.querySelector('.popup-image').style.display = 'block';
        document.querySelector('.popup-image img').src = slide.querySelector('img').src;
    }

    document.querySelector('.popup-image span').onclick = () => {
        document.querySelector('.popup-image').style.display = 'none';

    }
});
