def textFrom(element):
  text_run = element.get('textRun')
  return text_run.get('content') if text_run else ''

def doc2text(elements):
  text = ''
  for value in elements:
    if 'paragraph' in value:
      elements = value.get('paragraph').get('elements')
      for elem in elements:
        text += textFrom(elem)
  return text

class CGoogleDocument(object):
  def __init__(self, docId, api):
    self._id = docId
    self._api = api
  
  def plainText(self):
    doc = self._api.document(self._id)
    return doc2text(doc.get('body').get('content'))