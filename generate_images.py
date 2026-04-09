from PIL import Image, ImageDraw, ImageFilter
import os

# Crear carpeta para imágenes si no existe
os.makedirs('images', exist_ok=True)

def create_product_image(filename, product_name, color_main, color_accent):
    """Genera imagen de producto para sección Hogar"""
    width, height = 400, 400
    img = Image.new('RGB', (width, height), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')

    # Fondo degradado
    for y in range(height):
        ratio = y / height
        r = int(10 + (30 * ratio))
        g = int(14 + (40 * ratio))
        b = int(39 + (60 * ratio))
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

    # Círculo central con color del producto
    center_x, center_y = width // 2, height // 2
    radius = 80

    # Sombra
    draw.ellipse(
        [(center_x - radius - 20, center_y - radius + 30),
         (center_x + radius + 20, center_y + radius + 50)],
        fill=(0, 0, 0, 100)
    )

    # Objeto principal
    draw.ellipse(
        [(center_x - radius, center_y - radius),
         (center_x + radius, center_y + radius)],
        fill=color_main,
        outline=color_accent
    )

    # Brillo
    draw.ellipse(
        [(center_x - radius + 20, center_y - radius + 20),
         (center_x - radius + 50, center_y - radius + 50)],
        fill=(255, 255, 255, 150)
    )

    # Detalles adicionales según el tipo
    if 'soporte' in filename.lower():
        # Líneas de detalle para soporte
        for i in range(3):
            draw.line([(center_x - 30, center_y + 20 + i*15), (center_x + 30, center_y + 20 + i*15)],
                     fill=color_accent, width=2)

    elif 'organizador' in filename.lower():
        # Compartimentos
        draw.rectangle([(center_x - 50, center_y - 30), (center_x - 20, center_y + 40)],
                      outline=color_accent, width=2)
        draw.rectangle([(center_x + 20, center_y - 30), (center_x + 50, center_y + 40)],
                      outline=color_accent, width=2)

    elif 'iluminacion' in filename.lower():
        # Rayos de luz
        for angle in [0, 60, 120, 180, 240, 300]:
            import math
            rad = math.radians(angle)
            x1 = center_x + radius * math.cos(rad)
            y1 = center_y + radius * math.sin(rad)
            x2 = center_x + (radius + 40) * math.cos(rad)
            y2 = center_y + (radius + 40) * math.sin(rad)
            draw.line([(x1, y1), (x2, y2)], fill=color_accent, width=2)

    elif 'maceta' in filename.lower():
        # Patrón de maceta
        draw.arc([(center_x - radius, center_y - radius),
                 (center_x + radius, center_y + radius)],
                0, 360, fill=color_accent, width=3)
        draw.line([(center_x - 40, center_y + 60), (center_x + 40, center_y + 60)],
                 fill=color_accent, width=3)

    elif 'regalo' in filename.lower():
        # Moño
        draw.rectangle([(center_x - 60, center_y - 15), (center_x + 60, center_y + 15)],
                      fill=color_accent)
        draw.rectangle([(center_x - 15, center_y - 60), (center_x + 15, center_y + 60)],
                      fill=color_accent)
        draw.ellipse([(center_x - 20, center_y - 20), (center_x + 20, center_y + 20)],
                    fill=color_main, outline=color_accent, width=2)

    elif 'marco' in filename.lower():
        # Marco decorativo
        draw.rectangle([(center_x - 70, center_y - 70), (center_x + 70, center_y + 70)],
                      outline=color_accent, width=3)
        draw.rectangle([(center_x - 60, center_y - 60), (center_x + 60, center_y + 60)],
                      outline=color_accent, width=1)

    # Filtro de brillo suave
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # Guardar
    img.save(f'images/{filename}')
    print(f"✓ Creado: {filename}")

# Generar imágenes
create_product_image('soporte-decorativo.jpg', 'Soporte Decorativo', '#00d4ff', '#00f2ff')
create_product_image('organizador-personalizado.jpg', 'Organizador', '#4ecca3', '#00ff88')
create_product_image('iluminacion-accesorios.jpg', 'Iluminación', '#ffa500', '#ffcc00')
create_product_image('maceta-custom.jpg', 'Maceta', '#6b4423', '#d4a373')
create_product_image('regalo-personalizado.jpg', 'Regalo', '#ff6b9d', '#ff1493')
create_product_image('marco-soporte.jpg', 'Marco', '#a78bfa', '#c084fc')

print("\n✅ Todas las imágenes de productos han sido generadas correctamente.")
print("📁 Ubicación: images/")
