// Counter-Strike Portfolio JS Interactions

document.addEventListener('DOMContentLoaded', () => {

    // --- Particle Background (Sparks/Dust) ---
    const canvas = document.getElementById('cs-particles');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];

        function initParticles() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            particles = [];
            // Create particles
            for (let i = 0; i < 50; i++) {
                particles.push(new Particle());
            }
        }

        class Particle {
            constructor() {
                this.reset();
                this.y = Math.random() * height; // initial random spread
            }

            reset() {
                this.x = Math.random() * width;
                this.y = height + Math.random() * 100;
                this.size = Math.random() * 2 + 0.5;
                this.speedY = Math.random() * 0.3 + 0.1;
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.opacity = Math.random() * 0.5 + 0.1;
            }

            update() {
                this.y -= this.speedY;
                this.x += this.speedX;
                // Add slight wobble
                this.x += Math.sin(this.y * 0.05) * 0.2;

                if (this.y < -10) {
                    this.reset();
                }
            }

            draw() {
                ctx.fillStyle = `rgba(229, 57, 53, ${this.opacity})`; // Red color for embers
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function animateParticles() {
            ctx.clearRect(0, 0, width, height);
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            requestAnimationFrame(animateParticles);
        }

        initParticles();
        animateParticles();

        window.addEventListener('resize', initParticles);
    }

    // --- Custom CS Crosshair ---
    const crosshair = document.getElementById('cs-crosshair');

    if (crosshair) {
        // Add a center dot dynamically to match CSS structure
        if (!crosshair.querySelector('.cs-dot')) {
            const dot = document.createElement('div');
            dot.className = 'cs-dot';
            crosshair.appendChild(dot);
        }

        let crosshairX = window.innerWidth / 2;
        let crosshairY = window.innerHeight / 2;

        document.addEventListener('mousemove', (e) => {
            crosshairX = e.clientX;
            crosshairY = e.clientY;
            crosshair.style.transform = `translate(${crosshairX}px, ${crosshairY}px)`;
        });

        // Hover effects on interactive elements
        const interactives = document.querySelectorAll('a, .cs-btn-connect, .cs-btn-view, .cs-nav-item');
        interactives.forEach(el => {
            el.addEventListener('mouseenter', () => {
                crosshair.classList.add('active');
            });
            el.addEventListener('mouseleave', () => {
                crosshair.classList.remove('active');
            });
        });

        // Click effect - adding CSS class for recoil
        document.addEventListener('mousedown', () => {
            crosshair.classList.add('recoil');
        });
        document.addEventListener('mouseup', () => {
            crosshair.classList.remove('recoil');
        });
    }

    // --- Scroll Animations (Intersection Observer) ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.scroll-hidden').forEach((el) => {
        observer.observe(el);
    });

    // Handle smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });

                // Active state management for nav
                document.querySelectorAll('.cs-nav-item').forEach(nav => nav.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });
});
