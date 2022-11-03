-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.title, y.genre_id
FROM tv_shows x
LEFT JOIN tv_show_genres y
ON x.id = y.show_id
WHERE y.genre_id IS NULL
ORDER BY x.title ASC, y.genre_id ASC;

