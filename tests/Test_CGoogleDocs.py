from verify import expect
from bot.CGoogleDocs import CGoogleDocs

class Test_CGoogleDocs:
  def test_validLink_basic(self):
    docs = CGoogleDocs(configs=None)
    expect(docs.validLink('')).to_be(False)
    expect(docs.validLink('link')).to_be(False)
    expect(docs.validLink('https://docs.google.com/document/d/')).to_be(False)
    
    expect(docs.validLink('https://docs.google.com/document/d/1111111111111111111_111111111111111111111111/edit?usp=sharing')).to_be(True)
    expect(docs.validLink('https://docs.google.com/document/d/1111111111111111111_111111111111111111111111/edit')).to_be(True)
    expect(docs.validLink('https://docs.google.com/document/d/1111111111111111111_111111111111111111111111/')).to_be(True)
    expect(docs.validLink('https://docs.google.com/document/d/1111111111111111111_111111111111111111111111')).to_be(True)