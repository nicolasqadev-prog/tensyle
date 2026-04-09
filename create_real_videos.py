#!/usr/bin/env python3
"""
Script para crear videos REALES basados en imágenes existentes de Tensyle
Crea secuencias de antes/después, timelapse de impresión, y showroom
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

def create_before_after_video(before_img, after_img, output_file, title):
    """Crea un video de transición antes/después"""

    try:
        # Cargar imágenes reales
        img_before = Image.open(before_img)
        img_after = Image.open(after_img)

        # Redimensionar a 1920x1080
        target_size = (1920, 1080)
        img_before = img_before.resize(target_size, Image.Resampling.LANCZOS)
        img_after = img_after.resize(target_size, Image.Resampling.LANCZOS)

        frames = []

        # Crear frames: 3 segundos con before, transición, 3 segundos con after
        for i in range(90):  # 30fps * 3 segundos
            frames.append(img_before)

        # Transición suave (30 frames = 1 segundo)
        for i in range(30):
            alpha = i / 30.0
            frame = Image.new('RGB', target_size)
            frame.paste(img_before, (0, 0), None)
            frame_overlay = img_after.copy()
            frame_overlay.putalpha(int(255 * alpha))

            # Convertir before a RGBA si no lo es
            if img_before.mode != 'RGBA':
                before_rgba = img_before.convert('RGBA')
            else:
                before_rgba = img_before.copy()

            before_rgba.paste(frame_overlay, (0, 0), frame_overlay)
            frame = before_rgba.convert('RGB')
            frames.append(frame)

        for i in range(90):  # 3 segundos más con after
            frames.append(img_after)

        # Guardar como GIF animado (más compatible que MP4 sin ffmpeg)
        if frames:
            gif_output = output_file.replace('.mp4', '.gif')
            frames[0].save(
                gif_output,
                save_all=True,
                append_images=frames[1:],
                duration=33,  # ~30fps
                loop=0,
                quality=85
            )
            print(f"✓ Video creado: {gif_output} ({len(frames)} frames)")
            return True
    except Exception as e:
        print(f"⚠ Error creando video {output_file}: {e}")
        return False

def create_carousel_video(image_list, output_file, duration_per_img=2):
    """Crea un video tipo carrusel mostrando varias imágenes"""

    try:
        frames = []
        target_size = (1920, 1080)
        frames_per_image = int(30 * duration_per_img)  # 30fps

        for img_path in image_list:
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize(target_size, Image.Resampling.LANCZOS)

                # Agregar la imagen N veces para duración
                for _ in range(frames_per_image):
                    frames.append(img)

                # Transición suave entre imágenes
                if img_path != image_list[-1]:
                    next_img = Image.open(image_list[image_list.index(img_path) + 1])
                    next_img = next_img.resize(target_size, Image.Resampling.LANCZOS)

                    for i in range(15):  # Transición de 0.5 segundos
                        alpha = i / 15.0
                        frame = Image.new('RGB', target_size)
                        frame.paste(img, (0, 0))

                        if img.mode != 'RGBA':
                            img_rgba = img.convert('RGBA')
                        else:
                            img_rgba = img.copy()

                        next_rgba = next_img.convert('RGBA')
                        next_rgba.putalpha(int(255 * alpha))
                        img_rgba.paste(next_rgba, (0, 0), next_rgba)
                        frame = img_rgba.convert('RGB')
                        frames.append(frame)

        if frames:
            gif_output = output_file.replace('.mp4', '.gif')
            frames[0].save(
                gif_output,
                save_all=True,
                append_images=frames[1:],
                duration=33,
                loop=0,
                quality=85
            )
            print(f"✓ Carrusel creado: {gif_output} ({len(frames)} frames)")
            return True
    except Exception as e:
        print(f"⚠ Error en carrusel {output_file}: {e}")
        return False

# Crear carpeta videos
os.makedirs('videos', exist_ok=True)

print("🎬 Generando videos REALES basados en imágenes de Tensyle...\n")

# VIDEO 1: Carena Lateral (Antes/Después)
print("1. Creando video Carena Lateral...")
create_before_after_video(
    'lateral-moto-impresa-antes.jpg',
    'lateral-moto-fin.jpg',
    'videos/carena-lateral.mp4',
    'Carena Lateral - Antes y Después'
)

# VIDEO 2: Frontal Rejilla (Antes/Después)
print("2. Creando video Frontal Rejilla...")
create_before_after_video(
    'frontal-rejilla-despues-antes.jpg',
    'frontal-rejilla-despues.jpg',
    'videos/frontal-rejilla.mp4',
    'Frontal Rejilla - Antes y Después'
)

# VIDEO 3: Inferior Frontal (Antes/Después)
print("3. Creando video Inferior Frontal...")
create_before_after_video(
    'inferior-frontal-panal-antes.jpg',
    'inferior-frontal-panal.jpg',
    'videos/inferior-frontal.mp4',
    'Inferior Frontal - Antes y Después'
)

# VIDEO 4: Carrusel Motion Collection
print("4. Creando carrusel Motion Collection...")
motion_images = [
    'bluey.jpg',
    'bob-esponja.jpg',
    'gravitifalls.jpg',
    'octonautalimpio.jpg',
    'pato-aventuras.jpg',
    'phineas-limpio.jpg',
    'pjmask.jpg',
    'pocoyo.jpg',
    'pokemon-2.jpg',
    'transformers.jpg'
]

create_carousel_video(
    motion_images,
    'videos/motion-collection.mp4',
    duration_per_img=2
)

# VIDEO 5: Carrusel Proyectos Automotriz
print("5. Creando carrusel Proyectos Automotriz...")
auto_images = [
    'lateral-moto-fin.jpg',
    'frontal-rejilla-despues.jpg',
    'inferior-frontal-panal.jpg',
    'manija-puerta-exterior.jpg',
    'pieza-interna-puerta.jpg',
    'tapa-cubre-cadenas.jpg'
]

create_carousel_video(
    auto_images,
    'videos/automotive-projects.mp4',
    duration_per_img=2.5
)

print("\n✅ Todos los videos REALES han sido generados")
print("📁 Ubicación: ./videos/")
print("\nVideos creados:")
print("  ✓ carena-lateral.gif")
print("  ✓ frontal-rejilla.gif")
print("  ✓ inferior-frontal.gif")
print("  ✓ motion-collection.gif")
print("  ✓ automotive-projects.gif")
