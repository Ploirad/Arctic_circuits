@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
color 0A

REM ============================================
REM INSTALADOR AUTOMÁTICO - MINECRAFT + PYTHON
REM Academia Cervantes - Robótica
REM ============================================

title Instalador Automático Minecraft + Python

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║     INSTALADOR AUTOMÁTICO MINECRAFT + PYTHON 🎮🐍         ║
echo ║                                                            ║
echo ║           Academia Cervantes - Robótica                    ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo Este script instalará automáticamente:
echo   ✓ Java 21 (necesario para Minecraft)
echo   ✓ SKLauncher (para jugar)
echo   ✓ Python 3.11 (para programar)
echo   ✓ Minecraft Forge 1.12.2
echo   ✓ Servidor de Minecraft configurado
echo   ✓ RaspberryJamMod (conexión Python-Minecraft)
echo   ✓ Librería de Python
echo.
echo ⚠️  IMPORTANTE: Este proceso puede tardar 15-30 minutos
echo     según tu conexión a internet.
echo.
pause

REM ============================================
REM Configuración de variables
REM ============================================

set "INSTALL_DIR=%UserProfile%\MinecraftPython"
set "SERVER_DIR=%INSTALL_DIR%\ServerMinecraft"
set "DOWNLOADS_DIR=%INSTALL_DIR%\downloads"
set "JAVA21_DIR=%INSTALL_DIR%\java21"
set "SKLAUNCHER_DIR=%INSTALL_DIR%\SKLauncher"

echo.
echo [1/10] Creando directorios de instalación...
echo.

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
if not exist "%SERVER_DIR%" mkdir "%SERVER_DIR%"
if not exist "%DOWNLOADS_DIR%" mkdir "%DOWNLOADS_DIR%"

cd /d "%INSTALL_DIR%"

REM ============================================
REM PASO 1: Instalar Java 21
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 1: Instalando Java 21                                ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

java -version 2>nul | findstr /i "21" >nul
if %errorlevel% equ 0 (
    echo ✓ Java 21 ya está instalado
    echo.
) else (
    echo Descargando Java 21 de Adoptium...
    echo (Esto puede tardar varios minutos...)
    echo.
    
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando...'; Invoke-WebRequest -Uri 'https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3+9/OpenJDK21U-jdk_x64_windows_hotspot_21.0.3_9.msi' -OutFile '%DOWNLOADS_DIR%\java21.msi' -UseBasicParsing"
    
    if exist "%DOWNLOADS_DIR%\java21.msi" (
        echo.
        echo Instalando Java 21...
        echo IMPORTANTE: Si aparece una ventana, acepta las opciones por defecto
        echo.
        msiexec /i "%DOWNLOADS_DIR%\java21.msi" /qn ADDLOCAL=FeatureMain,FeatureEnvironment,FeatureJarFileRunWith,FeatureJavaHome INSTALLDIR="%JAVA21_DIR%"
        timeout /t 30 /nobreak >nul
        
        REM Configurar variables de entorno
        setx JAVA_HOME "%JAVA21_DIR%" /M >nul 2>&1
        setx PATH "%PATH%;%JAVA21_DIR%\bin" /M >nul 2>&1
        
        echo ✓ Java 21 instalado correctamente
    ) else (
        echo ❌ ERROR: No se pudo descargar Java 21
        echo Por favor, descárgalo manualmente desde https://adoptium.net/
        pause
        exit /b 1
    )
)

REM ============================================
REM PASO 2: Instalar Python 3.11
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 2: Instalando Python 3.11                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

python --version 2>nul | findstr /i "Python 3" >nul
if %errorlevel% equ 0 (
    echo ✓ Python ya está instalado
    echo.
) else (
    echo Descargando Python 3.11.6...
    echo.
    
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando...'; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe' -OutFile '%DOWNLOADS_DIR%\python.exe' -UseBasicParsing"
    
    if exist "%DOWNLOADS_DIR%\python.exe" (
        echo.
        echo Instalando Python 3.11.6...
        echo IMPORTANTE: Se instalará automáticamente con PATH configurado
        echo.
        "%DOWNLOADS_DIR%\python.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        timeout /t 30 /nobreak >nul
        
        echo ✓ Python instalado correctamente
    ) else (
        echo ❌ ERROR: No se pudo descargar Python
        pause
        exit /b 1
    )
)

