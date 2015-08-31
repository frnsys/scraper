import lxml.html
from urllib import request


def make_request(url):
    # spoof a user-agent to look like a person
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = request.urlopen(req)
    body = resp.read()

    # oops, something went wrong
    if resp.getcode() != 200:
        raise Exception('Non-200 status code for {}'.format(url))

    # return an lxml html obj to work with
    return lxml.html.fromstring(body)