import os, sys
import re
import htmlfileread
import string,cgi,time
from os import curdir, sep

# One of the main modules to determine which function will be called based on the url:
#
#
#   Two global dicts for URL

GLOBAL_POST_URLS = {}
GLOBAL_GET_URLS = {}



#   #
#   Server handling functions
#   Every URL will be associated with a funciton
#



# sets a url with fucniton
def Get(url, func):
    global GLOBAL_GET_URLS;
    GLOBAL_GET_URLS[url] = func;

# sets a url with funciton
def Post(url, func):
    global GLOBAL_POST_URLS
    GLOBAL_POST_URLS[url] = func;

# returns the function associated with url
def findInPost(url):
    global GLOBAL_POST_URLS
    for i in GLOBAL_POST_URLS:
        if i==url:
            return GLOBAL_POST_URLS[url]
    return False;


#returns the funciton associated with url
def findInGet(url):
    global GLOBAL_GET_URLS
    for i in GLOBAL_GET_URLS:
        if i==url:
            return GLOBAL_GET_URLS[url]
    return False;



###
#  Adding directory for sending html
#

# returns the HTML as string
def serveHTML(filename):
	fname = (curdir + filename)
	httpres=htmlfileread.file_html(fname);
	return httpres;
