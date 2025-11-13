# 🤖 Eurobot 2026 - Planificador de Tareas

Herramienta de gestión de tareas para el equipo de robótica de Academia Cervantes preparándose para Eurobot 2026 "Winter is Coming".

---

## 📋 ¿Qué es esto?

Esta herramienta te ayuda a **organizar y seguir** todas las tareas necesarias para construir vuestro robot y presentaros con garantías a la competición Eurobot 2026.

El proyecto está dividido en **6 FASES** con **32 tareas** organizadas para un equipo de **8 personas**.

---

## 🚀 Cómo Usarla

### Paso 1: Abrir la herramienta

1. Ve a la carpeta `EurobotPlanner`
2. Haz **doble clic** en el archivo `eurobot_2026_planner.html`
3. Se abrirá en tu navegador (Chrome, Firefox, Edge, etc.)

**⚠️ IMPORTANTE:** No necesitas internet, funciona totalmente offline.

### Paso 2: Asignar tareas

1. **Explora las 6 fases** haciendo scroll por la página
2. Para cada tarea, haz clic en el **desplegable "Sin asignar"**
3. Selecciona el nombre del miembro del equipo responsable
4. La sección "👥 Equipo" se actualiza automáticamente

### Paso 3: Marcar progreso

- ✅ **Checkbox**: Marca la tarea como **completada**
- ▶️ **Botón "Iniciar"**: Marca la tarea como **en progreso**
- ⏸️ **Botón "Pausar"**: Vuelve la tarea a **pendiente**

### Paso 4: Guardar tu trabajo

- Haz clic en **"💾 Guardar Progreso"**
- Los datos se guardan en el navegador (localStorage)
- ⚠️ Usa siempre el **mismo ordenador y navegador** o exporta/importa

### Paso 5: Exportar datos (opcional)

- Haz clic en **"📊 Exportar"**
- Se descarga un archivo JSON con fecha
- Úsalo para hacer backups o compartir con el equipo

### Paso 6: Importar progreso (desde archivo o Git)

- Haz clic en **"📥 Importar"**
- Selecciona un archivo JSON exportado anteriormente
- Los datos se cargan y actualizan la herramienta
- ✅ Perfecto para sincronizar con el equipo

---

## 🔄 Sincronización con Git (Trabajo en Equipo)

### ¿Cómo trabajan 8 personas juntas?

Tenemos **2 opciones** para compartir progreso:

#### **Opción A: PC Maestro** (Más Simple) ⭐

- Usar 1 ordenador del proyecto
- En reuniones semanales, todos actualizan ahí
- Exportar JSON como backup

#### **Opción B: Git + Importar/Exportar** (Más Flexible) ⭐⭐

1. **Al empezar tu sesión:**
   ```bash
   git pull origin miguel
   ```

2. **Importar progreso del equipo:**
   - Abrir herramienta
   - Clic "📥 Importar"
   - Seleccionar `progreso.json`

3. **Trabajar en tus tareas:**
   - Marcar progreso
   - Completar tareas

4. **Compartir tu progreso:**
   - Clic "📊 Exportar"
   - Sobrescribir `progreso.json` con el archivo descargado
   - Hacer commit y push:
   ```bash
   git add EurobotPlanner/progreso.json
   git commit -m "Completadas tareas X, Y, Z"
   git push origin miguel
   ```

5. **Avisar al equipo** (WhatsApp/Discord):
   - "Acabo de actualizar el progreso ✅"

### Guía Completa

👉 **[Ver WORKFLOW_GIT.md](WORKFLOW_GIT.md)** para instrucciones detalladas, resolver conflictos y mejores prácticas.

---

## 📊 Estadísticas en Tiempo Real

En la parte superior verás:
- **Tareas Totales**: 32 tareas
- **Completadas**: Cuántas habéis terminado
- **En Progreso**: En las que estáis trabajando ahora
- **Puntos Posibles**: ~200 puntos totales en el juego

---

## 🎯 Las 6 Fases del Proyecto

### 🏗️ FASE 1: Diseño y Mecánica Base
Construcción del chasis y sistemas de movimiento (4 tareas)

