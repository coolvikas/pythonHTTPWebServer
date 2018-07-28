import route
import os
import os.path
import string,cgi,time
from os import curdir, sep

# This is the list of functions :
# each function wtih one job to do


GLOBAL_LIST_OF_HANDLERS = [];




#
#   This si for WEBSERVER
#   It executes EVERY  handler in LIST. Each one should return a STRING
#
def ExecuteEveryHandler(obj):
    global GLOBAL_LIST_OF_HANDLERS;
    print "Executing All Handlers..."

    http_res = ""

    for handlers in GLOBAL_LIST_OF_HANDLERS:

        # Every jandler must return String
        # and last handler will be final returning thingy.
        http_res=handlers(obj);
        print http_res;

    return http_res;







#
#   Server Programmer can easily add and delete programs from it
#
#   First handler in LIST OF HANDLERS. IT matches the url depending on everything.
#
def url_match_and_execute_func(obj):

    if ( obj.html ):
        http_res = "HTTP/1.1 200 OK\nConnection: close\n\n" + route.serveHTML(obj.url);
        return http_res;

    else:

        if (obj.HTTPparams['type'] == 'GET'):
            fname = (curdir + obj.url)

            if(os.path.exists(fname)):
                os.system(" php "  + fname);
                return "HTTP/1.1 200 OK\nConncection:close\n\n"+route.serveHTML(obj.url);

            else:
                func = route.findInGet(obj.url);
        else:
            func = route.findInPost(obj.url);

        if ( func == False):
            return "HTTP/1.1 404 NOT FOUND"
        else:
            return func(obj);



#
# Add one to the list
#

GLOBAL_LIST_OF_HANDLERS = { url_match_and_execute_func }
