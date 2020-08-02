from bot.CGoogleDocument import CGoogleDocument
import re

class CGoogleDocs:
  def __init__(self, googleApi=None):
    self._docLinkRE = re.compile(r'^https?:\/\/docs\.google\.com\/document\/d\/([^\s\/]+)', re.IGNORECASE)
    self._api = googleApi
  
  def link2id(self, link):
    m = self._docLinkRE.match(link)
    if m:
      return m.group(1)
    return None

  def validLink(self, link):
    return not (self.link2id(link) is None)

  def document(self, link):
    return CGoogleDocument(docId=self.link2id(link), api=self._api)
  