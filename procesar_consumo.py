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
    print(f"✅ Base de datos creada: {DB_PATH.resolve()}")

def generar_reporte():
    """Extrae, procesa y exporta el reporte mensual."""
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM consumos;", conn)

    if df.empty:
        raise RuntimeError("La tabla 'consumos' está vacía.")

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
    print(f"📄 Reporte generado: {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    try:
        ensure_db()
        generar_reporte()
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
