import requests
import json
import html

def createMessagesListFromResponse(response):
  
  messagelist = []
  for message in response['messages']:
    try: 
      messagelist.append(json.dumps({"type": message['type'], "line": message['lastLine'], "message": message['message'] }))
    except Exception as e:
        print(response, 'RESPONSE')
  print(messagelist)
  return messagelist

params = {
'doc': 'https://co22debeautify.org/html-escape-unescape', #Target URL to be tested
'out': 'json' 
}
try:
    r = requests.get(
    "https://validator.w3.org/nu/",
    params=params,
    headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/41.0.2272.101 Safari/537.36",
            "Content-Type": "text/html; charset=UTF-8",
    },
)
#    return json.dumps({"messages": createMessagesList(html.unescape(r.json()))})

#    return json.dumps({"message": createMessagesList(r.json()['messages'])})
    try:
        print( createMessagesListFromResponse(r.json()))
    except Exception:
        print(r.json())
except Exception as e:
    print(e)
    print( json.dumps({"message" : "something happened when using the validator "}) )

