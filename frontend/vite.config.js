import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    allowedHosts: ['fk4wkwgkog04kk4c0gc48sc4.95.216.212.202.sslip.io']
  }
})
