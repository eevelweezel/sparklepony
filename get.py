import requests


def main(url):
    try:
        resp = requests.get(url)
        print(f"Called {url}, received {resp.text}, {resp.status_code}")
    except Exception as e:
        print(f"Error in call: {e}")


if __name__ is __main__:
    parser = argparse.ArgumentParser(description="Parser for URLs.")
    parser.add_argument('--url', help='Add the URL you want to call')
    args = parser.parse_args()
    main(args["url"])

