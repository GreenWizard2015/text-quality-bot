from verify import expect
from bot.CLanguageTool import CLanguageTool

class Test_CLanguageTool:
  def test_basic(self):
    def fakeRequest(text):
      expect(text).is_equal('text 123')
      return []
    
    api = CLanguageTool(request=fakeRequest)
    expect(api.check('text 123')).is_equal([])

  def test_singleMatch(self):
    def fakeRequest(text):
      return [{
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
      }]
    
    api = CLanguageTool(request=fakeRequest)
    expect(api.check('')).is_equal([
      {
        'kind': 'error',
        'message': '"text <b>tupo</b> text" - message.'
      }
    ])