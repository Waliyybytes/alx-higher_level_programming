-- script that lists all the cities of California that can be found in the database
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
