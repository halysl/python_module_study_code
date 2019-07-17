import re

pattern = re.compile(r'(\d+) google (\d+)')

result1 = pattern.search('runoob 123 google 456').group(2)
result2 = pattern.findall('run88oob123google456', 0, 100)

print(result1)
print(result2)
