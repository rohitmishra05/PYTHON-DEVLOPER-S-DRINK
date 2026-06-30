import re

index_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\index.html"
style_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\style.css"
js_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\main.js"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HTML INJECTIONS

# Progress bar
progress_bar_html = """
    <!-- Scroll Progress -->
    <div id="scroll-progress" class="fixed top-0 left-0 h-[2px] bg-primary z-[60] w-0 shadow-[0_0_10px_rgba(152,203,255,1)] transition-all duration-75"></div>
"""

# Navbar
navbar_html = """
    <!-- Premium Navigation -->
    <nav id="premium-nav" class="fixed top-6 left-1/2 -translate-x-1/2 z-50 glass-panel px-8 py-4 rounded-full flex gap-8 items-center shadow-[0_8px_32px_rgba(0,0,0,0.5)] border border-white/10 transition-all duration-500 transform -translate-y-24 opacity-0 hidden lg:flex">
        <a href="#intro-hero" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Home</a>
        <a href="#story" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Origin</a>
        <a href="#ingredients" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Formulation</a>
        <a href="#tech" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Hardware</a>
        <a href="#crafted" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Crafted</a>
        <a href="#inspiration" class="nav-link font-code-sm text-xs uppercase tracking-widest text-on-surface-variant hover:text-primary transition-colors duration-300">Inspiration</a>
    </nav>
"""

# Intro Hero
intro_hero_html = """
    <!-- Intro Hero Screen -->
    <div id="intro-hero" class="fixed inset-0 flex flex-col items-center justify-center z-40 pointer-events-none transition-all duration-[800ms] ease-out">
        <h1 class="font-headline-lg text-4xl md:text-6xl lg:text-8xl font-bold text-transparent bg-clip-text bg-gradient-to-br from-white to-primary tracking-tighter text-center animate-[breathe_4s_ease-in-out_infinite] drop-shadow-[0_0_25px_rgba(152,203,255,0.3)]">
            PYTHON<br/>DEVELOPER
        </h1>
        <div class="absolute bottom-12 flex flex-col items-center gap-3 text-on-surface-variant animate-bounce opacity-80">
            <span class="font-code-sm text-[10px] md:text-xs uppercase tracking-[0.3em]">Scroll to Begin</span>
            <span class="material-symbols-outlined text-sm">arrow_downward</span>
        </div>
    </div>
"""

# Back to top button
btt_html = """
    <!-- Back to Top -->
    <button id="back-to-top" class="fixed bottom-8 right-8 w-12 h-12 rounded-full glass-panel flex items-center justify-center z-50 opacity-0 translate-y-10 pointer-events-none transition-all duration-500 hover:bg-primary/20 hover:border-primary/50 group">
        <span class="material-symbols-outlined text-on-surface group-hover:text-primary transition-colors">arrow_upward</span>
    </button>
"""

if 'id="intro-hero"' not in html:
    # Insert right after the global-bg-container
    html = html.replace('</div>\n\n    <div class="scroll-container">', '</div>\n' + progress_bar_html + navbar_html + intro_hero_html + '\n    <div class="scroll-container">')

if 'id="back-to-top"' not in html:
    html = html.replace('</body>', btt_html + '\n</body>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. CSS INJECTIONS
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Expand scroll container from 500vh to 600vh
css = css.replace('height: 500vh;', 'height: 600vh;')

new_css = """
@keyframes breathe {
    0%, 100% { transform: scale(1); filter: brightness(1); }
    50% { transform: scale(1.02); filter: brightness(1.2); }
}

.nav-link.active {
    color: theme('colors.primary') !important;
    text-shadow: 0 0 10px rgba(152, 203, 255, 0.5);
}

#scroll-canvas {
    opacity: 0;
    transition: opacity 0.1s linear;
}

html {
    scroll-behavior: smooth;
}
"""
if '@keyframes breathe' not in css:
    with open(style_path, 'a', encoding='utf-8') as f:
        f.write('\n' + new_css)


# 3. JS INJECTIONS
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the scroll event logic
new_scroll_logic = """
// Updated Scroll Logic for Intro Fade & Navigation
const introHero = document.getElementById('intro-hero');
const scrollCanvas = document.getElementById('scroll-canvas');
const premiumNav = document.getElementById('premium-nav');
const progressBar = document.getElementById('scroll-progress');
const backToTop = document.getElementById('back-to-top');
let lastScrollTop = 0;

window.addEventListener('scroll', () => {
    const scrollTop = document.documentElement.scrollTop;
    const windowHeight = window.innerHeight;
    
    // 1. Progress Bar
    const totalScrollHeight = document.documentElement.scrollHeight - windowHeight;
    const progress = (scrollTop / totalScrollHeight) * 100;
    progressBar.style.width = `${progress}%`;
    
    // 2. Intro Hero & Canvas Fade Logic
    // Intro fades out from 0 to 100vh
    const introFadeFraction = Math.max(0, Math.min(1, scrollTop / windowHeight));
    
    if (scrollTop < windowHeight) {
        introHero.style.opacity = 1 - (introFadeFraction * 1.5); // fade out slightly faster
        introHero.style.transform = `scale(${1 + introFadeFraction * 0.1})`;
        scrollCanvas.style.opacity = introFadeFraction;
    } else {
        introHero.style.opacity = 0;
        scrollCanvas.style.opacity = 1;
    }

    // 3. Scrub Animation Logic (mapped from 100vh to 600vh)
    const maxScrollTop = document.querySelector('.scroll-container').scrollHeight - windowHeight;
    const animStartScroll = windowHeight; // 100vh
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
    
    // 4. Navigation Bar Auto-Hide Logic
    if (scrollTop > windowHeight) {
        // Show navbar on scroll up, hide on scroll down
        if (scrollTop < lastScrollTop) {
            premiumNav.style.transform = 'translateY(0) translateX(-50%)';
            premiumNav.style.opacity = 1;
            premiumNav.style.pointerEvents = 'auto';
        } else {
            premiumNav.style.transform = 'translateY(-150%) translateX(-50%)';
            premiumNav.style.opacity = 0;
            premiumNav.style.pointerEvents = 'none';
        }
    } else {
        // Hide at the very top
        premiumNav.style.transform = 'translateY(-150%) translateX(-50%)';
        premiumNav.style.opacity = 0;
        premiumNav.style.pointerEvents = 'none';
    }
    
    // 5. Back to top visibility
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

// Anchor smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if(targetId === '#intro-hero') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } else if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Scroll Spy for active navigation links
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

// Back to top functionality
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Initial trigger to set canvas opacity correctly on load
window.dispatchEvent(new Event('scroll'));
"""

# Replace the old scroll listener
js = re.sub(r"window\.addEventListener\('scroll', \(\) => \{[\s\S]*?\}\);", new_scroll_logic, js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Applied production polish (HTML, CSS, JS).")
