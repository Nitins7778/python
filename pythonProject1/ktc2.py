

# extracting concept or title of the page:

import re
from urllib.request import urlopen

url="https://knowthychoice.in/blog"
page=urlopen(url)
html=page.read().decode("utf-8")

pattern="<title.*?>.*?</title.*?>"
match_results=re.search(pattern,html,re.IGNORECASE)
title=match_results.group()
title=re.sub("<.*?>","",title)

print(title)


# for extracting domain name:

import tldextract

def extractDomain(url):
    if"https" in str(url) or "www" in str(url):
        parsed=tldextract.extract(url)
        parsed=".".join([i for i in parsed if i])
        return parsed
    else:return"NA"

op=open("out.txt",'w')
print(extractDomain("https://knowthychoice.in/blog"))


# for the links:
import requests

url="https://knowthychoice.in/blog"
resp=requests.get(url)
print(resp.status_code)
print(resp.text)


