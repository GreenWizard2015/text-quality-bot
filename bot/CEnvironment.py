import re
from cached_property import cached_property
from bot.CGoogleDocs import CGoogleDocs

class CEnvironment:
  def __init__(self, configs, update, context, googleApi):
    self.configs = configs
    self._update = update
    self._context = context
    self.google_docs = CGoogleDocs(googleApi)
    
  def send(self, message):
    return self._update.message.reply_text(message)
  
  @property
  def message(self):
    return self._update.message.text
  
  @cached_property
  def command(self):
    match = re.compile(r'^\/(\S+)').search(self.message)
    if match:
      return match.group(1).lower()
    return None