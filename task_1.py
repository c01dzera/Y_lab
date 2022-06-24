import re


def domain_name(url):
    patter = r'\W(\w+?)\W'
    return re.search(patter, url)[1]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"





