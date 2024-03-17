import re 

email = "john@google.com elise@123456.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern, email)
print(ans)