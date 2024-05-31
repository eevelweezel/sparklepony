import requests


def make_request(url):
    try:
        resp = requests.get(url)
        print(f"Called {url}, received {resp.text}, {resp.status_code}")
        return resp
    except Exception as e:
        print(f"Error in call: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for URLs.")
    parser.add_argument('--url', help='Add the URL you want to call')
    args = parser.parse_args()
    make_request(args["url"])