REM Refrescar variables de entorno en la sesión actual
call refreshenv.cmd >nul 2>&1
set "PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311;%USERPROFILE%\AppData\Local\Programs\Python\Python311\Scripts"

REM ============================================
REM PASO 3: Instalar librería Python
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 3: Instalando librería Python para Minecraft         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo Instalando raspberryjammod via pip...
echo.
pip install raspberryjammod
if %errorlevel% equ 0 (
    echo ✓ Librería Python instalada correctamente
) else (
    echo ⚠️  Advertencia: Error al instalar la librería Python
    echo    Podrás intentarlo manualmente más tarde con: pip install raspberryjammod
)

REM ============================================
REM PASO 4: Descargar SKLauncher
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 4: Descargando SKLauncher                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

if not exist "%DOWNLOADS_DIR%\SKlauncher.exe" (
    echo Descargando SKLauncher...
    echo NOTA: SKLauncher se actualizará a su última versión
    echo       Debes ejecutarlo manualmente después de este script
    echo.
    
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando desde sklauncher.com...'; try { Invoke-WebRequest -Uri 'https://skmedix.pl/downloads/SKlauncher%203.2.8.exe' -OutFile '%DOWNLOADS_DIR%\SKlauncher.exe' -UseBasicParsing } catch { Write-Host 'URL no disponible, intentando alternativa...'; Invoke-WebRequest -Uri 'https://sklauncher.com/downloads/SKlauncher_3.2.8.exe' -OutFile '%DOWNLOADS_DIR%\SKlauncher.exe' -UseBasicParsing }"
    
    if exist "%DOWNLOADS_DIR%\SKlauncher.exe" (
        echo ✓ SKLauncher descargado
    ) else (
        echo ⚠️  No se pudo descargar SKLauncher automáticamente
        echo    Descárgalo manualmente desde: https://skmedix.pl/
        echo    Y guárdalo en: %DOWNLOADS_DIR%
    )
) else (
    echo ✓ SKLauncher ya está descargado
)

REM ============================================
REM PASO 5: Descargar Forge installer
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 5: Descargando Minecraft Forge 1.12.2                ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

if not exist "%DOWNLOADS_DIR%\forge-installer.jar" (
    echo Descargando Forge 1.12.2-14.23.5.2860...
    echo.
    
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando...'; Invoke-WebRequest -Uri 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar' -OutFile '%DOWNLOADS_DIR%\forge-installer.jar' -UseBasicParsing"
    
    if exist "%DOWNLOADS_DIR%\forge-installer.jar" (
        echo ✓ Forge installer descargado
    ) else (
        echo ❌ ERROR: No se pudo descargar Forge
        pause
        exit /b 1
    )
) else (
    echo ✓ Forge installer ya está descargado
)

REM ============================================
REM PASO 6: Instalar servidor Forge
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 6: Instalando Servidor Forge                         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

cd /d "%SERVER_DIR%"

if not exist "%SERVER_DIR%\forge-1.12.2-14.23.5.2860.jar" (
    echo Instalando servidor Forge...
    echo (Esto puede tardar varios minutos...)
    echo.
    
    java -jar "%DOWNLOADS_DIR%\forge-installer.jar" --installServer
    
    if exist "%SERVER_DIR%\forge-1.12.2-14.23.5.2860.jar" (
        echo ✓ Servidor Forge instalado correctamente
    ) else (
        echo ❌ ERROR: No se pudo instalar el servidor Forge
        pause
        exit /b 1
    )
) else (
    echo ✓ Servidor Forge ya está instalado
)

REM ============================================
REM PASO 7: Descargar servidor vanilla para librerías
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 7: Descargando servidor Minecraft 1.12.2             ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

if not exist "%SERVER_DIR%\minecraft_server.1.12.2.jar" (
    echo Descargando minecraft_server.1.12.2.jar...
    echo.
    
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando...'; Invoke-WebRequest -Uri 'https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar' -OutFile '%SERVER_DIR%\minecraft_server.1.12.2.jar' -UseBasicParsing"
    
    if exist "%SERVER_DIR%\minecraft_server.1.12.2.jar" (
        echo ✓ Servidor Minecraft descargado
    ) else (
        echo ⚠️  Advertencia: No se pudo descargar el servidor vanilla
    )
) else (
    echo ✓ Servidor Minecraft ya está descargado
)

