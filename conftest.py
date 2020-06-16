import pytest
from fixture.application import Application


@pytest.fixture(scope = "session") # scope = "session" - запуск браузера на сессию, а не на каждый тест
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture