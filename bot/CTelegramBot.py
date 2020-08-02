from telegram.ext.commandhandler import CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from bot.CEnvironment import CEnvironment

class CTelegramBot:
  def __init__(self, configs):
    self.configs = configs
  
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
      context=context
    )

    try:
      # todo: Реализовать получение ссылки на документ и отправки сводки по тексту
      env.send('Unknown command. See /help')
    except Exception as e:
      env.send('Error: %s' % e)
    return
  
  def help(self, update, context):
    update.message.reply_text('')
