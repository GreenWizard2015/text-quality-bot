from bot.CGoogleDocument import CGoogleDocument

class CGoogleDocs:
  def __init__(self, configs):
    self._configs = configs
  
  def validLink(self, link):
    # todo: ����������� �������� ��� ������ �� �������� � Google Docs
    return False

  def document(self, link):
    # todo: ����������� ��������� ID ���������
    docId = None
    return CGoogleDocument(docId=docId)
  