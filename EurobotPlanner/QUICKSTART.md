# ⚡ Guía Rápida - Eurobot 2026 Planner

**Para impacientes que quieren empezar YA** 🚀

---

## 🎯 En 5 Minutos

### 1️⃣ Abrir la Herramienta

```bash
cd ~/githubs/Artic_circuits/EurobotPlanner
open eurobot_2026_planner.html
# O doble clic en el archivo
```

### 2️⃣ Cargar Progreso del Equipo

1. Clic botón **"📥 Importar"**
2. Seleccionar **`progreso.json`**
3. ¡Listo! Ves el progreso actual

### 3️⃣ Trabajar

- ▶️ **Iniciar tarea**: Botón "▶️ Iniciar"
- ✅ **Completar**: Checkbox ✅
- 👤 **Asignar**: Desplegable con tu nombre

### 4️⃣ Guardar

- Clic **"💾 Guardar Progreso"** → Guarda en navegador

### 5️⃣ Compartir con el Equipo

```bash
# 1. Exportar desde la herramienta
#    Clic "📊 Exportar" → Descarga JSON

# 2. Copiar el archivo exportado
cp ~/Descargas/eurobot2026_progreso_*.json ./progreso.json

# 3. Subir a Git
git add progreso.json
git commit -m "Completadas tareas X, Y, Z"
git push origin miguel

# 4. Avisar al equipo
# "Actualizado progreso ✅"
```

---

## 🔄 Workflow Diario

```bash
# AL EMPEZAR
git pull origin miguel          # Descargar cambios del equipo
open eurobot_2026_planner.html  # Abrir herramienta
# [Importar progreso.json]

# TRABAJAR
# - Marcar tareas
# - Guardar regularmente

# AL TERMINAR
# [Exportar desde herramienta]
cp ~/Descargas/eurobot2026_progreso_*.json ./progreso.json
git add progreso.json
git commit -m "Descripción"
git push origin miguel
# Avisar al equipo
```

---

## 📚 Más Información

- **Manual completo**: [README.md](README.md)
- **Workflow Git detallado**: [WORKFLOW_GIT.md](WORKFLOW_GIT.md)
- **Plan de clase**: [PLAN_CLASE.md](PLAN_CLASE.md)

---

## 🆘 Problemas Comunes

### "No veo el botón importar"

- Refresca la página (Ctrl+R o Cmd+R)
- Usa un navegador moderno (Chrome, Firefox)

### "Git push falla"

```bash
git pull origin miguel  # Sincronizar primero
# Si hay conflictos, acepta los del equipo:
git checkout --theirs progreso.json
git add progreso.json
git commit -m "Resolver conflicto"
git push origin miguel
```

### "Perdí mi progreso"

- Si guardaste: está en localStorage (mismo PC + navegador)
- Si exportaste: busca en `~/Descargas`
- Si hiciste commit: está en Git (`git log`)

---

## 🎯 Comandos Esenciales

```bash
# Ver estado
git status

# Descargar cambios
git pull origin miguel

# Subir cambios
git add progreso.json
git commit -m "Mensaje"
git push origin miguel

# Ver historial
git log --oneline

# Deshacer cambios locales
git checkout progreso.json
```

---

## 💡 Tips

✅ **Siempre hacer `git pull` antes de empezar**
✅ **Guardar progreso cada 15-30 min**
✅ **Exportar cuando completes tareas importantes**
✅ **Avisar al equipo cuando hagas push**
✅ **Usar mensajes de commit descriptivos**

---

**¡Listo! Ya puedes empezar a trabajar 🚀**
