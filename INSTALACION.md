# Instalación y Configuración - Tensyle Web

## 1. Instalar Dependencias Python

```bash
pip install -r requirements.txt
```

## 2. Configurar el Servidor de Correos (IMPORTANTE)

En el archivo `app.py`, modifica estas líneas con tus credenciales de Gmail:

```python
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # TU CORREO GMAIL
app.config['MAIL_PASSWORD'] = 'tu_contraseña_app'   # CONTRASEÑA DE APLICACIÓN
```

### Pasos para obtener la contraseña de aplicación en Gmail:

1. Ir a: https://myaccount.google.com/apppasswords
2. Seleccionar "Correo" y "Windows"
3. Copiar la contraseña de 16 caracteres generada
4. Pegar en `app.config['MAIL_PASSWORD']`

## 3. Ejecutar el Servidor

```bash
python app.py
```

El servidor estará en: `http://localhost:5000`

## 4. Conectar el Frontend

En `index.html`, el formulario ya está configurado para enviar a `/api/quotation`

Si ejecutas el servidor en otro puerto, modifica en `index.html`:

```javascript
const response = await fetch('http://localhost:5000/api/quotation', {
    method: 'POST',
    body: formData
});
```

## 5. Desplegar en Producción (Opcional)

Para usar en producción, instala gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Estructura de Archivos

```
tensyle-web/
├── index.html                 (Página principal)
├── app.py                     (Servidor Flask)
├── requirements.txt           (Dependencias Python)
├── logo-instagram.png         (Logo de la marca)
├── [imágenes de productos]    (Tus fotos)
└── uploads/                   (Carpeta para archivos cotizaciones)
```

## Funcionamiento

1. Cliente completa formulario de cotización
2. Servidor recibe datos + archivos
3. Envía correo a: **nicolas.qa.dev@gmail.com** con todos los detalles
4. Envía respuesta automática al cliente confirmando recepción
5. Archivos se guardan en carpeta `uploads/`

## Solución de Problemas

**Error: "SMTP connection refused"**
- Verifica que MAIL_USERNAME y MAIL_PASSWORD sean correctos
- Asegúrate de usar contraseña de aplicación (no la contraseña principal)

**Error: "403 Forbidden"**
- Gmail bloqueó la conexión
- Habilita "Acceso de apps menos seguras": https://myaccount.google.com/lesssecureapps

**Los archivos no se guardan:**
- Verifica permisos de la carpeta `uploads/`
- Crea manualmente si no existe

---

¿Necesitas ayuda con algún paso?
