import requests
import json
from py_w3c.validators.html.validator import HTMLValidator  
import validators
import html


def validateByURL(url):
  params = {
    'doc': url, #Target URL to be tested
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
    return html.unescape(r.json())
  except Exception:
    return json.dumps({"message" : "something happened when using the validator "})

def lambda_handler(event, context):




#  vld = HTMLValidator()
#  vld.validate('http://example.com')

  #Check if any parameter exists
  try:
    queryStringParameters = event['queryStringParameters']
    
    #Check if there's a targeturl parameter
    try:
      targeturl = queryStringParameters['targeturl'] #Can run into an exception
        
      #Check if targeturl is a valid url
      if validators.url(targeturl):

        return {    
       "statusCode": 400,  
       "body": json.dumps({
              "message": validateByURL(targeturl),
              "url": targeturl
            }),   
        }

      #if it's not a valid URL  
      else:
        return {    
       "statusCode": 400,  
       "body": json.dumps({
              "message": "Invalid URL, please check it and try again."
            }),   
        }
        

    except Exception:
      return {    
       "statusCode": 400,  
       "body": json.dumps({
              "message": "No targeturl parameter was found",
              "url": targeturl
            }),   
        }

  #I should learn how tryexcept blocks work
  except Exception:
      return {    
       "statusCode": 400,  
       "body": json.dumps({
              "message": "No parameters were found, please make sure to add the 'targeturl' parameter."
            }),   
        }



