import re

index_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\index.html"
style_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\style.css"
js_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\main.js"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_sections_html = """
<!-- Crafted With Passion -->
<section class="relative py-section-gap w-full bg-transparent" id="crafted">
    <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop w-full text-center mb-24 reveal-up">
        <h2 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-on-surface font-semibold mb-4">Crafted With Passion</h2>
        <p class="font-code-sm text-code-sm text-on-surface-variant uppercase tracking-widest">The Architecture of Energy</p>
    </div>
    
    <div class="max-w-4xl mx-auto px-margin-mobile md:px-margin-desktop relative">
        <!-- Timeline line -->
        <div class="absolute left-[39px] md:left-1/2 top-0 bottom-0 w-1 bg-surface-variant/50 transform md:-translate-x-1/2 rounded-full hidden sm:block"></div>
        
        <!-- Timeline Item 1 -->
        <div class="relative flex flex-col md:flex-row items-center justify-between mb-16 reveal-up group">
            <div class="w-full md:w-5/12 text-left md:text-right mb-6 md:mb-0 order-2 md:order-1">
                <h3 class="font-headline-lg text-2xl font-semibold text-primary mb-2">01. Requirement Gathering</h3>
                <p class="font-body-md text-on-surface-variant">Before the first drop was synthesized, we analyzed the critical dependencies of a developer's workflow: focus, endurance, and flow state.</p>
            </div>
            <div class="absolute left-4 md:left-1/2 transform -translate-x-1/2 w-12 h-12 rounded-full glass-panel flex items-center justify-center z-10 group-hover:ambient-glow transition-all duration-500 order-1 hidden sm:flex">
                <span class="material-symbols-outlined text-primary">psychology</span>
            </div>
            <div class="w-full md:w-5/12 order-3"></div>
        </div>

        <!-- Timeline Item 2 -->
        <div class="relative flex flex-col md:flex-row items-center justify-between mb-16 reveal-up group">
            <div class="w-full md:w-5/12 order-2 md:order-1"></div>
            <div class="absolute left-4 md:left-1/2 transform -translate-x-1/2 w-12 h-12 rounded-full glass-panel flex items-center justify-center z-10 group-hover:ambient-glow-yellow transition-all duration-500 order-1 hidden sm:flex">
                <span class="material-symbols-outlined text-secondary">science</span>
            </div>
            <div class="w-full md:w-5/12 text-left mb-6 md:mb-0 order-3">
                <h3 class="font-headline-lg text-2xl font-semibold text-secondary mb-2">02. Synthesizing the Core</h3>
                <p class="font-body-md text-on-surface-variant">We architected a proprietary blend of nootropics and clean caffeine. It's not just energy; it's a meticulously compiled formula for your brain.</p>
            </div>
        </div>

        <!-- Timeline Item 3 -->
        <div class="relative flex flex-col md:flex-row items-center justify-between reveal-up group">
            <div class="w-full md:w-5/12 text-left md:text-right mb-6 md:mb-0 order-2 md:order-1">
                <h3 class="font-headline-lg text-2xl font-semibold text-primary mb-2">03. Refactoring Taste</h3>
                <p class="font-body-md text-on-surface-variant">A premium fuel requires a premium UX. We iterated over hundreds of flavor profiles to achieve a crisp, refreshing taste that never causes a crash.</p>
            </div>
            <div class="absolute left-4 md:left-1/2 transform -translate-x-1/2 w-12 h-12 rounded-full glass-panel flex items-center justify-center z-10 group-hover:ambient-glow transition-all duration-500 order-1 hidden sm:flex">
                <span class="material-symbols-outlined text-primary">done_all</span>
            </div>
            <div class="w-full md:w-5/12 order-3"></div>
        </div>
    </div>
</section>

