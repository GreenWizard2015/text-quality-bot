from bot.CTextRuAPI import CTextRuAPI
import time

class CTextQuality(object):
  def __init__(self, configs):
    self.configs = configs
    self._textRu = CTextRuAPI(configs.TextRu.key)

  def TextRu_check(self, text):
    results = self._textRu.check(text)
    while not results.isReady():
      results = results.pull()
      time.sleep(0 if results.isReady() else 5)
    return results

  def evaluate(self, text):
    return self.TextRu_check(text)