import { defineConfig } from "vite";
import react from "@vitejs/plugin-react"; // optional if using React
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      "/api": "http://localhost:5001",
    },
  },
});
