"""
Checks metadata of Python package
"""

import argparse
import re
import requests

try:
    import importlib.metadata
    HAVE_METADATA = True
except ImportError:
    HAVE_METADATA = False


def check_project_url(package_name):
    dist = importlib.metadata.distribution(package_name)
    url = dist.metadata['Project-URL']
    if not url:
        print("Skipping check since importlib.metadata is not available. Python version <= 3.8?")
        return

    parsed_url = re.search(r"(?P<url>https?://[^\s]+)", url).group("url")
    print(f"Found Project-URL: {parsed_url}")

    response = requests.get(parsed_url)
    if not response or not response.status_code == 200:
        raise RuntimeError(f"Could not retrieve a successfull response from {parsed_url}. Is the Homepage metadata in "
                           f"pyproject.toml for \"{package_name}\" correct? Response: {response}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package-name')
    args = parser.parse_args()

    if not HAVE_METADATA:
        print("Skipping check since importlib.metadata is not available. Python version <= 3.8?")
        return

    if args.package_name:
        check_project_url(args.package_name)
    else:
        for d in importlib.metadata.distributions():
            if d.name and d.name.startswith('tree-sitter-'):
                check_project_url(d.name)

    print("Metadata check successful")


if __name__ == '__main__':
    main()
