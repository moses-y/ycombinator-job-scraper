import unittest
from unittest.mock import patch
from src.scraper import parse_jobs

class TestScraper(unittest.TestCase):
  @patch('src.scraper.fetch_page_content')
  def test_parse_jobs(self, mock_fetch_page_content):
      mock_html = '''
      <div class="job">
          <h2>Software Engineer</h2>
          <span class="company">TechCorp</span>
          <span class="location">San Francisco, CA</span>
          <a href="/jobs/123">Apply</a>
      </div>
      '''
      mock_fetch_page_content.return_value = mock_html
      
      jobs = parse_jobs(mock_html)
      
      self.assertEqual(len(jobs), 1)
      self.assertEqual(jobs[0]['title'], 'Software Engineer')
      self.assertEqual(jobs[0]['company'], 'TechCorp')
      self.assertEqual(jobs[0]['location'], 'San Francisco, CA')
      self.assertEqual(jobs[0]['url'], 'https://www.ycombinator.com/jobs/123')

if __name__ == '__main__':
  unittest.main()