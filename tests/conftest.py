import sys
from typing import Generator

import pytest  # noqa:E402
from faker import Factory

sys.path = ["", ".."] + sys.path[1:]  # noqa:E402


from fastapi.testclient import TestClient  # noqa:E402
from main import create_app  # noqa:E402

app = create_app()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def faker() -> Generator:
    return Factory.create("pt_BR")
