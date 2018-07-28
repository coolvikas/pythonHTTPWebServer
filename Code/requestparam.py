def parse_GET_param(url):
    params_dict={}

    if ('?' not in url):
        return params_dict
    params_in_url = url.split("?")[1];
    params_list = params_in_url.split("&");

    for params_pair in params_list:
        pp = params_pair.split("=");

        params_dict[pp[0]] = pp[1];

    return params_dict;

def parse_PUT_param(request):
        params_dict={}
        split_req=request.splitlines();
        for lines in split_req:
            first_word=lines.split(":")

            if(first_word[0]=="Content-Type"):
                if("x-www-form-urlencoded" in first_word[1]):
                    #print("x-www-form-urlencoded detected");
                    #print(split_req)
                    linewa=split_req[-1];
                    params_list=linewa.split("&")
                    for params_pair in params_list:
                        pp=params_pair.split("=")
                        params_dict[pp[0]]=pp[1]

                if("form-data" in first_word[1]):
                    #print("form-data detected");
                    boundary=first_word[1].split("=")[1];
                    params_split_at_bound=request.split(boundary)
                    #print params_split_at_bound
                    for entries in params_split_at_bound:
                        if("Content-Disposition" in entries):
                            get_param_list=entries.split("\r\n")
                            #print get_param_list
                            params_dict[get_param_list[1].split("=")[1]]=get_param_list[3];
        return params_dict;
        pass

def parse_POST_param(request):

    params_dict = {}
    #search for content disposition & content-length;
    split_req = request.splitlines();

    for lines in split_req:
        first_word = lines.split(":");

        if ( first_word[0] == "Content-Type"):
            #if multipart then boundary
            # else simple header data;
            if ( "x-www-form-urlencoded" in first_word[1]):
                print("x-www-form-urlencoded detected");
                linewa = split_req[-1];
                params_list = linewa.split("&");
                for params_pair in params_list:
                    pp = params_pair.split("=");
                    params_dict[pp[0]] = pp[1];


            if ("multipart" in first_word[1]):
                #print("multipart detected");
                bound = first_word[1].split("=")[1];
                #print (bound);
                params_split_at_bound = request.split(bound);
                #print params_split_at_bound;
                for entries in params_split_at_bound:
                    if ("Content-Disposition" in entries):
                        get_param_list = entries.split("\r\n");
                        #print(get_param_list);
                        params_dict[get_param_list[1].split("=")[1]]=get_param_list[3];'''
                        #test=get_param_list[1].split("=")
                        #print test;
                        if("filename" in get_param_list[1].split("=")[1]):
                            print "filename detected"
                            new_params_list=get_param_list[4:len(get_param_list)+1]
                            print len(get_param_list);
                            print len(new_params_list);
                            file_param_list=''.join(new_params_list);
                            import zlib
                            with open("filetosave","wb") as f1:
                            #i=4;
                            #length=len(get_param_list)
                            #length=length-1;
                            #while i<length:
                             #   i=i+1;
                                #print i
                                f1.write(get_param_list[4])
                            f1.close();
                            fopen=open("filetosave","r")
                            #import StringIO
                            #compressedstream=StringIO.StringIO(file_param_list)

                            with open("filetosave","rb") as f:
                                data=f.read()
                            print len(data);

                            len1=zlib.decompress(data)
                            print(len1)
                            with open("filetosave","w") as final:
                                final.write(data)
                            #for line in fopen:
                             #   print line;
                            fopen.close();

                        else:
                            params_dict[get_param_list[1].split("=")[1]]=get_param_list[3];
                    '''



    return params_dict;







def parse(request):

    parsed_request = {}
    split_req = request.splitlines();

    #print(split_req);
    #Line split request;

    #Line 1 : contains type of Request and URL;
    line1 = split_req[0].split(" ");

    #type of request
    parsed_request["type"] = str(line1[0]);
    parsed_request["url"] = str(line1[1]);

    print parsed_request;

    print split_req;

    parse_params={}



    #returns parsed request;
    #print(parsed_request);

    #if ( parsed_request["type"] == "GET"):
        #print(parse_GET_param(parsed_request["url"]));

    if (parsed_request["type"] == "POST"):
        print(parse_POST_param(request));

    if(parsed_request["type"]=="PUT"):
        print(parse_PUT_param(request));

    return parsed_request;
