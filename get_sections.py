import re
from field_section import FieldSection

def init_field_hash():
  field_hash = {}

  thiskey = 'title'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<title>[^<]*</title>"
  thisfield.end_regex = None
  thisfield.inner_regex = r"<title>\s*(.*)\s*</title>"
  field_hash[thiskey] = thisfield

  thiskey = 'cover_image'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<img[^>]*src=\"[^\"]*\""
  thisfield.end_regex = None
  thisfield.inner_regex = r"<img[^>]*src=\"(.*)\""
  field_hash[thiskey] = thisfield

  thiskey = 'quote_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<I>"
  thisfield.end_regex = r"</I>"
  thisfield.inner_regex = None
  field_hash[thiskey] = thisfield

  thiskey = 'p_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<P>"
  thisfield.end_regex = r"<P>"
  thisfield.inner_regex = None
  thisfield.prerequisites = [field_hash['quote_list']]
  field_hash[thiskey] = thisfield

  thiskey = 'includes_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<UL>"
  thisfield.end_regex = r"</UL>"
  thisfield.inner_regex = None
  field_hash[thiskey] = thisfield

  thiskey = 'sample_page_image'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<img[^>]*src=\"[^\"]*\""
  thisfield.end_regex = None
  thisfield.inner_regex = r"<img[^>]*src=\"(.*)\""
  field_hash[thiskey] = thisfield

  return field_hash

def init_field_list():
  field_hash = init_field_hash()
  fieldname_list = [
    'title',
    'cover_image',
    'quote_list',
    'p_list',
    'includes_list',
    'sample_page_image',
  ]
  field_list = []
  for fieldname in fieldname_list:
    field_list.append(field_hash[fieldname])
  return field_list

for i in range(1,51):
  if i <= 9:
    file = 'ctr/ctr_00' + str(i) + '.html'
  else:
    file = 'ctr/ctr_0' + str(i) + '.html'

  field_list = init_field_list()

  with open(file) as fd:
    lines = fd.read().splitlines()
    for thisline in lines:
      for thisfield in field_list:
        # true means we skip checking rest of lines for this field
        # false means we keep going
        should_i_skip_rest_of_fields_for_this_line = thisfield.check_and_process_field(thisline)
        if should_i_skip_rest_of_fields_for_this_line:
          break
      if should_i_skip_rest_of_fields_for_this_line:
        continue
  print("*************")
#  for thisfield in field_list:
#    print(thisfield.fieldname)
#    print(thisfield.value)
#    if thisfield.inner_regex:
#      print('Trying to grab the rest')
#      textblob = ' '.join(thisfield.value)
#      inner_value = re.search(thisfield.inner_regex,textblob)
#      if inner_value:
#        print("inner value: " + inner_value.group(1))
#    print("*************")


# Back to being messy...
# TODO p_list is hard to parse because links mixed in with non-links and not necessarily consistent for these pages at least.
  field_hash = {}
  for thisfield in field_list:
    field_hash[thisfield.fieldname] = thisfield
  title_lines = field_hash['title'].value
  title_blob = ' '.join(title_lines)
  title_regex = r"<title>\s*(.*)\s*</title>"
  value = re.search(title_regex,title_blob).group(1)
  print(value)
  cover_image_lines = field_hash['cover_image'].value
  cover_image_blob = ' '.join(cover_image_lines)
  cover_image_regex = r"<img[^>]*src=\"(.*)\""
  value = re.search(cover_image_regex,cover_image_blob).group(1)
  print(value)
  quote_list_lines = field_hash['quote_list'].value
  value = []
  for thisline in quote_list_lines:
    linevalue_regex = r"^(.*?)\s*(?:<BR>\s*)?$"
    linevalue = re.search(linevalue_regex,thisline).group(1)
    value.append(linevalue)
  print(value)
  p_list_lines = field_hash['p_list'].value
  p_list_blob = ' '.join(p_list_lines)
  value = []
  justlinks = re.findall(r"<a href=[^\"]*\"[^\"]*\"[^>]*>[^<]*</a>",p_list_blob,re.IGNORECASE)
  for thislink in justlinks:
    linevalue_regex = r"<(?:a|A)[^>]*(?:href|HREF)=\"(.*?)\"[^>]*>\s*(.*)\s*</(?:a|A)>"
    linevalue = [re.search(linevalue_regex,thislink,re.IGNORECASE).group(1),re.search(linevalue_regex,thislink,re.IGNORECASE).group(2)]
    #linevalue = [[re.search(linevalue_regex,thislink,re.IGNORECASE).group(1)]]
    value.append(linevalue)
  print(value)
  #print(p_list_blob)
  includes_list_lines = field_hash['includes_list'].value
  includes_list_blob = ' '.join(includes_list_lines)
  value = []
  for thisline in includes_list_lines:
    linevalue_regex = r"^\s*<LI>\s*<A[^>]*HREF=\"(.*?)\"[^>]*>\s*(.*)\s*</A>\s*$"
    linevalue = [re.search(linevalue_regex,thisline).group(1),re.search(linevalue_regex,thisline).group(2)]
    value.append(linevalue)
  print(value)
  sample_page_image_lines = field_hash['sample_page_image'].value
  sample_page_image_blob = ' '.join(sample_page_image_lines)
  sample_page_image_regex = r"<img[^>]*src=\"(.*)\""
  value = re.search(sample_page_image_regex,sample_page_image_blob).group(1)
  print(value)