import sys
from typing import Generator

sys.path = ["", ".."] + sys.path[1:]  # noqa:E402

import pytest
from fastapi.testclient import TestClient
from main import create_app  # noqa:E402

app = create_app()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