### 🔧 FASE 2: Sistemas de Manipulación
Mecanismos para recoger y depositar objetos (4 tareas)

### 🧠 FASE 3: Electrónica y Sensores
Sistemas de control y detección (5 tareas)

### 💻 FASE 4: Programación y Estrategia
Software de control y lógica del robot (7 tareas)

### 🧪 FASE 5: Pruebas y Optimización
Testing y mejoras del robot (6 tareas)

### 📋 FASE 6: Homologación y Competición
Preparación final y documentación (6 tareas)

---

## 👥 Gestión del Equipo

La herramienta soporta **8 miembros** (puedes cambiar los nombres en el código si necesitas).

**Roles sugeridos:**
- 👷 Jefe de Mecánica (1-2 personas)
- ⚡ Jefe de Electrónica (1-2 personas)
- 💻 Jefe de Programación (1-2 personas)
- 🎨 Diseño CAD (1 persona)
- 🧪 Testing & Calibración (1-2 personas)
- 📋 Documentación (1 persona)

---

## 🎮 Las 5 Acciones del Robot Eurobot 2026

| Acción | Puntos Máx. | Prioridad |
|--------|-------------|-----------|
| 🎯 **Mantener bellotas calientes** (recolectar cajas) | ~150 pts | ⭐⭐⭐ CRÍTICA |
| 🐿️ **SIMA del granero** (vaciar refrigeradores) | 28 pts | ⭐⭐ Alta |
| 🌡️ **Ajustar temperatura** (mover cursor) | 10 pts | ⭐ Media |
| 🏠 **Regresar al nido** (posición final) | 10 pts | ⭐⭐ Alta |
| 🍽️ **SIMAs comer** (robots pequeños a despensas) | 55 pts | ⭐⭐ Alta |

---

## 🔧 Funcionalidades Avanzadas

### Filtros

Usa los botones en la barra de control:
- **Todas**: Muestra todas las tareas
- **Pendientes**: Solo las que faltan por empezar
- **En Progreso**: Las que estáis haciendo ahora
- **Completadas**: Las que ya habéis terminado

### Prioridades

Cada tarea tiene una prioridad visual:
- 🔴 **Alta**: Crítica para el funcionamiento básico
- 🟡 **Media**: Importante pero no crítica
- 🟢 **Baja**: Opcional o de mejora

### Puntos

Las tareas que dan puntos en la competición muestran:
- 🎯 **Badge azul** con el número de puntos

---

## 💾 Guardar y Recuperar Progreso

### Método 1: Guardar en el navegador (Recomendado para uso local)

1. Clic en **"💾 Guardar Progreso"**
2. Se guarda automáticamente en el navegador
3. La próxima vez que abras el HTML, tu progreso estará ahí

**⚠️ Limitaciones:**
- Solo funciona en el mismo ordenador
- Solo en el mismo navegador
- Si borras historial/cookies, se pierde

### Método 2: Exportar archivo JSON (Recomendado para compartir)

1. Clic en **"📊 Exportar"**
2. Se descarga: `eurobot2026_progreso_2025-XX-XX.json`
3. Guarda este archivo en la carpeta del proyecto
4. Para recuperar (próximamente): importar el JSON

**Ventajas:**
- Puedes hacer backups
- Puedes compartir con el equipo
- Puedes ver el historial de fechas

### Método 3: Reset (Empezar de cero)

1. Clic en **"🔄 Reset"**
2. Confirma que quieres borrar todo
3. Todas las tareas vuelven a "pendiente" y "sin asignar"

---

## 📅 Cronograma Sugerido

```
SEMANAS 1-4: FASE 1 y 2
- Diseño completo del robot
- Construcción del chasis
- Primeros mecanismos de recolección

SEMANAS 5-8: FASE 3 y 4
- Montaje de electrónica
- Primeros programas de prueba
- Integración mecánica-electrónica

SEMANAS 9-12: FASE 5
- Pruebas intensivas
- Optimización de rutinas
- Resolución de problemas

SEMANAS 13-14: FASE 6
- Homologación simulada
- Ajustes finales
- Preparación de competición

SEMANA 15: 🏆 COMPETICIÓN
```

