from urllib.request import urlopen

textpage = urlopen("https://github.com/udanic19344/SHAPEAI---Project/blob/main/weather.py")

print(str(textpage.read(),'utf8'))

