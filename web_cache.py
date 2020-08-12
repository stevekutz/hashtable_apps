import urllib.request

cache = {}

def web_cache():

     while True:
          url = input("Enter a URL: ")

          if url == 'exit':
               break

          if url not in cache:
               print(f' cache MISS')
               resp = urllib.request.urlopen(url)
               data = resp.read()
               cache[url] = data

          else:
               print(f'!!! 💪💪💪 cache HIT 💪💪💪 ')     

          print(cache[url])


web_cache()