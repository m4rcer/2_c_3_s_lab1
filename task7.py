links = ["www.google.com", "www.yandex.ru", "www.youtube"]

def checkWWW(link):
    if("www" == ''.join(link[0:3]).lower()):
        return True
    raise ValueError()

for link in links:
    checkWWW(link)

links = [("http://" + link) for link in links]

def addCom(link):
    if(".com" != ''.join(link[-4:].lower())):
        return link + ".com"
    return link

links = [(addCom(link)) for link in links]

print(links)