REM ============================================
REM PASO 8: Configurar EULA
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 8: Aceptando EULA de Minecraft                       ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo #By changing the setting below to TRUE you are indicating your agreement to our EULA> eula.txt
echo #https://account.mojang.com/documents/minecraft_eula>> eula.txt
echo eula=true>> eula.txt

echo ✓ EULA aceptada automáticamente

REM ============================================
REM PASO 9: Descargar RaspberryJamMod
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 9: Descargando RaspberryJamMod                       ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

if not exist "%SERVER_DIR%\mods" mkdir "%SERVER_DIR%\mods"

REM Intentar copiar RaspberryJamMod.jar desde el repositorio
set "REPO_MOD=%~dp0RaspberryJamMod.jar"

if exist "%REPO_MOD%" (
    echo Copiando RaspberryJamMod.jar desde el repositorio...
    copy "%REPO_MOD%" "%SERVER_DIR%\mods\RaspberryJamMod.jar" >nul 2>&1
    if exist "%SERVER_DIR%\mods\RaspberryJamMod.jar" (
        echo ✓ RaspberryJamMod copiado desde el repositorio
    ) else (
        echo ❌ ERROR: No se pudo copiar RaspberryJamMod
        pause
        exit /b 1
    )
) else (
    REM Si no está en el repositorio, intentar descargarlo
    if not exist "%SERVER_DIR%\mods\RaspberryJamMod.jar" (
        echo RaspberryJamMod.jar no encontrado en el repositorio.
        echo Descargando desde GitHub...
        echo.
        
        powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Descargando...'; Invoke-WebRequest -Uri 'https://github.com/arpruss/raspberryjammod/releases/download/0.94/RaspberryJamMod.jar' -OutFile '%SERVER_DIR%\mods\RaspberryJamMod.jar' -UseBasicParsing"
        
        if exist "%SERVER_DIR%\mods\RaspberryJamMod.jar" (
            echo ✓ RaspberryJamMod descargado desde GitHub
        ) else (
            echo ❌ ERROR CRÍTICO: No se pudo obtener RaspberryJamMod
            echo.
            echo El mod es esencial para que Python funcione con Minecraft.
            echo.
            echo SOLUCIÓN MANUAL:
            echo 1. Descarga desde: https://github.com/arpruss/raspberryjammod/releases/download/0.94/RaspberryJamMod.jar
            echo 2. Guárdalo en: %SERVER_DIR%\mods\
            echo.
            pause
            exit /b 1
        )
    ) else (
        echo ✓ RaspberryJamMod ya está instalado
    )
)

REM También copiar a la carpeta de cliente para SKLauncher
echo.
echo Preparando RaspberryJamMod para el cliente...

set "CLIENT_MODS=%AppData%\.minecraft\mods"
if not exist "%CLIENT_MODS%" mkdir "%CLIENT_MODS%"

if exist "%SERVER_DIR%\mods\RaspberryJamMod.jar" (
    copy "%SERVER_DIR%\mods\RaspberryJamMod.jar" "%CLIENT_MODS%\" >nul 2>&1
    echo ✓ Mod copiado a carpeta del cliente
)

REM ============================================
REM PASO 10: Configurar servidor
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║ PASO 10: Configurando servidor                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Crear server.properties con configuración optimizada
echo #Minecraft server properties> server.properties
echo #Generado automáticamente por el instalador>> server.properties
echo server-port=25565>> server.properties
echo gamemode=1>> server.properties
echo difficulty=0>> server.properties
echo spawn-protection=0>> server.properties
echo max-players=20>> server.properties
echo online-mode=false>> server.properties
echo pvp=false>> server.properties
echo enable-command-block=true>> server.properties
echo level-name=world>> server.properties
echo motd=§aServidor Minecraft + Python - Academia Cervantes>> server.properties
echo allow-flight=true>> server.properties
echo max-world-size=29999984>> server.properties
echo force-gamemode=false>> server.properties
echo spawn-animals=true>> server.properties
echo spawn-monsters=false>> server.properties
echo spawn-npcs=true>> server.properties

echo ✓ server.properties configurado

REM ============================================
REM Crear script de inicio del servidor
REM ============================================

