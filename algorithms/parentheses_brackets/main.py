def is_valid(string):
    string_set = {'(': 1, ')': 2, '[': 3,
                  ']':4,   '{': 5,  '}': 6}

    strings_before = list()
    for s in string:
      string_num = string_set[s]
      if (string_num - 1) not in strings_before:
        strings_before.append(string_num) 
      else:
        if strings_before[-1] != string_num -1:
          return False
        strings_before.remove(string_num - 1)      
    if not strings_before:
      return True
    return False
