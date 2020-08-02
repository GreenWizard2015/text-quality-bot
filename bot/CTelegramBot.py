from telegram.ext.commandhandler import CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from bot.CEnvironment import CEnvironment
from bot.CTextQuality import CTextQuality

class CTelegramBot:
  def __init__(self, configs, googleApi):
    self.configs = configs
    self.textQuality = CTextQuality(configs=configs)
    self.googleApi = googleApi
  
  def bind(self, dp):
    dp.add_handler(MessageHandler(Filters.update.edited_message, self.ignoreEdit))
    #######################
    dp.add_handler(CommandHandler("help", self.help))
    #######################
    dp.add_handler(MessageHandler((Filters.text | Filters.command) & (~Filters.update.edited_message), self.process))
    return True
  
  def ignoreEdit(self, update, context):
    pass
  
  @run_async
  def process(self, update, context):
    env = CEnvironment(
      configs=self.configs,
      update=update,
      context=context,
      googleApi=self.googleApi
    )

    try:
      if env.google_docs.validLink(env.message):
        return self.checkDocument(env, env.google_docs.document(env.message))
      env.send('Unknown command. See /help')
    except Exception as e:
      env.send('Error: %s' % e)
    return
  
  def help(self, update, context):
    update.message.reply_text('')

  def checkDocument(self, env, doc):
    summary = self.textQuality.evaluate(doc.plainText())
    env.send(summary.asText())
    return