echo.
echo Creando script de inicio del servidor...

(
echo @echo off
echo setlocal EnableDelayedExpansion
echo.
echo echo ============================================
echo echo Minecraft Forge 1.12.2 Server
echo echo ============================================
echo echo.
echo.
echo REM Check if Java 8 portable exists, if not download it
echo if not exist "java8\bin\java.exe" ^(
echo     echo Java 8 portable not found. Downloading...
echo     echo.
echo.
echo     if not exist "java8" mkdir java8
echo.
echo     echo Downloading Java 8 from Adoptium...
echo     echo Please wait, this may take several minutes...
echo     powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u432-b06/OpenJDK8U-jdk_x64_windows_hotspot_8u432b06.zip' -OutFile 'java8.zip'"
echo.
echo     if not exist "java8.zip" ^(
echo         echo ERROR: Download failed! Please check your internet connection.
echo         pause
echo         exit /b 1
echo     ^)
echo.
echo     echo.
echo     echo Extracting Java 8...
echo     powershell -Command "Expand-Archive -Path 'java8.zip' -DestinationPath '.' -Force"
echo.
echo     REM Move files from extracted folder to java8
echo     for /d %%%%i in ^(jdk8u432-b06^) do ^(
echo         xcopy "%%%%i" "java8\" /E /I /H /Y ^>nul
echo         rmdir "%%%%i" /S /Q
echo     ^)
echo.
echo     del java8.zip
echo.
echo     echo.
echo     echo Java 8 downloaded and extracted successfully!
echo     echo.
echo ^)
echo.
echo REM Show Java version
echo echo Using portable Java 8:
echo java8\bin\java.exe -version
echo echo.
echo.
echo echo Starting Minecraft Server with 2GB RAM...
echo echo.
echo echo ⚠️  Para detener el servidor correctamente, escribe 'stop' y pulsa Enter
echo echo ❌  NO cierres esta ventana directamente o podrías perder datos
echo echo.
echo.
echo REM Start server with Java 8
echo java8\bin\java.exe -Xmx2G -Xms2G -jar forge-1.12.2-14.23.5.2860.jar nogui
echo.
echo echo.
echo echo Server stopped.
echo pause
) > "%SERVER_DIR%\start_server.bat"

echo ✓ start_server.bat creado

REM ============================================
REM Crear carpeta de scripts de ejemplo
REM ============================================

echo.
echo Creando carpeta de scripts de ejemplo...

if not exist "%SERVER_DIR%\scripts" mkdir "%SERVER_DIR%\scripts"

REM Crear script de ejemplo 1: Torre de diamantes
(
echo from mcpi.minecraft import Minecraft
echo from mcpi import block
echo import time
echo.
echo print^("Conectando a Minecraft..."^)
echo try:
echo     mc = Minecraft.create^(^)
echo     print^("✓ Conectado correctamente"^)
echo except ConnectionRefusedError:
echo     print^("❌ ERROR: No se puede conectar al servidor"^)
echo     print^("   Verifica que:"^)
echo     print^("   1. El servidor está arrancado"^)
echo     print^("   2. Estás dentro del juego ^(conectado^)"^)
echo     print^("   3. RaspberryJamMod está instalado ^(ver menú Mods^)"^)
echo     input^("Pulsa Enter para salir..."^)
echo     exit^(^)
echo.
echo mc.postToChat^("¡Hola desde Python!"^)
echo.
echo pos = mc.player.getPos^(^)
echo print^(f"Tu posición: X={int^(pos.x^)}, Y={int^(pos.y^)}, Z={int^(pos.z^)}"^)
echo.
echo mc.postToChat^("Construyendo torre..."^)
echo for i in range^(10^):
echo     mc.setBlock^(pos.x + 3, pos.y + i, pos.z, block.DIAMOND_BLOCK.id^)
echo     time.sleep^(0.1^)
echo.
echo mc.postToChat^("¡Torre de diamante construida!"^)
echo print^("✓ Torre construida correctamente"^)
) > "%SERVER_DIR%\scripts\torre.py"

