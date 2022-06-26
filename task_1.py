

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("") == ""
assert domain_name("https://foobar.co.uk") == "foobar"
assert domain_name("https://facebook.com?") == "facebook"
assert domain_name("https://com.com.com") == "com"
assert domain_name("https://shopping.online") == "shopping"
assert domain_name("www.something.net/index.com") == "something"
