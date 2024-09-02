import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import os

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--ignore-certificate-errors')

    # Check for Brave browser
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    if os.path.exists(brave_path):
        chrome_options.binary_location = brave_path
        service = ChromeService("C:/Users/moses_y/OneDrive/Desktop/ML Projects/chromedriver-win64/chromedriver.exe")
        print("Using Brave browser")
    else:
        # Default to Chrome
        service = ChromeService("/usr/local/bin/chromedriver")  # Adjust path for your environment
        print("Using Chrome browser")

    return webdriver.Chrome(service=service, options=chrome_options)

def fetch_page_content(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            driver = setup_driver()
            driver.get(url)
            time.sleep(5)
            page_content = driver.page_source
            driver.quit()
            return page_content
        except Exception as e:
            print(f"Error fetching page content (attempt {attempt + 1}): {str(e)}")
            if attempt == max_retries - 1:
                raise
            time.sleep(5)

def clean_text(text):
    return ' '.join(text.split()).strip()

def parse_jobs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_listings = soup.find_all('a', href=re.compile(r'/companies/.+/jobs/.+'))

    jobs = []
    for job_elem in job_listings:
        url = job_elem['href'] if job_elem.has_attr('href') else 'No URL'
        
        match = re.search(r'/companies/(.+)/jobs/[^-]+-(.+)', url)
        if match:
            company = clean_text(match.group(1).replace('-', ' ').title())
            title = clean_text(match.group(2).replace('-', ' ').title())
        else:
            company = 'Unknown Company'
            title = 'Unknown Title'
        
        location_elem = job_elem.find('div', string=re.compile(r'(Remote|On-site|Hybrid)'))
        location = clean_text(location_elem.text) if location_elem else 'Location not available'
        
        job = {
            'title': title,
            'company': company,
            'location': location,
            'url': f"https://www.ycombinator.com{url}"
        }
        jobs.append(job)

    return jobs

def scrape_jobs():
    url = 'https://www.ycombinator.com/jobs'
    html_content = fetch_page_content(url)
    return parse_jobs(html_content)

# Test the scraping
jobs = scrape_jobs()
print(f"Found {len(jobs)} job listings")
for job in jobs[:5]:  # Print first 5 jobs as a sample
    print(job)