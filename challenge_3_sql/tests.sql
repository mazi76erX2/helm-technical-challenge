-- Test case: Verify that the year field is updated to 2015 for faulty records
-- between id 20 and 100 (inclusive).
-- Assume the original year values are between 2000 and 2020.

-- Create a temporary table to store the test data.
CREATE TEMPORARY TABLE enrollments_test AS
SELECT * FROM enrollments;

-- Add default values to the year field.
INSERT INTO enrollments_test (id, year, studentId)
VALUES
    (10, 2021, 1),
    (15, 2022, 2),
    (25, 2023, 3),
    (50, 2024, 4),
    (75, 2025, 5),
    (100, 2026, 6)

-- Execute the SQL query to update the faulty records.
UPDATE enrollments_test
SET year = 2015
WHERE id BETWEEN 20 AND 100;

-- Verify the updated records.
-- Count the number of records that have year equal to 2015.
SELECT COUNT(*)
FROM enrollments_test
WHERE year = 2015
  AND id BETWEEN 20 AND 100;
-- The expected count should be equal to the number of faulty records which is 4.

-- Clean up the temporary table.
DROP TABLE enrollments_test;
