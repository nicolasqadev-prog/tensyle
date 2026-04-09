# Cambios Realizados en Tensyle Web

## ✅ COMPLETADOS

### 1. **Logo en Navbar**
- Logo de Tensyle ahora tiene fondo blanco con borde redondeado
- Ubicado en la parte superior izquierda
- Tamaño: 45x45px con padding y border-radius

### 2. **Fondo Dinámico en Home**
- Gradientes radiales que crean profundidad
- Patrón de puntos sutil como referencia técnica
- Efecto visual premium sin recargar

### 3. **Logos Reales de Redes Sociales**
- WhatsApp: SVG con logo oficial (verde)
- Instagram: SVG con logo oficial (gradiente)
- Botones flotantes en la derecha con colores de fondo reales

### 4. **Flotabilidad Natural**
- Animación `floatBtn` que sube/baja continuamente (3s)
- Se detiene al hover y se amplifican
- Labels descriptivos: "Consulta Rápida" y "Síguenos"

### 5. **Texturas en Filamentos**
- Cada spool (carrete) tiene:
  - Gradientes complejos (3 colores)
  - Sombras inset para efecto 3D
  - Brillo glossy con filtro blur
  - Patrón de líneas finas simulando el filamento enrollado
- Diferencia visual clara entre materiales:
  - ABS: Negro mate
  - PETG: Rojo fuerte
  - PLA: Verde brillante
  - TPU: Naranja vibrante

### 6. **Efecto Antes/Después Automático**
- Hover sobre imágenes de Automotive/Motion/Hogar
- Transición suave de opacidad (0.6s)
- Imagen "Antes" visible por defecto
- Al pasar mouse aparece imagen "Después"
- Labels "ANTES" y "DESPUÉS" en las esquinas

### 7. **Formulario de Cotización**
- Modal elegante con bordes cyan
- Campos incluyen:
  - Nombre, email, teléfono, empresa
  - Selector de tipo de producto
  - Selector de material preferido
  - Descripción detallada del proyecto
  - Upload de archivos (PDF, DWG, STEP, OBJ, STL, imágenes)
- Validación en cliente
- Drag & drop para archivos

### 8. **Slogans en Cada Sección**
- **TENSYLE**: "Precisión en Cada Capa" + "Soluciones 3D de Ingeniería"
- **AUTOMOTIVE**: "Componentes Descontinuados" + "Reconstrucción y Precisión Técnica"
- **MOTION**: "Figuras Articuladas Premium" + "Colecciones de Ultra Precisión"
- **HOGAR**: "Diseño & Funcionalidad" + "Accesorios Personalizados para tu Espacio"

### 9. **Imágenes de Productos Hogar**
- Generadas en SVG (escalables, sin pérdida)
- 6 categorías con diseños únicos:
  - Soportes Decorativos (azul cyan)
  - Organizadores (verde)
  - Iluminación (naranja con rayos)
  - Macetas (marrón con plantas)
  - Regalos (rosa con moño)
  - Marcos (púrpura con borde)

---

## 📧 Backend - Envío de Cotizaciones

### Archivo: `app.py` (Python Flask)

**Funcionalidades:**
1. Recibe datos del formulario multipart/form-data
2. Valida extensiones de archivos permitidas
3. Guarda archivos en carpeta `uploads/` con timestamp
4. **Envía correo al administrador**:
   - Destinatario: nicolas.qa.dev@gmail.com
   - Incluye: datos del cliente, especificaciones, archivos adjuntos
5. **Envía respuesta automática al cliente**:
   - Confirma recepción de cotización
   - Establece expectativa de contacto en 24-48h
   - Proporciona números de contacto alternativos

### Configuración Requerida:
```python
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'
app.config['MAIL_PASSWORD'] = 'contraseña_app_gmail'
```

Ver archivo `INSTALACION.md` para instrucciones detalladas.

---

## 🎨 Mejoras de Diseño

1. **Color Scheme Consistente**
   - Cyan primario (#00d4ff)
   - Negro profundo (#0a0e27)
   - Texto gris claro (#e0e0e0)

2. **Animaciones Suaves**
   - Transiciones 0.3s - 0.8s
   - Reveal effects en scroll
   - Hover states en todos los elementos interactivos

3. **Responsivo**
   - Mobile-first approach
   - Breakpoint 768px
   - Formulario adaptable

---

## 📁 Archivos Generados

- `app.py` - Servidor Flask backend
- `requirements.txt` - Dependencias Python
- `generate_images.py` - Script para generar imágenes (alternativo)
- `INSTALACION.md` - Guía completa de instalación
- `CAMBIOS_REALIZADOS.md` - Este archivo

---

## 🚀 Próximos Pasos

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar credenciales de Gmail** en `app.py`

3. **Ejecutar servidor**:
   ```bash
   python app.py
   ```

4. **Abrir en navegador**:
   ```
   http://localhost:5000
   ```
   o simplemente abre `index.html` si solo quieres ver el frontend

---

## 📝 Notas Importantes

- Las imágenes de productos (automotive, motion) deben estar en la carpeta raíz
- Los archivos subidos se guardan automáticamente en `uploads/`
- El servidor Flask debe estar corriendo para que funcione el formulario
- En producción, usa gunicorn + nginx para mayor seguridad
