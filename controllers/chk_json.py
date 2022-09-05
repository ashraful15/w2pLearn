
def json_post():
    import requests

    url = 'http://127.0.0.1:8000/test/chk_json/json_post'
    myobj = {'somekey': 'somevalue'}

    x = requests.post(url, json = myobj)

    return x.text













def chk():
    import urllib
    page = urllib.urlopen('http://universities.hipolabs.com/search?country=United+States').read()

    return page

def chk1():
    import json
    from gluon.tools import fetch
    page = fetch('http://universities.hipolabs.com/search?country=United+States')

    
    return json.dumps(page)




