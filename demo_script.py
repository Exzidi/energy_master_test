import sqlite3
from pathlib import Path
import pandas as pd
import sys

DB_PATH = Path("energy_data.db")
INIT_SQL = Path("init_db.sql")
OUTPUT_PATH = Path("reporte_consumo_mensual.csv")

def ensure_db():
    """Crea la base de datos a partir de init_db.sql si no existe."""
    if DB_PATH.exists():
        return
    if not INIT_SQL.exists():
        raise FileNotFoundError(
            f"No existe {DB_PATH} y tampoco {INIT_SQL}. Proporcione uno de los dos."
        )
    with sqlite3.connect(DB_PATH) as conn, INIT_SQL.open(encoding="utf-8") as f:
        conn.executescript(f.read())
    print(f"[OK] Base de datos creada: {DB_PATH.resolve()}")

def simular_datos_frontend():
    """Simula la inserción de datos desde el formulario React."""
    print(">> Simulando datos del formulario React...")

    # Datos que simularían venir del frontend
    nuevo_registro = {
        'fecha': '2025-09-16 14:30:00',
        'fuente': 'solar',
        'ubicacion': 'Planta Norte',
        'consumo_kwh': 175
    }

    print(f"   Fecha: {nuevo_registro['fecha']}")
    print(f"   Fuente: {nuevo_registro['fuente']}")
    print(f"   Ubicacion: {nuevo_registro['ubicacion']}")
    print(f"   Consumo: {nuevo_registro['consumo_kwh']} kWh")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO consumos (fecha, fuente, ubicacion, consumo_kwh)
            VALUES (?, ?, ?, ?)
        """, (nuevo_registro['fecha'], nuevo_registro['fuente'],
              nuevo_registro['ubicacion'], nuevo_registro['consumo_kwh']))
        conn.commit()

    print("[OK] Nuevo registro agregado exitosamente desde el formulario")
    print()

def mostrar_datos_actuales():
    """Muestra los datos actuales en la base de datos."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM consumos")
        total = cursor.fetchone()[0]

        cursor.execute("""
            SELECT fecha, fuente, ubicacion, consumo_kwh
            FROM consumos
            ORDER BY fecha DESC
            LIMIT 3
        """)
        ultimos = cursor.fetchall()

    print(f">> Total de registros en la base de datos: {total}")
    print(">> Ultimos 3 registros:")
    for i, (fecha, fuente, ubicacion, consumo) in enumerate(ultimos, 1):
        print(f"   {i}. {fecha} | {fuente} | {ubicacion} | {consumo} kWh")
    print()

def generar_reporte():
    """Extrae, procesa y exporta el reporte mensual."""
    print(">> Procesando datos y generando reporte mensual...")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM consumos;", conn)

    if df.empty:
        raise RuntimeError("La tabla 'consumos' esta vacia.")

    # Asegurar tipo datetime y crear columna de mes YYYY-MM
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)

    # Agrupar por mes, fuente y ubicación, sumando consumo
    reporte = (
        df.groupby(["mes", "fuente", "ubicacion"], as_index=False)["consumo_kwh"]
          .sum()
          .rename(columns={"consumo_kwh": "consumo_total_kwh"})
    )

    # Exportar el reporte final a CSV
    reporte.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"[OK] Reporte generado: {OUTPUT_PATH.resolve()}")
    print(f">> El reporte contiene {len(reporte)} filas de datos agregados")

if __name__ == "__main__":
    try:
        print("=== DEMO: Energy Master - Flujo Completo ===")
        print("=" * 50)

        # Paso 1: Asegurar que existe la base de datos
        ensure_db()

        # Paso 2: Mostrar estado actual
        print("ANTES DE AGREGAR NUEVO REGISTRO:")
        mostrar_datos_actuales()

        # Paso 3: Simular inserción desde frontend
        simular_datos_frontend()

        # Paso 4: Mostrar datos después de la inserción
        print("DESPUES DE AGREGAR NUEVO REGISTRO:")
        mostrar_datos_actuales()

        # Paso 5: Generar reporte actualizado
        generar_reporte()

        print("[OK] DEMO COMPLETADA: El flujo frontend -> backend -> reporte funciona correctamente")

    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)