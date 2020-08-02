from bot.CGoogleDocument import CGoogleDocument
import re

class CGoogleDocs:
  def __init__(self, configs):
    self._configs = configs
    self._docLinkRE = re.compile(r'^https?:\/\/docs\.google\.com\/document\/d\/([\da-f_\-]{44})', re.IGNORECASE)
  
  def validLink(self, link):
    return not (self._docLinkRE.match(link) is None)

  def document(self, link):
    # todo: Реализовать получение ID документа
    docId = None
    return CGoogleDocument(docId=docId)
  