import pytest
import os

def pytest_addoption(parser):
    parser.addoption(
        "--test", action="store", default="all", help="select the test function"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--test")