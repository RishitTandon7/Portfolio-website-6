import re

# We have 40 certificates: cert_1.jpg to cert_40.jpg
certs = [f"certificates/cert_{i}.jpg" for i in range(1, 41)]

# 1. Marquee (Ticker View)
# We will create 2 rows of marquees
half = len(certs) // 2
row1 = certs[:half]
row2 = certs[half:]

def build_marquee_track(images, reverse=False):
    # Duplicate the track content for seamless infinite scrolling
    img_html = ""
    for img in images:
        img_html += f'<img src="{img}" class="marquee-item hover-trigger lightbox-trigger" data-lb="{img}" alt="Certificate" />\n'
    
    # Track twice
    direction = "marquee-reverse" if reverse else "marquee-forward"
    track_html = f"""
    <div class="marquee-track {direction}">
        <div class="marquee-content">
            {img_html}
        </div>
        <div class="marquee-content" aria-hidden="true">
            {img_html}
        </div>
    </div>
    """
    return track_html

marquee_html = f"""
            <div id="panel-ticker" class="certs-panel active">
                <div class="marquee-container">
                    {build_marquee_track(row1, False)}
                    {build_marquee_track(row2, True)}
                </div>
            </div>
"""

# 2. Masonry Grid (Gallery View)
grid_items = ""
for img in certs:
    grid_items += f'<img src="{img}" class="masonry-item hover-trigger lightbox-trigger" data-lb="{img}" alt="Certificate" />\n'

masonry_html = f"""
            <div id="panel-gallery" class="certs-panel">
                <div class="neo-card pink p-4 sm:p-8 hover-trigger group h-[800px] overflow-y-auto custom-scrollbar">
                    <div class="masonry-grid">
                        {grid_items}
                    </div>
                </div>
            </div>
"""

# 3. Heading and Toggles
heading_html = f"""
            <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-12 gap-6 spring-up">
                <h2 class="font-sans text-5xl md:text-6xl font-extrabold lowercase flex items-center gap-4">
                    <span class="text-neonLime animate-spin-slow">❋</span>
                    <span id="certs-heading">certs ticker.</span>
                </h2>
                <!-- Unique Toggle -->
                <div class="certs-toggle-wrap" id="certs-toggle" role="tablist" aria-label="Certificate view toggle">
                    <div class="certs-toggle-slider" id="certs-toggle-slider"></div>
                    <button class="certs-toggle-btn active" id="btn-ticker" role="tab" aria-selected="true" onclick="switchCertsView('ticker')">
                        <span class="toggle-icon">🎞️</span>
                        ticker view
                    </button>
                    <button class="certs-toggle-btn" id="btn-gallery" role="tab" aria-selected="false" onclick="switchCertsView('gallery')">
                        <span class="toggle-icon">🖼️</span>
                        gallery view
                    </button>
                </div>
            </div>
"""

# Full Certs Block Replacement
full_certs_html = heading_html + marquee_html + masonry_html

# 4. Lightbox HTML to go before </body>
lightbox_html = """
    <!-- Lightbox Overlay -->
    <div id="lightbox" class="fixed inset-0 z-[9999] bg-black/90 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300 flex items-center justify-center p-4">
        <button id="lightbox-close" class="absolute top-6 right-6 text-white hover:text-neonPink text-4xl font-sans font-bold hover-trigger z-50 transition-colors">&times;</button>
        <img id="lightbox-img" src="" class="max-w-full max-h-full object-contain scale-95 transition-transform duration-300 border-4 border-neonPink shadow-[0_0_50px_rgba(255,0,255,0.3)]" alt="Expanded Certificate" />
    </div>
"""

# Now apply to index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the certs section inside <section id="certs"> ... </section>
certs_pattern = re.compile(r'(<section class="max-w-\[1400px\] mx-auto px-6 py-32" id="certs">\n)(.*?)(        </section>)', re.DOTALL)
html_content = certs_pattern.sub(r'\1' + full_certs_html + '\n' + r'\3', html_content)

# Inject Lightbox before </body>
html_content = html_content.replace('</body>', lightbox_html + '\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Applied HTML replacements.")
