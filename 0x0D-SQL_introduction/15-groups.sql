-- script that lists number by score of records of the table second_table 
SELECT score, COUNT(score) AS number
FROM second_table 
ORDER BY number DESC;
