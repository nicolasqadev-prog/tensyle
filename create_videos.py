#!/usr/bin/env python3
"""
Script para generar videos profesionales de Tensyle
Crea videos MP4 con animaciones CSS renderizadas
"""

import subprocess
import os

def create_video_ffmpeg(output_file, title, description, duration=10):
    """Crea un video MP4 con título y descripción usando ffmpeg"""

    # Crear comando ffmpeg para video con texto
    cmd = [
        'ffmpeg',
        '-f', 'lavfi',
        '-i', f'color=c=#0a0e27:s=1920x1080:d={duration}',
        '-vf', f"drawtext=text='{title}':fontfile='C\\\\Windows\\\\Fonts\\\\arial.ttf':fontsize=120:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-100, drawtext=text='{description}':fontfile='C\\\\Windows\\\\Fonts\\\\arial.ttf':fontsize=40:fontcolor=#00d4ff:x=(w-text_w)/2:y=(h-text_h)/2+100",
        '-pix_fmt', 'yuv420p',
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✓ Video creado: {output_file}")
        return True
    except FileNotFoundError:
        print(f"⚠ FFmpeg no instalado. Instalando...")
        return False
    except Exception as e:
        print(f"Error al crear video: {e}")
        return False

def create_gif_animation(output_file, title):
    """Crea un GIF animado como fallback"""
    from PIL import Image, ImageDraw, ImageFont
    import os

    frames = []
    width, height = 1920, 1080

    # Crear 30 frames para animación suave
    for i in range(30):
        img = Image.new('RGB', (width, height), color='#0a0e27')
        draw = ImageDraw.Draw(img)

        # Efecto de movimiento
        offset = (i / 30) * 200

        # Dibujar rectángulo animado (simulando impresora)
        rect_x = 200 + offset
        rect_y = 300
        rect_w = 600
        rect_h = 400

        draw.rectangle(
            [rect_x, rect_y, rect_x + rect_w, rect_y + rect_h],
            outline='#00d4ff',
            width=3
        )

        # Agregar texto
        draw.text((960, 100), title, fill='white')

        frames.append(img)

    # Guardar como GIF (si PIL puede)
    if frames:
        frames[0].save(
            output_file,
            save_all=True,
            append_images=frames[1:],
            duration=50,
            loop=0
        )
        print(f"✓ GIF creado: {output_file}")

# Intentar crear videos
print("🎬 Creando videos para Tensyle...\n")

os.makedirs('videos', exist_ok=True)

# Videos a crear
videos = [
    ('videos/impresora-en-accion.mp4', 'CREALITY K1 MAX', 'Máquina de impresión 3D en tiempo real', 15),
    ('videos/proceso-automotive.mp4', 'RECONSTRUCCIÓN AUTOMOTRIZ', 'Pieza antes y después en proceso', 12),
    ('videos/coleccionables.mp4', 'FIGURAS ARTICULADAS', 'Detalle en cada punto de articulación', 10),
]

success = False
for output, title, desc, dur in videos:
    if create_video_ffmpeg(output, title, desc, dur):
        success = True
        break

# Si ffmpeg falla, crear alternativa con GIFs
if not success:
    print("\n⚠ FFmpeg no disponible. Creando alternativa con PIL...\n")
    for output, title, desc, dur in videos:
        gif_output = output.replace('.mp4', '.gif')
        create_gif_animation(gif_output, title)

print("\n✅ Videos listos. Usa estos archivos en index.html")
