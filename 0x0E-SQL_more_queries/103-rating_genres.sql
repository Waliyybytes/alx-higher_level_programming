-- script that lists all genres from hbtn_0d_tvshows_rate by their rating.
SELECT x.name, SUM(z.rate) AS rating
FROM tv_genres x
LEFT JOIN tv_show_genres y
ON x.id = y.genre_id
LEFT JOIN tv_show_ratings z
ON y.show_id = z.show_id
GROUP BY x.name
ORDER BY rating DESC;
