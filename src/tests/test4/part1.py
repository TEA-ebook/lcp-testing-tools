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
    self.original_time = self.status.get_updated_status()

  def test_a_check_status_ready(self):
    """- Check the current status is 'ready'"""
    self.assertTrue(self.status.is_ready(), "The status is not 'ready'")

  def test_b_register_and_check_status(self):
    """- Register with non empty id and name string parameters"""
    link = self.status.get_link(self.status.REGISTER) 
    self.assertTrue(link['templated'], "The register link is not templated")
    # Save updated.status to compare on test_e...
    self.status.register(self.status.DEVICEID1, self.status.DEVICENAME1)

  def test_c_check_status_schema(self):
    """- Check that the status document which was returned is valid, using the corresponding JSON schema"""
    try:
      self.status.check_schema()
    except:
      self.fail("Status schema validation failure")

  def test_d_check_status_active(self):
    """- Check that a new status is 'active'"""
    self.assertTrue(self.status.is_active())

  def test_e_updated_time(self):
    """- Check the the 'updated.status' timestamp has been updated"""
    updated = self.status.get_updated_status()
    self.assertLess(self.original_time, updated)
    
  def test_f_register_event(self):
    """- Test if a new register event appears in the status document"""
    pass
