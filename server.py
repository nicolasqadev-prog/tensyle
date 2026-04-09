#!/usr/bin/env python3
"""
Servidor simple para servir archivos locales
Ejecuta esto para poder usar el generador de videos
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
DIRECTORY = str(Path(__file__).parent)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Permitir CORS para imágenes
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # Log más limpio
        print(f"[{self.client_address[0]}] {format % args}")

os.chdir(DIRECTORY)

print("\n" + "="*60)
print("🚀 SERVIDOR TENSYLE INICIADO")
print("="*60)
print(f"📁 Carpeta: {DIRECTORY}")
print(f"🌐 URL: http://localhost:{PORT}")
print("\n✅ AHORA PUEDES:")
print("   1. Abrir http://localhost:8000/generate_videos_local.html")
print("   2. Generar los videos")
print("   3. Descargarlos")
print("\n📝 Para detener: Presiona Ctrl+C")
print("="*60 + "\n")

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ Servidor detenido")
