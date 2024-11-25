import os
import pytest

@pytest.fixture(scope='session', autouse=True)
def set_test_env():
    os.environ['TEST_ENV'] = 'true'  # Set the environment variable
    yield
    del os.environ['TEST_ENV']  # Clean up after tests