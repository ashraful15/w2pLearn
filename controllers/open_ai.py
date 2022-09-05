# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
import urllib, json

def index(): 
    
    reqUrl = 'https://api.openai.com/v1/completions'
    bodyData = {
        "model": "text-davinci-002",
        "prompt": "the mango",
        "max_tokens": 200,
        "temperature": 0
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }
    method = 'POST'

    bodyData = json.dumps(bodyData)     # json
    bodyData = bodyData.encode('utf-8')   # bytes
        
    req = urllib.request.Request(reqUrl, bodyData, headers, method=method)   
    with urllib.request.urlopen(req) as res:
        response = json.load(res)        

        return str(response['choices'][0]['text'])
        

