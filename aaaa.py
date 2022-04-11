import requests
import html
params = {
    'doc': '43',
    'out': 'json'
}

try:
        r = requests.get('https://validator.w3.org/nu/',
                 params=params,
                 headers={
                     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/41.0.2272.101 Safari/537.36',
                     'Content-Type': 'text/html; charset=UTF-8'})

except Exception:
        print('F')
        print(r)

print(html.unescape(r.json()))



#vld = HTMLValidator()
#print("validasao", vld.validate('https://sdab/dev2aelop/samcli/lib/utils/tar.py'))
#print(vld.warnings)

#for err in vld.errors:
#        print(u'line: {0}; col: {1}; message: {2}'.
#                format(err['type'], err['type'], html.unescape(err['message']))
#                 )
 #                 
#for err in vld.warnings:
 #   print(u'line: {0}; col: {1}; message: {2}'.
#                format(err['line'], err['col'], html.unescape(err['message']))
#                )
#vld.errors