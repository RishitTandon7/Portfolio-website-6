/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        dark: '#09090b',
        light: '#fafafa',
        neonLime: '#ccff00',
        neonPink: '#ff00ff',
        neonBlue: '#00e5ff',
        cardBg: '#18181b',
      },
      fontFamily: {
        sans: ['"Bricolage Grotesque"', 'sans-serif'],
        mono: ['"Space Mono"', 'monospace'],
      },
      boxShadow: {
        'brutal': '6px 6px 0px 0px rgba(204, 255, 0, 1)',
        'brutal-pink': '6px 6px 0px 0px rgba(255, 0, 255, 1)',
        'brutal-blue': '6px 6px 0px 0px rgba(0, 229, 255, 1)',
        'brutal-white': '4px 4px 0px 0px rgba(250, 250, 250, 1)',
      },
      animation: {
        'marquee': 'marquee 15s linear infinite',
        'spin-slow': 'spin 8s linear infinite',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' },
        }
      }
    },
  },
  plugins: [],
}
