from bot.CTextRuPendingRequest import CTextRuPendingRequest
import requests

def defaultHttp(url, params):
  return requests.post(url, data=params).json()

class CTextRuAPI(object):
  def __init__(self, key, request=None):
    self._key = key
    self._request = request if request else defaultHttp
  
  def check(self, text):
    uid = self.addPost(text)
    return CTextRuPendingRequest(uid=uid)
  
  def addPost(self, text):
    resp = self._request(
      'http://api.text.ru/post',
      {
        'userkey': self._key,
        'text': text,
        'copying': 'noadd'
      }
    )
    
    if 'text_uid' in resp:
      return resp['text_uid']
    
    raise Exception('(Text.Ru) Error #%d: %s' % (resp['error_code'], resp['error_desc']))