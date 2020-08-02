from bot.CGoogleDocument import CGoogleDocument

class CGoogleDocs:
  def __init__(self, configs):
    self._configs = configs
  
  def validLink(self, link):
    # todo: Реализовать проверку что ссылка на документ в Google Docs
    return False

  def document(self, link):
    # todo: Реализовать получение ID документа
    docId = None
    return CGoogleDocument(docId=docId)
  