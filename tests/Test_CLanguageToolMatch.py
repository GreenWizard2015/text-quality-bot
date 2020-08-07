from verify import expect
from bot.CLanguageToolMatch import CLanguageToolMatch

class Test_CLanguageToolMatch:
  def test_basic(self):
    data = {
      'message': 'message',
      'replacements': [],
      'context': {
        'text': 'text tupo text',
        'offset': 5,
        'length': 4
      },
      'rule': {
        'category': {
          'name': 'error'
        }
      }
    }
    
    match = CLanguageToolMatch(data)
    expect(match.kind).is_equal('error')
    expect(match.asText()).is_equal('"text <b>tupo</b> text" - message.')
    
  def test_context(self):
    data = {
      'context': {
        'text': 'text',
        'offset': 1,
        'length': 2
      }
    }
    
    match = CLanguageToolMatch(data)
    expect(match.context()).is_equal('t<b>ex</b>t')
    
  def test_replacements_empty(self):
    data = {
      'replacements': []
    }
    
    match = CLanguageToolMatch(data)
    expect(match.replacements()).is_equal('')
    
    
  def test_replacements_multiple(self):
    data = {
      'replacements': [{ 'value': 'a' }, { 'value': 'bb'}]
    }
    
    match = CLanguageToolMatch(data)
    expect(match.replacements()).is_equal('\nВарианты: "<b>a</b>", "<b>bb</b>".')