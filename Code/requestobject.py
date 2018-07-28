from requestparam import parse_GET_param, parse_PUT_param, parse_POST_param
import session
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message




def extractVariablesFromRequest(req):
    allvar = {}
    request = HTTPRequest(req)
    allvar['type'] = request.command
    allvar['url'] = request.path
    if( "cookie" in request.headers):
        allvar['cookie'] = True;
        print "COOKIE in Header --> " + str(request.headers['cookie'])
        allvar['sessionid'] = request.headers['cookie']
    else:
        allvar['cookie'] = False;

    if(allvar['type'] == 'GET'):
        allvar['params'] = parse_GET_param(req);
    if(allvar['type'] == 'POST'):
        allvar['params'] = parse_POST_param(req);
    return allvar



"""class RequestObject:
	def __init__(self, request):
        #self.session_param = {}
		self.request = request
		self.HTTPparams = extractVariablesFromRequest(self.request);
		self.isSession = self.HTTPparams['cookie']
		self.sessionid = ""

        #self.url = self.HTTPparams['url']
        #self.html = False;
        if (self.isSession):
			self.sessionid = self.HTTPparams['sessionid'];
            #self.session_param = session.searchSession(self.sessionid);
        if (".html" in self.url ):
            self.html = True;"""


class RequestObject:

    def __init__(self, request):
        self.request = request;
        self.html = False
        self.url = ""
        self.HTTPparams = extractVariablesFromRequest(request)
        self.isSession = self.HTTPparams['cookie']
        self.sessionid = ""
        self.url = self.HTTPparams['url']
        if (self.isSession):
            #print "Session is working"
            self.sessionid = self.HTTPparams['sessionid'].split("=")[1];
            print str(self.sessionid)
            self.session_param = session.searchSession(self.sessionid);

        if (".html" in self.url):
            self.html = True;
            self.url = self.url.split(".html")[0] + ".html"
            print self.url;

