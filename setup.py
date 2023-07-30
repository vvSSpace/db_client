from distutils.core import setup

REQUIRES = [
    'structlog~=23.1.0',
    'allure-pytest',
    'records~=0.5.3',
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/vvSSpace/orm_client.git',
    license='MIT',
    author='Vyacheslav Sevastyanov',
    author_email='-',
    install_requires=REQUIRES,
    description='db client with allure and logger'
)
