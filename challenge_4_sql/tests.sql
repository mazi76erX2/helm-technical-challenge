-- Test case: Verify the query that selects userId and average session duration for each user
-- who has more than one session.

-- Insert test data into the sessions table.
INSERT INTO sessions (id, userId, duration)
VALUES
    (1, 1, 30),
    (2, 1, 45),
    (3, 2, 60),
    (4, 2, 75),
    (5, 3, 90),
    (6, 3, 120),
    (7, 3, 150);

-- Execute the query to select userId and average session duration for each user who has more than one session.
SELECT userId, AVG(duration) AS average_duration
FROM sessions
GROUP BY userId
HAVING COUNT(*) > 1;
-- The expected result should include user with userId 1 and userId 3.

-- Insert a user with a single session
INSERT INTO sessions (id, userId, duration)
VALUES (8, 4, 60)
-- Execute the SQL query to select userId and average session duration for each user

-- Clean up the test data.
DELETE FROM sessions;
