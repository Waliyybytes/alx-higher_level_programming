-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
WHERE month IN (7, 8)
ORDER BY avg_temp DESC
LIMIT 3;
