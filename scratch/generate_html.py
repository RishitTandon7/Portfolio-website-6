import json

projects = [
    {
        "id": "project_01.sh",
        "title": "Agentic-AI",
        "github": "https://github.com/RishitTandon7/Agentic-AI",
        "desc": "Advanced AI agents framework for autonomous task execution and problem-solving using LangChain and OpenAI",
        "tags": ["Python", "LangChain", "OpenAI"],
        "color": "pink",
        "col_span": "md:col-span-6"
    },
    {
        "id": "project_02.sh",
        "title": "LinkedOut – AI LinkedIn Post Scheduler",
        "github": "https://github.com/RishitTandon7/LinkedIn-Uploader",
        "desc": "Full-stack PWA with LinkedIn OAuth 2.0; agentic caption & hashtag generation via Gemini API with persona-based prompting. Post scheduling engine that auto-publishes at user-defined times. Deployed on Vercel with Supabase backend.",
        "tags": ["Next.js", "FastAPI", "Supabase", "Gemini API", "LinkedIn OAuth", "PWA"],
        "color": "lime",
        "col_span": "md:col-span-6"
    },
    {
        "id": "project_03.sh",
        "title": "VaxTrack",
        "github": "https://github.com/RishitTandon7/VaxTrack",
        "desc": "Comprehensive vaccination tracking system for managing immunization records and schedules",
        "tags": ["React", "Node.js", "MongoDB"],
        "color": "blue",
        "col_span": "md:col-span-5"
    },
    {
        "id": "project_04.sh",
        "title": "TREAT – Community Meal Discovery Platform",
        "github": "https://github.com/RishitTandon7/Prasad",
        "desc": "Multilingual WhatsApp chatbot supporting food donations, event registration, volunteer onboarding, feedback, and location-based temple meal discovery. Java backend with MySQL, automated SMS/WhatsApp via Twilio webhooks.",
        "tags": ["Java", "MySQL", "Twilio API", "WhatsApp Automation"],
        "color": "dark",
        "col_span": "md:col-span-7"
    },
    {
        "id": "project_05.sh",
        "title": "EduStream",
        "github": "https://github.com/RishitTandon7/EduStream",
        "desc": "Java-based virtual classroom with role-based access control for secure content management and teacher-student collaboration. Integrated Python-based video calling module and classroom creation via unique codes.",
        "tags": ["Java", "Python", "Client-Server Architecture"],
        "color": "pink",
        "col_span": "md:col-span-7"
    },
    {
        "id": "project_06.sh",
        "title": "ULTRON",
        "github": "https://github.com/RishitTandon7/ULTRON",
        "desc": "Advanced AI system designed for automation and intelligent task management",
        "tags": ["Python", "AI", "Automation"],
        "color": "lime",
        "col_span": "md:col-span-5"
    },
    {
        "id": "project_07.sh",
        "title": "KisanVikas",
        "github": "https://github.com/RishitTandon7/KisanVikas",
        "desc": "Agricultural platform empowering farmers with modern tools and market insights",
        "tags": ["Android", "Java", "Firebase"],
        "color": "blue",
        "col_span": "md:col-span-4"
    },
    {
        "id": "project_08.sh",
        "title": "NeuroVibe",
        "github": "https://github.com/RishitTandon7/NeuroVibe",
        "desc": "Brain-Computer Interface (BCI) system using EEG signals (BioAmp Band + ESP32) to control wheelchair movement in real time. Trained a Random Forest classifier to decode mental commands (Move, Stop, LED ON/OFF). Low-latency, low-cost assistive mobility solution integrating ML model with motor control.",
        "tags": ["ESP32", "BioAmp EXG Pill", "Machine Learning", "Arduino", "BCI"],
        "color": "dark",
        "col_span": "md:col-span-8"
    },
    {
        "id": "project_09.sh",
        "title": "AI Smart Glasses (AISGR)",
        "github": "https://github.com/RishitTandon7/AISGR",
        "desc": "Wearable AI system with onboard camera, microphone, and speaker for real-time object detection and voice interaction. Added hands-free video/phone calls, object identification, environment summaries, and distance cues for assistive use. Optimized vision and audio pipeline for low-latency real-time performance.",
        "tags": ["LLaMA 3.2 Vision", "Python", "OpenCV", "Agentic AI"],
        "color": "pink",
        "col_span": "md:col-span-8"
    },
    {
        "id": "project_10.sh",
        "title": "MedAssist",
        "github": "https://github.com/RishitTandon7/MedAssist",
        "desc": "Symptom checker and medicine delivery robot. Identifies potential diseases from user-provided symptoms and recommends medications. WhatsApp chatbot via Twilio + Python backend + Ngrok tunnel. Frontend in HTML/CSS with Home, Prevention, Shop, Cart, Order Tracking sections.",
        "tags": ["Python", "Twilio WhatsApp API", "Arduino", "HC-05", "HTML/CSS"],
        "color": "lime",
        "col_span": "md:col-span-4"
    },
    {
        "id": "project_11.sh",
        "title": "Agent Marketplace",
        "github": "https://github.com/RishitTandon7/agent-marketplace",
        "desc": "Full-stack AI agent marketplace where developers discover, purchase, and consume specialized AI agents via auto-provisioned REST API keys. Python/FastAPI backend + Supabase (PostgreSQL). Razorpay payment gateway with webhook-driven order fulfillment — API keys auto-generated on payment confirmation. Deployed on AWS.",
        "tags": ["React", "Next.js", "Python", "FastAPI", "Supabase", "Razorpay", "AWS"],
        "color": "blue",
        "col_span": "md:col-span-6"
    },
    {
        "id": "project_12.sh",
        "title": "AI Negotiation System",
        "github": "https://github.com/RishitTandon7/AI-Negotiation-System",
        "desc": "Autonomous multi-agent negotiation system (Buyer vs Seller) using Gemini 2.0 and recursive feedback loops. Llama 3.2 as LLM judge achieving 0.87 ROC-AUC score. Playwright-based scraper with Google Shopping fallback; 99.9% data reliability by bypassing CAPTCHAs.",
        "tags": ["Python", "Flask", "Gemini 2.0", "Playwright", "Ollama", "Llama 3.2"],
        "color": "dark",
        "col_span": "md:col-span-6"
    },
    {
        "id": "project_13.sh",
        "title": "Multiverse (IoT Digital Twin)",
        "github": "https://github.com/RishitTandon7/Multiverse",
        "desc": "Real-time Digital Twin system synchronizing live telemetry from 20+ ESP-based nodes (100+ sensor data points) into a Unity 3D environment. Bi-directional control via custom API pipeline. 40% improvement in monitoring responsiveness.",
        "tags": ["React", "Next.js", "Tailwind CSS", "Unity", "C#", "ESP32", "REST APIs"],
        "color": "lime",
        "col_span": "md:col-span-12"
    }
]

