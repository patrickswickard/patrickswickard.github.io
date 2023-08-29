import re
#for i in range(1,10):
#  file = 'ctr/ctr_00' + str(i) + '.html'

            #title = thistitle.group(1)
            
def check_line(regex):
    return

def blarf(thisfield):
  if regex_hash[thisfield]['end_regex'] == None:
    if regex_hash[thisfield]['value'] == None:
      thisregex = regex_hash[thisfield]['start_regex']
      if re.search(thisregex,thisline):
        regex_hash[thisfield]['in_section'] = True
        regex_hash[thisfield]['temp_list'] = []
        regex_hash[thisfield]['temp_list'].append(thisline)
        regex_hash[thisfield]['in_section'] = False
        regex_hash[thisfield]['value'] = regex_hash[thisfield]['temp_list']
        return True
  else:
    if regex_hash[thisfield]['value'] == None:
      if regex_hash[thisfield]['in_section']:
        this_end_regex = regex_hash[thisfield]['end_regex']
        thisquote = re.search(this_end_regex,thisline)
        if thisquote:
          regex_hash[thisfield]['in_section'] = False
          regex_hash[thisfield]['value'] = regex_hash[thisfield]['temp_list']
          return True
        else:
          regex_hash[thisfield]['temp_list'].append(thisline)
          return True
      if not regex_hash[thisfield]['in_section']:
        this_start_regex = regex_hash[thisfield]['start_regex']
        thisquote = re.search(this_start_regex,thisline)
        if thisquote:
          regex_hash[thisfield]['in_section'] = True
          regex_hash[thisfield]['temp_list'] = []
          return True
  return False

for i in range(10,51):
  regex_hash = {}

  thiskey = 'title'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<title>([^<]*)</title>",
    'end_regex' : None,
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
  }
  regex_hash[thiskey] = thishash

  thiskey = 'cover_image'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<img[^>]*src=\"([^\"]*)\"",
    'end_regex' : None,
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
  }
  regex_hash[thiskey] = thishash

  thiskey = 'quote_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<I>",
    'end_regex' : r"</I>",
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
  }
  regex_hash[thiskey] = thishash

  thiskey = 'p_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<P>",
    'end_regex' : r"<P>",
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
  }
  regex_hash[thiskey] = thishash

  thiskey = 'includes_list'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<UL>",
    'end_regex' : r"</UL>",
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
  }
  regex_hash[thiskey] = thishash

  thiskey = 'sample_page_image'
  thisvalue = ''
  thishash = {
    'start_regex' : r"<img[^>]*src=\"([^\"]*)\"",
    'end_regex' : None,
    'value' : None,
    'in_section' : False,
    'temp_list' : [],
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
      should_i_continue = blarf(thisfield)
      if should_i_continue:
        continue
      thisfield = 'cover_image'
      should_i_continue = blarf(thisfield)
      if should_i_continue:
        continue
      thisfield = 'quote_list'
      should_i_continue = blarf(thisfield)
      if should_i_continue:
        continue
      thisfield = 'p_list'
      previousfield = 'quote_list'
      if not regex_hash[previousfield]['value'] == None:
        should_i_continue = blarf(thisfield)
        if should_i_continue:
          continue
      thisfield = 'includes_list'
      should_i_continue = blarf(thisfield)
      if should_i_continue:
        continue
      thisfield = 'sample_page_image'
      should_i_continue = blarf(thisfield)
      if should_i_continue:
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
