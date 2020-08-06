class CtqsJoined(object):
  def __init__(self, summarys):
    self._summarys = summarys
  
  def asText(self):
    return '\n\n'.join(
      summary.asText() for summary in self._summarys
    )