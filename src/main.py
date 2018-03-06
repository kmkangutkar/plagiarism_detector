import cherrypy
import multicode
import multifile
import multiimage
import os
import tempfile
import cgi

image_names = []

class myFieldStorage(cgi.FieldStorage):
    
    def make_file(self, binary=None):
        return tempfile.NamedTemporaryFile()

def noBodyProcess():
    cherrypy.request.process_request_body = False

cherrypy.tools.noBodyProcess = cherrypy.Tool('before_request_body', noBodyProcess)

class PlagiarismDetector(object):
	#home page
	@cherrypy.expose
	def index(self):
        	return """<html><style>
                    form {
                        border: 3px solid #f1f1f1;
                    }

 
                    button {
                        background-color: #4CAF50;
                        padding: 14px 20px;
                        margin: 8px 0;
                        border: none;
                        cursor: pointer;
                        width: 100%;
                    }

                    button:hover {
                        opacity: 0.8;
                    }

                    
                    .imgcontainer {
                        text-align: center;
                        margin: 24px 0 12px 0;
                    }

                    img.avatar {
                        width: 20%;
                        border-radius: 30%;
                    }

                    .container {
                        padding: 16px;
                    }

                    span.psw {
                        float: right;
                        padding-top: 16px;
                    }

                   
                </style>
            <head><title>Rivelatore Copia</title></head>
            <body>

                <h1> Rivelatore Copia </h1>

                <form method="get", action="selection">
                    <div class="imgcontainer">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGq2u81tUZGaZUnYRTT4ZE8V6oyDk__7af7makehUB508VcjKV" alt="Avatar" class="avatar">
                    </div>

                   <button type="submit">Start</button>
                    <head>
        <style> 
        div {
            width:370px;
            height: 200px;
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTA7MmLH6MVPmncfaW-MOUDosNqxz-6Xihs7FbRp_6u1t_WniEDvQ");
            position: relative;
            -webkit-animation: mymove 5s infinite; /* Safari 4.0 - 8.0 */
            -webkit-animation-delay: 2s; /* Safari 4.0 - 8.0 */
            animation: mymove 5s infinite;
            animation-delay: 0s;
        }

        /* Safari 4.0 - 8.0 */
        @-webkit-keyframes mymove {
            from {left: 0px;}
            to {left: 500px;}
        }

        @keyframes mymove {
            from {left: 0px;}
            to {left: 700px;}
        }
        </style>
        </head>

                </form>
	<p></br><b>Plagiarism Detector:</b></br><i>Detects Plagiarism in texts, C programming language codes and Images!</i></p>
            </body>
        </html>"""
	
	#detector selection page	
	@cherrypy.expose
	def selection(self):
		 return """<html>
            <head>
                <style>
                    .dropbtn {
                        background-color: #4CAF50;
                        color: white;
                        padding: 16px;
                        font-size: 16px;
                        border: none;
                        cursor: pointer;
                    }

                    .dropdown {
                        position: relative;
                        display: inline-block;
                    }

                    .dropdown-content {
                        display: none;
                        position: absolute;
                        background-color: #4CAF50;
                        min-width: 160px;
                        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                        z-index: 1;
                    }

                    .dropdown-content a {
                        color: black;
                        padding: 12px 16px;
                        text-decoration: none;
                        display: block;
                    }

                    .dropdown-content a:hover {background-color: #f1f1f1}

                    .dropdown:hover .dropdown-content {
                        display: block;
                    }

                    .dropdown:hover .dropbtn {
                        background-color: #3e8841;
                    }
                </style>
                <title>Select Detector</title>
            </head>
            <body>
            
                <style>
                    body {
                        color: blue;
                    }

                    h1 {
                        color: green;
                    }
                    </style>

                
                <h2><p> Choose the catagory in which you want to detect Plagiarism.</p></h2>

                <div class="dropdown">
                <button class="dropbtn", action="generate">Select Your Choice</button>
                <div class="dropdown-content">
                    <a href="http://localhost:8080/code">CODE</a>
                    <a href="http://localhost:8080/text">TEXT</a>
                    <a href="http://localhost:8080/image">IMAGE</a>
                </div>
                </div>
                </br></br>
                <div class="imgcontainer">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0FxVLXzevnCTTSJV4bEuNMElIyThBKTxwaFZ5-6qIEr8HicNF" alt="Avatar" width=700" height="400" class="avatar">
                    </div>

            </body>
        </html>"""

	#code detector page
	@cherrypy.expose
	def code(self):
		
       		return """<html>
            	<head><title>Upload Codes</title></head>
            	<style>
                    body {
                        color: red;
                    }

                    h2 {
                        color: green;
                    }
                    </style>
            
            <h2>  CODE Plagiarism Detector </h2><p>Upload C program files to compare!</p>
        <form id="myform" action="codeUpload" enctype="multipart/form-data" method="post">
		Codes: <input type="file" id="files" name="files" multiple />
	<input type="submit" id="button" />
          </html>
        """
       
        #function: read and store code and display results
        @cherrypy.expose
	def codeUpload(self, **kwargs):
		reader = []
		out = """<html><head><title>Detector Results!</title></head><body><h1>RESULT</h1> %s</body></html>"""
		try:
			filesUploaded = 0
			for f in kwargs['files']:
				reader.append([f.filename, f.file.read()])
			  	filesUploaded = filesUploaded + 1
			result = multicode.multicode(reader)
		except IOError:
			result = "</br>Error"
			pass
		return out %(result)
			 	
	
	#text detector page
	@cherrypy.expose
	def text(self):
		return """<html>
            <head><title>Upload Text Docs</title></head>
            <style>
                    body {
                        color: red;
                    }

                    h2 {
                        color: green;
                    }
                    </style>
            
            <h2>  TEXT Plagiarism Detector </h2><p>Upload text files to check for plagiarism!</p>
        <form id="myform" action="textUpload" enctype="multipart/form-data" method="post">
		Files: <input type="file" id="files" name="files" multiple />
	<input type="submit" id="button" />
           <html>
        """
        
			
        #function: read and store text and display results
        @cherrypy.expose
	def textUpload(self, **kwargs):
		reader = []
		out = """<html><head><title>Detector Results!</title></head><body><h1>RESULT</h1> %s</body></html>"""
		try:
			filesUploaded = 0
			for f in kwargs['files']:
				reader.append([f.filename, f.file.read()])
			  	filesUploaded += 1
			result = multifile.multifile(reader)
			
		except IOError:
			result = "</br>Error"
			pass
		return out %(result)
	
	#image detector page
	@cherrypy.expose
	def image(self):
		global image_names
		image_names = []
        	return """
            <html><head><title>Upload Images</title></head>
                        <style>
                    body {
                        color: red;
                    }

                    h2 {
                        color: green;
                    }
                    </style>
            <body>
            <h2>  IMAGE Plagiarism Detector </h2><p>Upload images to check for plagiarism!</br><b>Note: </b>Please wait while image is uploading before clicking "Submit" button.</p>
                <form action="uploadImage" method="post" enctype="multipart/form-data">
                    Image1: <input type="file" name="image"/> <br/>
                    <input type="submit"/>
                </form>
                <form action="uploadImage" method="post" enctype="multipart/form-data">
                    Image2: <input type="file" name="image"/> <br/>
                    <input type="submit"/>
                </form>
                <form action="process" method="post" enctype="multipart/form-data">
                    <button type="submit">Submit</button>
                </form>
                
            </body>
            </html>
            """
	

	#upload image to /tmp/ base folder
	@cherrypy.tools.noBodyProcess()
	@cherrypy.expose
	def uploadImage(self):
		supported_formats = [".JPG", ".jpg", ".png", ".tiff", ".bmp"]
		image = None
		cherrypy.response.timeout = 3600
		lcHDRS = {}
		for key, val in cherrypy.request.headers.iteritems():
		    lcHDRS[key.lower()] = val
		formFields = myFieldStorage(fp=cherrypy.request.rfile,
					    headers=lcHDRS,
					    environ={'REQUEST_METHOD':'POST'},
					    keep_blank_values=True)
		
		image = formFields['image']
		name, ext = os.path.splitext(image.filename)
		if (len(ext) < 1) or ext not in supported_formats:
			return "Upload correct format file..."
		if(len(image.filename) < 1):
			return "Empty upload"
		if(not os.path.exists('/tmp/'+image.filename)):
			os.link(image.file.name, '/tmp/'+image.filename)
		image_names.append(image.filename)
		return "File upload successful! Go back to continue..."
		
	#function: display results of image detector
	@cherrypy.expose
	def process(self):
		global image_names
		out = """<html><head><title>Detector Results!</title></head><body><h1>RESULT</h1> %s</body></html>"""
		result = multiimage.multiimage(image_names)
		image_names = []
		return out %(result)
	
if __name__ == '__main__':
    cherrypy.quickstart(PlagiarismDetector())



