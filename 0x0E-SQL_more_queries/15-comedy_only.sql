-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.title
FROM tv_shows x
INNER JOIN tv_show_genres y
ON x.id = y.show_id
INNER JOIN tv_genres z
ON y.genre_id = z.id
WHERE z.name = 'Comedy'
ORDER BY x.title;

