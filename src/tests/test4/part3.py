from  unittest import TestCase
from config.config import TestConfig 
from lcp.license import License
from lcp.status import Status

class LCPTests(TestCase):

  def setUp(self):
    # get config
    self.config = TestConfig('b1')
    license = License(self.config.license())
    # Get status from config license
    self.status = Status(license)
    self.status.update_status()

  def test_a_register_without_id_and_name(self):
    """- Register b1 without id and name string parameters and check that the server returns an error"""
    with self.assertRaisesRegexp(IOError, 'POST .* HTTP error 400$'):
      self.status.register('', '')
