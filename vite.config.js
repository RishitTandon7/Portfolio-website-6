import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  root: './',
  base: './',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
  },
  css: {
    postcss: './postcss.config.js',
  },
  server: {
    port: 5173,
    // work around the '#' in directory path
    fs: {
      strict: false,
    },
  },
  preview: {
    port: 4174,
  },
})
