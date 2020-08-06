class CtqsMessage(object):
  def __init__(self, message):
    self._message = message
  
  def asText(self):
    return self._message