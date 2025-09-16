-- Crea tabla 'consumos'
CREATE TABLE consumos (id INTEGER PRIMARY KEY AUTOINCREMENT,
 fecha TEXT, fuente TEXT, ubicacion TEXT, consumo_kwh INTEGER);
-- Inserta datos de ejemplo
INSERT INTO consumos (fecha, fuente, ubicacion, consumo_kwh) VALUES
('2025-08-10 10:00:00', 'electricidad', 'Planta Norte', 150),
('2025-08-11 11:30:00', 'gas', 'Planta Sur', 75),
('2025-08-12 12:45:00', 'electricidad', 'Planta Sur', 200),
('2025-08-13 09:15:00', 'electricidad', 'Planta Norte', 180),
('2025-08-14 14:00:00', 'solar', 'Planta Oeste', 50),
('2025-09-01 08:00:00', 'electricidad', 'Planta Norte', 120),
('2025-09-02 16:30:00', 'gas', 'Planta Sur', 90),
('2025-09-03 13:20:00', 'electricidad', 'Planta Sur', 210),
('2025-09-04 10:40:00', 'electricidad', 'Planta Norte', 190),
('2025-09-05 15:50:00', 'solar', 'Planta Oeste', 60);