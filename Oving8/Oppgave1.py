videoer = [
"http://www.youtube.com/watch?v=oKI-tD0L18A",
"http://www.youtube.com/watch?v=82LCKBdjywQ",
"http://www.youtube.com/watch?v=GpNSip5gyKo",
"http://www.youtube.com/watch?v=rHG-JO8gIGk",
"http://www.youtube.com/watch?v=ZFngtBIxRPk",
"http://www.youtube.com/watch?v=OZBWfyYtYQY"
]

def main():
	for link in return_shortlink(videoer):
		print (link)

def return_shortlink(long_link):
	short_link = []
	for i in range(len(long_link)):
		short_link.append("youtu.be/" + (videoer[i])[31:])
	return short_link

main ()