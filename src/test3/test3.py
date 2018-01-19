from  unittest import TestCase
from config.testconfig import TestConfig 
from lcp.license import License
from lcp.status import Status
import urllib

class Test3(TestCase):

  def test_a_check_status_link_https(self):
    """- Check that the 'status' link is a valid https url"""
    link = self.license.get_link('status', 'href')
    self.assertTrue(link.startswith('https://'))

  def test_b_check_status_document(self):
    """- Check that the JSON document is valid, using the corresponding JSON schema"""
    link = self.license.get_link('status', 'href')
    response = urllib.urlopen(link)
    status = Status(response.read())
    self.assertIsNotNone(status)
    try:
      status.check_schema()
    except:
      self.fail("Status schema validation failure")

  def test_c_status_events(self):
    """- Check if events are (or not) available"""
    link = self.license.get_link('status', 'href')
    response = urllib.urlopen(link)
    status = Status(response.read())
    events = status.get_events()

  def test_d_check_status_license_link(self):
    """- Check if the 'license' link is a valid https url"""
    link = self.license.get_link('status', 'href')
    response = urllib.urlopen(link)
    status = Status(response.read())
    link = status.get_link('license', 'href')
    self.assertIsNotNone(link)
    self.assertTrue(link.startswith('https://'))

  def test_e_check_license_mimetype(self):
    """- Check that the corresponding mime-type is 'application/vnd.readium.lcp.license-1.0+json'"""
    link = self.license.get_link('status', 'href')
    response = urllib.urlopen(link)
    status = Status(response.read())
    mimetype = status.get_link('license', 'type')
    self.assertEquals(mimetype, License.MIMETYPE)