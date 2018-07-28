import socket
from StringIO import StringIO
import requestobject
import route
import handlers
import session
import redirect









# SErver Code before starting Server

def func_hello(obj):
    print "hello"
    return "TESTING --->  hello"

def func_Explore(obj):
    print obj.isSession;
    return obj.isSession;


route.Get("/hello", func_hello)
route.Get("/explore", func_Explore);


def func_PostTest(obj):
    print obj.HTTPparams['params']
    return obj.HTTPparams['params']



route.Post("/PostTest", func_PostTest);



def func_GetTest(obj):
    print obj.HTTPparams['params']

route.Get("/GetTest", func_GetTest);
# Only URL_PARAMS supported.



def func_SessionStartTest(obj):
    #
    #   A normal authentication test:
    #
    #   POST login_info with it :)
    user = obj.HTTPparams['params']['user']
    pwd = obj.HTTPparams['params']['pwd']

    # Any random contition

    if ( user == "dev"):
        #start new session:
        sid = session.start_new_session();
        session.add_param_to_session(sid, "user", user);

        print "SESSION GENERATED ->" + str(sid);

        # Session Headers;
        return  session.genSessionHeader(sid);

    else:
        return "HTTP/1.1 404 NOT FOUND\n"


def func_SessionMaintainsTest(obj):

    #
    #   A Test for testing whether the session is recognized by the server ornot
    #
    print "IsSession -->" + str(obj.isSession)
    print "Session Params -->" + str(obj.session_param);

    return "HTTP/1.1 200 OK\nConnection:Close\n\n<html><h1>Session Maintianed</h1></html>"




route.Post("/s_StartTest", func_SessionStartTest);
route.Get("/s_MaintainTest", func_SessionMaintainsTest);


###############################################################################################################

"""def func_VerifyUser(obj):
	x= obj.HTTPparams['params']
	if(x['u']=="IIT"):
		sid = session.start_new_session()
        session.add_param_to_session(sid, "user", x['u'])
        print "SESSION GENERATED ->" + str(sid)
        # Session Headers;
        x = session.genSessionHeader(sid)
        x  = x+redirect.redirect_to_url(obj,"/main.html");
        return x;

	else:
		redirect.redirect_to_url(obj, "/index.html");
		return x;
	return "HTTP/1.1 404 OK\nConnection:Close\n\n<html><h1>NOt Found</h1></html>"""




def func_VerifyUser (obj):
	x= obj.HTTPparams['params']
	if (x['u']=="DEV" and x['p']=="dev"):
		sid = session.start_new_session()
		session.add_param_to_session(sid, "user", x['u'])
		print "SESSION GENERATED ->" + str(sid)
		x = session.genSessionHeader(sid)
		x  = x+redirect.redirect_to_url(obj,"/dev.html")
		return x
        else:
            if (x['u'] == "vik" and x['p'] == "vik"):
                sid = session.start_new_session()
                session.add_param_to_session(sid, "user", x['u'])
                print "SESSION GENERATED ->" + str(sid)
                x = session.genSessionHeader(sid)
                x = x + redirect.redirect_to_url(obj, "/viaks.html")
                return x
            else:

                y = "HTTP/1.1 200 OK\nConnection:close\n\n" + redirect.redirect_to_url(obj, "/index.html")
                return y

route.Post("/execute",func_VerifyUser)



def func_logout(obj):
    # get session id;
    ssid = obj.sessionid;
    session.remove_this_session(ssid)
    y = "HTTP/1.1 200 OK\nConnection:close\n\n" + redirect.redirect_to_url(obj, "/index.html")
    return y;

route.Get("/logout", func_logout)














#####################################################################################################################



HOST, PORT = '', 8899

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(8192*2)
    print request
    #webServer.parse(request)

    obj = requestobject.RequestObject(request)
    #print



    if ("POST" in request):
		print("POST REQUEST RECV-->");

#    http_response = """\
#HTTP/1.1 200 OK

#Content-Type: text/html; charset=utf-8
#Server: Microsoft-IIS/7.0
#X-AspNet-Version: 2.0.50727
#X-Powered-By: ASP.NET
#Connection: close\n\n
#""" +
    http_response = str(handlers.ExecuteEveryHandler(obj));
    client_connection.sendall(http_response)
    client_connection.close()
