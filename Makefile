.PHONY: test_1, test_2, test_3, test_4, run_pandas, run_torch, run_sklearn

test_1:
    pytest challenge_1_python/tests.py --disable-warnings --cov

test_2:
    pytest challenge_2_python/tests.py --disable-warnings --cov

test_3:
	pytest challenge_3_sql/enrollments_tests.py --disable-warnings --cov

test_4:
	pytest challenge_4_sql/session_tests.py --disable-warnings --cov

run_pandas:
	python challenge_5_data_proceessing/movies_data_processing.py

run_torch:
	python challenge_5_data_proceessing/model_pytorch.py

run_sklearn:
	python challenge_5_data_proceessing/model_scikitlearn.py
