from bot.CTextRuPendingRequest import CTextRuPendingRequest

class CTextRuAPI(object):
  def __init__(self, key):
    self._key = key

  def check(self, text):
    # todo: ����������� �������� ������ �� �������� � ��������� text_uid
    uid = None 
    return CTextRuPendingRequest(uid=uid, key=self._key)