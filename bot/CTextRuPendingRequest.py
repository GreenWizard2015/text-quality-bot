from bot.CTextRuSummary import CTextRuSummary

class CTextRuPendingRequest(object):
  def __init__(self, uid, request):
    self._uid = uid
    self._request = request
  
  def isReady(self):
    return False
  
  def pull(self):
    resp = self._request(self._uid)
    if resp is None: return self

    if 'spell_check' in resp:
      if not ('' == resp['spell_check']):
        return CTextRuSummary(resp)
    return self