html = ""
for p in projects:
    color = p["color"]
    # map color to neon class
    if color == "lime":
        neon_color = "neonLime"
    elif color == "pink":
        neon_color = "neonPink"
    elif color == "blue":
        neon_color = "neonBlue"
    else:
        neon_color = "white"
    
    # generate tags
    tags_html = ""
    for t in p["tags"]:
        tags_html += f'<span class="pill group-hover:text-{neon_color} group-hover:border-{neon_color}">{t.lower()}</span>\n                            '
    
    # fallback to main github if 404
    github_link = p["github"]
    
    card_html = f"""                <!-- {p['id']} -->
                <div class="neo-card {color} col-span-1 {p['col_span']} p-8 min-h-[350px] flex flex-col justify-between hover-trigger spring-up group">
                    <div class="flex justify-between items-start mb-6 border-b-2 border-zinc-800 pb-4">
                        <div class="font-mono font-bold text-zinc-500 group-hover:text-{neon_color} transition-colors">{p['id']}</div>
                        <a href="{github_link}" target="_blank" onclick="fetch(this.href, {{method: 'HEAD'}}).then(r => {{ if(!r.ok) window.open('https://github.com/RishitTandon7', '_blank'); return false; }}).catch(()=>window.open('https://github.com/RishitTandon7', '_blank')); return false;" class="font-mono text-sm hover:underline decoration-2 underline-offset-4 flex items-center gap-2 group-hover:text-{neon_color}">
                            code ↗
                        </a>
                    </div>
                    <div>
                        <h3 class="font-sans text-3xl md:text-4xl font-bold mb-4 uppercase leading-none group-hover:text-{neon_color} transition-colors">{p['title']}</h3>
                        <p class="font-mono text-zinc-400 text-sm md:text-base max-w-xl mb-6">
                            {p['desc'].lower()}
                        </p>
                    </div>
                    <div class="flex flex-wrap gap-2 mt-auto">
                        {tags_html.strip()}
                    </div>
                </div>
"""
    html += card_html

with open("scratch/projects.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done generating projects.")

# Certificates mapping
certs_known = [
    ("Machine Learning", "NPTEL IIT Kharagpur"),
    ("Python for Data Science, AI & Development", "IBM"),
    ("Unity Essentials", "Unity Technologies"),
    ("Database Management Systems (DBMS)", "Udemy"),
    ("Machine Learning Bootcamp (Arcade Intelligence)", "Next-Gen AI, SRM IST"),
    ("Learn Ethical Hacking From Scratch", "Udemy"),
    ("Outstanding Student of 1st year", "C.Tech Department")
]

certs_html = ""
for i in range(1, 41):
    img_path = f"certificates/cert_{i}.jpg"
    
    if i <= len(certs_known):
        title, issuer = certs_known[i-1]
    else:
        title = f"Certification {i}"
        issuer = "Verified Issuer"
        
    certs_html += f"""                        <li class="cert-item flex items-center justify-between border-b border-zinc-800 pb-4 group/item cursor-crosshair" data-img="{img_path}">
                            <div class="flex items-center gap-3">
                                <span class="w-2 h-2 rounded-full bg-neonLime flex-shrink-0"></span>
                                <span class="group-hover/item:text-neonLime group-hover/item:font-bold transition-all">{title}</span>
                            </div>
                            <span class="text-zinc-600 text-xs uppercase bg-zinc-900 px-2 py-1 rounded font-bold tracking-wider">{issuer}</span>
                        </li>
"""

with open("scratch/certs.html", "w", encoding="utf-8") as f:
    f.write(certs_html)

print("Done generating certs.")
