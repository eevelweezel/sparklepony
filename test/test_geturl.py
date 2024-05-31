from sparklepony.geturl import make_request
import pytest


url = "https://github.com"


def test_get(mocker):
    mock_requests = mocker.patch("sparklepony.geturl.requests.get")
    resp = make_request(url)
    assert resp
    mock_requests.assert_called()


def test_get_exception(mocker):
    mock_request_exception = mocker.patch("sparklepony.geturl.requests.get", side_effect=Exception)
    with pytest.raises(Exception):
        make_request(url)
    mock_request_exception.assert_called()
