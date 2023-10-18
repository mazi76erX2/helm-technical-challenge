.PHONY: test-1, test-2

test-1:
    pytest challenge_1_python/tests.py --disable-warnings

test-2:
    pytest challenge_2_python/tests.py --disable-warnings
