class CLanguageToolMatch(object):
  def __init__(self, data):
    self._data = data
  
  @property
  def kind(self):
    return self._data['rule']['category']['name']
  
  def context(self):
    context = self._data['context']
    ctxText = context['text']
    start = context['offset']
    end = start + context['length']
    return '%s<b>%s</b>%s' % (ctxText[:start], ctxText[start:end], ctxText[end:])

  def replacements(self):
    replacements = ['"<b>%s</b>"' % x['value'] for x in self._data['replacements']]
    if replacements:
      return '\nВарианты: %s.' % (', '.join(replacements))
    return ''

  def asText(self):
    message = self._data['message'] + '.'
    return '"%s" - %s%s' % (self.context(), message, self.replacements())