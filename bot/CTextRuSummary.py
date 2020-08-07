class CTextRuSummary(object):
  def __init__(self, data):
    self._data = data
    return
  
  def isReady(self):
    return True
  
  @property
  def text_unique(self):
    return float(self._data['text_unique'])

  def asText(self):
    return 'Уникальность текста: %.0f / 100' % self.text_unique