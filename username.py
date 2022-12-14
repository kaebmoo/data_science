import re
  
# compiling the pattern for alphanumeric string
pat = re.compile(r"^[A-Za-z][A-Za-z0-9]*(?:_+[A-Za-z0-9]+)*$")
  
# Prompts the user for input string
test = input("Enter the string: ")
  
# Checks whether the whole string matches the re.pattern or not
if re.findall(pat, test) and (len(test) >= 4 and len(test) <= 25):
    print(f"'{test}' is True")
else:
    print(f"'{test}' is False")