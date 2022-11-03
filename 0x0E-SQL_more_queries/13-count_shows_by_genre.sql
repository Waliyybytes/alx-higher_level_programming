-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.name AS genre, COUNT(y.genre_id) AS number_of_shows
FROM tv_genres x
INNER JOIN tv_show_genres y
ON x.id = y.genre_id
GROUP BY x.genre_id
ORDER BY number_of_shows DESC;

