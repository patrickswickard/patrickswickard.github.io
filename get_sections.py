import re
import json
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

def get_field_hash():
  field_hash = {}
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
#    print("*************")
    field_hash[i] = {}
    for thisfield in field_list:
      field_hash[i][thisfield.fieldname] = thisfield
  return field_hash



# Back to being messy...
# TODO p_list is hard to parse because links mixed in with non-links and not necessarily consistent for these pages at least.
def do_stuff_with_field_hash(field_hash):
  field_value_hash = {}
  fieldname_list = [
    'title',
    'cover_image',
    'quote_list',
    'p_list',
    'includes_list',
    'sample_page_image',
  ]
  for i in range(1,51):
    for this_fieldname in fieldname_list:
      if this_fieldname == 'title':
        field_value_hash[i] = {}
        thisfield_lines = field_hash[i][this_fieldname].value
        thisfield_blob = ' '.join(thisfield_lines)
        thisfield_regex = r"<title>\s*(.*)\s*</title>"
        this_value = re.search(thisfield_regex,thisfield_blob).group(1)
        final_title = this_value
        field_value_hash[i][this_fieldname] = final_title
      #######################
      if this_fieldname == 'cover_image':
        thisfield_lines = field_hash[i][this_fieldname].value
        thisfield_blob = ' '.join(thisfield_lines)
        thisfield_regex = r"<img[^>]*src=\"(.*)\""
        this_value = re.search(thisfield_regex,thisfield_blob).group(1)
        final_cover_image = this_value
        field_value_hash[i][this_fieldname] = final_cover_image
      #######################
      if this_fieldname == 'quote_list':
        thisfield_lines = field_hash[i][this_fieldname].value
        this_value = []
        for thisline in thisfield_lines:
          linevalue_regex = r"^(.*?)\s*(?:<BR>\s*)?$"
          linevalue = re.search(linevalue_regex,thisline).group(1)
          this_value.append(linevalue)
        final_quote_list = this_value
        field_value_hash[i]['quote_list'] = final_quote_list
      #######################
      if this_fieldname == 'p_list':
        thisfield_lines = field_hash[i][this_fieldname].value
        thisfield_blob = ' '.join(thisfield_lines)
        this_value = []
        justlinks = re.findall(r"<a href=[^\"]*\"[^\"]*\"[^>]*>[^<]*</a>",thisfield_blob,re.IGNORECASE)
        for thislink in justlinks:
          linevalue_regex = r"<(?:a|A)[^>]*(?:href|HREF)=\"(.*?)\"[^>]*>\s*(.*)\s*</(?:a|A)>"
          thisurl = re.search(linevalue_regex,thislink,re.IGNORECASE).group(1)
          thistext = re.search(linevalue_regex,thislink,re.IGNORECASE).group(2)
          thishash = {
            'url' : thisurl,
            'text' : thistext,
          }
          linevalue = thishash
          this_value.append(linevalue)
        final_p_list = this_value
        field_value_hash[i][this_fieldname] = final_p_list
    #######################
      if this_fieldname == 'includes_list':
        thisfield_lines = field_hash[i][this_fieldname].value
        thisfield_blob = ' '.join(thisfield_lines)
        this_value = []
        for thisline in thisfield_lines:
          linevalue_regex = r"^\s*<LI>\s*<A[^>]*HREF=\"(.*?)\"[^>]*>\s*(.*)\s*</A>\s*$"
          thisurl = re.search(linevalue_regex,thisline,re.IGNORECASE).group(1)
          thistext = re.search(linevalue_regex,thisline,re.IGNORECASE).group(2)
          thishash = {
            'url' : thisurl,
            'text' : thistext,
          }
          linevalue = thishash
          this_value.append(linevalue)
        final_includes_list = this_value
        field_value_hash[i][this_fieldname] = final_includes_list
    #######################
      if this_fieldname == 'sample_page_image':
        thisfield_lines = field_hash[i][this_fieldname].value
        thisfield_blob = ' '.join(thisfield_lines)
        thisfield_regex = r"<img[^>]*src=\"(.*)\""
        this_value = re.search(thisfield_regex,thisfield_blob).group(1)
        final_sample_page = this_value
        field_value_hash[i][this_fieldname] = final_sample_page
  return field_value_hash

field_hash = get_field_hash()
field_value_hash = do_stuff_with_field_hash(field_hash)
print(json.dumps(field_value_hash))
