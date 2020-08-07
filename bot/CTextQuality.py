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
    # todo: Возвращать фейковый отчёт с ошибкой и 0% text_unique, если возникла ошибка
    results = self._textRu.check(text)
    while not results.isReady():
      results = results.pull()
      time.sleep(0 if results.isReady() else 5)
    return results

  def evaluate(self, text):
    spelling = self._languagetool.check(text)
    
    errors = CtqsErrors(spelling)
    if len(spelling) < self.configs.MaxSpellingErrors:
      textRu = self.TextRu_check(text)
      res = [errors, textRu]
      if textRu.text_unique < self.configs.MinUnique:
        res.append(CtqsMessage(
          '<b>ВНИМАНИЕ!</b> Текст уникален лишь на %.0f%%, а минимальный уровень уникальности - %.0f%%.' %
          (textRu.text_unique, self.configs.MinUnique)
        ))
      return CtqsJoined(res)

    return CtqsJoined([
      errors,
      CtqsMessage('Слишком много ошибок в тексте! Проверка уникальности не выполнена.')
    ])
