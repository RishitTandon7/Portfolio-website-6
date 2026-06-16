import re

# Read generated chunks
with open("scratch/projects.html", "r", encoding="utf-8") as f:
    projects_html = f.read()

with open("scratch/certs.html", "r", encoding="utf-8") as f:
    certs_html = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace #projects grid
projects_pattern = re.compile(r'(<section[^>]*id="projects"[^>]*>.*?<div class="grid grid-cols-1 md:grid-cols-12 gap-6">\n)(.*?)(            </div>\n        </section>)', re.DOTALL)
content = projects_pattern.sub(r'\1' + projects_html + r'\3', content)

# 2. Replace #certs list
certs_pattern = re.compile(r'(<div id="panel-certificates" class="certs-panel active">\s*<div class="neo-card lime p-8 hover-trigger group">\s*<ul class="font-mono text-base text-zinc-300 space-y-6 max-h-\[500px\] overflow-y-auto pr-4 custom-scrollbar">\n)(.*?)(                    </ul>\s*</div>\s*</div>)', re.DOTALL)
content = certs_pattern.sub(r'\1' + certs_html + r'\3', content)

# 3. Replace #wins neo-card
wins_html = """            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- 1st Place -->
                <div class="neo-card pink p-8 flex flex-col justify-center items-center text-center hover-trigger spring-up group bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-zinc-800 to-cardBg">
                    <div class="font-sans text-7xl md:text-8xl font-extrabold text-neonPink mb-4 group-hover:scale-110 transition-transform">1st</div>
                    <div class="font-mono font-bold text-xl uppercase tracking-widest text-zinc-300">place winner</div>
                    <div class="font-mono text-sm text-zinc-400 mt-6 border-t-2 border-zinc-800 pt-6 w-full space-y-2">
                        <div>sutd smorphi (singapore)</div>
                        <div>cismohack (national)</div>
                        <div>ml project expo</div>
                        <div>south india conclave</div>
                        <div>semiconductor expo</div>
                        <div>nwc expo</div>
                    </div>
                </div>
                <!-- 2nd Place -->
                <div class="neo-card blue p-8 flex flex-col justify-center items-center text-center hover-trigger spring-up group bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-zinc-800 to-cardBg">
                    <div class="font-sans text-7xl md:text-8xl font-extrabold text-neonBlue mb-4 group-hover:scale-110 transition-transform">2nd</div>
                    <div class="font-mono font-bold text-xl uppercase tracking-widest text-zinc-300">runner up</div>
                    <div class="font-mono text-sm text-zinc-400 mt-6 border-t-2 border-zinc-800 pt-6 w-full space-y-2">
                        <div>c.tech project expo</div>
                        <div>arduino hackathon</div>
                        <div>sutd smorphi (category)</div>
                    </div>
                </div>
                <!-- Top Rankings -->
                <div class="neo-card lime p-8 flex flex-col justify-center items-center text-center hover-trigger spring-up group bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-zinc-800 to-cardBg">
                    <div class="font-sans text-7xl md:text-8xl font-extrabold text-neonLime mb-4 group-hover:scale-110 transition-transform">Top</div>
                    <div class="font-mono font-bold text-xl uppercase tracking-widest text-zinc-300">rankings</div>
                    <div class="font-mono text-sm text-zinc-400 mt-6 border-t-2 border-zinc-800 pt-6 w-full space-y-2">
                        <div>3rd – bis hackathon</div>
                        <div>4th – hack sustain</div>
                        <div>5th – srm founder's hack</div>
                    </div>
                </div>
            </div>"""

wins_pattern = re.compile(r'(<section[^>]*id="wins"[^>]*>.*?<span class="text-neonPink animate-spin-slow">❋</span> wins.\s*</h2>\n)(.*?)(        </section>)', re.DOTALL)
content = wins_pattern.sub(r'\1' + wins_html + '\n' + r'\3', content)

# 4. Replace Resume link
resume_pattern1 = re.compile(r'<a href="https://rishit-tandon\.netlify\.app" target="_blank" class="hover:underline decoration-4 underline-offset-4 hover:scale-110 transition-transform">resume ↗</a>')
content = resume_pattern1.sub(r'<a href="Rishit%20Tandon%20Image.pdf" target="_blank" class="hover:underline decoration-4 underline-offset-4 hover:scale-110 transition-transform">resume ↗</a>', content)

resume_pattern2 = re.compile(r'<a href="https://rishit-tandon\.netlify\.app" target="_blank" class="hover:text-white transition-colors">resume ↗</a>')
content = resume_pattern2.sub(r'<a href="Rishit%20Tandon%20Image.pdf" target="_blank" class="hover:text-white transition-colors">resume ↗</a>', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done applying HTML replacements to index.html.")
