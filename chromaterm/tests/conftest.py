'''pytest configuration'''
from ctypes.util import find_library


def pytest_generate_tests(metafunc):
    '''Run tests with the `pcre` fixture twice; Once with `pcre=False`, another
    time with `pcre=True` if the library is present.'''
    if 'pcre' not in metafunc.fixturenames:
        return

    params = [False]
    if find_library('pcre2-8'):
        params.append(True)
    metafunc.parametrize('pcre', params)
