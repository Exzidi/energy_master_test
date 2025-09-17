--Consultas sql
-- 1) Consumo total de 'electricidad' en 'Planta Norte
SELECT SUM(consumo_kwh) AS total_electricidad_norte
FROM consumos
WHERE fuente = 'electricidad'
  AND ubicacion = 'Planta Norte';
-- 2) Consumo promedio por fuente energética, ordenado de mayor a menor
SELECT
    fuente,
    AVG(consumo_kwh) AS consumo_promedio
FROM consumos
GROUP BY fuente
ORDER BY consumo_promedio DESC;
-- 3) Consumos registrados en los últimos 30 días (desde hoy)
SELECT *
FROM consumos
WHERE date(fecha) >= date('now','-30 day');
