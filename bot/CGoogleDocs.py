from bot.CGoogleDocument import CGoogleDocument
import re

class CGoogleDocs:
  def __init__(self, configs):
    self._configs = configs
    self._docLinkRE = re.compile(r'^https?:\/\/docs\.google\.com\/document\/d\/([\da-f_\-]{44})', re.IGNORECASE)
  
  def link2id(self, link):
    m = self._docLinkRE.match(link)
    if m:
      return m.group(1)
    return None

  def validLink(self, link):
    return not (self.link2id(link) is None)

  def document(self, link):
    return CGoogleDocument(docId=self.link2id(link))
  