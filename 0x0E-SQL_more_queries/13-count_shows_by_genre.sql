-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.genre_id AS genre, COUNT(y.title) AS number_of_shows
FROM tv_show_genres x
INNER JOIN tv_shows y
ON x.show_id = y.id
ORDER BY number_of_shows DESC;

