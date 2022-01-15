
def to_camel_case(string):
  string = string.replace('_', ' ')
  string = string.title()
  string = string.replace(' ', '')
  return string
                            
print(to_camel_case("my_function_name"))
print(to_camel_case("i_phone"))
print(to_camel_case("this_function_is_empty"))
print(to_camel_case("name"))