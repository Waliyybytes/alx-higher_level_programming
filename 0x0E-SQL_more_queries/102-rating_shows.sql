-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT x.title, SUM(y.rate) AS rating
FROM tv_shows x
INNER JOIN tv_show_ratings y
ON x.id = y.show_id
GROUP BY x.title
ORDER BY rating DESC;
