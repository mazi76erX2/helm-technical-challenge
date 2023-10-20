# Helm Technical Challenge

## Backend PYTHON AND SQL Challenge

This repository contains backend Python and SQL challenge solutions.

## Installation

To get started, clone the repository from GitHub:

```bash
git clone https://github.com/mazi76erX2/helm-technical-challenge.git
```

Navigate to the cloned repository:

```bash
cd helm-technical-challenge
```

Install the project dependencies using pipenv:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

## Running Tests

The repository provides several test suites that you can run using the following commands:

- **Test 1** (Python): Run pytest for challenge_1_python/tests.py:

  ```bash
  make test_1
  ```

- **Test 2** (Python): Run pytest for challenge_2_python/tests.py:

  ```bash
  make test_2
  ```

- **Test 3** (SQL): Run pytest for challenge_3_sql/enrollments_tests.py:

  ```bash
  make test_3
  ```

- **Test 4** (SQL): Run pytest for challenge_4_sql/session_tests.py:

  ```bash
  make test_4
  ```

## Running Data Processing Scripts

The repository also includes data processing scripts that can be executed using the following commands:

- **Pandas**: Run the movies_data_processing.py script:

  ```bash
  make run_pandas
  ```

- **PyTorch**: Run the model_pytorch.py script:

  ```bash
  make run_torch
  ```

- **scikit-learn**: Run the model_scikitlearn.py script:

  ```bash
  make run_sklearn
  ```

Make sure to activate the pipenv virtual environment before running the scripts.
