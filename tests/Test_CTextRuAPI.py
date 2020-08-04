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
    
  def test_getTask_valid(self):
    response = { 'result': True }
    def fakeRequest(url, params):
      expect(url).is_equal('http://api.text.ru/post')
      expect(params['userkey']).is_equal('user key')
      expect(params['uid']).is_equal('uid')
      expect(params['jsonvisible']).is_equal('details')
      return response
    
    api = CTextRuAPI(key='user key', request=fakeRequest)
    expect(api.getTask('uid')).is_equal(response)

  def test_getTask_NoneIfNotReady(self):
    def fakeRequest(url, params):
      return { 'error_code': 81 }
    
    api = CTextRuAPI(key='user key', request=fakeRequest)
    expect(api.getTask('uid')).is_equal(None)

  def test_getTask_NoneIfBusy(self):
    def fakeRequest(url, params):
      return { 'error_code': 44 }
    
    api = CTextRuAPI(key='user key', request=fakeRequest)
    expect(api.getTask('uid')).is_equal(None)