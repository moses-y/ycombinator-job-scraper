import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

def setup_driver():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  service = Service(ChromeDriverManager().install())
  return webdriver.Chrome(service=service, options=chrome_options)

def fetch_page_content(url, max_retries=3):
  for attempt in range(max_retries):
      try:
          driver = setup_driver()
          driver.get(url)
          time.sleep(5)  # Wait for JavaScript to load content
          page_content = driver.page_source
          driver.quit()
          return page_content
      except Exception as e:
          print(f"Error fetching page content (attempt {attempt + 1}): {str(e)}")
          if attempt == max_retries - 1:
              raise
          time.sleep(5)

def parse_jobs(html_content):
  soup = BeautifulSoup(html_content, 'html.parser')
  job_listings = soup.find_all('div', class_='job')
  
  jobs = []
  for job in job_listings:
      title = job.find('h2').text.strip()
      company = job.find('span', class_='company').text.strip()
      location = job.find('span', class_='location').text.strip()
      url = 'https://www.ycombinator.com' + job.find('a')['href']
      
      jobs.append({
          'title': title,
          'company': company,
          'location': location,
          'url': url
      })
  
  return jobs

def scrape_jobs():
  url = 'https://www.ycombinator.com/jobs'
  html_content = fetch_page_content(url)
  return parse_jobs(html_content)