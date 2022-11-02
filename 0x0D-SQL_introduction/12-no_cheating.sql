-- script that lists all records of the table second_table 
UPDATE second_table SET score = 10 WHERE name = 'BOB';
SELECT score, name 
FROM second_table
ORDER BY score DESC;
