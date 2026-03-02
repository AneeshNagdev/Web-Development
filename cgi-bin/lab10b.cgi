#!/usr/bin/ruby -wT
require 'cgi'

cgi = CGI.new

city    = cgi['city']
country = cgi['country']
image   = cgi['image']
color   = cgi['color']

print "Content-type: text/html\n\n"

print "<!DOCTYPE html>"
print "<html lang='en'>"
print "<head>"
print "<title>City Display</title>"
print "<link href='https://fonts.googleapis.com/css2?family=Roboto&family=Merriweather&display=swap' rel='stylesheet'>"
print "</head>"
print "<body>"

print "<div style='font-size:3em; text-align:center; color:#{color}; font-family:Roboto;'>"
print "#{city}, #{country}"
print "</div>"

print "<div style='text-align:center; margin-top:20px;'>"
print "<img src='#{image}' style='width:80%; border:12px solid #{color};'>"
print "</div>"

print "</body></html>"
