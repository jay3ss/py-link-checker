"""Web scraper components"""
from urllib import parse
import time

import requests

from helpers import print_same_line


def get_full_links(links, base):
    full_links = set()

    for link in links:
        if not has_protocol(link):
            link = parse.urljoin(base, link['href'])
        else:
            link = link['href']
        full_links.add(link)

    return full_links


def has_protocol(source):
    return source['href'][:4] == 'http'


def resolves(link):
    try:
        requests.get(link)
        return True
    except:
        return False


def verify_links(links, base, callback=None, sleep=0.1):
    """Verifies that the given links are able to be resolved

    Args:
        links:
            list of links to be verified. Doesn't need to have unique elements,
            this will be taken care of
        base:
            Base URL of site (essentially the starting URL) used for relative
            links
        callback:
            Callback function
        sleep:
            Amount of time to sleep between verifying links

    Returns:
        Dictionary of links:
            working:
                list of links that resolve
            not_working:
                list of links that don't resolve
    """
    full_links = get_full_links(links, base)
    good_links = []
    bad_links = []

    for num, link in enumerate(full_links):
        if callback is not None:
            callback(link)

        print_same_line(f'Verifying link {link}: {num+1}/{len(full_links)}')
        good_links.append(link) if resolves(link) else bad_links.append(link)

        time.sleep(sleep)

    return {'working': good_links, 'not_working': bad_links}
