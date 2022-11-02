-- script that lists all records of the table second_table 
UPDATE 
(SELECT score, name 
FROM second_table
ORDER BY score DESC)
SET score = 10
WHERE name = 'Bob';
