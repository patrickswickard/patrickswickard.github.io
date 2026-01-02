"""Demonstrate regex replace by line"""
import re

file = 'all_playlists.txt'
with open(file,'r',encoding='utf-8') as myinfile:
  lines = myinfile.read().splitlines()

# find and report
for thisline in lines:
  branch = re.search(r"playlist_(\S+)\.html",thisline)
  if branch:
    #print(branch.group(1))
    thisdate = branch.group(1)
    print("<LI>" + "<a href=\"" + thisdate + "\">" + thisdate + "</a>" + "</LI>")


## find and report
#for thisline in lines:
#  newline = re.sub(r"\W","",thisline)
#  print(newline)

