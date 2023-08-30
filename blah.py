import re

class FieldSection:
  def __init__(self,fieldname):
    self.fieldname = fieldname
    self.start_regex = None
    self.end_regex = None
    self.value = None
    self.in_section = False
    self.temp_list = []
    self.prerequisites = []

  def check_and_process_field(self):
    # if we already found this field then we are NOT done
    # and we should check other fields
    if not self.value == None:
      return False
    # if prerequisites for this field are not met we should
    # check other fields that might match this line
    for prereq in self.prerequisites:
      if prereq.value == None:
        return False
    # we may only have one start_regex, i.e. a one-liner
    # if this matches this field we're done, otherwise we carry on
    if self.end_regex == None:
      if re.search(self.start_regex,thisline):
        self.in_section = True
        self.temp_list = []
        self.temp_list.append(thisline)
        self.in_section = False
        self.value = self.temp_list
        return True
    else:
      # if we have a start and end regex then we have to care
      # whether we are "in" the section and act accordingly
      # if we're inside the section then no reason to check other sections
      # so when done doing our "stuff" return true
      if self.in_section:
        if re.search(self.end_regex,thisline):
          self.in_section = False
          self.value = thisfield.temp_list
        else:
          self.temp_list.append(thisline)
        return True
      # if we're not in the section then we check to see
      # if we enter it and if we do then we don't care about
      # other fields so return true
      if re.search(self.start_regex,thisline):
        self.in_section = True
        self.temp_list = []
        return True
    # at this point nothing matched so keep trying other fields
    return False

for i in range(1,51):
  if i <= 9:
    file = 'ctr/ctr_00' + str(i) + '.html'
  else:
    file = 'ctr/ctr_0' + str(i) + '.html'
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
  with open(file) as fd:
    lines = fd.read().splitlines()
    for thisfield in field_list:
      thisfield.in_section = False
    for thisline in lines:
      for thisfield in field_list:
        # true means we skip checking rest of lines for this field
        # false means we keep going
        should_i_skip_rest_of_fields_for_this_line = thisfield.check_and_process_field()
        if should_i_skip_rest_of_fields_for_this_line:
          break
      if should_i_skip_rest_of_fields_for_this_line:
        continue
  print("*************")
  print(field_hash['title'].value)
  print(field_hash['cover_image'].value)
  print(field_hash['sample_page_image'].value)
  print("*************")
  print("PLIST!!!")
  print(field_hash['p_list'].value)
  print("*************")
  print(field_hash['includes_list'].value)
  print("*************")
  print(field_hash['quote_list'].value)
