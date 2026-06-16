with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("scratch/projects.html", "r", encoding="utf-8") as f:
    projects_html = f.read()

with open("scratch/certs.html", "r", encoding="utf-8") as f:
    certs_html = f.read()

with open("scratch/wins.html", "r", encoding="utf-8") as f:
    wins_html = f.read()

# 1. Replace #wins grid
# It starts at line 163 (neo-card) and ends at line 171
# wait, actually let's use exact line numbers:
# In the original file, line 163 is `<div class="neo-card pink ...">`
# and line 171 is `            </div>`
# Then line 172 is `        </section>`

start_wins = -1
end_wins = -1
for i, line in enumerate(lines):
    if '<section class="max-w-[1400px] mx-auto px-6 py-32 border-b-2 border-dashed border-zinc-800" id="wins">' in line:
        start_wins = i + 4 # skip the heading
    if '<!-- EXPERIENCE -->' in line:
        end_wins = i - 2
        break

if start_wins != -1 and end_wins != -1:
    lines = lines[:start_wins] + [wins_html + "\n"] + lines[end_wins:]
    print("Replaced wins")

# 2. Replace #projects grid
start_proj = -1
end_proj = -1
for i, line in enumerate(lines):
    if '<div class="grid grid-cols-1 md:grid-cols-12 gap-6">' in line and 'id="projects"' in lines[i-4]:
        start_proj = i + 1
    if '<!-- CERTIFICATES -->' in line:
        end_proj = i - 3
        break

if start_proj != -1 and end_proj != -1:
    lines = lines[:start_proj] + [projects_html + "\n"] + lines[end_proj:]
    print("Replaced projects")

# 3. Replace certs list
start_certs = -1
end_certs = -1
for i, line in enumerate(lines):
    if '<ul class="font-mono text-base text-zinc-300 space-y-6 max-h-[500px] overflow-y-auto pr-4 custom-scrollbar">' in line:
        start_certs = i + 1
    if '<!-- CERTIFICATIONS PANEL -->' in line:
        end_certs = i - 4
        break

if start_certs != -1 and end_certs != -1:
    lines = lines[:start_certs] + [certs_html + "\n"] + lines[end_certs:]
    print("Replaced certs")

# 4. Replace resume
content = "".join(lines)
content = content.replace('https://rishit-tandon.netlify.app', 'Rishit Tandon Image.pdf')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
