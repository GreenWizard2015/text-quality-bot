from bot.CTextRuPendingRequest import CTextRuPendingRequest
import requests

def defaultHttp(url, params):
  req = requests.post(url, data=params)
  print(req.text) # debug
  return req.json()

class CTextRuAPI(object):
  def __init__(self, key, request=None):
    self._key = key
    self._request = request if request else defaultHttp
  
  def check(self, text):
    uid = self.addPost(text)
    return CTextRuPendingRequest(uid=uid, request=self.getTask)
  
  def addPost(self, text):
    resp = self._request(
      'http://api.text.ru/post',
      {
        'userkey': self._key,
        'text': text
      }
    )
    
    if 'text_uid' in resp:
      return resp['text_uid']
    
    raise Exception('(Text.Ru) Error #%d: %s' % (resp['error_code'], resp['error_desc']))
  
  def getTask(self, uid):
    resp = self._request(
      'http://api.text.ru/post',
      {
        'userkey': self._key,
        'uid': uid
      }
    )
    
    if 'error_code' in resp:
      if 181 == resp['error_code']: return None
      if 144 == resp['error_code']: return None
      raise Exception('(Text.Ru) Error #%d: %s' % (resp['error_code'], resp['error_desc']))

    return resp
