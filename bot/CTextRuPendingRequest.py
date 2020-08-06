from bot.CTextRuSummary import CTextRuSummary

class CTextRuPendingRequest(object):
  def __init__(self, uid, request, spellRequired):
    self._uid = uid
    self._request = request
    self._spellRequired = spellRequired
  
  def isReady(self):
    return False
  
  def pull(self):
    resp = self._request(self._uid)
    if resp is None: return self

    if self._spellRequired:
      if 'spell_check' not in resp: return self
      if '' == resp['spell_check']: return self
    return CTextRuSummary(resp)