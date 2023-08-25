import re
#for i in range(1,10):
#  file = 'ctr/ctr_00' + str(i) + '.html'
for i in range(10,51):
  file = 'ctr/ctr_0' + str(i) + '.html'
  with open(file) as fd:
    lines = fd.read().splitlines()
    title = ''
    cover_image = ''
    inquotesection = False
    quotelist = []
    inpsection = False
    plist = []
    inincludessection = False
    includeslist = []
    sample_page_image = ''
    for thisline in lines:
      if title == '':
        if thisline:
          thistitle = re.search(r"<title>\s*(.*?)\s*</title>",thisline)
          if thistitle:
            title = thistitle.group(1)
            continue
      if cover_image == '':
        if thisline:
          thiscover = re.search(r"<img[^>]*src=\"(.*?)\"",thisline)
          if thiscover:
            cover_image = thiscover.group(1)
            continue
      if quotelist == []:
        if inquotesection:
          if thisline:
            thisquote = re.search(r"(</I>)",thisline)
            if thisquote:
              quotesection = thisquote.group(1)
              inquotesection = False
              quotelist = temp_quotelist
              continue
            else:
              temp_quotelist.append(thisline)
        if not inquotesection:
          if thisline:
            thisquote = re.search(r"(<I>)",thisline)
            if thisquote:
              inquotesection = True
              temp_quotelist = []
              continue
      if plist == []:
        if inpsection:
          if thisline:
            thisp = re.search(r"(<P>)",thisline)
            if thisp:
              psection = thisp.group(1)
              inpsection = False
              plist = temp_plist
              continue
            else:
              temp_plist.append(thisline)
        if not inpsection:
          if thisline:
            thisp = re.search(r"(<P>)",thisline)
            if thisp:
              inpsection = True
              temp_plist = []
              continue
      if includeslist == []:
        if inincludessection:
          if thisline:
            thisincludes = re.search(r"(</UL>)",thisline)
            if thisincludes:
              includessection = thisincludes.group(1)
              inincludessection = False
              includeslist = temp_includeslist
              continue
            else:
              temp_includeslist.append(thisline)
        if not inincludessection:
          if thisline:
            thisincludessection = re.search(r"(<UL>)",thisline)
            if thisincludessection:
              inincludessection = True
              temp_includeslist = []
              continue
      if sample_page_image == '':
        if thisline:
          thissamp = re.search(r"<img[^>]*src=\"(.*?)\"",thisline)
          if thissamp:
            sample_page_image = thissamp.group(1)
            continue
  print("*************")
  print(title)
  print(cover_image)
  print(sample_page_image)
  print("*************")
  print(plist)
  print("*************")
  print(includeslist)
  print("*************")
  print(quotelist)
