import pytest

'''
Pytest default function to set default fixtures.
Enables command line options for fixtures.
You can pass in parameters using the .env file or just using command line parameters listed below.
eg:
$ pytest --file evtxfiles/1.evtx
'''
def pytest_addoption(parser):
    parser.addoption('--file', action='store', default='evtxfiles/1.evtx', help='Path to .evtx file.')


# Pytest fixture for 10minutemail object.
# Used by some test functions to register, read email etc.
@pytest.fixture
def evtxFile(request):
    return request.config.getoption('--file')
