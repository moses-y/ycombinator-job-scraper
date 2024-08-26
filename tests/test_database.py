import unittest
from src.database import init_db, insert_job, get_existing_job_urls

class TestDatabase(unittest.TestCase):
  def setUp(self):
      init_db()

  def test_insert_and_retrieve_job(self):
      job = {
          'title': 'Software Engineer',
          'company': 'Tech Co',
          'location': 'Remote',
          'url': 'https://www.ycombinator.com/jobs/1'
      }
      self.assertTrue(insert_job(job))
      urls = get_existing_job_urls()
      self.assertIn(job['url'], urls)

if __name__ == '__main__':
  unittest.main()