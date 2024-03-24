document.addEventListener("DOMContentLoaded", function() {
    let scrollLinks = document.querySelectorAll('.scroll-link');

    scrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            let targetId = this.getAttribute('data-target');
            let targetSection = document.querySelector(targetId);

            if (targetSection) {
                let offsetTop = targetSection.offsetTop;

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Highlight active navbar link based on scroll position
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('.scroll-link');

    window.addEventListener('scroll', () => {
        let currentSection = '';

        sections.forEach(sec => {
            const sectionTop = sec.offsetTop;
            const sectionHeight = sec.offsetHeight;

            if (pageYOffset >= sectionTop - sectionHeight * 0.25) {
                currentSection = sec.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-target') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });
});