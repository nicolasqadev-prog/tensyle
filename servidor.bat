@echo off
REM Servidor HTTP simple para Tensyle
REM Este archivo inicia un servidor en puerto 8000

cd /d "%~dp0"

REM Intenta con Python primero
python -m http.server 8000 2>nul && goto :success

REM Si Python no funciona, intenta python3
python3 -m http.server 8000 2>nul && goto :success

REM Si nada funciona, muestra instrucciones
echo.
echo ERROR: No se encontro Python instalado
echo.
echo OPCIONES:
echo 1. Instala Python desde python.org
echo 2. Abre directamente el archivo: index.html en tu navegador
echo 3. Usa "Live Server" extension en Visual Studio Code
echo.
pause
exit /b 1

:success
echo.
echo ==============================================
echo Servidor iniciado en: http://localhost:8000
echo ==============================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
timeout /t 2
start http://localhost:8000
