import copy
import route
def redirect_to_url(obj, url):
	 obj1=copy.deepcopy(obj);
	 obj1.url=url;
	 if(".html" in url ):
	 	http_res =  route.serveHTML(url);
	 	return http_res;
	 elif ( ".jpg" in url or ".pdf" in url):
		 http_res = route.serveHTML(url);
		 return http_res;
	 else:
	 	func = route.findInGet(url);
	 	if ( func == False):
	 		return "HTTP/1.1 404 NOT FOUND"
	 	else:
	 		return func(obj1);

       

