import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search('http://www.youtube.com/videos/asd/das/ads') 

print(f'Protocol: {match.group(1)}')
print(f'Domain: {match.group(2)}')
print(f'Path: {match.group(3)}')
