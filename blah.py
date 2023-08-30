import re
from field_section import FieldSection

def init_field_hash():
  field_hash = {}

  thiskey = 'title'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<title>[^<]*</title>"
  thisfield.end_regex = None
  field_hash[thiskey] = thisfield

  thiskey = 'cover_image'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<img[^>]*src=\"[^\"]*\""
  thisfield.end_regex = None
  field_hash[thiskey] = thisfield

  thiskey = 'quote_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<I>"
  thisfield.end_regex = r"</I>"
  field_hash[thiskey] = thisfield

  thiskey = 'p_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<P>"
  thisfield.end_regex = r"<P>"
  thisfield.prerequisites = [field_hash['quote_list']]
  field_hash[thiskey] = thisfield

  thiskey = 'includes_list'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<UL>"
  thisfield.end_regex = r"</UL>"
  field_hash[thiskey] = thisfield

  thiskey = 'sample_page_image'
  thisfield = FieldSection(thiskey)
  thisfield.start_regex = r"<img[^>]*src=\"[^\"]*\""
  thisfield.end_regex = None
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
  for thisfield in field_list:
    print(thisfield.fieldname)
    print(thisfield.value)
    print("*************")
