.PHONY: test_1, test_2

test_1:
    pytest challenge_1_python/tests.py --disable-warnings --cov

test_2:
    pytest challenge_2_python/tests.py --disable-warnings --cov
