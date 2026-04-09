# 🚀 GUÍA INSTALACIÓN - PASO A PASO (WINDOWS)

## PASO 1: Descargar Python

1. Ve a: https://www.python.org/downloads/
2. Descarga **Python 3.11** (o más nueva)
3. **IMPORTANTE**: En el instalador, marca ✅ **"Add Python to PATH"**
4. Haz clic en "Install Now"
5. Espera a que termine

### Verificar instalación:
Abre **PowerShell** (Windows+R, escribe `powershell`)
```powershell
python --version
```
Debe mostrar: `Python 3.11.x` (o similar)

---

## PASO 2: Instalar Dependencias

1. Abre **PowerShell** en la carpeta del proyecto
   - Opción fácil: Abre la carpeta `tensyle-web` en Windows Explorer
   - Shift + Click derecho en la carpeta
   - Selecciona "Abrir ventana PowerShell aquí"

2. Ejecuta este comando:
```powershell
pip install -r requirements.txt
```

Debe mostrar algo como:
```
Successfully installed Flask-2.3.3 Flask-CORS-4.0.0 Flask-Mail-0.9.1 Werkzeug-2.3.7
```

---

## PASO 3: Configurar Correo Gmail

**Esto es CRÍTICO para que funcione el envío de cotizaciones**

### 3.1 - Habilitar "Contraseñas de Aplicación" en Gmail

1. Abre: https://myaccount.google.com/apppasswords
2. Si te pide, inicia sesión con tu cuenta Gmail
3. En el dropdown "Select app", elige **"Correo (Mail)"**
4. En "Select device", elige **"Windows"**
5. Haz clic en "GENERATE"
6. **Copia la contraseña de 16 caracteres** (la que aparece en amarillo)

### 3.2 - Guardar credenciales en el código

1. Abre el archivo `app.py` con un editor de texto (Notepad o VS Code)
2. Busca estas líneas (alrededor de la línea 18-19):
```python
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'
app.config['MAIL_PASSWORD'] = 'tu_contraseña_app'
```

3. Reemplaza:
   - `tu_correo@gmail.com` → Tu correo Gmail real (ej: `miCorreo@gmail.com`)
   - `tu_contraseña_app` → La contraseña de 16 caracteres que copiaste (ej: `abcd efgh ijkl mnop`)

**Ejemplo final:**
```python
app.config['MAIL_USERNAME'] = 'nicolas.qa.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'abcd efgh ijkl mnop'
```

4. Guarda el archivo (Ctrl+S)

---

## PASO 4: Ejecutar el Servidor

En la misma PowerShell, ejecuta:
```powershell
python app.py
```

Debes ver algo como:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

---

## PASO 5: Abrir la Página

1. Abre tu navegador (Chrome, Firefox, Edge)
2. Ve a: **http://localhost:5000**
3. ¡Listo! La página debería cargar

---

## 🧪 Probar el Formulario de Cotización

1. En la página, haz clic en **"SOLICITAR COTIZACIÓN"**
2. Rellena el formulario:
   - Nombre: Tu nombre
   - Email: Tu correo
   - Tipo de producto: Elige uno
   - Descripción: Escribe algo
3. Haz clic en **"ENVIAR COTIZACIÓN"**

### ¿Qué debe pasar?

✅ Debes ver: "¡Cotización enviada! Nos pondremos en contacto pronto."

✅ Un correo debe llegar a: `nicolas.qa.dev@gmail.com` con todos tus datos

✅ Un correo debe llegar a tu correo confirmando que se recibió

---

## ❌ Si Algo Sale Mal

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solución:** No instalaste las dependencias. Vuelve al PASO 2

### Error: "SMTP connection refused"
**Solución:** 
- Verifica que MAIL_USERNAME y MAIL_PASSWORD sean correctos en `app.py`
- Asegúrate de usar la contraseña de APLICACIÓN (no tu contraseña de Gmail)
- Espera 5 minutos y vuelve a intentar

### Error: "403 Forbidden"
**Solución:** Gmail bloqueó la conexión. Haz esto:
1. Ve a: https://myaccount.google.com/lesssecureapps
2. Activa "Permitir aplicaciones menos seguras"

### El correo no llega a nicolas.qa.dev@gmail.com
**Solución:** Verifica que en `app.py` esté configurado ese correo (PASO 3.2)

---

## 🛑 Detener el Servidor

En PowerShell, presiona: **Ctrl + C**

---

## 💡 Notas Importantes

- El servidor debe estar corriendo para que funcione la cotización
- La página HTML se puede abrir sin servidor, pero el formulario NO funcionará
- Si cierras PowerShell, se detiene el servidor

---

## ✅ Checklist de Verificación

- [ ] Python instalado y en PATH
- [ ] Carpeta `tensyle-web` abierta en PowerShell
- [ ] `pip install -r requirements.txt` ejecutado sin errores
- [ ] Gmail configurado en `app.py`
- [ ] Servidor ejecutándose (`python app.py`)
- [ ] Navegador en `http://localhost:5000`
- [ ] Formulario funciona y correos llegan

---

¿Necesitas ayuda en algún paso? 🤔
