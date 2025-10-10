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

### Instalación

1. Ve a [RaspberryJamMod Releases en GitHub](https://github.com/arpruss/raspberryjammod/releases)
2. Descarga la versión más reciente compatible con **Minecraft 1.12.2** (`.jar`).

#### Instala la librería de Python

Abre el símbolo del sistema (`cmd`) y escribe:
```
pip install raspberryjammod
```
Si da error con `pip`, instala Python desde [python.org](https://www.python.org/downloads/) y **marca la casilla “Add Python to PATH”** durante la instalación.

#### Coloca el mod en Minecraft

1. Pulsa `Windows + R` → escribe `%appdata%` y Enter.
2. Abre la carpeta `.minecraft` → entra en `mods` (si no existe, créala).
3. Copia dentro el `.jar` de RaspberryJamMod.

#### Comprueba que funciona

1. Abre Minecraft con el perfil Forge 1.12.2.
2. En el menú principal, entra en **Mods**.
3. Si ves “RaspberryJamMod” en la lista, ¡todo listo! 🎉

---

## 🖥️ Paso 4: Montando tu servidor

### ¿Por qué un servidor?

Porque así tú y tus amigos podréis compartir mundo, jugar juntos y ejecutar scripts Python que afecten a todos. Además, tú mandas 😏.

#### 1️⃣ Descarga el servidor Forge

1. Desde la [misma página de Forge](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.12.2.html), descarga de nuevo el **Installer**.
2. Crea una carpeta llamada, por ejemplo, `C:\MinecraftServer`.

#### 2️⃣ Instálalo

1. Copia el `.jar` del instalador en esa carpeta.
2. Ejecútalo y selecciona **Install server**.
3. Espera a que se generen los archivos.

#### 3️⃣ Acepta la EULA

1. Abre el archivo `eula.txt`.
2. Cambia `eula=false` por `eula=true`.
3. Guarda y cierra.

#### 4️⃣ Añade el mod al servidor

1. En la carpeta del servidor, abre `mods`.
2. Copia el `.jar` de RaspberryJamMod.

#### 5️⃣ Crea el archivo para arrancar el servidor

1. Crea un nuevo archivo de texto y renómbralo a `start_server.bat`.
2. Ábrelo con el Bloc de notas y pega esto:
   ```batch
   java -Xmx2G -Xms2G -jar forge-1.12.2-14.23.5.XXXX-universal.jar nogui
   pause
   ```
3. Guarda y ciérralo.
4. Haz doble clic para arrancar el servidor.

#### 6️⃣ Configura las propiedades

Abre `server.properties` y cambia, por ejemplo:
```
gamemode=creative
difficulty=peaceful
pvp=false
max-players=20
```
Guarda y cierra.

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

1. Crea una carpeta para tus scripts, por ejemplo `C:\MinecraftPython`.
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

3. Ejecuta el script desde la consola con:
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

