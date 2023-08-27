import re
#for i in range(1,10):
#  file = 'ctr/ctr_00' + str(i) + '.html'

            #title = thistitle.group(1)
            
def check_line(regex):
    return

for i in range(10,51):
  regex_hash = {}

  thiskey = 'title'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<title>([^<]*)</title>",
    'end_regex' : None,
    'value' : None,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'cover_image'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<img[^>]*src=\"([^\"]*)\"",
    'end_regex' : None,
    'value' : None,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'quote_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<I>",
    'end_regex' : r"</I>",
    'value' : None,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'p_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<P>",
    'end_regex' : r"<P>",
    'value' : None,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'includes_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<UL>",
    'end_regex' : r"</UL>",
    'value' : None,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'sample_page_image'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<img[^>]*src=\"([^\"]*)\"",
    'end_regex' : None,
    'value' : None,
  }
  regex_hash[thiskey] = thishash

#for i in range(50,51):
  file = 'ctr/ctr_0' + str(i) + '.html'
  with open(file) as fd:
    lines = fd.read().splitlines()
    title = None
    cover_image = None
    inquotesection = False
    quotelist = None
    inpsection = False
    plist = None
    inincludessection = False
    includeslist = None
    sample_page_image = None
    for thisline in lines:
      if regex_hash['title']['value'] == None:
        if thisline:
          thisregex = regex_hash['title']['start_regex']
          thistitle = re.search(thisregex,thisline)
          if thistitle:
            #title = thisline
            regex_hash['title']['value'] = thisline
            continue
      if regex_hash['cover_image']['value'] == None:
        if thisline:
          thisregex = regex_hash['cover_image']['start_regex']
          thiscover = re.search(thisregex,thisline)
          if thiscover:
            #cover_image = thisline
            regex_hash['cover_image']['value'] = thisline
            continue
      if regex_hash['quote_list']['value'] == None:
        if inquotesection:
          if thisline:
            this_end_regex = regex_hash['quote_list']['end_regex']
            thisquote = re.search(this_end_regex,thisline)
            if thisquote:
              inquotesection = False
              regex_hash['quote_list']['value'] = temp_quotelist
              continue
            else:
              temp_quotelist.append(thisline)
        if not inquotesection:
          if thisline:
            this_start_regex = regex_hash['quote_list']['start_regex']
            thisquote = re.search(this_start_regex,thisline)
            if thisquote:
              inquotesection = True
              temp_quotelist = []
              continue
      if regex_hash['p_list']['value'] == None:
        if inpsection:
          if thisline:
            this_end_regex = regex_hash['p_list']['end_regex']
            thisp = re.search(this_end_regex,thisline)
            if thisp:
              inpsection = False
              #plist = temp_plist
              regex_hash['p_list']['value'] = temp_plist
              continue
            else:
              temp_plist.append(thisline)
        if not inpsection:
          if thisline:
            this_start_regex = regex_hash['p_list']['start_regex']
            thisp = re.search(this_start_regex,thisline)
            if thisp:
              inpsection = True
              temp_plist = []
              continue

      #if includeslist == None:
      if regex_hash['includes_list']['value'] == None:
        if inincludessection:
          if thisline:
            this_end_regex = regex_hash['includes_list']['end_regex']
            thisp = re.search(this_end_regex,thisline)
            thisincludes = re.search(this_end_regex,thisline)
            if thisincludes:
              inincludessection = False
              #includeslist = temp_includeslist
              regex_hash['includes_list']['value'] = temp_includeslist
              continue
            else:
              temp_includeslist.append(thisline)
        if not inincludessection:
          if thisline:
            this_start_regex = regex_hash['includes_list']['start_regex']
            thisincludessection = re.search(this_start_regex,thisline)
            if thisincludessection:
              inincludessection = True
              temp_includeslist = []
              continue
      if sample_page_image == None:
        if thisline:
          this_regex = regex_hash['sample_page_image']['start_regex']
          thissamp = re.search(this_regex,thisline)
          if thissamp:
            sample_page_image = thissamp.group(1)
            continue
  print("*************")
  #print(title)
  print(regex_hash['title']['value'])
  #print(cover_image)
  print(regex_hash['cover_image']['value'])
  print(sample_page_image)
  print("*************")
  #print(plist)
  print("PLIST!!!")
  print(regex_hash['p_list']['value'])
  print("*************")
  #print(includeslist)
  print(regex_hash['includes_list']['value'])
  print("*************")
  #print(quotelist)
  print(regex_hash['quote_list']['value'])
