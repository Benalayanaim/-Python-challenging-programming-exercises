email = "john@google.com"
email = email.split('@')
print(email[0])



#Another solution 

import re

email = "john@google.com elise@python.com"
pattern = "(\w+)@\w+.com"
ans = re.findall(pattern,email)
print(ans)