from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuración
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Configuración de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # Cambiar
app.config['MAIL_PASSWORD'] = 'tu_contraseña_app'  # Usar contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@tensyle.co'

mail = Mail(app)

# Crear carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'dwg', 'step', 'obj', 'stl', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/quotation', methods=['POST'])
def handle_quotation():
    try:
        # Obtener datos del formulario
        fullname = request.form.get('fullname', 'No especificado')
        email = request.form.get('email', 'No especificado')
        phone = request.form.get('phone', 'No especificado')
        company = request.form.get('company', 'No especificado')
        product_type = request.form.get('product_type', 'No especificado')
        material = request.form.get('material', 'No especificado')
        description = request.form.get('description', 'No especificado')

        # Procesar archivos
        uploaded_files = []
        if 'files' in request.files:
            files = request.files.getlist('files')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                    filename = timestamp + filename
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    uploaded_files.append(filename)

        # Crear mensaje para el administrador
        admin_subject = f"Nueva Cotización de {fullname}"
        admin_body = f"""
        ===== NUEVA SOLICITUD DE COTIZACIÓN =====

        INFORMACIÓN DEL CLIENTE:
        Nombre: {fullname}
        Correo: {email}
        Teléfono: {phone}
        Empresa: {company}

        DETALLES DEL PROYECTO:
        Tipo de Producto: {product_type}
        Material Preferido: {material}
        Descripción:
        {description}

        ARCHIVOS ADJUNTOS: {', '.join(uploaded_files) if uploaded_files else 'Ninguno'}

        Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        ========================================
        """

        # Enviar correo al administrador
        try:
            admin_msg = Message(
                subject=admin_subject,
                recipients=['nicolas.qa.dev@gmail.com'],
                body=admin_body
            )

            # Adjuntar archivos
            for filename in uploaded_files:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                with open(filepath, 'rb') as attachment:
                    admin_msg.attach(filename, 'application/octet-stream', attachment.read())

            mail.send(admin_msg)
        except Exception as e:
            print(f"Error enviando correo al admin: {e}")

        # Enviar respuesta automática al cliente
        try:
            client_subject = "Cotización Recibida - Tensyle"
            client_body = f"""
Hola {fullname},

¡Gracias por tu interés en Tensyle!

Hemos recibido tu solicitud de cotización correctamente. Nuestro equipo de expertos
en fabricación aditiva ya está analizando los detalles de tu proyecto.

RESUMEN DE TU SOLICITUD:
- Tipo de Producto: {product_type}
- Material: {material}
- Archivos Adjuntos: {len(uploaded_files)} archivo(s)

Nos pondremos en contacto contigo en las próximas 24-48 horas a través del
correo electrónico o el número telefónico proporcionado para ofrecerte una
cotización personalizada y discutir los detalles técnicos de tu proyecto.

Si tienes alguna pregunta urgente, puedes contactarnos a través de:
📱 WhatsApp: +57 317 168 7777
📧 Email: info@tensyle.co

Gracias por confiar en nosotros.

Saludos,
TENSYLE SOLUTIONS
Fabricación Aditiva de Precisión Industrial
Chía, Colombia
"""

            client_msg = Message(
                subject=client_subject,
                recipients=[email],
                body=client_body
            )
            mail.send(client_msg)
        except Exception as e:
            print(f"Error enviando respuesta automática: {e}")

        return jsonify({'status': 'success', 'message': 'Cotización enviada correctamente'}), 200

    except Exception as e:
        print(f"Error en el servidor: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
