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
    'in_section' : False,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'p_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<P>",
    'end_regex' : r"<P>",
    'value' : None,
    'in_section' : False,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'includes_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<UL>",
    'end_regex' : r"</UL>",
    'value' : None,
    'in_section' : False,
  }
  regex_hash[thiskey] = thishash

  thiskey = 'sample_page_image'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<img[^>]*src=\"([^\"]*)\"",
    'end_regex' : None,
    'value' : None,
    'in_section' : False,
  }
  regex_hash[thiskey] = thishash

#for i in range(50,51):
  file = 'ctr/ctr_0' + str(i) + '.html'
  with open(file) as fd:
    lines = fd.read().splitlines()
    regex_hash['quote_list']['in_section'] = False
    regex_hash['p_list']['in_section'] = False
    inpsection = False
    regex_hash['includes_list']['in_section'] = False
    for thisline in lines:
      thisfield = 'title'
      if regex_hash[thisfield]['value'] == None:
        thisregex = regex_hash[thisfield]['start_regex']
        if re.search(thisregex,thisline):
          regex_hash[thisfield]['value'] = thisline
          continue
      thisfield = 'cover_image'
      if regex_hash[thisfield]['value'] == None:
        thisregex = regex_hash[thisfield]['start_regex']
        if re.search(thisregex,thisline):
          regex_hash[thisfield]['value'] = thisline
          continue
      thisfield = 'quote_list'
      if regex_hash[thisfield]['value'] == None:
        if regex_hash[thisfield]['in_section']:
          this_end_regex = regex_hash[thisfield]['end_regex']
          thisquote = re.search(this_end_regex,thisline)
          if thisquote:
            regex_hash[thisfield]['in_section'] = False
            regex_hash[thisfield]['value'] = temp_quotelist
            continue
          else:
            temp_quotelist.append(thisline)
        if not regex_hash[thisfield]['in_section']:
          this_start_regex = regex_hash[thisfield]['start_regex']
          thisquote = re.search(this_start_regex,thisline)
          if thisquote:
            regex_hash[thisfield]['in_section'] = True
            temp_quotelist = []
            continue
      thisfield = 'p_list'
      previousfield = 'quote_list'
      if regex_hash[thisfield]['value'] == None and not regex_hash[previousfield]['value'] == None:
        if regex_hash[thisfield]['in_section']:
          this_end_regex = regex_hash[thisfield]['end_regex']
          thisp = re.search(this_end_regex,thisline)
          if thisp:
            regex_hash[thisfield]['in_section'] = False
            regex_hash[thisfield]['value'] = temp_plist
            continue
          else:
            temp_plist.append(thisline)
        if not regex_hash[thisfield]['in_section']:
          this_start_regex = regex_hash[thisfield]['start_regex']
          thisp = re.search(this_start_regex,thisline)
          if thisp:
            regex_hash[thisfield]['in_section'] = True
            temp_plist = []
            continue
      thisfield = 'includes_list'
      if regex_hash[thisfield]['value'] == None:
        if regex_hash[thisfield]['in_section']:
          this_end_regex = regex_hash[thisfield]['end_regex']
          thisp = re.search(this_end_regex,thisline)
          thisincludes = re.search(this_end_regex,thisline)
          if thisincludes:
            regex_hash[thisfield]['in_section'] = False
            regex_hash[thisfield]['value'] = temp_includeslist
            continue
          else:
            temp_includeslist.append(thisline)
        if not regex_hash['includes_list']['in_section']:
          this_start_regex = regex_hash[thisfield]['start_regex']
          thisincludessection = re.search(this_start_regex,thisline)
          if thisincludessection:
            regex_hash[thisfield]['in_section'] = True
            temp_includeslist = []
            continue
      thisfield = 'sample_page_image'
      if regex_hash[thisfield]['value'] == None:
        this_regex = regex_hash[thisfield]['start_regex']
        if re.search(this_regex,thisline):
          regex_hash[thisfield]['value'] = thisline
          continue
  print("*************")
  print(regex_hash['title']['value'])
  print(regex_hash['cover_image']['value'])
  print(regex_hash['sample_page_image']['value'])
  print("*************")
  print("PLIST!!!")
  print(regex_hash['p_list']['value'])
  print("*************")
  print(regex_hash['includes_list']['value'])
  print("*************")
  print(regex_hash['quote_list']['value'])
