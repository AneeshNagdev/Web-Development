#!/usr/bin/python
import cgi

print "Content-type:text/html\n\n"

form = cgi.FieldStorage()
city = form.getvalue("city", "")
country = form.getvalue("country", "")
image = form.getvalue("image", "")
color = form.getvalue("color", "#000")

print "<!DOCTYPE html>"
print "<html lang='en'>"
print "<head>"
print "<title>City Display</title>"
print "<link href='https://fonts.googleapis.com/css2?family=Roboto&family=Merriweather&display=swap' rel='stylesheet'>"
print "</head>"
print "<body>"

print "<div style='font-size:3em; text-align:center; color:%s; font-family:Roboto;'>" % color
print city + ", " + country
print "</div>"

print "<div style='text-align:center; margin-top:20px;'>"
print "<img src='%s' style='width:80%%; border:12px solid %s;'>" % (image, color)
print "</div>"

print "</body></html>"