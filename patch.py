import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Tailwind CDN and inline style, replace with <link href="/style.css" rel="stylesheet">
# The block starts at <!-- Tailwind CSS --> and ends at </style>
pattern = re.compile(r'<!-- Tailwind CSS -->.*?</style>', re.DOTALL)
content = pattern.sub('<link href="./style.css" rel="stylesheet">', content)

# 2. Fix sys_status.js wrapping by adding whitespace-nowrap
content = content.replace(
    '<div class="window-body text-left pointer-events-none">',
    '<div class="window-body text-left pointer-events-none whitespace-nowrap">'
)

# 3. Fix AGENT MARKETPLACE text wrap (remove <br>, change font sizes, add text-balance)
content = content.replace(
    '<h3 class="font-sans text-5xl md:text-7xl font-bold mb-4 uppercase leading-none group-hover:text-neonLime transition-colors">agent<br>marketplace</h3>',
    '<h3 class="font-sans text-5xl md:text-6xl lg:text-7xl font-bold mb-4 uppercase leading-none group-hover:text-neonLime transition-colors text-balance">agent marketplace</h3>'
)

# 4. Add JS smooth scrolling fallback before closing </body>
js_fallback = """
    <script>
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    </script>
</body>
"""
content = content.replace('</body>', js_fallback)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html successfully updated.")
