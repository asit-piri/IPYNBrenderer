import pytest
from IPYNBrenderer import get_time_info
from IPYNBrenderer.custom_exception import InvalidURLException

good_URL_data = [
    ("https://youtu.be/68annotEgHs", 0),
    ("https://www.youtube.com/watch?v=68annotEgHs", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
]


URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=68annotEgHs"),  # exception
    ("https://www.youtube.com/watch?v=68annotEgHs&t"),  # exception
    ("https://www.youtube.com/watch?v=68annotEgHs&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==68annotEgHs&t=22s")
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)