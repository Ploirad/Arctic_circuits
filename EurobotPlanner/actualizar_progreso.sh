#!/bin/bash

# Script de ayuda para actualizar progreso.json con Git
# Eurobot 2026 - Academia Cervantes

echo "🤖 Eurobot 2026 - Actualizador de Progreso"
echo "=========================================="
echo ""

# Verificar que estamos en la carpeta correcta
if [ ! -f "progreso.json" ]; then
    echo "❌ Error: No se encuentra progreso.json"
    echo "   Ejecuta este script desde la carpeta EurobotPlanner"
    exit 1
fi

# Mostrar estado actual
echo "📊 Estado actual de Git:"
git status --short

echo ""
echo "📝 Pasos para actualizar el progreso:"
echo ""
echo "1. Abre eurobot_2026_planner.html en tu navegador"
echo "2. Trabaja en tus tareas"
echo "3. Haz clic en '📊 Exportar'"
echo "4. Se descargará: eurobot2026_progreso_[FECHA].json"
echo ""
echo "5. Copia el archivo descargado aquí:"
echo "   cp ~/Descargas/eurobot2026_progreso_*.json ./progreso.json"
echo ""
echo "¿Ya hiciste esto? (s/n)"
read -r respuesta

if [ "$respuesta" != "s" ] && [ "$respuesta" != "S" ]; then
    echo "❌ Cancelado. Completa los pasos anteriores primero."
    exit 0
fi

echo ""
echo "✅ Perfecto! Continuando..."
echo ""

# Verificar que progreso.json cambió
if ! git diff --quiet progreso.json; then
    echo "✅ Detectados cambios en progreso.json"
    echo ""

    # Mostrar estadísticas del archivo
    echo "📊 Estadísticas del archivo:"
    if command -v jq &> /dev/null; then
        echo "   Fecha: $(jq -r '.fecha' progreso.json)"
        echo "   Completadas: $(jq -r '.estadisticas.completadas' progreso.json)"
        echo "   En Progreso: $(jq -r '.estadisticas.enProgreso' progreso.json)"
    else
        echo "   (Instala 'jq' para ver estadísticas: sudo apt install jq)"
    fi
    echo ""

    # Pedir mensaje de commit
    echo "📝 Describe qué tareas completaste:"
    echo "   Ejemplo: Completadas tareas diseño chasis y sistema tracción"
    read -r mensaje

    if [ -z "$mensaje" ]; then
        mensaje="Actualizar progreso del proyecto"
    fi

    # Hacer commit
    echo ""
    echo "🔄 Haciendo commit..."
    git add progreso.json
    git commit -m "Actualizar progreso: $mensaje

🤖 Eurobot 2026 - Academia Cervantes"

    if [ $? -eq 0 ]; then
        echo "✅ Commit realizado correctamente"
        echo ""

        # Preguntar si hacer push
        echo "¿Quieres hacer push ahora? (s/n)"
        read -r push_respuesta

        if [ "$push_respuesta" = "s" ] || [ "$push_respuesta" = "S" ]; then
            echo ""
            echo "🚀 Haciendo push a GitHub..."
            git push origin miguel

            if [ $? -eq 0 ]; then
                echo ""
                echo "✅ ¡Push completado!"
                echo ""
                echo "📱 Recuerda avisar al equipo en el grupo:"
                echo "   'Acabo de actualizar el progreso: $mensaje ✅'"
            else
                echo ""
                echo "❌ Error al hacer push. Verifica tu conexión o permisos."
                echo "   Puedes intentar manualmente: git push origin miguel"
            fi
        else
            echo ""
            echo "⏸️  Push pospuesto. Puedes hacerlo luego con:"
            echo "   git push origin miguel"
        fi
    else
        echo "❌ Error al hacer commit"
    fi
else
    echo "ℹ️  No hay cambios en progreso.json"
    echo "   Asegúrate de:"
    echo "   1. Exportar desde la herramienta HTML"
    echo "   2. Copiar el archivo a esta carpeta como progreso.json"
fi

echo ""
echo "✅ Script completado"
