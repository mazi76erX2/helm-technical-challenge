import pytest
import sqlite3


class TestSelectSessions:
    @pytest.fixture(scope="module")
    def setup_method(self, method):
        # Set up a test database connection
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

        # Create a test table
        self.cursor.execute(
            """
            CREATE TABLE sessions (
                id INTEGER PRIMARY KEY,
                userId INTEGER NOT NULL,
                duration DECIMAL NOT NULL
            )
        """
        )

        # Insert test data
        self.cursor.execute(
            """
            INSERT INTO sessions (id, userId, duration)
            VALUES
                (1, 1, 30),
                (2, 1, 45),
                (3, 2, 60),
                (4, 2, 75),
                (5, 3, 90),
                (6, 3, 120),
                (7, 3, 150)
        """
        )
        self.conn.commit()

    def teardown_method(self, method):
        # Clean up the test table and close the database connection
        self.cursor.execute("DROP TABLE sessions")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def test_select_users_with_multiple_sessions(self):
        # Execute the SQL query to select userId and average session duration for each user
        self.cursor.execute(
            """
            SELECT userId, AVG(duration) AS average_duration
            FROM sessions
            GROUP BY userId
            HAVING COUNT(*) > 1
        """
        )
        results = self.cursor.fetchall()

        # Verify the expected users and their average session durations
        expected_results = [(1, 37.5), (3, 120.0)]
        assert results == expected_results

    def test_select_users_with_single_session(self):
        # Insert a user with a single session
        self.cursor.execute(
            """
            INSERT INTO sessions (id, userId, duration)
            VALUES (8, 4, 60)
        """
        )
        self.conn.commit()

        # Execute the SQL query to select userId and average session duration for each user
        self.cursor.execute(
            """
            SELECT userId, AVG(duration) AS average_duration
            FROM sessions
            GROUP BY userId
            HAVING COUNT(*) > 1
        """
        )
        results = self.cursor.fetchall()

        # Verify that no users with multiple sessions are returned
        assert results == []

    def test_select_users_with_no_sessions(self):
        # Execute the SQL query to select userId and average session duration for each user
        self.cursor.execute(
            """
            SELECT userId, AVG(duration) AS average_duration
            FROM sessions
            GROUP BY userId
            HAVING COUNT(*) > 1
        """
        )
        results = self.cursor.fetchall()

        # Verify that no users with multiple sessions are returned
        assert results == []
