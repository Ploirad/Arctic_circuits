# 🎮 MINECRAFT + PYTHON CHALLENGE 🐍

## ¡Bienvenidos al reto más épico del curso!

---

## 📋 Índice

1. [¿De qué va este reto?](#de-qué-va-este-reto)
2. [Paso 1: Instalando SKLauncher](#paso-1-instalando-sklauncher)
3. [Paso 2: Instalando Minecraft Forge](#paso-2-instalando-minecraft-forge)
4. [Paso 3: Instalando el RaspberryJamMod (el mod de Python)](#paso-3-instalando-el-raspberryjammod-el-mod-de-python)
5. [Paso 4: Montando tu servidor](#paso-4-montando-tu-servidor)
6. [Paso 5: Cómo invitar a tus colegas](#paso-5-cómo-invitar-a-tus-colegas)
7. [Paso 6: Apagar y reiniciar el servidor](#paso-6-apagar-y-reiniciar-el-servidor)
8. [Paso 7: Tu primer script en Python](#paso-7-tu-primer-script-en-python)
9. [Ayuda y comunidad](#ayuda-y-comunidad)
10. [Problemas comunes y cómo arreglarlos](#problemas-comunes-y-cómo-arreglarlos)
11. [Retos y próximos pasos](#retos-y-próximos-pasos)

---

## 🎯 ¿De qué va este reto?

¡Atención, aventureros del código! En los próximos dos días vais a convertiros en auténticos **hackers de Minecraft** (de los buenos, no de los tramposos 😎).

### 🧭 La misión:
- Instalar una versión de Minecraft que se lleve bien con Python.
- Crear vuestro propio servidor local.
- Dejar que vuestros amigos se unan a vuestro mundo.
- Construir cosas alucinantes con código en vez de hacer clics como principiantes.

Al acabar, podréis invocar bloques de diamante, levantar ciudades enteras con unas líneas de Python y presumir de ser auténticos dioses del bloque. 💎✨

---

## 🚀 Paso 1: Instalando SKLauncher

### ¿Por qué SKLauncher?

Porque es gratuito, fácil de usar, permite mods sin dramas y se lleva genial con Forge (que necesitaremos más adelante). Además, es más cómodo que el launcher oficial para hacer experimentos.

### ⚙️ Instalación paso a paso

#### 1️⃣ **Descarga Java 21 (muy importante)**

Minecraft necesita Java para funcionar. Sin Java, el juego ni arranca.

**En Windows:**
1. Entra en [Adoptium](https://adoptium.net/)
2. Pulsa el botón **"Latest LTS Release"** (debería ser Java 21)
3. Descarga el instalador `.msi`
4. Instálalo y, MUY IMPORTANTE, marca estas tres casillas cuando te lo pida:
   - ✅ **Add to PATH**
   - ✅ **Set JAVA_HOME variable**
   - ✅ **JavaSoft (Oracle) registry keys**

5. Finaliza la instalación.

**Para comprobar que todo va bien:**
1. Pulsa `Windows + R`
2. Escribe `cmd` y pulsa Enter
3. Escribe `java -version` y pulsa Enter
4. Si ves algo como `openjdk version 21.0.x`, todo correcto 👌

Si no aparece la versión 21, pide ayuda antes de seguir.

#### 2️⃣ **Descarga SKLauncher**

1. Entra en la web oficial: [https://skmedix.pl/](https://skmedix.pl/)
   - ⚠️ **Cuidado:** hay webs falsas. Usa solo la oficial o te la puede liar con malware.

2. Ve a **"Downloads"**
3. Elige tu versión:
   - **Windows Setup (.exe)** – Recomendado para principiantes.
   - **Portable** – Solo si sabes lo que haces.
   - **.jar** – Para usuarios avanzados.

4. Descarga el instalador `.exe` (el primero, el fácil).

#### 3️⃣ **Instala SKLauncher**

1. Ejecuta el `.exe`
2. Si Windows te muestra una alerta, pulsa "Más información" → "Ejecutar de todas formas" (si viene de la web oficial, es seguro).
3. Sigue el asistente de instalación.
4. Abre SKLauncher.

#### 4️⃣ **Primer arranque**

Al abrirlo verás la pantalla principal con el login:
- Si tienes cuenta de Microsoft y Minecraft comprado, usa esa.
- Si no, puedes usar el modo gratuito de SKLauncher (solo para pruebas locales).

---

## ⚙️ Paso 2: Instalando Minecraft Forge

### ¿Qué es Forge?

Forge es como la base sobre la que funcionan los mods. Sin él, el mod de Python (RaspberryJamMod) no funcionaría.

### 🧱 ¿Qué versión usamos?

Usaremos **Minecraft 1.12.2** porque:
- Es la más estable para mods.
- RaspberryJamMod va perfecto con ella.
- Todos los tutoriales de Python la usan.
- No es ni demasiado antigua ni demasiado nueva: está en la zona dorada de Minecraft 😄

### Instalación paso a paso

#### 1️⃣ **Primero ejecuta Minecraft 1.12.2 vanilla**

Necesitamos lanzarlo al menos una vez antes de poner Forge:

1. Abre SKLauncher.
2. En el menú de versiones, selecciona **"release 1.12.2"**.
3. Pulsa **Play** y deja que descargue todo.
4. Cuando se abra, ciérralo. Esto crea las carpetas necesarias para Forge.

#### 2️⃣ **Descarga Forge 1.12.2**

1. Entra en [la web de Forge](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.12.2.html)
2. Busca la versión **Recommended** (suele ser 14.23.5.2859 o parecida).
3. Pulsa **Installer**.
4. Espera 5 segundos en la página de anuncios y pulsa **SKIP** arriba a la derecha.
5. Descarga el `.jar`.

#### 3️⃣ **Instala Forge**

1. Abre el archivo descargado (`forge-1.12.2-14.23.5.XXXX-installer.jar`).
2. Selecciona **"Install client"**.
3. Deja la ruta por defecto.
4. Pulsa **OK** y espera.
5. Si ves el mensaje “Successfully installed client profile forge”, ¡misión cumplida!

#### 4️⃣ **Lanza Forge desde SKLauncher**

1. Abre SKLauncher.
2. En el menú de versiones, elige **"1.12.2-forge-14.23.5.XXXX"**.
3. Pulsa **Play**.
4. Si todo va bien, verás el botón **Mods** en el menú de Minecraft.
5. Cierra el juego — ya podemos pasar al mod de Python 😎.

---

## 🐍 Paso 3: Instalando el RaspberryJamMod (el mod de Python)

Aquí empieza la magia: RaspberryJamMod es el mod que conecta Minecraft con Python. A partir de ahora, podrás construir, teletransportarte o crear estructuras locas usando código.

### 🪄 Lo que podrás hacer:
- Crear bloques con código.
- Hacer bucles para construir estructuras automáticas.
- Crear minijuegos o trampas.
- Automatizar tareas como un auténtico ingeniero de Redstone.

### Instala Python
1. Vete a [Python.org](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe) e instala python.
2. **marca la casilla “Add Python to PATH”** durante la instalación:
<img width="646" height="397" alt="image" src="https://github.com/user-attachments/assets/e6ede275-25b7-495a-8ba6-7184d0e2b5dc" />
3. Termina de instalar python en tu ordenador.

### Instalación

1. Ve a [RaspberryJamMod Releases en GitHub](https://github.com/arpruss/raspberryjammod/releases)
2. Ve a la versión 0.94 y descarga el fichero **RaspberryJamMod-Installer.exe**
3. Asegúrate de que tienes las opciones como en la foto <img width="493" height="380" alt="image" src="https://github.com/user-attachments/assets/9b976412-5afc-43eb-9e90-0a85e512cba0" />
4. Cuando hayas finalizado la ejecución totalmente, te habrá creado el fichero "RaspberryJamMod.jar" en la carpeta %appdata%\.minecraft\mods

#### Comprueba que existe el mod de minecraft en su sitio

1. Pulsa `Windows + R` → escribe `%appdata%` y Enter.
2. Abre la carpeta `.minecraft` → entra en `mods` (debería existir la carpeta, si hiciste el paso anterior bien)
3. Comprueba que existe RaspberryJamMod.jar

#### Instala la librería de Python

Abre el símbolo del sistema (`cmd`) y escribe:
```
pip install raspberryjammod
```


#### Comprueba que funciona

1. Abre Minecraft con el perfil Forge 1.12.2.
2. En el menú principal, entra en **Mods**.
3. Si ves “RaspberryJamMod” en la lista, ¡todo listo! 🎉
<img width="847" height="505" alt="image" src="https://github.com/user-attachments/assets/109feaca-41c5-4019-a63d-172273d73b1f" />

---

## 🖥️ Paso 4: Montando tu servidor

### ¿Por qué un servidor?

Porque así tú y tus amigos podréis compartir mundo, jugar juntos y ejecutar scripts Python que afecten a todos. Además, tú mandas 😏.

#### 1️⃣ Descarga el servidor Forge

1. Desde la [misma página de Forge](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.12.2.html), descarga de nuevo el **Installer**.
2. Pulsa windows + R y escribe %UserProfile%\Documents
3. Se abrirá la carpeta de mis documentos del usuario actual. Crea una carpeta que se llame "ServerMinecraft" y descarga ahí el installer de Forge

#### 2️⃣ Instálalo

1. Accede a la carpeta donde descargaste Forge (%UserProfile%\Documents\ServerMinecraft)
2. Ejecuta el instalador y selecciona **Install server**, con las opciones que te muestro en la foto, eligiendo la carpeta %UserProfile%\Documents\ServerMinecraft :
<img width="385" height="307" alt="image" src="https://github.com/user-attachments/assets/83af65cb-596d-4807-a40d-230b20b81c60" />
3. Espera a que se generen los archivos.
4. Verás todos estos ficheros:
<img width="1159" height="689" alt="image" src="https://github.com/user-attachments/assets/67d44c00-b2db-4c8e-b8b4-4b9ff9ebce58" />
5. Haz doble click en el que pone minecraft_server.1.12.2.jar y se te crearán todos estos ficheros:
<img width="1153" height="687" alt="image" src="https://github.com/user-attachments/assets/cada32cd-5168-4eb6-a0d6-438fb8323ce6" />

#### 3️⃣ Acepta la EULA

1. Abre el archivo `eula.txt`.
2. Cambia `eula=false` por `eula=true`.
3. Guarda y cierra.
4. Vuelve a ejecutar el fichero minecraft_server.1.12.2.jar y se te abrirá la siguiente pantalla con el servidor:
<img width="1067" height="573" alt="image" src="https://github.com/user-attachments/assets/e908fdc9-9e02-4443-a10f-8c6276cad14e" />
5. Te saldrá una ventana que te dirá si quieres permitir que se hagan cambios. Dile que permitir.
6. 

#### 4️⃣ Añade el mod al servidor

1. En la carpeta del servidor, crea una carpeta `mods`.
2. Descarga el fichero [RaspberryJamMod](https://github.com/blockpush25/SNOW-DRIFTERS/blob/main/minecraft_challenge/RaspberryJamMod.jar) en la carpeta mods que acabas de crear
3. Abre visual studio code, y selecciona archivo -> nueva ventana
4. selecciona el botón azul "abrir carpeta" y elige, dentro de documentos, la carpeta que creaste "ServerMinecraft"

#### 5️⃣ Configura las propiedades

Abre `server.properties` (desde visual studio code) y cambia:
```
gamemode=creative
difficulty=peaceful
pvp=false
online-mode=false
```
Guarda y cierra. (desde visual studio, lo puedes hacer con control + s para ir rápido)

#### 6️⃣ Crea el archivo para arrancar el servidor

1. Crea un nuevo archivo de texto y renómbralo a `start_server.bat`. Para hacer eso en visual studio, haz click derecho en el explorador de archivos (parte izquierda de la ventana) y selecciona nuevo archivo. en el cuadro de texto, pon "start_server.bat"
3. Ábrelo y pega esto:


```batch
@echo off
setlocal EnableDelayedExpansion

echo ============================================
echo Minecraft Forge 1.12.2 Server
echo ============================================
echo.

REM Check if Java 8 portable exists, if not download it
if not exist "java8\bin\java.exe" (
    echo Java 8 portable not found. Downloading...
    echo.

    if not exist "java8" mkdir java8

    echo Downloading Java 8 from Adoptium...
    echo Please wait, this may take several minutes...
    powershell -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u432-b06/OpenJDK8U-jdk_x64_windows_hotspot_8u432b06.zip' -OutFile 'java8.zip'"

    if not exist "java8.zip" (
        echo ERROR: Download failed! Please check your internet connection.
        pause
        exit /b 1
    )

    echo.
    echo Extracting Java 8...
    powershell -Command "Expand-Archive -Path 'java8.zip' -DestinationPath '.' -Force"

    REM Move files from extracted folder to java8
    for /d %%i in (jdk8u432-b06) do (
        xcopy "%%i" "java8\" /E /I /H /Y >nul
        rmdir "%%i" /S /Q
    )

    del java8.zip

    echo.
    echo Java 8 downloaded and extracted successfully!
    echo.
)

REM Show Java version
echo Using portable Java 8:
java8\bin\java.exe -version
echo.

REM Accept EULA check
if not exist "eula.txt" (
    echo EULA not found. Creating eula.txt...
    echo #By changing the setting below to TRUE you are indicating your agreement to our EULA https://account.mojang.com/documents/minecraft_eula> eula.txt
    echo eula=false>> eula.txt
    echo.
    echo Please edit eula.txt and change eula=false to eula=true
    echo Then run this script again.
    pause
    exit /b 1
)

echo Starting Minecraft Server with 2GB RAM...
echo.

REM Start server with Java 8
java8\bin\java.exe -Xmx2G -Xms2G -jar forge-1.12.2-14.23.5.2860.jar nogui

echo.
echo Server stopped.
pause

   ```
4. Guarda y ciérralo. (recuerda: control + s)
5. Haz click derecho en el explorador de visual studio y selecciona "abrir terminal integrado". Se te verá de esta manera:
<img width="1454" height="795" alt="image" src="https://github.com/user-attachments/assets/d265bb19-66c0-4ca0-887b-beb105c75ecb" />
   
6. escribe .\start_server.bat para ejecutar el servidor

---

## 🌐 Paso 5: Cómo invitar a tus colegas

1. Lanza el servidor con `start_server.bat`.
2. Busca tu IP local con `ipconfig` en la consola de Windows (IPv4 Address).
3. Tus amigos deben:
   - Tener el mismo mod instalado.
   - Estar en la misma red WiFi.
   - Usar la misma versión de Minecraft.

### Conexión

Tus colegas deben:
1. Ir a **Multijugador → Añadir servidor**.
2. Nombre: el que quieran.
3. Dirección: tu IP (por ejemplo, `192.168.1.100:25565`).
4. Pulsar **Hecho** y unirse.

Si no conecta:
- Comprueba el cortafuegos.
- Asegúrate de que el servidor está en marcha.
- Verifica la IP.

---

## 🔄 Paso 6: Apagar y reiniciar el servidor

### Cómo apagarlo bien

❌ No cierres la ventana a lo bruto.
✅ Escribe `stop` en la consola y pulsa Enter.

Así Minecraft guarda el mundo y no se corrompe.

### Reiniciar

Solo tienes que volver a ejecutar `start_server.bat`. Fácil.

### Consejo pro 💡

Haz copias de seguridad antes de hacer locuras con Python:
- Para ello, copia toda la carpeta del servidor.

---

## 🧠 Paso 7: Tu primer script en Python

Llega el momento que estabas esperando: ¡programar en Minecraft!

1. Con el servidor arrancado, crea una carpeta para tus scripts donde tengas el servidor, por ejemplo `scripts`.
2. Dentro, crea un archivo `torre.py` y pega este código:

```python
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
mc.postToChat("¡Hola desde Python!")

pos = mc.player.getPos()
for i in range(10):
    mc.setBlock(pos.x + 3, pos.y + i, pos.z, block.DIAMOND_BLOCK.id)

mc.postToChat("¡Torre de diamante construida!")
```

3. ¡Importante! tienes que tener el servidor arrancado, y al menos una jugador dentro del juego para que funcione! Después ejecuta el script desde la consola con:
```
python torre.py
```
Y... ¡boom! Una torre de diamantes aparecerá junto a ti 💎

---

## 💬 Ayuda y comunidad

Si te atascas:
1. Mira el mensaje de error: suele decirte el problema.
2. Busca en Google o en [GitHub Issues del mod](https://github.com/arpruss/raspberryjammod/issues).
3. Pregunta a tus compis o al profe (que seguro se lo ha roto antes también 😅).

---

## 🔧 Problemas comunes

**❌ Java no reconocido:** reinstala Java 21 y marca “Add to PATH”.  
**❌ El mod no aparece:** asegúrate de que el `.jar` está en `mods` y que estás usando Forge.  
**❌ No conecta al servidor:** revisa IP, firewall y que todos tengáis la misma versión.  
**❌ Script sin efecto:** entra al mundo antes de ejecutarlo y asegúrate de usar `mc.player.getPos()`.

---

## 🧩 Retos y próximos pasos

### Nivel principiante
- Construye una casa con Python.
- Crea un arco iris de lana.
- Genera un camino que te siga.

### Nivel intermedio
- Crea un laberinto automático.
- Haz un ascensor.
- Programa un minijuego tipo parkour.

### Nivel avanzado
- Generador de arte pixelado.
- Fractales (tipo triángulo de Sierpinski).
- Juego multijugador con puntuaciones.

---

## 🎓 Lo que has aprendido

Has:
- Instalado y configurado mods de Minecraft.
- Montado tu propio servidor.
- Aprendido a usar Python para controlar un mundo 3D.
- Colaborado y depurado errores como un pro.

Eso ya son **habilidades de desarrollador y administrador de sistemas**. 🔥

---

## 🚀 Próximos pasos

1. Aprende más Python (funciones, clases, ficheros...).
2. Prueba otros mods como **ComputerCraft** o **Create**.
3. Comparte tus creaciones y enseña a otros.

---

## 🎮 ¡A jugar y programar!

Ya tienes todo preparado. Cierra este documento, abre Minecraft y... ¡a picar código y bloques! 🧱🐍

**Hecho con 💚 para la clase de Robótica de Academia Cervantes**

