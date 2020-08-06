from bot.CTextRuAPI import CTextRuAPI
import time
from bot.CLanguageTool import CLanguageTool
from TextQualitySummary.CtqsErrors import CtqsErrors
from TextQualitySummary.CtqsJoined import CtqsJoined
from TextQualitySummary.CtqsMessage import CtqsMessage

class CTextQuality(object):
  def __init__(self, configs):
    self.configs = configs
    self._textRu = CTextRuAPI(configs.TextRu.key)
    self._languagetool = CLanguageTool()

  def TextRu_check(self, text):
    results = self._textRu.check(text)
    while not results.isReady():
      results = results.pull()
      time.sleep(0 if results.isReady() else 5)
    return results

  def evaluate(self, text):
    spelling = self._languagetool.check(text)
    
    errors = CtqsErrors(spelling)
    if len(spelling) < self.configs.MaxSpellingErrors:
      return CtqsJoined([errors, self.TextRu_check(text)])

    return CtqsJoined([
      errors,
      CtqsMessage('Слишком много ошибок в тексте! Проверка уникальности не выполнена.')
    ])
