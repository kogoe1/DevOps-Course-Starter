import os

def test_travis_env_var():
    test_env_var=os.environ.get('TEST_ENV_VAR')

    print('TEST ENV VAR: ', test_env_var)

    assert test_env_var == 'test_env_var'