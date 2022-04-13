import requests
import json
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
      timeout=11
    )
  except Exception:
    return json.dumps({"testResult" : "Validator not responding. Please try again later"})
  finally:
    return json.dumps({"testResult" : html.unescape(r.json())})

def lambda_handler(event, context):

  #Check if any parameter exists
  try:
    queryStringParameters = event['queryStringParameters']
    
    #Check if there's a targeturl parameter
    try:
      targeturl = queryStringParameters['targeturl'] #Can run into an exception
        
      #Check if targeturl is a valid url
      if validators.url(targeturl):
        statuscode = 200
        try:
          message = validateByURL(targeturl)
        except Exception:
          statuscode = 504
          message = json.dumps({"testResult": "Validation timed out, targeturl took too long to send back a response"})

      #if it's not a valid URL  
      else:
        statuscode = 400
        message = json.dumps({"testResult": "Invalid URL, please check it and try again"})

    except Exception:
      statuscode = 400
      message = json.dumps({"testResult": "No targeturl parameter was found"}) 

  #I should learn how tryexcept blocks work
  except Exception:

    statuscode = 400
    message = json.dumps({"testResult": "No parameters were found, please make sure to add the 'targeturl' parameter."}) 

  finally:
    return {    
        "headers": {"content-type": "application/json"},
        "statusCode": statuscode,
        "body": message 
      }



