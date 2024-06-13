import requests


def make_request(url):
    try:
        resp = requests.get(url)
        print(f"Called {url}, received {resp.text}, {resp.status_code}")
        return resp
    except Exception as e:
        print(f"Error in call: {e}")
        raise