<!-- Developer Inspiration -->
<section class="relative py-section-gap w-full bg-transparent overflow-hidden" id="inspiration">
    <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop w-full grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        
        <!-- Terminal UI -->
        <div class="reveal-up order-2 lg:order-1">
            <div class="glass-panel rounded-2xl overflow-hidden ambient-glow shadow-2xl border-[0.5px] border-white/20">
                <!-- Terminal Header -->
                <div class="bg-black/40 px-4 py-3 border-b border-white/10 flex items-center gap-2">
                    <div class="w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div class="w-3 h-3 rounded-full bg-green-500"></div>
                    <span class="ml-4 font-code-sm text-xs text-on-surface-variant">developer_mindset.py</span>
                </div>
                <!-- Terminal Body -->
                <div class="p-6 font-code-sm text-sm md:text-base leading-relaxed bg-black/60 min-h-[250px] relative">
                    <pre class="m-0"><code id="typewriter-code" class="text-white/90"></code><span class="animate-pulse absolute w-2 h-5 bg-primary ml-1 inline-block align-middle" id="typewriter-cursor"></span></pre>
                </div>
            </div>
        </div>

        <!-- Quote Grid -->
        <div class="order-1 lg:order-2 reveal-up">
            <h2 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-on-surface font-semibold mb-6">Fuel for the Mind</h2>
            <p class="font-body-md text-body-md text-on-surface-variant mb-10">
                Energy isn't just physical. True greatness is compiled through consistency, curiosity, and an unwavering passion for building the future.
            </p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="glass-panel p-5 rounded-xl hover:-translate-y-1 transition-transform duration-300">
                    <p class="font-body-md italic text-on-surface">"Every bug teaches something."</p>
                </div>
                <div class="glass-panel p-5 rounded-xl hover:-translate-y-1 transition-transform duration-300 sm:translate-y-4">
                    <p class="font-body-md italic text-primary">"Small commits build legendary products."</p>
                </div>
                <div class="glass-panel p-5 rounded-xl hover:-translate-y-1 transition-transform duration-300">
                    <p class="font-body-md italic text-on-surface">"Code today. Inspire tomorrow."</p>
                </div>
                <div class="glass-panel p-5 rounded-xl hover:-translate-y-1 transition-transform duration-300 sm:translate-y-4">
                    <p class="font-body-md italic text-secondary">"Consistency compiles success."</p>
                </div>
            </div>
        </div>
        
    </div>
    
    <!-- Floating Particles for this section -->
    <div class="absolute inset-0 pointer-events-none z-[-1] overflow-hidden">
        <div class="particle absolute w-1 h-1 bg-primary rounded-full blur-[1px] top-1/4 left-1/4 animate-[float_8s_infinite]"></div>
        <div class="particle absolute w-2 h-2 bg-secondary rounded-full blur-[2px] top-3/4 left-1/3 animate-[float_12s_infinite_reverse]"></div>
        <div class="particle absolute w-1.5 h-1.5 bg-primary rounded-full blur-[1px] top-1/2 right-1/4 animate-[float_10s_infinite]"></div>
        <div class="particle absolute w-1 h-1 bg-white rounded-full blur-[1px] top-1/3 right-1/3 animate-[float_9s_infinite_reverse]"></div>
    </div>
</section>
"""

# Insert before <!-- Creator Section -->
if 'id="crafted"' not in html:
    html = html.replace('<!-- Creator Section -->', new_sections_html + '\n<!-- Creator Section -->')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

# CSS Update
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Typewriter syntax highlighting classes */
.syntax-keyword { color: #ff7b72; text-shadow: 0 0 8px rgba(255,123,114,0.4); }
.syntax-function { color: #d2a8ff; text-shadow: 0 0 8px rgba(210,168,255,0.4); }
.syntax-string { color: #a5d6ff; text-shadow: 0 0 8px rgba(165,214,255,0.4); }
.syntax-comment { color: #8b949e; font-style: italic; }
.syntax-operator { color: #79c0ff; text-shadow: 0 0 8px rgba(121,192,255,0.4); }

@keyframes float {
    0%, 100% { transform: translateY(0) translateX(0); opacity: 0.3; }
    50% { transform: translateY(-20px) translateX(10px); opacity: 0.8; }
}
"""

if '.syntax-keyword' not in css:
    with open(style_path, 'a', encoding='utf-8') as f:
        f.write('\n' + new_css)

# JS Update
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
// Typewriter effect
const codeSnippet = `<span class="syntax-keyword">while</span> dream:
    <span class="syntax-function">learn</span>()
    <span class="syntax-function">build</span>()
    <span class="syntax-function">repeat</span>()

success <span class="syntax-operator">+=</span> consistency
failure <span class="syntax-operator">-=</span> excuses`;

const typewriterEl = document.getElementById('typewriter-code');
if (typewriterEl) {
    let i = 0;
    let isTag = false;
    let text = "";
    
    function typeWriter() {
        if (i < codeSnippet.length) {
            let char = codeSnippet.charAt(i);
            if (char === '<') isTag = true;
            
            text += char;
            typewriterEl.innerHTML = text;
            i++;
            
            if (char === '>') isTag = false;
            
            if (isTag) {
                typeWriter();
            } else {
                setTimeout(typeWriter, Math.random() * 50 + 20);
            }
        }
    }
    
    const observer2 = new IntersectionObserver((entries) => {
        if(entries[0].isIntersecting) {
            typeWriter();
            observer2.disconnect();
        }
    }, { threshold: 0.5 });
    
    observer2.observe(document.getElementById('inspiration'));
}
"""

if 'typewriter-code' not in js:
    with open(js_path, 'a', encoding='utf-8') as f:
        f.write('\n' + new_js)

print("Updated HTML, CSS, and JS.")
