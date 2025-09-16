# Energy Master – Prueba Técnica

Este repositorio contiene la solución a la **Prueba Técnica Integral: Desarrollo y Análisis de Datos Energéticos**.  
Incluye:

* Respuestas del **Módulo 1** (consultas SQL y ejercicios de lógica).
* Script en **Python (Módulo 2)** para crear la base de datos, procesar los datos y generar un reporte.
* Carpeta para el **dashboard de Power BI (Módulo 3)**.
* Carpeta para el **formulario React y video demostrativo (Módulos 4 y 5)**.

---

## 📂 Estructura del proyecto
```
.
├─ init_db.sql                 # Script para crear y poblar la base de datos
├─ module1_answers.sql         # Respuestas del Módulo 1 (consultas SQL)
├─ procesar_consumo.py         # Script de Python para generar el reporte CSV
├─ reporte_consumo_mensual.csv # (Generado automáticamente por el script)
├─ powerbi/
│   └─ modulo3_powerbi.pbix    # Dashboard de Power BI (añádelo aquí)
├─ frontend/                   # Código React del formulario (opcional)
│   └─ ...
└─ video/
    └─ demo_video_link.txt     # Enlace al video demostrativo (opcional)
```

---

## 🛠️ Requisitos

- **Python 3.8 o superior**  
- **pip** (gestor de paquetes de Python)  
- **Power BI Desktop** (solo si deseas abrir el dashboard `.pbix`)

---

## 🚀 Ejecución paso a paso

### 1️⃣ Clonar el repositorio
```bash
git clone <URL-de-tu-repositorio>
cd energy-master-test
```

### 2️⃣ Instalar la única dependencia
El proyecto solo usa la librería **pandas** además de `sqlite3` (que ya viene con Python).  
Instálala con:

```bash
pip install pandas
```

No se necesita `requirements.txt` porque la única dependencia externa es `pandas`.

### 3️⃣ Crear la base de datos y generar el reporte
El script se encarga de todo:

```bash
python procesar_consumo.py
```

El proceso:
1. Si no existe `energy_data.db`, el script usa `init_db.sql` para crear la tabla `consumos` e insertar los datos de ejemplo.  
2. Calcula el consumo total mensual, agrupado por fuente energética y ubicación.  
3. Genera el archivo `reporte_consumo_mensual.csv` en la carpeta raíz.

### 4️⃣ Visualizar en Power BI (Módulo 3)
1. Abre **Power BI Desktop**.  
2. Carga el archivo `reporte_consumo_mensual.csv` como fuente de datos.  
3. Crea las visualizaciones solicitadas (gráfico de barras por fuente, filtro por ubicación, tarjeta KPI).

---

## 🧩 Módulo 1 – Consultas SQL
El archivo `module1_answers.sql` incluye:

**Consumo total de electricidad en Planta Norte**
```sql
SELECT SUM(consumo_kwh) AS total_electricidad_norte
FROM consumos
WHERE fuente = 'electricidad'
  AND ubicacion = 'Planta Norte';
```

**Consumo promedio por fuente energética, ordenado de mayor a menor**
```sql
SELECT
    fuente,
    AVG(consumo_kwh) AS consumo_promedio
FROM consumos
GROUP BY fuente
ORDER BY consumo_promedio DESC;
```

**Consumos registrados en el último mes**
```sql
SELECT *
FROM consumos
WHERE date(fecha) >= date('now','-1 month');
```

**Ejercicio de lógica – Ahorro de Consumo**  
Consumo diario: 120 kWh  
Reducción en fines de semana: 15 %  
Mes de 30 días con 8 días de fin de semana  
Ahorro total = 120 × 0.15 × 8 = **144 kWh**

---

## 🔵 Módulo 4 y 5 (Opcionales)

* **Frontend React**: si se desarrolla el formulario, el código debe ir en la carpeta `frontend/`.
* **Dashboard avanzado**: coloca el archivo `.pbix` del Módulo 5 en `powerbi/`.
* **Video demostrativo**: guarda el enlace (YouTube o similar) en `video/demo_video_link.txt`.

---

## 💡 Notas finales
- Al ejecutarlo por primera vez se creará el archivo `energy_data.db` en la carpeta raíz.
- No depende de ninguna ruta específica ni de configuraciones en DataGrip.
- Para limpiar los archivos generados, elimina:
  ```
  energy_data.db
  reporte_consumo_mensual.csv
  ```
  y vuelve a ejecutar el script.

---

**Autor:** [Tu nombre]  
**Contacto:** [Tu correo]
