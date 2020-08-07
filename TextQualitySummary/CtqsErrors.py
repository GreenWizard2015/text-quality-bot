from _collections import defaultdict
class CtqsErrors(object):
  def __init__(self, errors):
    self._errors = errors
  
  def asText(self):
    byKind = defaultdict(list)
    for e in self._errors:
      kind = e['kind']
      byKind[kind].append(e)

    return '\n\n'.join(
      '%s\n%s' % (kind, '\n'.join('\n- ' + e['message'] for e in items))
      for kind, items in byKind.items()
    )