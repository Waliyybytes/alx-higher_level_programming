-- script that lists all shows contained in hbtn_0d_tvshows
SELECT x.name
FROM tv_genres x
LEFT JOIN 
	(SELECT DISTINCT(x.name), x.id, z.title
	FROM tv_genres x
	INNER JOIN tv_show_genres y
	ON x.id = y.genre_id
	INNER JOIN tv_shows z
	ON y.show_id = z.id
	WHERE z.title = 'Dexter') AS i
ON x.id = i.id
WHERE i.title IS NULL
ORDER BY x.name;
