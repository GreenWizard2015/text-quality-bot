from bot.CLanguageToolMatch import CLanguageToolMatch
import requests

# taken from https://github.com/Findus23/pyLanguagetool/blob/master/pylanguagetool/api.py

def _is_in_pwl(match, pwl):
  start = match['context']['offset']
  end = start + match['context']['length']
  word = match['context']['text'][start:end]
  return word in pwl

def check(input_text, api_url, lang, mother_tongue=None, preferred_variants=None,
      enabled_rules=None, disabled_rules=None,
      enabled_categories=None, disabled_categories=None,
      enabled_only=False, verbose=False,
      pwl=None,
      **kwargs):
  post_parameters = {
    "text": input_text,
    "language": lang,
  }
  if mother_tongue:
    post_parameters["motherTongue"] = mother_tongue
  if preferred_variants:
    post_parameters["preferredVariants"] = preferred_variants
  if enabled_rules:
    post_parameters["enabledRules"] = enabled_rules
  if disabled_rules:
    post_parameters["disabledRules"] = disabled_rules
  if enabled_categories:
    post_parameters["enabledCategories"] = enabled_categories
  if disabled_categories:
    post_parameters["disabledCategories"] = disabled_categories
  if enabled_only:
    post_parameters["enabledOnly"] = 'true'

  r = requests.post(api_url + "check", data=post_parameters)
  if r.status_code != 200:
    raise ValueError(r.text)
  if verbose:
    print(post_parameters)
    print(r.json())
  data = r.json()
  if pwl:
    matches = data.pop('matches', [])
    data['matches'] = [
      match for match in matches
      if not _is_in_pwl(match, pwl)
    ]
  return data
#################################
def LanguageToolAPICall(text):
  return check(text, 'https://languagetool.org/api/v2/', 'ru-RU').pop('matches', [])

class CLanguageTool(object):
  def __init__(self, request=None):
    self._request = request if request else LanguageToolAPICall

  def check(self, text):
    matches = (CLanguageToolMatch(m) for m in self._request(text))
    return [
      { 'kind': m.kind, 'message': m.asText() } for m in matches
    ]
