.PHONY: test_1, test_2, test_3, test_4

test_1:
    pytest challenge_1_python/tests.py --disable-warnings --cov

test_2:
    pytest challenge_2_python/tests.py --disable-warnings --cov

test_3:
	pytest challenge_3_sql/enrollments_tests.py --disable-warnings --cov

test_4:
	pytest challenge_4_sql/session_tests.py --disable-warnings --cov
