	# importing the HTTP request handler and the server clases
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
	# importing cgi for sending message to the server (common gateway interface)
import cgi

	# definition of webserverHandler class
class webserverHandler(BaseHTTPRequestHandler):
		# definition of do_GET()
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><a href = '/hola' >Spanish<br></a>Hello!</br>"
				output += '''<form method='POST' enctype='multipart/form-data'
					action='/hello'><h2>What would you like me to say?</h2>
					<input name='message' type='text'><input type='submit'
			 		value='Submit'> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><a href = '/hello' >English<br></a>&#161Hola</br>"
				output += '''<form method='POST' enctype='multipart/form-data'
					action='/hello'><h2>What would you like me to say?</h2>
					<input name='message' type='text'><input type='submit'
			 		value='Submit'> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return
		except IOError:
				self.send_error(404, "File Not Found %s" % self.path)
		# definition of do_POST()
	def do_POST(self):
		try:
			self.send_response(301)
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')

			output = ""
			output += "<html><body>"
			output += "<h2> Okay, how about this: </h2>"
			output += "<h1> %s </h1>" % messagecontent[0]

			output += '''<form method='POST' enctype='multipart/form-data'
				action='/hello'><h2>What would you like me to say?</h2>
				<input name='message' type='text'><input type='submit'
			 	value='Submit'> </form>'''
			output += "</body></html>"
			self.wfile.write(output)
			print output

		except:
			pass


	# definition of main()
def main():
	try: 
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server"
		server.socket.close()

	# calling main
if __name__ == '__main__':
	main()
