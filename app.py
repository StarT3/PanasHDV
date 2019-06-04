from flask import Flask
from flask import Response
from flask import Request
from flask import jsonify
from flask import request
import json
import requests

application = Flask(__name__)


@application.route('/')
def hello():
    return "Hello World!"

@application.route('/MakeCallJSON/', methods=['GET', 'POST'])
def hello_name0():    
	customHeaders = {}
	#content = request.json
	if request.method == 'POST':
		#print "POST"
		#print request
		#print "Request printed"
		data = request.json
		data2= json.dumps(data)
		#print (json.dumps(data))
		#print data ['comment']
		if data ['comment']=="":
			return "No phone ip address"
	#print request.json
	XML='<?xml version="1.0" encoding="utf-8"?> \n <ppxml xmlns="http://panasonic/sip_menu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://panasonic/sip_menu sip_menu.xsd">	\n	<Trigger version="2.0">\n <Source>http://192.168.20.111/{}.xml</Source> \n </Trigger> \n </ppxml>'.format("9"+data ['MakeCall'])
	#print XML
	PhoneUrl = "http://"+data ['comment'] +":6666/Request.cgi"
	#print PhoneUrl
	
	print requests.get("http://"+data ['comment'] +":6666/Request.cgi", headers={"content-type":"text/xml"}, data=XML).text
	return Response(XML, mimetype='text/xml')
	#return "200"

@application.route('/MakeCall=<number>')
def hello_name(number):    
	customHeaders = {}
	
	XML='<?xml version="1.0" encoding="utf-8"?> \n <ppxml xmlns="http://panasonic/sip_menu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://panasonic/sip_menu sip_menu.xsd">	\n	<Trigger version="2.0">\n <Source>http://192.168.20.111/{}.xml</Source> \n </Trigger> \n </ppxml>'.format(number)
	#print XML
	
	print requests.get('http://192.168.20.106:6666/Request.cgi', headers={"content-type":"text/xml"}, data=XML).text
	return Response(XML, mimetype='text/xml')
    
    
@application.route('/Call=<number>')
def hello_name4(number):
    customHeaders = {}
    XML='<?xml version="1.0" encoding="utf-8"?> <ppxml xmlns="http://panasonic/sip_screen" ',\
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://panasonic/sip_screen sip_screen.xsd"> ',\
        '<Screen version="2.0">',\
        '<Timer name="Timer1" repeat="false" interval="1">',\
        '<Events>',\
        '<OnExpired>',\
        '<MakeCall number="{}" />'.format(number),\
        '</OnExpired>',\
        '</Events>',\
        '</Timer>',\
        '</Screen>',\
        '</ppxml>'
    
    print requests.get('http://192.168.20.106:6666/Request.cgi', headers={"content-type":"text/xml"}, data=XML).text
    return Response(XML, mimetype='text/xml')


@application.route('/<number>.xml')
def hello_name2(number):
    XML='<?xml version="1.0" encoding="utf-8"?> <ppxml xmlns="http://panasonic/sip_screen" ',\
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://panasonic/sip_screen sip_screen.xsd"> ',\
        '<Screen version="2.0">',\
        '<Timer name="Timer1" repeat="false" interval="1">',\
        '<Events>',\
        '<OnExpired>',\
        '<MakeCall number="{}" />'.format(number),\
        '</OnExpired>',\
        '</Events>',\
        '</Timer>',\
        '</Screen>',\
        '</ppxml>'
    return Response(XML, mimetype='text/xml')
    

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=80)
