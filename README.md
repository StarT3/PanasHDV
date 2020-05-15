# PanasHDV
Simple Panasonic KX-HDV remote control server (uses XML)
Web server that receives JSON data "comment" (phone ip address), "MakeCall" (Called number) and initiates call from IP Phone Panasonic KX-HDV100/130.
XML Applications should be enabled on phone, no password set. In my case phones are in different non routed subnet, so i created new VM with access to both networks - LAN and phone subnet. 
More info on 
https://www.blog.itdoca.com/panasonickxhdvmanagexml/
https://www.blog.itdoca.com/kxdhvand1c/

Process:
- Something sends POST request with json to our web server. It could be browser, REST Client, in my case - ERP system 1C.
- Web server sends GET with XML to phone. XML contains URL with commands to phone. (So called PUSH system in Panasonic documentation)
- Phone gets XML in wich we pass call command and called number, and after 1 sec timeout it calls. (couldn't do it without timer)
- Phone sends status to our web server (200 - ok if XML was fine)
- Web server sends answer to Something (REST client, browser, ERP)

Here is a sample XML wich web server sends to Phone

```xml
<?xml version="1.0" encoding="utf-8"?>
<ppxml xmlns="http://panasonic/sip_menu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://panasonic/sip_menu sip_menu.xsd">
	<Trigger version="2.0">
		<Source>http://192.168.20.111/989101234567.xml</Source> 
	</Trigger> 
</ppxml>
```
Where http://192.168.20.111/989101234567.xml is web server address and number to call.

Phone GETs XML from web server:
```xml
<?xml version="1.0" encoding="utf-8"?> 
<ppxml xmlns="http://panasonic/sip_screen" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://panasonic/sip_screen sip_screen.xsd"> 
	<Screen version="2.0">
		<Timer name="Timer1" repeat="false" interval="1">
			<Events>
				<OnExpired>
					<MakeCall number="989101234567" />
				</OnExpired>
			</Events>
		</Timer>
	</Screen>
</ppxml>
```
To use, just run python app.py and send POST to http://YourWebServer/MakeCallJSON/ with json
```json
{
	"comment": "192.168.20.106",
	"MakeCall": "989101234567"
}
```
or simply browse to http://YourWebServer/MakeCall=<number> , it would initiate call to ip address hardcoded to script.
Please be carefull, there is a security concern, because anyone could make call anywhere with access to server.
