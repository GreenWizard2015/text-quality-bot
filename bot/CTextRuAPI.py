from bot.CTextRuPendingRequest import CTextRuPendingRequest

class CTextRuAPI(object):
  def __init__(self, key):
    self._key = key

  def check(self, text):
    # todo: Реализовать отправку текста на проверку и получение text_uid
    uid = None 
    return CTextRuPendingRequest(uid=uid, key=self._key)