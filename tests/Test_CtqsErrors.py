from verify import expect
from TextQualitySummary.CtqsErrors import CtqsErrors

class Test_CtqsErrors:
  def test_basic(self):
    summary = CtqsErrors([
      { 'kind': 'A', 'message': 'error 1' },
      { 'kind': 'B', 'message': 'error 2' },
      { 'kind': 'A', 'message': 'error 3' }
    ]) 
    expect(summary.asText()).is_equal('''
A
error 1
error 3

B
error 2
    '''.strip())