---

## 🎯 Estrategia Recomendada

### Estrategia Mínima Viable (50-60 puntos)

```
✅ Recolectar 6 cajas → nido (12 pts)
✅ Llenar 3 despensas con 3 cajas c/u (27 pts)
✅ Regresar al nido (10 pts)
```

### Estrategia Completa (100+ puntos)

```
✅ Llenar 4-5 despensas (40-50 pts)
✅ Conseguir 2 primas de despensa (10 pts)
✅ Llenar nido con 6 cajas (12 pts)
✅ SIMA vaciar granero (8 pts)
✅ SIMA llenar con vacías (20 pts)
✅ Mover termómetro (5-10 pts)
✅ Regresar al nido (10 pts)
```

---

## ❓ Preguntas Frecuentes

### ¿Puedo cambiar los nombres de los miembros del equipo?

Sí, edita el archivo HTML:
1. Abre `eurobot_2026_planner.html` con un editor de texto (VS Code, Notepad++)
2. Busca la sección `teamMembers:`
3. Cambia 'Miembro 1', 'Miembro 2', etc. por los nombres reales
4. Guarda y recarga la página

### ¿Puedo añadir más tareas?

Sí, pero requiere editar el código JavaScript:
1. Busca la sección `projectData.phases`
2. Añade objetos `task` siguiendo el formato existente
3. Guarda y recarga

### ¿Puedo imprimir esto?

Sí:
1. Usa `Ctrl+P` (Windows/Linux) o `Cmd+P` (Mac)
2. La página está optimizada para impresión
3. Los controles interactivos se ocultan automáticamente

### ¿Funciona en móvil/tablet?

Sí, el diseño es **responsive** y funciona en cualquier dispositivo.

### ¿Necesito instalar algo?

No, solo necesitas un navegador web moderno.

---

## 🛠️ Solución de Problemas

### "Se borró mi progreso"

**Causa:** Borraste las cookies/caché del navegador
**Solución:**
- Usa el método de exportar JSON regularmente
- Haz backups semanales

### "No puedo asignar tareas"

**Causa:** JavaScript deshabilitado en el navegador
**Solución:**
- Habilita JavaScript en la configuración del navegador

### "La página no se ve bien"

**Causa:** Navegador muy antiguo
**Solución:**
- Actualiza tu navegador (Chrome, Firefox, Edge)

---

## 📚 Recursos Adicionales

- **Normativa oficial**: Carpeta raíz → `Eurobot2026.pdf`
- **Website oficial**: https://www.eurobot.org/
- **FAQ oficial**: https://www.eurobot.org/faq/
- **Videos de inspiración**: YouTube → "Eurobot 2025" / "Eurobot 2024"

---

## 📧 Contacto y Soporte

Para dudas sobre la herramienta o el proyecto:
- Pregunta en clase a tu profesor
- Consulta con tu equipo
- Revisa la normativa oficial de Eurobot

---

## 🎓 Consejos para el Equipo

### ✅ HACER:
- Comunicar si te atascas en una tarea
- Pedir ayuda a compañeros
- Actualizar el progreso semanalmente
- Probar e iterar (fallar está bien)
- Celebrar pequeños logros

### ❌ NO HACER:
- Dejar todo para el final
- Trabajar en silos sin comunicar
- Complicar innecesariamente (KISS: Keep It Simple)
- Rendirse si algo falla (iterar y mejorar)
- Ignorar las prioridades

---

## 📜 Licencia y Créditos

**Creado para:** Academia Cervantes Robótica - Eurobot 2026
**Versión:** 1.0
**Última actualización:** 2025-01-13

Esta herramienta es de uso libre para equipos educativos participantes en Eurobot.

---

## 🏆 ¡Mucha Suerte en Eurobot 2026!

> "La única forma de hacer un gran trabajo es amar lo que haces." - Steve Jobs

**Vamos equipo, a por el Eurobot 2026! 🤖❄️🐿️**
