-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.title
FROM tv_shows x
LEFT JOIN 
	(SELECT DISTINCT(x.title), x.id, z.name
	FROM tv_shows x
	INNER JOIN tv_show_genres y
	ON x.id = y.show_id
	INNER JOIN tv_genres z
	ON y.genre_id = z.id
	WHERE z.name = 'Comedy') AS i
ON x.id = i.id
WHERE i.name IS NULL
ORDER BY x.title;
