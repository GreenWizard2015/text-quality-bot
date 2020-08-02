from bot.CTextQualitySummary import CTextQualitySummary

class CTextQuality(object):
  def __init__(self, configs):
    self.configs = configs

  def evaluate(self, text):
    return CTextQualitySummary()