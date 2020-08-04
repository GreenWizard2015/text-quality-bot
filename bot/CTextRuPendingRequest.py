class CTextRuPendingRequest(object):
  def __init__(self, uid):
    self._uid = uid
  
  def isReady(self):
    return False
  
  def pull(self):
    # todo: Реализовать получение результатов обработки текста и возврат CTextRuSummary 
    return None