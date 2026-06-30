gsap.registerPlugin(ScrollTrigger, TextPlugin);

const canvas = document.getElementById('scroll-canvas');
const context = canvas.getContext('2d');

// Frame config
const frameCount = 240;
const currentFrame = index => (
  `public/frames/ezgif-frame-${index.toString().padStart(3, '0')}.jpg`
);

// Preload images
const images = [];
let imagesLoaded = 0;

for (let i = 1; i <= frameCount; i++) {
    const img = new Image();
    img.src = currentFrame(i);
    img.onload = () => {
        imagesLoaded++;
        if (imagesLoaded === 1) {
            drawFrame(1);
        }
    };
    images.push(img);
}

// Function to draw image and maintain aspect ratio
function drawFrame(index) {
    if (!images[index - 1] || !images[index - 1].complete) return;
    
    const img = images[index - 1];
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const canvasRatio = canvas.width / canvas.height;
    const imgRatio = img.width / img.height;
    
    let drawWidth, drawHeight, offsetX, offsetY;
    
    if (canvasRatio > imgRatio) {
        drawWidth = canvas.width;
        drawHeight = canvas.width / imgRatio;
        offsetX = 0;
        offsetY = (canvas.height - drawHeight) / 2;
    } else {
        drawWidth = canvas.height * imgRatio;
        drawHeight = canvas.height;
        offsetX = (canvas.width - drawWidth) / 2;
        offsetY = 0;
    }
    
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
}

const introHero = document.getElementById('intro-hero');
const scrollCanvas = document.getElementById('scroll-canvas');
const premiumNav = document.getElementById('premium-nav');
const progressBar = document.getElementById('scroll-progress');
const backToTop = document.getElementById('back-to-top');
let lastScrollTop = 0;

window.addEventListener('scroll', () => {
    const scrollTop = document.documentElement.scrollTop;
    const windowHeight = window.innerHeight;
    
    const totalScrollHeight = document.documentElement.scrollHeight - windowHeight;
    const progress = (scrollTop / totalScrollHeight) * 100;
    progressBar.style.width = `${progress}%`;
    
    const introFadeFraction = Math.max(0, Math.min(1, scrollTop / windowHeight));
    
    if (scrollTop < windowHeight) {
        introHero.style.opacity = 1 - (introFadeFraction * 1.5);
        introHero.style.transform = `scale(${1 + introFadeFraction * 0.1})`;
        scrollCanvas.style.opacity = introFadeFraction;
    } else {
        introHero.style.opacity = 0;
        scrollCanvas.style.opacity = 1;
    }

    const maxScrollTop = document.querySelector('.scroll-container').scrollHeight - windowHeight;
    const animStartScroll = windowHeight;
    const animScrollRange = maxScrollTop - animStartScroll;
    
    let scrollFraction = 0;
    if (scrollTop >= animStartScroll) {
        scrollFraction = Math.max(0, Math.min(1, (scrollTop - animStartScroll) / animScrollRange));
    }
    
    const frameIndex = Math.min(
        frameCount - 1,
        Math.floor(scrollFraction * frameCount)
    );
    
    requestAnimationFrame(() => drawFrame(frameIndex + 1));
    
    if (scrollTop > windowHeight) {
        premiumNav.style.transform = 'translateY(0) translateX(-50%)';
        premiumNav.style.opacity = 1;
        premiumNav.style.pointerEvents = 'auto';
    } else {
        premiumNav.style.transform = 'translateY(-150%) translateX(-50%)';
        premiumNav.style.opacity = 0;
        premiumNav.style.pointerEvents = 'none';
    }
    
    if (scrollTop > windowHeight * 2) {
        backToTop.style.opacity = 1;
        backToTop.style.transform = 'translateY(0)';
        backToTop.style.pointerEvents = 'auto';
    } else {
        backToTop.style.opacity = 0;
        backToTop.style.transform = 'translateY(10px)';
        backToTop.style.pointerEvents = 'none';
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if(targetId === '#intro-hero') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } else if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

const sections = document.querySelectorAll('section, #intro-hero');
const navLinks = document.querySelectorAll('.nav-link');

const spyObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${entry.target.id}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}, { threshold: 0.3 });

sections.forEach(section => spyObserver.observe(section));

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

window.dispatchEvent(new Event('scroll'));

window.addEventListener('resize', () => {
    const scrollTop = document.documentElement.scrollTop;
    const maxScrollTop = document.querySelector('.scroll-container').scrollHeight - window.innerHeight;
    let scrollFraction = scrollTop / maxScrollTop;
    if (isNaN(scrollFraction)) scrollFraction = 0;
    
    const frameIndex = Math.min(
        frameCount - 1,
        Math.floor(scrollFraction * frameCount)
    );
    
    drawFrame(frameIndex + 1);
});

function initObserver() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal-up').forEach(el => {
        observer.observe(el);
    });
}

if (document.readyState === 'loading') {
    document.addEventListener("DOMContentLoaded", initObserver);
} else {
    initObserver();
}

const codeSnippet = `<span class="syntax-keyword">while</span> dream:
    <span class="syntax-function">learn</span>()
    <span class="syntax-function">build</span>()
    <span class="syntax-function">repeat</span>()

success <span class="syntax-operator">+=</span> consistency
failure <span class="syntax-operator">-=</span> excuses`;

const typewriterEl = document.getElementById('typewriter-code');
if (typewriterEl) {
    let i = 0;
    let text = "";
    typewriterEl.innerHTML = "";
    let isTyping = false;
    
    function typeWriter() {
        if (i < codeSnippet.length) {
            if (codeSnippet.charAt(i) === '<') {
                const closeIndex = codeSnippet.indexOf('>', i);
                if (closeIndex !== -1) {
                    text += codeSnippet.substring(i, closeIndex + 1);
                    i = closeIndex + 1;
                } else {
                    text += codeSnippet.charAt(i);
                    i++;
                }
            } else {
                text += codeSnippet.charAt(i);
                i++;
            }
            typewriterEl.innerHTML = text;
            setTimeout(typeWriter, Math.random() * 40 + 10);
        }
    }
    
    ScrollTrigger.create({
        trigger: "#inspiration",
        start: "top 70%",
        onEnter: () => {
            if (!isTyping) {
                isTyping = true;
                typeWriter();
            }
        },
        once: true
    });
}


// GSAP Footer Animations
if (document.getElementById('cinematic-footer')) {
    gsap.to('.gsap-footer-item', {
        scrollTrigger: {
            trigger: '#cinematic-footer',
            start: 'top 80%',
        },
        y: 0,
        opacity: 1,
        duration: 1.2,
        stagger: 0.2,
        ease: 'power3.out'
    });
}

// Set current year
const yearEl = document.getElementById('copyright-year');
if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
}
