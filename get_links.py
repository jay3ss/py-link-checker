"""Test script for getting all links from a web page"""
import argparse
import os
import signal
import sys
import time

from bs4 import BeautifulSoup
import requests

from helpers import *
from scraper import *

# This is a hack so that we can kill the process b/c SIGINT isn't working...
print(f'PID is {os.getpid()}')


def signal_handler(sig, frame):
    """Found https://stackoverflow.com/a/1112350/3562890"""
    print('Quit signal received, exiting...')
    # os.kill(os.getpgid(), signal.SIGUSR1)
    # sys.exit(0)
    os.system(f'kill -1 {os.getpid()}')
    # sys.exit('Quit signal received, exiting...')


# register the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
# signal.signal(signal.SIGUSR1, signal_handler)

parser = argparse.ArgumentParser(
    description='Test script for getting all links from a web page')

parser.add_argument('-u', action='store', dest='url', help='URL to test')

args = parser.parse_args()

test_url = args.url
# test_url = 'https://www.reddit.com'
response = requests.get(test_url)
headers = response.headers
print('Headers:')
print(headers)
print()

soup = BeautifulSoup(response.text, 'lxml')
# print('HTML:')
# print(soup.prettify())
# print()

links = soup.find_all('a')
print('Links:')
print(f'Number of links: {len(links)}')
# print('First 10 links:')
# print(links[:10])

print('Validating links')
start_time = time.time()
verified_links = verify_links(links, test_url)
print(f'\nTook {time.time() - start_time}')
print()
print(f'{len(verified_links["working"])} are working')
print('Working links:')
print(verified_links['working'])
print('\nNon-working links:')
print(verified_links['not_working'])

