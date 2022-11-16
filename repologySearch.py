#!/usr/bin/env python3
"""
Search for packages in repologys database
"""
import json
import argparse
import re
import logging
from json import JSONDecodeError
from urllib import request
from urllib.error import HTTPError, URLError

def _url_content(url) -> bytes:
    try:
        with request.urlopen(url) as response:
            content = response.read()
    except HTTPError:
        return None
    except URLError:
        logging.warning("invalid url: " + url)
        return None
    return content

def getPackages(url: str) -> list[dict]:
    packages = []
    package_info = _url_content(url)
    try:
        package_info = json.loads(package_info)
    except JSONDecodeError:
        return None
    if package_info is None:
        return None
    for package_list in package_info.values():
        for package in package_list:
            packages.append(package)
    return packages
        

def pprintPackage(package: dict):
    for k in package.keys():
        print(k, ":", package[k])

def main():
    parser = argparse.ArgumentParser(
        description="Search for packages using repologys package database."
    )
    parser.add_argument(
        "name",
        help="Name of a software"
    )
    parser.add_argument(
        "-s", 
        "--strict",
        action="store_true",
        help="Display only packages that match name exactly"
    )
    parser.add_argument(
        "-r",
        "--repo",
        nargs=1,
        help="Filter output for a Repository. The argument for this flag is"
        + " a regular expression. For example to match the searchterm exactly"
        + " ^repo$ could be used."
    )
    args = parser.parse_args()

    url = 'https://repology.org/api/v1/projects/?search='
    url += args.name
    url += '&maintainer=&category=&inrepo=&notinrepo=&repos=&families='
    url += '&repos_newest=&families_newest=&newest=on'
    packages = getPackages(url)
    for p in packages:
        if args.repo:
            repo = p.get("repo", None)
            if repo is None:
                continue
            if re.search(args.repo[0], repo.strip()) is None:
                continue
        if args.strict:
            if p.get("srcname") == args.name:
                pass
            elif p.get("binname") == args.name:
                pass
            elif p.get("visiblename") == args.name:
                pass
            else:
                continue

        print()
        pprintPackage(p)

if __name__ == "__main__":
    main()
