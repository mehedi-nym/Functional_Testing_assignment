# Functional Testing Assignment

[![Functional Testing CI](https://github.com/mehedi-nym/Functional_Testing_assignment/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mehedi-nym/Functional_Testing_assignment/actions/workflows/ci.yml)

## Project Overview

This project focuses on functional testing, automated test execution, continuous integration, and live deployment using Python and GitHub Actions.

The project tests the functions provided in `target.py`. The test suite covers normal inputs, boundary conditions, invalid inputs, exception handling, and return types. The goal is to verify the behavior of the functions and achieve complete line and branch coverage without modifying the original `target.py` file.

## Project Objectives

- Write functional tests for all 16 functions in `target.py`.
- Test valid inputs, boundary values, invalid inputs, and expected exceptions.
- Use `pytest` and parameterized tests to reduce repetition.
- Verify exception types and relevant error messages.
- Measure line and branch coverage using `pytest-cov`.
- Use Ruff for code linting.
- Automate testing with GitHub Actions.
- Build a frontend to interact with the functions and display their results.
- Deploy the application and verify the live version through health checks and smoke tests.

## Technologies Used

- **Python** — application logic and test implementation
- **pytest** — functional testing
- **pytest-cov** — line and branch coverage measurement
- **Ruff** — code linting
- **Git and GitHub** — version control and source code management
- **GitHub Actions** — continuous integration and automated testing

## Project Structure

```text
Functional_Testing_assignment/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_target.py
├── target.py
├── requirements.txt
├── .gitignore
└── README.md
```

The frontend and deployment-related files will be added as those parts of the project are completed.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mehedi-nym/Functional_Testing_assignment.git
cd Functional_Testing_assignment
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```bash
python -m pytest
```

Run the tests with line coverage, branch coverage, and a minimum coverage requirement of 100%:

```bash
python -m pytest --cov=target --cov-branch --cov-report=term-missing --cov-fail-under=100
```

The coverage requirement ensures that the test run fails if the measured coverage of `target.py` falls below 100%.

## Code Quality Check

Run Ruff to check the source code and tests for linting issues:

```bash
python -m ruff check target.py tests/
```

## Test Coverage Results

The latest successful local test run reported:

- **Tests passed:** 161
- **Line coverage:** 100%
- **Branch coverage:** 100%
- **Missed statements:** 0
- **Uncovered branches:** 0

These results reflect the reported local test run. GitHub Actions provides automated verification across the configured Python versions.

## Continuous Integration

The project uses GitHub Actions to automate quality checks.

The workflow is configured to run when changes are pushed to the `main` branch or when a pull request targets `main`.

The CI workflow includes:

1. Checking out the repository.
2. Setting up Python 3.10, 3.11, and 3.12.
3. Installing project dependencies.
4. Running Ruff lint checks.
5. Executing the test suite with line and branch coverage.
6. Failing the test job if coverage falls below 100%.
7. Uploading the HTML coverage report as a workflow artifact.

Check the [Functional Testing CI workflow](https://github.com/mehedi-nym/Functional_Testing_assignment/actions) for the latest execution results.

## Suspected Issues in the Original Code

The original `target.py` file is kept unchanged as required by the assignment. During testing, the following behaviors were identified for consideration:

- **Leap-year input validation:** `is_leap_year()` does not explicitly restrict its input to integers. A floating-point year may be accepted and evaluated instead of raising a `TypeError`.
- **Greeting input validation:** `greet()` does not explicitly validate that a provided name is a string. Inputs of unexpected types may produce an attribute-related error.
- **Input type consistency:** Some functions explicitly validate input types, while others rely on Python's built-in operations. This may lead to inconsistent behavior for unexpected input types.

These observations describe potential input-validation issues, not necessarily confirmed defects against a defined specification. The original function implementations have not been changed.

## Frontend

The frontend will provide an interface for calling the functions in `target.py` and displaying their results or errors.

**Status:** Add the framework, startup instructions, and usage examples here once the frontend has been implemented and tested.

## Deployment

**Live application:** To be added after deployment.

The deployment stage will connect successful CI runs to the deployment process. A health endpoint will report the deployed commit SHA, and automated smoke tests will verify that the expected version is running.

## Author

**Mehedi Hasan Nayem**

GitHub: [@mehedi-nym](https://github.com/mehedi-nym)