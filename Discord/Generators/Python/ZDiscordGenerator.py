# -*- coding: utf-8 -*-

import base64, os, random, string
from itertools import cycle
from random import randint

print(u"\u001b[31m██████╗ ██╗     ██╗  ██╗██╗  ██╗██████╗ ███████╗██████╗ \n██╔══██╗██║     ╚██╗██╔╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗\n██████╔╝██║      ╚███╔╝  ╚███╔╝ ██║  ██║█████╗  ██║  ██║\n██╔══██╗██║      ██╔██╗  ██╔██╗ ██║  ██║██╔══╝  ██║  ██║\n██████╔╝███████╗██╔╝ ██╗██╔╝ ██╗██████╔╝███████╗██████╔╝\n╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═════╝ \u001b[0m")
N = input(u"\n\u001b[36m[ZDiscordGenerator] » How many tokens you want to generate? \u001b[0m")

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

while(int(count) < int(N)):
	tokens = []
	base64_string = "=="
	while(base64_string.find("==") != -1):
		sample_string = str(randint(000000000000000000, 999999999999999999))
		sample_string_bytes = sample_string.encode("ascii")
		base64_bytes = base64.b64encode(sample_string_bytes)
		base64_string = base64_bytes.decode("ascii")
	else:
		token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
		for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		count += 1
		tokens.append(token)
	for token in tokens:
		f = open(current_path+"/"+"tokens.txt", "a")
		f.write(token+"\n")
	tokens.remove(token)
print(f"\u001b[36m[ZDiscordGenerator] » Saved {count} tokens in tokens.txt. \u001b[0m")
