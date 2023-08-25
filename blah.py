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
    #quotesection = ''
    #psection = ''
    inpsection = False
    plist = []
    #includes_section = ''
    inincludessection = False
    includeslist = []
    sample_page_image = ''
    for thisline in lines:
      #print(thisline)
      if title == '':
        print("no title yet\n")
        if thisline:
          thistitle = re.search(r"<title>\s*(.*?)\s*</title>",thisline)
          if thistitle:
            title = thistitle.group(1)
            print("found title\n")
            print(title)
            print("\n")
            continue
      if cover_image == '':
        print("no cover image yet\n")
        if thisline:
          thiscover = re.search(r"<img[^>]*src=\"(.*?)\"",thisline)
          if thiscover:
            cover_image = thiscover.group(1)
            print("found cover_image\n")
            print(cover_image)
            print("\n")
            continue
      if quotelist == []:
        if inquotesection:
          print("now in quote section\n")
          if thisline:
            thisquote = re.search(r"(</I>)",thisline)
            if thisquote:
              quotesection = thisquote.group(1)
              print("exiting quote section\n")
              inquotesection = False
              print("\n")
              quotelist = temp_quotelist
              continue
            else:
              temp_quotelist.append(thisline)
        if not inquotesection:
          print("no quote section yet\n")
          if thisline:
            thisquote = re.search(r"(<I>)",thisline)
            if thisquote:
              print("found quote section\n")
              inquotesection = True
              temp_quotelist = []
              print("\n")
              continue
      if plist == []:
        if inpsection:
          print("now in psection\n")
          if thisline:
            thisp = re.search(r"(<P>)",thisline)
            if thisp:
              psection = thisp.group(1)
              print("exiting psection\n")
              inpsection = False
              print("\n")
              plist = temp_plist
              continue
            else:
              temp_plist.append(thisline)
        if not inpsection:
          print("no psection yet\n")
          if thisline:
            thisp = re.search(r"(<P>)",thisline)
            if thisp:
              print("found psection\n")
              inpsection = True
              temp_plist = []
              print("\n")
              continue
      if includeslist == []:
        if inincludessection:
          print("now in includessection\n")
          if thisline:
            thisincludes = re.search(r"(</UL>)",thisline)
            if thisincludes:
              includessection = thisincludes.group(1)
              print("exiting includessection\n")
              inincludessection = False
              print("\n")
              includeslist = temp_includeslist
              continue
            else:
              temp_includeslist.append(thisline)
        if not inincludessection:
          print("no includes section yet\n")
          if thisline:
            thisincludessection = re.search(r"(<UL>)",thisline)
            if thisincludessection:
              print("found includessection\n")
              inincludessection = True
              temp_includeslist = []
              print("\n")
              continue
      if sample_page_image == '':
        print("no sample page image yet\n")
        if thisline:
          thissamp = re.search(r"<img[^>]*src=\"(.*?)\"",thisline)
          if thissamp:
            sample_page_image = thissamp.group(1)
            print("found sample page image\n")
            print(sample_page_image)
            print("\n")
            continue
      print(thisline)
      print("****************\n")
  print(title)
  print(cover_image)
  print(sample_page_image)
  print("*************")
  print(plist)
  print("*************")
  print(includeslist)
  print("*************")
  print(quotelist)
