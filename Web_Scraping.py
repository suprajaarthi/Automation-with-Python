import newspaper 
url="http://www.supraja.me/"
u=newspaper.Article(url="%s" % (url),language='en')
u.download()
u.parse()
print(u.text);
print(u.title)
