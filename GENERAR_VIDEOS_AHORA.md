# 🎬 GENERAR VIDEOS - INSTRUCCIONES RÁPIDAS

## ⚡ SOLUCIÓN RÁPIDA (3 PASOS)

### PASO 1: Abre PowerShell en la carpeta tensyle-web

```
Windows: 
  1. Abre la carpeta tensyle-web en Windows Explorer
  2. Presiona Shift + Click derecho en la carpeta vacía
  3. Selecciona "Abrir ventana PowerShell aquí"
```

### PASO 2: Ejecuta el servidor

Copia y pega esto en PowerShell:

```powershell
python server.py
```

**Deberías ver algo así:**

```
============================================================
🚀 SERVIDOR TENSYLE INICIADO
============================================================
📁 Carpeta: C:\Users\Usuario\OneDrive\Escritorio\tensyle-web
🌐 URL: http://localhost:8000

✅ AHORA PUEDES:
   1. Abrir http://localhost:8000/generate_videos_local.html
   2. Generar los videos
   3. Descargarlos

📝 Para detener: Presiona Ctrl+C
============================================================
```

### PASO 3: Genera los videos

1. **Abre tu navegador** y ve a: `http://localhost:8000/generate_videos_local.html`

2. **Verás 6 tarjetas** con tus proyectos

3. **En cada tarjeta**:
   - Haz clic en "Generar Video"
   - Espera 20-30 segundos
   - Verás "✓ Video listo para descargar"
   - Haz clic en el botón azul para descargar

4. **Archivos descargados**:
   ```
   carena-lateral.gif
   frontal-rejilla.gif
   inferior-frontal.gif
   manija-puerta.gif
   pieza-interna.gif
   tapa-cubre.gif
   ```

### PASO 4: Coloca los videos en la carpeta correcta

```
Crea una carpeta llamada "videos" en tu proyecto:

C:\Users\Usuario\OneDrive\Escritorio\tensyle-web\videos\
```

Mueve los 6 GIF que descargaste a esa carpeta.

### PASO 5: Detén el servidor

En PowerShell presiona: **Ctrl + C**

---

## ✅ RESULTADO FINAL

Cuando abras `index.html` en tu navegador, verás:
- Sección "Nuestro Trabajo" con tus 6 proyectos
- Los GIF animados mostrando antes/después
- Efecto smooth de transición

---

## 🆘 SI ALGO FALLA

### Error: "No se puede cargar la imagen"
- **Solución**: Asegúrate de que el servidor está corriendo (Step 2)
- **Verificación**: Abre http://localhost:8000 en tu navegador (debería ver archivos)

### Error: "Python no encontrado"
- **Solución**: Necesitas instalar Python
- **Descarga**: https://www.python.org/downloads/
- **IMPORTANTE**: Marca "Add Python to PATH" en el instalador

### Los videos se descargan pero no aparecen en el sitio
- **Verificación**: ¿Creaste la carpeta `./videos/`?
- **Verificación**: ¿Moviste los 6 GIF a esa carpeta?
- **Solución**: Actualiza el navegador (Ctrl+F5)

---

## 💡 ALTERNATIVA SIN VIDEOS

Si no quieres generar videos, tu sitio ya funciona con:
- ✅ Imágenes reales de tus proyectos
- ✅ Efecto hover antes/después
- ✅ Descripción de cada proyecto

Los clientes ya ven tu evidencia real. Los videos solo hacen que sea más impactante.

---

## 🎯 UNA VEZ LISTO

Cuando termines:
1. Coloca los 6 GIF en `./videos/`
2. Abre `index.html` en tu navegador
3. Ve a la sección "Nuestro Trabajo"
4. Verás tus proyectos con animaciones

Listo para mostrar a tus clientes.
