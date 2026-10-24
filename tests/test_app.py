
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_homepage_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Functional Testing Playground" in response.data


def test_homepage_displays_all_functions(client):
    response = client.get("/")

    for function_name in [
        "is_adult",
        "celsius_to_fahrenheit",
        "count_vowels",
        "invert",
        "greet",
        "find_max",
        "get_price",
        "swap",
        "common_items",
        "is_leap_year",
        "to_int",
        "divide",
        "power",
        "square_root",
        "factorial",
        "average",
    ]:
        assert function_name.encode() in response.data


def test_execute_function_successfully(client):
    response = client.post(
        "/",
        data={"function": "is_adult", "arguments": "(18,)"},
    )

    assert response.status_code == 200
    assert b"Result" in response.data
    assert b"True" in response.data


def test_display_function_error(client):
    response = client.post(
        "/",
        data={"function": "divide", "arguments": "(10, 0)"},
    )

    assert response.status_code == 200
    assert b"ZeroDivisionError" in response.data


def test_reject_unknown_function(client):
    response = client.post(
        "/",
        data={"function": "unknown_function", "arguments": "()"},
    )

    assert response.status_code == 200
    assert b"Please select a valid function." in response.data


def test_reject_invalid_python_syntax(client):
    response = client.post(
        "/",
        data={"function": "is_adult", "arguments": "not valid python"},
    )

    assert response.status_code == 200
    assert b"Input error" in response.data


def test_reject_non_tuple_arguments(client):
    response = client.post(
        "/",
        data={"function": "is_adult", "arguments": "18"},
    )

    assert response.status_code == 200
    assert b"TypeError" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