REM Crear script de ejemplo 2: Cubo de colores
(
echo from mcpi.minecraft import Minecraft
echo from mcpi import block
echo import time
echo.
echo mc = Minecraft.create^(^)
echo mc.postToChat^("Creando cubo arcoíris..."^)
echo.
echo pos = mc.player.getPos^(^)
echo.
echo # Lista de bloques de colores ^(lana^)
echo colores = [block.WOOL.id] * 16
echo.
echo # Crear un cubo de 5x5x5
echo size = 5
echo for x in range^(size^):
echo     for y in range^(size^):
echo         for z in range^(size^):
echo             color = ^(x + y + z^) %% 16
echo             mc.setBlock^(pos.x + x, pos.y + y, pos.z + z, block.WOOL.id, color^)
echo             time.sleep^(0.01^)
echo.
echo mc.postToChat^("¡Cubo completado!"^)
) > "%SERVER_DIR%\scripts\cubo_colores.py"

REM Crear script de ejemplo 3: Teletransporte
(
echo from mcpi.minecraft import Minecraft
echo.
echo mc = Minecraft.create^(^)
echo.
echo mc.postToChat^("¡Te voy a teletransportar!"^)
echo pos = mc.player.getPos^(^)
echo.
echo # Teletransportar 50 bloques hacia arriba
echo mc.player.setPos^(pos.x, pos.y + 50, pos.z^)
echo mc.postToChat^("¡Mira qué altura!"^)
) > "%SERVER_DIR%\scripts\teletransporte.py"

echo ✓ Scripts de ejemplo creados

REM Copiar script de diagnóstico
if exist "%~dp0test_conexion.py" (
    copy "%~dp0test_conexion.py" "%SERVER_DIR%\scripts\" >nul 2>&1
    echo ✓ Script de diagnóstico copiado
)

REM ============================================
REM Crear guía rápida
REM ============================================

echo.
echo Creando guía rápida...

(
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║          GUÍA RÁPIDA - MINECRAFT + PYTHON                     ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo ✓ INSTALACIÓN COMPLETADA CORRECTAMENTE
echo.
echo ═══════════════════════════════════════════════════════════════
echo SIGUIENTES PASOS:
echo ═══════════════════════════════════════════════════════════════
echo.
echo 1. INSTALAR SKLAUNCHER ^(cliente^)
echo    -----------------------------------
echo    • Ejecuta: %DOWNLOADS_DIR%\SKlauncher.exe
echo    • Instálalo normalmente
echo    • Abre SKLauncher y configura tu cuenta
echo    • En el menú de versiones, selecciona: 1.12.2-forge
echo    • IMPORTANTE: Ejecuta Minecraft una vez para generar carpetas
echo.
echo 2. INSTALAR FORGE EN EL CLIENTE
echo    -----------------------------------
echo    • Ejecuta: %DOWNLOADS_DIR%\forge-installer.jar
echo    • Selecciona "Install client"
echo    • Deja la ruta por defecto
echo    • Pulsa OK
echo.
echo 3. ARRANCAR EL SERVIDOR
echo    -----------------------------------
echo    • Ve a: %SERVER_DIR%
echo    • Ejecuta: start_server.bat
echo    • Espera a que aparezca "Done" en la consola
echo.
echo 4. CONECTARTE AL SERVIDOR
echo    -----------------------------------
echo    • Abre Minecraft con SKLauncher
echo    • Selecciona el perfil Forge 1.12.2
echo    • Ve a Multijugador → Añadir servidor
echo    • Dirección: localhost:25565
echo    • Conecta y ¡a jugar!
echo.
echo 5. EJECUTAR TUS PRIMEROS SCRIPTS
echo    -----------------------------------
echo    • IMPORTANTE: El servidor debe estar arrancado
echo    • Y debes estar dentro del juego
echo    • Abre una consola ^(cmd^) en: %SERVER_DIR%\scripts
echo    • Ejecuta: python torre.py
echo    • ¡Verás una torre de diamantes aparecer!
echo.
echo ═══════════════════════════════════════════════════════════════
echo SCRIPTS INCLUIDOS:
echo ═══════════════════════════════════════════════════════════════
echo.
echo DIAGNÓSTICO:
echo • test_conexion.py - Verifica que Python conecta con Minecraft
echo.
echo EJEMPLOS:
echo • torre.py - Crea una torre de diamantes
echo • cubo_colores.py - Genera un cubo arcoíris
echo • teletransporte.py - Te teletransporta hacia arriba
echo.
echo ⚠️  SI LOS SCRIPTS NO FUNCIONAN: Ejecuta primero test_conexion.py
echo    para diagnosticar el problema
echo.
echo ═══════════════════════════════════════════════════════════════
echo UBICACIONES IMPORTANTES:
echo ═══════════════════════════════════════════════════════════════
echo.
echo Servidor:        %SERVER_DIR%
echo Scripts:         %SERVER_DIR%\scripts
echo SKLauncher:      %DOWNLOADS_DIR%
echo Mods cliente:    %%AppData%%\.minecraft\mods
echo.
echo ═══════════════════════════════════════════════════════════════
echo PROBLEMAS COMUNES:
echo ═══════════════════════════════════════════════════════════════
echo.
echo ❌ "Java no reconocido"
echo    → Reinicia el ordenador para que se cargue la variable PATH
echo.
echo ❌ "El mod no aparece en Minecraft"
echo    → Asegúrate de usar el perfil Forge 1.12.2
echo    → Verifica que RaspberryJamMod.jar esté en la carpeta mods
echo.
echo ❌ "Scripts de Python no funcionan"
echo    → El servidor debe estar arrancado
echo    → Debes estar dentro del juego
echo    → Ejecuta: pip install raspberryjammod
echo.
echo ═══════════════════════════════════════════════════════════════
echo PARA INVITAR AMIGOS:
echo ═══════════════════════════════════════════════════════════════
echo.
echo 1. Arranca el servidor con start_server.bat
echo 2. Abre cmd y ejecuta: ipconfig
echo 3. Busca tu IPv4 Address ^(ej: 192.168.1.100^)
echo 4. Tus amigos deben conectarse a: TU_IP:25565
echo 5. Deben tener el mod RaspberryJamMod instalado también
echo.
echo ═══════════════════════════════════════════════════════════════
echo.
echo 💚 Creado para Academia Cervantes - Robótica
echo.
) > "%INSTALL_DIR%\GUIA_RAPIDA.txt"

