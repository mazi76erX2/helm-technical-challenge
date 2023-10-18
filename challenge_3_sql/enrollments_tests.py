import pytest
import sqlite3


@pytest.fixture
def db_connection():
    # Set up a temporary in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create the enrollments table
    cursor.execute(
        """
        CREATE TABLE enrollments_test (
            id INTEGER PRIMARY KEY,
            year INTEGER,
            studentID INTEGER
        );
    """
    )

    # Insert sample data into the enrollments table
    cursor.execute("INSERT INTO enrollments_test VALUES (10, 2021, 1)")
    cursor.execute("INSERT INTO enrollments_test VALUES (15, 2022, 2)")
    cursor.execute("INSERT INTO enrollments_test VALUES (25, 2023, 3)")
    cursor.execute("INSERT INTO enrollments_test VALUES (50, 2024, 4)")
    cursor.execute("INSERT INTO enrollments_test VALUES (75, 2025, 5)")
    cursor.execute("INSERT INTO enrollments_test VALUES (100, 2025, 5)")

    # Commit the changes to the database
    conn.commit()

    yield conn

    # Close the database connection and clean up
    conn.close()


def test_update_enrollments(db_connection):
    cursor = db_connection.cursor()

    # Execute the SQL update statement
    cursor.execute(
        """
        UPDATE enrollments_test
        SET year = 2015
        WHERE id BETWEEN 20 AND 100;
    """
    )

    # Commit the changes to the database
    db_connection.commit()

    # Verify that the enrollments have been updated correctly
    cursor.execute("SELECT year FROM enrollments_test WHERE id = 10")
    result = cursor.fetchone()
    assert result[0] == 2021

    cursor.execute("SELECT year FROM enrollments_test WHERE id = 15")
    result = cursor.fetchone()
    assert result[0] == 2022

    cursor.execute("SELECT year FROM enrollments_test WHERE id = 25")
    result = cursor.fetchone()
    assert result[0] == 2015

    cursor.execute("SELECT year FROM enrollments_test WHERE id = 50")
    result = cursor.fetchone()
    assert result[0] == 2015

    cursor.execute("SELECT year FROM enrollments_test WHERE id = 75")
    result = cursor.fetchone()
    assert result[0] == 2015

    cursor.execute("SELECT year FROM enrollments_test WHERE id = 100")
    result = cursor.fetchone()
    assert result[0] == 2015
