// Custom Chart Configurations
document.addEventListener('DOMContentLoaded', function() {
    // Animación de contadores
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const increment = target / 100;
        
        const updateCounter = () => {
            const c = +counter.innerText;
            if(c < target) {
                counter.innerText = Math.ceil(c + increment);
                setTimeout(updateCounter, 20);
            } else {
                counter.innerText = target;
            }
        };
        updateCounter();
    });
});

