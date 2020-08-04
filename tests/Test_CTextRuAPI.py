from verify import expect
from bot.CTextRuAPI import CTextRuAPI

class Test_CTextRuAPI:
  def test_addPost_valid(self):
    def fakeRequest(url, params):
      expect(url).is_equal('http://api.text.ru/post')
      expect(params['userkey']).is_equal('user key')
      expect(params['text']).is_equal('text 123')
      expect(params['copying']).is_equal('noadd')
      return {
        'text_uid': 'text id'
      }
    
    api = CTextRuAPI(key='user key', request=fakeRequest)
    expect(api.addPost('text 123')).is_equal('text id')
    
  def test_addPost_errorRaiseException(self):
    def fakeRequest(url, params):
      return {
        'error_code': 321,
        'error_desc': 'description'
      }
    
    api = CTextRuAPI(key='user key', request=fakeRequest)
    try:
      api.addPost('text 123')
    except Exception as e:
      expect(str(e)).is_equal('(Text.Ru) Error #321: description')
    else:
      raise Exception('Exception expected')