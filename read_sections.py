import re
import json
from field_section import FieldSection

json_file = open('all_sections.json', 'r')
json_hash = json.load(json_file)
json_file.close()


for i in range(1,51):
  if i <= 9:
    filename = 'ctr2/ctr_00' + str(i) + '.html'
  else:
    filename = 'ctr2/ctr_0' + str(i) + '.html'
  this_page_data = json_hash[str(i)]
  title = this_page_data['title']
  cover_image = this_page_data['cover_image']
  quote_list = this_page_data['quote_list']
  output_file = open(filename, 'w')
  html_contents = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="mystyle.css">
</head>
<body>
<title>"""
  html_contents += title
  html_contents += "</title>\n"
  html_contents += "<H1>"
  html_contents += title
  html_contents += "</H1>\n"
  html_contents += "<P>\n"
  html_contents += "<img style=\"max-width:100%;height:auto;\" src=\"" + cover_image + "\">\n"
  html_contents += "<P>\n"
  html_contents += "<I>\n"
  for thisline in quote_list:
    html_contents += thisline
    html_contents += "<BR>\n"
  html_contents += "</I>\n"
  output_file.write(html_contents)
  output_file.close()