echo ✓ Guía rápida creada

REM ============================================
REM Crear acceso directo en el escritorio
REM ============================================

echo.
echo Creando accesos directos...

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%UserProfile%\Desktop\Servidor Minecraft.lnk'); $Shortcut.TargetPath = '%SERVER_DIR%\start_server.bat'; $Shortcut.WorkingDirectory = '%SERVER_DIR%'; $Shortcut.IconLocation = '%SystemRoot%\System32\shell32.dll,14'; $Shortcut.Save()"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%UserProfile%\Desktop\Scripts Python Minecraft.lnk'); $Shortcut.TargetPath = '%SERVER_DIR%\scripts'; $Shortcut.IconLocation = '%SystemRoot%\System32\shell32.dll,4'; $Shortcut.Save()"

echo ✓ Accesos directos creados en el escritorio

REM ============================================
REM Resumen final
REM ============================================

echo.
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║               ✓ INSTALACIÓN COMPLETADA                        ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo Todo está listo para empezar a programar en Minecraft!
echo.
echo 📝 IMPORTANTE - Lee esto antes de continuar:
echo.
echo    1. Abre el archivo GUIA_RAPIDA.txt en tu escritorio
echo    2. Sigue los pasos numerados
echo    3. Instala SKLauncher y Forge en el cliente
echo    4. Arranca el servidor con el acceso directo del escritorio
echo    5. ¡Empieza a programar!
echo.
echo 📁 Archivos importantes:
echo    • Guía rápida: %INSTALL_DIR%\GUIA_RAPIDA.txt
echo    • Servidor: %SERVER_DIR%
echo    • Scripts: %SERVER_DIR%\scripts
echo.
echo 💡 Consejo: Abre Visual Studio Code en la carpeta del servidor
echo    para editar scripts y configuración fácilmente.
echo.
echo.

REM Abrir la guía automáticamente
start notepad "%INSTALL_DIR%\GUIA_RAPIDA.txt"

REM Abrir el explorador en la carpeta del servidor
start explorer "%SERVER_DIR%"

echo.
echo Pulsa cualquier tecla para finalizar...
pause >nul

REM Volver al directorio original
cd /d "%~dp0"

echo.
echo ✓ Proceso completado
echo.
timeout /t 3

exit /b 0

