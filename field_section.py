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

  def check_and_process_field(self,thisline):
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
          self.value = self.temp_list
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
