import re

index_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\index.html"
style_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\style.css"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add WebGL shader
shader_html = """
    <div class="fixed inset-0 w-full h-full z-[-1] opacity-60 pointer-events-none" id="global-bg-container">
        <canvas id="shader-canvas-global" style="display:block;width:100%;height:100%"></canvas>
        <script>
        (function() {
          const canvas = document.getElementById('shader-canvas-global');
          function syncSize() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            if (canvas.width !== w || canvas.height !== h) {
              canvas.width  = w;
              canvas.height = h;
            }
          }
          window.addEventListener('resize', syncSize);
          syncSize();

          const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
          if (!gl) return;
          const vs = `attribute vec2 a_position;
          varying vec2 v_texCoord;
          void main() {
            v_texCoord = a_position * 0.5 + 0.5;
            gl_Position = vec4(a_position, 0.0, 1.0);
          }`;
          const fs = `precision highp float;
          varying vec2 v_texCoord;
          uniform float u_time;
          uniform vec2 u_resolution;
          uniform vec2 u_mouse;
          float noise(vec2 p) { return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
          void main() {
              vec2 uv = v_texCoord;
              vec2 mouse = u_mouse / u_resolution;
              vec3 color = vec3(0.01, 0.02, 0.05);
              for(float i = 1.0; i < 4.0; i++) {
                  float speed = u_time * 0.2 * i;
                  float y = sin(uv.x * 2.0 + speed) * 0.2 + 0.5;
                  float dist = abs(uv.y - y);
                  float glow = 0.02 / (dist + 0.01);
                  vec3 ribbonColor = (mod(i, 2.0) == 0.0) ? vec3(0.22, 0.46, 0.67) : vec3(1.0, 0.83, 0.23); 
                  color += ribbonColor * glow * 0.5;
              }
              float n = noise(uv + u_time * 0.05);
              if(n > 0.995) { color += vec3(1.0) * 0.8; }
              float mDist = distance(uv, mouse);
              color += vec3(0.2, 0.3, 0.5) * (1.0 / (mDist * 10.0 + 1.0)) * 0.3;
              gl_FragColor = vec4(color, 1.0);
          }`;
          function cs(type, src) {
            const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s;
          }
          const prog = gl.createProgram();
          gl.attachShader(prog, cs(gl.VERTEX_SHADER, vs)); gl.attachShader(prog, cs(gl.FRAGMENT_SHADER, fs));
          gl.linkProgram(prog); gl.useProgram(prog);
          const buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
          gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, 1,1]), gl.STATIC_DRAW);
          const pos = gl.getAttribLocation(prog, 'a_position'); gl.enableVertexAttribArray(pos);
          gl.vertexAttribPointer(pos, 2, gl.FLOAT, false, 0, 0);
          const uTime = gl.getUniformLocation(prog, 'u_time');
          const uRes = gl.getUniformLocation(prog, 'u_resolution');
          const uMouse = gl.getUniformLocation(prog, 'u_mouse');
          let mouse = { x: canvas.width / 2, y: canvas.height / 2 };
          window.addEventListener('mousemove', (event) => { mouse.x = event.clientX; mouse.y = window.innerHeight - event.clientY; });
          function render(t) {
            gl.viewport(0, 0, canvas.width, canvas.height);
            if (uTime) gl.uniform1f(uTime, t * 0.001);
            if (uRes) gl.uniform2f(uRes, canvas.width, canvas.height);
            if (uMouse) gl.uniform2f(uMouse, mouse.x, mouse.y);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
            requestAnimationFrame(render);
          }
          render(0);
        })();
        </script>
    </div>
"""
if 'id="global-bg-container"' not in html:
    html = html.replace('<body class="antialiased selection:bg-primary-container selection:text-on-primary-container">', 
                        '<body class="antialiased selection:bg-primary-container selection:text-on-primary-container">\n' + shader_html)

# 2. Remove hardcoded backgrounds
html = html.replace('bg-surface-container-low', 'bg-transparent')
html = html.replace('bg-background', 'bg-transparent')
html = html.replace('bg-surface-container-lowest', 'bg-transparent')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update style.css
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make body transparent so fixed bg shows
css = css.replace('background-color: #000;', 'background-color: transparent;')
css = css.replace("background-color: theme('colors.background');", "background-color: transparent;")

# Add mask to sticky-container
if '-webkit-mask-image' not in css:
    css = css.replace('overflow: hidden;', 
                      'overflow: hidden;\n    -webkit-mask-image: linear-gradient(to bottom, black 0%, black 85%, transparent 100%);\n    mask-image: linear-gradient(to bottom, black 0%, black 85%, transparent 100%);')

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated HTML and CSS.")
