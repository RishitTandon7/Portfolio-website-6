css_addition = """
/* =========================================
   CERTIFICATES REDESIGN (MARQUEE + MASONRY + LIGHTBOX)
   ========================================= */

/* Marquee Container */
.marquee-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    overflow: hidden;
    padding: 2rem 0;
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    background: #18181b;
    border-top: 2px dashed #27272a;
    border-bottom: 2px dashed #27272a;
}

.marquee-track {
    display: flex;
    width: max-content;
}

.marquee-forward {
    animation: scroll-left 60s linear infinite;
}

.marquee-reverse {
    animation: scroll-right 60s linear infinite;
}

/* Pause on hover */
.marquee-track:hover {
    animation-play-state: paused;
}

.marquee-content {
    display: flex;
    gap: 2rem;
    padding-right: 2rem; /* Matches gap */
}

.marquee-item {
    height: 250px;
    width: auto;
    object-fit: cover;
    border: 4px solid #3f3f46;
    border-radius: 8px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    cursor: zoom-in;
    background: #000;
}

.marquee-item:hover {
    transform: scale(1.05) rotate(1deg);
    border-color: #ccff00;
    box-shadow: 8px 8px 0 0 rgba(204,255,0,0.5);
    z-index: 10;
}

@keyframes scroll-left {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}

@keyframes scroll-right {
    from { transform: translateX(-50%); }
    to { transform: translateX(0); }
}

/* Masonry Grid */
.masonry-grid {
    column-count: 1;
    column-gap: 1.5rem;
    padding: 1rem;
}

@media (min-width: 640px) {
    .masonry-grid { column-count: 2; }
}

@media (min-width: 1024px) {
    .masonry-grid { column-count: 3; }
}

@media (min-width: 1280px) {
    .masonry-grid { column-count: 4; }
}

.masonry-item {
    width: 100%;
    margin-bottom: 1.5rem;
    display: block;
    border: 4px solid #3f3f46;
    border-radius: 8px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    cursor: zoom-in;
    background: #000;
}

.masonry-item:hover {
    transform: scale(1.03) rotate(-1deg);
    border-color: #ff00ff;
    box-shadow: 8px 8px 0 0 rgba(255,0,255,0.5);
    z-index: 10;
}

/* Custom scrollbar specifically for gallery */
.custom-scrollbar::-webkit-scrollbar {
    width: 12px;
}
.custom-scrollbar::-webkit-scrollbar-track {
    background: #18181b;
    border-radius: 6px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #ff00ff;
    border-radius: 6px;
    border: 3px solid #18181b;
}

/* Lightbox active states */
body.lightbox-open {
    overflow: hidden; /* Prevent scrolling when lightbox is open */
}

#lightbox.active {
    opacity: 1;
    pointer-events: auto;
}

#lightbox.active #lightbox-img {
    transform: scale(1);
}
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_addition)
    
print("Added CSS for Redesign.")

# Now update the JavaScript logic in index.html
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to replace the old switchCerts and initCertsSlider logic with switchCertsView
# Let's locate the script block.

js_replacement = """            // --- Certs View Toggle Logic ---
            const certsToggle = document.getElementById('certs-toggle');
            const certsSlider = document.getElementById('certs-toggle-slider');

            function initCertsSlider() {
                const activeBtn = document.getElementById('btn-ticker');
                if(activeBtn && certsSlider) {
                    certsSlider.style.width = activeBtn.offsetWidth + 'px';
                    certsSlider.style.left = activeBtn.offsetLeft + 'px';
                }
            }
            // Init after fonts/layout settle
            setTimeout(initCertsSlider, 150);
            window.addEventListener('resize', initCertsSlider);

            window.switchCertsView = function(mode) {
                const btns = document.querySelectorAll('.certs-toggle-btn');
                const heading = document.getElementById('certs-heading');
                const targetPanel = document.getElementById('panel-' + mode);
                const targetBtn = document.getElementById('btn-' + mode);

                if(!targetBtn || !targetPanel) return;

                // Slide the indicator
                certsSlider.style.width = targetBtn.offsetWidth + 'px';
                certsSlider.style.left = targetBtn.offsetLeft + 'px';

                // Toggle color mode on wrapper
                if (mode === 'gallery') {
                    certsToggle.classList.add('mode-certifications');
                    heading.textContent = 'gallery.';
                } else {
                    certsToggle.classList.remove('mode-certifications');
                    heading.textContent = 'ticker.';
                }

                // Swap active button
                btns.forEach(b => {
                    b.classList.remove('active');
                    b.setAttribute('aria-selected', 'false');
                });
                targetBtn.classList.add('active');
                targetBtn.setAttribute('aria-selected', 'true');

                // Fade out current panel, then switch
                const currentPanel = document.querySelector('.certs-panel.active');
                if (currentPanel && currentPanel !== targetPanel) {
                    currentPanel.classList.add('fade-out');
                    setTimeout(() => {
                        currentPanel.classList.remove('active', 'fade-out');
                        targetPanel.classList.add('active');
                    }, 280);
                } else if (!currentPanel) {
                    targetPanel.classList.add('active');
                }
            };

            // --- Lightbox Logic ---
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightbox-img');
            const lightboxClose = document.getElementById('lightbox-close');
            const triggers = document.querySelectorAll('.lightbox-trigger');

            function openLightbox(src) {
                lightboxImg.src = src;
                lightbox.classList.add('active');
                document.body.classList.add('lightbox-open');
            }

            function closeLightbox() {
                lightbox.classList.remove('active');
                document.body.classList.remove('lightbox-open');
                setTimeout(() => {
                    lightboxImg.src = '';
                }, 300);
            }

            triggers.forEach(trigger => {
                trigger.addEventListener('click', (e) => {
                    e.preventDefault();
                    openLightbox(trigger.getAttribute('data-lb'));
                });
            });

            lightboxClose.addEventListener('click', closeLightbox);
            
            // Close on background click
            lightbox.addEventListener('click', (e) => {
                if(e.target === lightbox) {
                    closeLightbox();
                }
            });

            // Close on escape key
            document.addEventListener('keydown', (e) => {
                if(e.key === 'Escape' && lightbox.classList.contains('active')) {
                    closeLightbox();
                }
            });
"""

# Replace the old cert logic with the new js_replacement.
# Old logic starts at "// --- Certs Toggle Logic ---" and ends before "});" for DOMContentLoaded.
script_pattern = re.compile(r'(// --- Certs Toggle Logic ---.*?)(        \}\);\n    </script>)', re.DOTALL)

# Let's verify the script is replaced correctly
if script_pattern.search(html):
    html = script_pattern.sub(js_replacement + r'\n\2', html)
    print("Replaced JS successfully.")
else:
    print("Failed to find JS pattern. Appending to the end of the script.")
    # Fallback if pattern fails
    html = html.replace('});\n    </script>', js_replacement + '\n        });\n    </script>')

# Remove the old Floating Image Preview Element HTML that's now obsolete
html = html.replace('<img id="cert-preview-img" src="" class="fixed top-0 left-0 pointer-events-none z-[1000] opacity-0 transition-opacity duration-300 w-64 md:w-80 h-auto rounded-xl border-4 object-cover" alt="Certificate Preview" style="will-change: transform, opacity;" />', '')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
