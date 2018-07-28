def file_html(fname):
	fptr=open(fname,"r")
	to_send = ""
	for lines in fptr:
		to_send += lines;
	return to_send

#file_html("myfile.html");
