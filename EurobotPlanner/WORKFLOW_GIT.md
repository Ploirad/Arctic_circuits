# 🔄 Workflow con Git - Sincronizar Progreso del Equipo

Esta guía explica cómo usar Git para que los 8 miembros del equipo puedan compartir y sincronizar el progreso del proyecto Eurobot 2026.

---

## 🎯 Objetivo

Que todos los miembros del equipo puedan:
- ✅ Ver el progreso actualizado del proyecto
- ✅ Actualizar tareas desde cualquier ordenador
- ✅ Mantener un historial de cambios
- ✅ Evitar conflictos y pérdida de datos

---

## 📋 Flujo de Trabajo Recomendado

### **Método 1: PC Maestro + Git Backup** ⭐ (Más Sencillo)

```
1. Reunión semanal presencial
2. Todos actualizan tareas en el PC maestro
3. Exportan progreso.json
4. Una persona hace commit y push a Git
5. Todos pueden descargar para ver en casa
```

### **Método 2: Colaboración Total con Git** ⭐⭐ (Más Flexible)

```
1. Cada persona trabaja en su PC
2. Exporta su progreso cuando completa tareas
3. Hace commit y push a Git
4. Los demás hacen pull e importan
```

---

## 🚀 Guía Paso a Paso

### **PASO 1: Configuración Inicial** (Solo una vez)

#### 1.1. Clonar el repositorio (si no lo tienes)

```bash
cd ~/githubs
git clone [URL_DEL_REPO]
cd Artic_circuits/EurobotPlanner
```

#### 1.2. Verificar que tienes los archivos

```bash
ls -la
# Deberías ver:
# - eurobot_2026_planner.html
# - progreso.json
# - README.md
# - WORKFLOW_GIT.md
```

---

### **PASO 2: Empezar a Trabajar** (Cada sesión)

#### 2.1. Sincronizar con el equipo (descargar cambios)

```bash
cd ~/githubs/Artic_circuits
git pull origin miguel
```

> ⚠️ **Importante:** Si hay conflictos, ver sección "Resolver Conflictos" abajo.

#### 2.2. Abrir la herramienta

```bash
# Opción A: Abrir desde navegador
open EurobotPlanner/eurobot_2026_planner.html

# Opción B: Doble clic en el archivo
```

#### 2.3. Importar el progreso actual del equipo

1. Clic en botón **"📥 Importar"**
2. Seleccionar archivo **`progreso.json`**
3. Verás el progreso actualizado del equipo

---

### **PASO 3: Trabajar en Tareas**

1. Marca tus tareas como **"▶️ En progreso"**
2. Cuando termines, marca el **checkbox ✅**
3. Actualiza asignaciones si es necesario
4. Clic en **"💾 Guardar Progreso"** (guarda en navegador)

---

### **PASO 4: Compartir tu Progreso** (Cuando termines)

#### 4.1. Exportar desde la herramienta

1. Clic en **"📊 Exportar"**
2. Se descarga: `eurobot2026_progreso_2025-XX-XX.json`
3. **IMPORTANTE:** Copia/mueve este archivo como `progreso.json` en la carpeta EurobotPlanner

```bash
# Desde la carpeta de Descargas (ajusta la ruta)
cp ~/Descargas/eurobot2026_progreso_2025-XX-XX.json ~/githubs/Artic_circuits/EurobotPlanner/progreso.json
```

#### 4.2. Verificar cambios con Git

```bash
cd ~/githubs/Artic_circuits
git status

# Deberías ver:
# modified:   EurobotPlanner/progreso.json
```

#### 4.3. Hacer commit

```bash
git add EurobotPlanner/progreso.json

git commit -m "Actualizar progreso: completadas tareas X, Y y Z

- Completada tarea: Diseñar chasis
- En progreso: Sistema de tracción
- Asignadas nuevas tareas a [Nombre]

🤖 Eurobot 2026"
```

> 💡 **Consejo:** Describe qué tareas completaste en el mensaje de commit.

#### 4.4. Subir a GitHub

```bash
git push origin miguel
```

---

### **PASO 5: Otros Miembros Sincronizan**

Cuando otro miembro quiere ver tu progreso:

```bash
cd ~/githubs/Artic_circuits
git pull origin miguel
```

Luego:
1. Abre `eurobot_2026_planner.html`
2. Clic en **"📥 Importar"**
3. Selecciona `progreso.json`
4. ¡Listo! Ve tu progreso actualizado

---

## 🔧 Resolver Conflictos

### ¿Qué es un conflicto?

Ocurre cuando 2 personas modifican `progreso.json` al mismo tiempo y intentan hacer push.

### Solución Simple (Recomendada)

**Persona A** (hizo push primero): ✅ Todo bien

**Persona B** (intenta hacer push después):

```bash
git pull origin miguel
# ⚠️ CONFLICT en progreso.json

# OPCIÓN 1: Aceptar cambios del equipo (perder los tuyos)
git checkout --theirs EurobotPlanner/progreso.json
git add EurobotPlanner/progreso.json
git commit -m "Resolver conflicto: aceptar progreso del equipo"
git push origin miguel

# Luego importas el progreso.json en la herramienta
# Y vuelves a exportar tus cambios
```

**OPCIÓN 2: Mantener tus cambios (sobrescribir los del equipo)**

