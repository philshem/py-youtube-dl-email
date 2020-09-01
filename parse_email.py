
from imap_tools import MailBox, AND
from urlextract import URLExtract
from urllib.parse import urlparse

'''
reads unread emails and scans for youtube
'''

import utils

def parse_email(imap,u,pw):
    # get list of email subjects from INBOX folder - equivalent verbose version
    mailbox = MailBox(imap)
    mailbox.login(u, pw, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
    
    # for debugging, you can set mark_seen=False
    # texts = [msg.html for msg in mailbox.fetch(AND(all=True),mark_seen=False)]
    # sometimes html, sometimes text
    h = [msg.html for msg in mailbox.fetch(AND(all=True),mark_seen=False)]
    h += [msg.text for msg in mailbox.fetch(AND(all=True),mark_seen=False)]
    #print(h) # debugging
    mailbox.logout()
    return h

def parse_urls(t):
    ul = []
    for h in t:
        #print(h)
        extractor = URLExtract()
        # it's a little buggy, since youtube urls have a path that is case sensitive
        # but the domain and tld are themselves case insensitive
        u = extractor.find_urls(h)
        #print(u)
        ul += u

    ul = list(set(ul))
    return ul

def validate_urls(url_list, domain_whitelist):

    # receive list of urls, check if their domains match the whitelist

    valid_urls = [x for x in url_list if extract_domain(x).lower() in domain_whitelist]

    return valid_urls

def extract_domain(u):
    domain = urlparse(u).hostname.lower()
    if domain.startswith('www.'):
        domain = domain.replace('www.','')
    #print(domain)
    return domain

