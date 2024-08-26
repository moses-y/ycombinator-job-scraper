import unittest
from src.scraper import parse_jobs

class TestScraper(unittest.TestCase):
  def test_parse_jobs(self):
      # Example HTML content for testing
      html_content = '''
      <div class="job">
          <h2>Software Engineer</h2>
          <span class="company">Tech Co</span>
          <span class="location">Remote</span>
          <a href="/jobs/1">Job Link</a>
      </div>
      '''
      jobs = parse_jobs(html_content)
      self.assertEqual(len(jobs), 1)
      self.assertEqual(jobs[0]['title'], 'Software Engineer')
      self.assertEqual(jobs[0]['company'], 'Tech Co')
      self.assertEqual(jobs[0]['location'], 'Remote')
      self.assertEqual(jobs[0]['url'], 'https://www.ycombinator.com/jobs/1')

if __name__ == '__main__':
  unittest.main()