```bash
git checkout --ours EurobotPlanner/progreso.json
git add EurobotPlanner/progreso.json
git commit -m "Resolver conflicto: mantener mi progreso"
git push origin miguel
```

**OPCIÓN 3: Combinar manualmente (Avanzado)**

```bash
# Ver las diferencias
git diff EurobotPlanner/progreso.json

# Editar el archivo manualmente combinando ambos cambios
code EurobotPlanner/progreso.json

# Luego commit y push
git add EurobotPlanner/progreso.json
git commit -m "Resolver conflicto: combinado ambos progresos"
git push origin miguel
```

---

## 📅 Rutina Recomendada

### **Reunión Semanal (Presencial)**

```
1. Todos traen sus PCs (o usan PC maestro)
2. Alguien hace git pull
3. Importan progreso.json en la herramienta
4. Cada uno reporta sus tareas
5. Actualizan tareas en vivo
6. Exportan progreso.json
7. Una persona hace commit + push
8. Todos hacen git pull antes de irse
```

### **Durante la Semana (Individual)**

```
1. Antes de empezar: git pull
2. Importar progreso.json
3. Trabajar en tus tareas
4. Guardar progreso (localStorage)
5. Cuando completes algo importante:
   - Exportar
   - Commit + Push
6. Avisar en el grupo de WhatsApp/Discord
```

---

## 🎯 Mejores Prácticas

### ✅ HACER:

1. **Hacer `git pull` SIEMPRE antes de empezar**
   - Evita conflictos
   - Ves el progreso más reciente

2. **Commits descriptivos**
   ```bash
   git commit -m "Completada FASE 1: diseño del chasis"
   # ✅ BUENO

   git commit -m "update"
   # ❌ MALO
   ```

3. **Comunicar cuando hagas push**
   - Avisar en el grupo: "Acabo de actualizar progreso con la tarea X"
   - Otros saben que deben hacer pull

4. **Hacer commit cuando completes tareas importantes**
   - No necesitas commit por cada checkbox
   - Sí cuando completes una tarea entera o sesión de trabajo

5. **Usar la rama correcta**
   ```bash
   git branch
   # Verifica que estás en 'miguel'
   ```

### ❌ NO HACER:

1. **No hacer push sin pull antes**
   - Causa conflictos innecesarios

2. **No modificar progreso.json manualmente**
   - Siempre usar la herramienta HTML
   - Solo exportar/importar

3. **No hacer commit si no has cambiado nada**
   ```bash
   git status
   # Si no hay cambios, no hace falta commit
   ```

4. **No usar force push**
   ```bash
   git push -f origin miguel  # ❌ NUNCA HAGAS ESTO
   ```

5. **No borrar progreso.json del repositorio**
   - Es el archivo principal de sincronización

---

## 🆘 Comandos de Emergencia

### "Metí la pata, quiero volver atrás"

```bash
# Ver commits recientes
git log --oneline -5

# Volver al commit anterior (perder tus cambios)
git reset --hard HEAD~1

# O volver a un commit específico
git reset --hard [COMMIT_HASH]
```

### "Quiero descartar todos mis cambios locales"

```bash
git checkout EurobotPlanner/progreso.json
```

### "Quiero ver qué cambió en el último commit"

```bash
git show HEAD
```

### "Quiero ver quién hizo qué cambios"

```bash
git log --oneline --all --graph
git blame EurobotPlanner/progreso.json
```

---

## 📊 Historial del Proyecto

Git guarda TODO el historial. Puedes ver:

```bash
# Ver todos los commits
git log --oneline --graph --all

# Ver cambios de un archivo específico
git log -p EurobotPlanner/progreso.json

# Ver quién trabajó más
git shortlog -sn
```

---

## 🎓 Recursos Adicionales

### Aprender Git Básico

- **Tutorial interactivo:** https://learngitbranching.js.org/
- **Cheatsheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Git en español:** https://git-scm.com/book/es/v2

### Ayuda

Si tienes problemas:
1. Pregunta en el grupo del equipo
2. Consulta este documento
3. Busca el error en Google: "git error [mensaje]"
4. Pide ayuda al profesor

---

## 📝 Resumen Rápido

```bash
# Al empezar tu sesión
git pull origin miguel

# Abrir herramienta
open eurobot_2026_planner.html

# Importar progreso
[Clic 📥 Importar] → Selecciona progreso.json

# Trabajar...

# Al terminar
[Clic 📊 Exportar] → Guarda como progreso.json

# Subir cambios
git add EurobotPlanner/progreso.json
git commit -m "Descripción de cambios"
git push origin miguel

# Avisar al equipo en WhatsApp/Discord
```

---

## ✅ Checklist de Sesión de Trabajo

Antes de empezar:
- [ ] `git pull origin miguel`
- [ ] Abrir herramienta HTML
- [ ] Importar `progreso.json`

Durante el trabajo:
- [ ] Marcar tareas como "en progreso"
- [ ] Completar tareas
- [ ] Guardar progreso regularmente

Al terminar:
- [ ] Exportar progreso
- [ ] Sobrescribir `progreso.json`
- [ ] `git add` + `git commit` + `git push`
- [ ] Avisar al equipo

---

**¡Listo! Ahora todo el equipo puede colaborar sin perder progreso! 🚀🤖**
