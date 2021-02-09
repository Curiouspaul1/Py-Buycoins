import pytest
from pycoins.core import APIClient


@pytest.fixture(autoreuse=True)
def test_pyclient():
    client = APIClient.PycoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
    return client
