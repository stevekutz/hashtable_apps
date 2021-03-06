import urllib.request
import datetime

TIMEOUT_SECONDS = 10

class CacheEntry:
     def __init__(self, url, data):
          self.url = url
          self.data = data
          self.timestamp = datetime.datetime.now().timestamp()

cache = {}

def web_cache():

     while True:
          url = input("Enter a URL: ")

          if url == 'exit':
               break

          needs_refresh = False

          if url not in cache:
               needs_refresh = True

          else:
               # did data become stale ?
               cur_time = datetime.datetime.now().timestamp()
               diff_time = cur_time - cache[url].timestamp      

               # these 2 lines can be replaced with single line below
               # if diff_time > TIMEOUT_SECONDS:
               #      needs_refresh = True

               # creates boolean     
               needs_refresh = diff_time > TIMEOUT_SECONDS
               print(f' TIME: {needs_refresh}')

          if needs_refresh:
               print(f' GETTING FROM SERVER')
               resp = urllib.request.urlopen(url)
               data = resp.read()
               cache[url] = CacheEntry(url, data)      

          else:
               print(f'!!! 💪💪💪 cache HIT 💪💪💪 ')     

          print(cache[url].data[:60])  # just print last 60 bytes


web_cache()