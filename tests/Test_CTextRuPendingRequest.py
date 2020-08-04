from verify import expect
from bot.CTextRuPendingRequest import CTextRuPendingRequest
from bot.CTextRuSummary import CTextRuSummary

class Test_CTextRuPendingRequest:
  def test_pull_returnSelfIfNone(self):
    def fakeRequest(uid):
      expect(uid).is_equal('uid')
      return None
    
    req = CTextRuPendingRequest(uid='uid', request=fakeRequest)
    expect(req.pull()).is_equal(req)
    
  def test_pull_returnSummary(self):
    def fakeRequest(uid):
      return { }
    
    res = CTextRuPendingRequest(uid='uid', request=fakeRequest).pull()
    expect(res).is_type(CTextRuSummary)
    