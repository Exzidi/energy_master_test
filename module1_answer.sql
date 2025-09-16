-- 1. Ahorro de Consumo: Un sistema consume 120 kWh al día. Si se reduce el
-- consumo en un 15% durante los fines de semana (sábado y domingo),
-- ¿cuánto se ahorra en un mes de 30 días que tiene 8 días de fin de
-- semana?
-- R/: 
-- Consumo diario:
-- 120kWh/día
-- Reducción fines de semana:
-- 15 % de 120 kWh = 120×0.15=18kWh de ahorro por cada fin de semana (Sabado y Domingo).
-- Días de fin de semana en el mes:
-- El mes tiene 8 días de fin de semana.
-- Ahorro total:
-- Ahorro diario (18 kWh) × 8 días = 18×8=144kWh.

-- 2. Análisis de Pseudocódigo: Analice el siguiente pseudocódigo y explique qué
-- hace y cuál es el valor final de la variable x:

-- Inicio
-- x = 5
-- Mientras x < 20
-- Si x es par
-- x = x + 3
-- Sino
-- x = x + 2
-- Fin Mientras
-- Fin

-- R/: Este código es un ciclo en el cual se empieza con el numero 5 y se finaliza al llegar al numero 20, cada que es par se suman 3 al numero inicial acumulando su resultado, en caso de no ser par par (Este caso) se suman 2, acumulando también el resultado.

-- Como en este caso el numero inicial no es par se le suma un 2 dando como resultado 7, numero impar también. ya que cada numero impar suma 2 este ciclo siempre generara números impares, haciendo que el resultado final sea 21 finalizando el ciclo.

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
