const text = document.querySelector(".sec-text");

const textLoad = () => {
    setTimeout(() => {
        text.textContent = "ALİ BURAK PEKIŞIK";
    }, 0);
    setTimeout(() => {
        text.textContent = "DEVELOPER";
    }, 4000);
    setTimeout(() => {
        text.textContent = "STUDENT";
    }, 8000);
}

textLoad();
setInterval(textLoad, 12000);