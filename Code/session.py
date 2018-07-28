import random

SessionDict = {};

isSessionOn = 0;

session = {};


def set_session_on():
    global isSessionOn;
    isSessionOn = 1;

# if session is On -> Create Set-Cookie header in HTTP header.
def session_token_gen():
    return "SES" + str(random.randint(-9999,9999))

def add_session_to_list (sessionid):
    dic = {}
    session[sessionid] = dic;

def add_param_to_session(session_id, param_name, param_param):
    session[session_id][param_name] = param_param;

def genSessionHeader(session_id):
    return """HTTP/1.1 200 OK\nContent-Type: text/html\nSet-Cookie: SESSIONID="""+str(session_id)+""";path=/\nConnection: close\n\n"""


def searchSession(session_id):
    global session;
    print session;
    for ss in session:
        if ss == session_id:
            return session[ss]
    return False



################################3
#
#   For servers function
#
#############################


def start_new_session():
    sid = session_token_gen()
    add_session_to_list(sid);
    print session;
    return sid;

def remove_this_session(session_id):
    del session[session_id]
