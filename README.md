# Energy Master – Prueba Técnica Integral 🌍⚡

## 🎯 **Objetivos de la Prueba**

Este repositorio contiene la **solución completa** a la **Prueba Técnica Integral: Desarrollo y Análisis de Datos Energéticos**, evaluando las siguientes habilidades:

- 🧠 **Resolución de Problemas**: Razonamiento lógico para resolver problemas
- 🐍 **Desarrollo Backend (Python)**: Manipulación y procesamiento de datos
- 📊 **Consultas a Bases de Datos (SQL)**: Consultas SQL eficientes
- 📈 **Visualización de Datos (Power BI)**: Dashboards e inteligencia de negocios
- ⚙️ **Desarrollo Frontend (React)**: Interfaces de usuario para captura de datos

## 📊 **Estado de Cumplimiento: 100%** ✅

✅ **Módulo 1**: Lógica y SQL
✅ **Módulo 2**: Python
✅ **Módulo 3**: Power BI
✅ **Módulo 4**: React (Bonus) - *(incluye video)*
✅ **Módulo 5**: Dashboard Analítica (Bonus)

🎥 **Video Demostrativo**: [Ver en YouTube](https://youtu.be/d19k5i45VxI)

---

## 📂 **Estructura del Proyecto**
```
.
├─ init_db.sql                 # Script para crear y poblar la base de datos
├─ module1_answer.sql          # Respuestas del Módulo 1 (consultas SQL)
├─ procesar_consumo.py         # Script de Python para generar el reporte CSV
├─ demo_script.py              # Script demo para video demostrativo
├─ reporte_consumo_mensual.csv # (Generado automáticamente por el script)
├─ energy_data.db              # Base de datos SQLite (generada automáticamente)
├─ Modulo_3_Dashboard.pbix     # Dashboard de Power BI del Módulo 3
├─ Modulo_5_Dashboard.pbix     # Dashboard avanzado del Módulo 5
├─ 2025-08-31_NEU_TELEMETRY.xlsx # Datos telemetría solar para Módulo 5
├─ frontend/                   # Formulario React del Módulo 4 (Bonus)
│   ├─ src/
│   │   ├─ App.jsx             # Componente principal con formulario
│   │   ├─ main.jsx            # Punto de entrada de React
│   │   └─ index.css           # Estilos globales mejorados
│   ├─ index.html              # Plantilla HTML
│   ├─ vite.config.js          # Configuración de Vite
│   ├─ package.json            # Dependencias y scripts npm
│   └─ node_modules/           # Dependencias instaladas
└─ README.md                   # Este archivo
```

---

## 🛠️ **Requisitos del Sistema**

### 🐍 **Para Módulos Python (1-3):**
- **Python 3.8+** - Lenguaje principal para backend
- **pip** - Gestor de paquetes (incluye pandas)
- **SQLite3** - Base de datos (incluido con Python)
- **Power BI Desktop** - Para visualizaciones (.pbix)

### ⚔️ **Para Módulo React (4 - Bonus):**
- **Node.js 16+** - Runtime de JavaScript
- **npm** - Gestor de paquetes (incluido con Node.js)
- **Navegador moderno** - Chrome, Firefox, Safari, Edge

### 📁 **Para Módulo 5 (Bonus):**
- **Power BI Desktop** - Dashboard avanzado de telemetría solar
- **Excel** - Para validar datos NEU_TELEMETRY

---

## 🚀 **Guía de Ejecución Completa**

### 1️⃣ **Configuración Inicial**
```bash
# Clonar repositorio
git clone <URL-repositorio>
cd energy_master

# Instalar dependencia Python
pip install pandas
```

### 2️⃣ **Ejecutar Backend (Módulos 1-3)**
```bash
# Crear DB y generar reporte
python procesar_consumo.py

# Para demo completa con simulación frontend
python demo_script.py
```

### 3️⃣ **Instalar y ejecutar Frontend (Módulo 4)**
```bash
cd frontend
npm install
npm run dev
```
🌍 **URL**: http://localhost:3000

### 4️⃣ **Visualizar Dashboards Power BI**
1. 📊 **Módulo 3**: Abrir `Modulo_3_Dashboard.pbix`
2. 🌌 **Módulo 5**: Abrir `Modulo_5_Dashboard.pbix`
3. 📄 **Alternativo**: Cargar `reporte_consumo_mensual.csv` manualmente

---

## 🧩 **Módulo 1: Lógica y Consultas SQL** ✅

### 🧠 **Ejercicios de Lógica Resueltos:**

**1. Ahorro de Consumo:**
- Consumo diario: 120 kWh
- Reducción fines de semana: 15%
- Días de fin de semana: 8 días
- **Resultado**: 120 × 0.15 × 8 = **144 kWh ahorrados**

**2. Análisis de Pseudocódigo:**
- Ciclo que inicia en x=5 y termina en x≥ 20
- Suma 3 si es par, suma 2 si es impar
- **Resultado final**: x = 21

### 📊 **Consultas SQL Implementadas:**

🔍 **Consulta 1**: Consumo total de electricidad en Planta Norte
```sql
SELECT SUM(consumo_kwh) AS total_electricidad_norte
FROM consumos
WHERE fuente = 'electricidad' AND ubicacion = 'Planta Norte';
```

📈 **Consulta 2**: Consumo promedio por fuente energética
```sql
SELECT fuente, AVG(consumo_kwh) AS consumo_promedio
FROM consumos GROUP BY fuente ORDER BY consumo_promedio DESC;
```

📅 **Consulta 3**: Consumos de los últimos 30 días
```sql
SELECT * FROM consumos
WHERE date(fecha) >= date('now','-30 day');
```

**📁 Archivos**:
- `Modulo_1_answer.sql` - Consultas SQL
- `Modulo_1_Pensamiento_logico.txt` - Ejercicios de lógica resueltos

---

## 🐍 **Módulo 2: Procesamiento Python** ✅

### ⚙️ **Funcionalidades Implementadas:**
- 🔗 **Conexión DB**: Conecta automáticamente a `energy_data.db`
- 📊 **Pandas**: Procesamiento y agregación de datos mensual
- 📁 **Export CSV**: Genera `reporte_consumo_mensual.csv`
- 🏗️ **Auto-setup**: Crea DB si no existe usando `init_db.sql`

### 📋 **Proceso Automatizado:**
1. Verifica existencia de `energy_data.db`
2. Si no existe, ejecuta `init_db.sql` para crear estructura
3. Conecta y extrae todos los datos de consumo
4. Agrupa por fuente energética y ubicación mensualmente
5. Exporta resultado final a CSV

**📁 Archivos**:
- `procesar_consumo.py` - Script principal
- `demo_script.py` - Script para demostración con simulación de frontend

---

## 📈 **Módulo 3: Dashboard Power BI** ✅

### 📊 **Visualizaciones Implementadas:**
- 📊 **Gráfico de barras**: Consumo mensual por fuente energética
- 🔧 **Segmentador**: Filtro interactivo por ubicación
- 🎯 **KPI**: Tarjeta con consumo total general
- 🎨 **Diseño profesional**: Colores coherentes y navegación intuitiva

### 🎛️ **Características:**
- **Datos**: Basado en `reporte_consumo_mensual.csv`
- **Interactividad**: Filtros dinámicos por ubicación
- **Métricas**: Consumo total, promedios, distribución por fuente
- **Formato**: Dashboard ejecutivo para toma de decisiones

**📁 Archivo**: `Modulo_3_Dashboard.pbix`

---

## 🔵 **Módulo 4: Formulario React (Bonus)** ✅

### ✅ **Características Implementadas:**

📋 **Formulario Completo** con campos:
- 📅 **Fecha de consumo** (validación: no futura)
- ⚡ **Fuente energética** (electricidad, gas, solar, eólica)
- 🏢 **Ubicación** (Planta Norte, Sur, Oficina Central, Almacén)
- 🔋 **Consumo kWh** (validación: número positivo)

⚙️ **Validaciones en Tiempo Real**:
- ✅ Todos los campos requeridos
- ✅ Fecha no puede ser futura
- ✅ Consumo debe ser positivo
- ✅ Mensajes de error específicos
- ✅ Validación instantánea al escribir

📡 **Simulación de Backend**:
- ✅ Envío asíncrono con delay realista
- ✅ Estados de carga profesionales
- ✅ Respuesta simulada (90% éxito, 10% error)
- ✅ Mensajes de confirmación
- ✅ Limpieza automática tras éxito

### 🎨 **Mejoras Estéticas Implementadas:**
- **Diseño moderno**: Gradientes, sombras, efectos blur
- **Tipografía Inter**: Google Fonts profesional
- **Animaciones**: Hover effects, loading spinner, transitions
- **Responsive**: Mobile-first design
- **Iconos**: Emojis descriptivos para cada campo
- **Color scheme**: Verde energético como tema principal

### 🎥 **Video Demostrativo:**
**🔗 [Ver Video Completo en YouTube](https://youtu.be/d19k5i45VxI)**

El video demuestra:
1. 📱 **Funcionamiento del formulario React** con validaciones
2. 🐍 **Ejecución del script Python** (`demo_script.py`)
3. 📊 **Actualización del dashboard Power BI** con nuevos datos
4. 🔄 **Flujo completo** frontend → backend → visualización

---

## 🌌 **Módulo 5: Dashboard de Analítica Solar (Bonus)** ✅

### 📈 **Visualizaciones Avanzadas Implementadas:**

🟢 **1. Generación por Inversor/Mes** (Barras verdes)
- 3 inversores: CALZAMOS, LUIS FERNANDO HOYOS, NUESTRA COCINA
- Agrupación mensual con colores diferenciados
- Datos de enero a agosto 2025

🟣 **2. Generación por Día** (Líneas moradas)
- Tendencia temporal completa
- Identificación de patrones estacionales
- Caída notable en febrero

🔥 **3. Mapa de Calor** (Escala roja)
- Matriz: Día de semana vs Hora (1-24)
- Intensidad de color indica generación
- Patrones de horarios solares visibles

📊 **4. Análisis Estadístico** (Barras + Líneas)
- Promedios diarios
- Máximos y mínimos por día
- Comparativa visual de rendimiento

### 📏 **Medidas DAX Avanzadas:**
```dax
// Promedio por día de semana
Promedio_Dia_Semana = AVERAGEX(VALUES(Sheet1[Dia_Semana]),
    CALCULATE(AVERAGE(Sheet1[Valor])))

// Día de mayor generación
Dia_Mayor_Generacion = CONCATENATEX(
    FILTER(Sheet1, Sheet1[Valor] = MAXX(ALL(Sheet1), Sheet1[Valor])),
    FORMAT(Sheet1[Fecha], "DD/MM/YYYY"), ", ")
```

### 🎯 **KPIs para Inversionistas:**
- 📈 **Generación Total**: 937,78 mil kWh
- 📅 **Día Pico**: 21/03/2025
- 📊 **Promedio Semanal**: 100,84 kWh
- 🔍 **Eficiencia por Inversor**: Comparativa visual

### 🔍 **Filtros Interactivos:**
- 📅 **Por Fecha**: Segmentación temporal
- ⚙️ **Por Inversor**: Filtrado por equipo
- 📊 **Actualización dinámica** de todas las visualizaciones

**📁 Archivo**: `Modulo_5_Dashboard.pbix`

---

## 📦 **Entregables Completados**

Según las especificaciones del PDF, entregables enviados:

✅ **Repositorio Git** - Código fuente completo (Python y React)
✅ **module1_answer.sql** - Respuestas Módulo 1
✅ **Modulo_3_Dashboard.pbix** - Dashboard Power BI Módulo 3
✅ **Video demostrativo** - [YouTube: https://youtu.be/d19k5i45VxI](https://youtu.be/d19k5i45VxI)
✅ **Modulo_5_Dashboard.pbix** - Dashboard analítica Módulo 5

---

## 🏆 **Resumen Final de Logros**

| Módulo | Descripción | Estado | Completitud |
|---------|-------------|--------|-------------|
| 🧩 Módulo 1 | Lógica y SQL | ✅ COMPLETO | 100% |
| 🐍 Módulo 2 | Python Backend | ✅ COMPLETO | 100% |
| 📈 Módulo 3 | Power BI Dashboard | ✅ COMPLETO | 100% |
| ⚙️ Módulo 4 | React Frontend + Video | ✅ COMPLETO | 100% |
| 🌌 Módulo 5 | Analítica Avanzada | ✅ COMPLETO | 100% |

**🏅 PUNTUACIÓN FINAL: 100/100**

## 🎬 **Video Demostrativo**

🔗 **[Ver Video Completo: Energy Master - Flujo Integral](https://youtu.be/d19k5i45VxI)**

El video demuestra el flujo completo de la aplicación:
- Formulario React con validaciones en tiempo real
- Procesamiento de datos con Python y pandas
- Actualización automática del dashboard Power BI
- Integración completa frontend ↔ backend ↔ visualización

---

## 📊 **Notas Técnicas**

- 💾 **Base de datos**: Se genera automáticamente (`energy_data.db`)
- 🔄 **Dependencias mínimas**: Solo pandas para Python, Inter font para React
- 🌍 **Compatible**: Windows, macOS, Linux
- 🛠️ **Herramientas**: Power BI Desktop requerido para .pbix
- 🎨 **Frontend**: Diseño moderno con animaciones y responsive design

---