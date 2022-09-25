import pytest
from IPYNBrenderer import render_YouTube_video
from IPYNBrenderer.custom_exception import InvalidURLException


class TestYTvideoRenderer:
    URL_test_success_data = [
        ("https://youtu.be/68annotEgHs", "success"),
        ("https://www.youtube.com/watch?v=68annotEgHs", "success"),
        ("https://www.youtube.com/watch?v=68annotEgHs&t=42s", "success"),
    ]
    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=68annotEgHsdxcfvg"),
        ("https://www.youtube.com/watch?v=68annotEgHs0"),
        ("https://www.youtube.com/watch?v=68annotEgHs__"),
        ("https://www.youtube.com/watch?v=68annotEgHsss"),
        ("https://www.youtube.com/watch?v=68annotEgHs&t"),
        ("https://www.youtube.com/watch?v=68annotEgHs&t==22s"),
        ("https://www.youtube.com/watch?v==68annotEgHs&t=22s"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_YT_success(self, URL, response):
        assert render_YouTube_video(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)