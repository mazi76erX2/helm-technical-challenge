SELECT userId, AVG(duration) AS average_duration
FROM sessions
GROUP BY userId
HAVING COUNT(*) > 1;
