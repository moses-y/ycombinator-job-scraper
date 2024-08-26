from scraper import scrape_jobs
from database import init_db, insert_job, get_existing_job_urls
from messaging import send_whatsapp_message

def main():
  init_db()
  existing_job_urls = get_existing_job_urls()
  
  jobs = scrape_jobs()
  new_jobs = []
  
  for job in jobs:
      if job['url'] not in existing_job_urls:
          if insert_job(job):
              new_jobs.append(job)
  
  if new_jobs:
      message = "New jobs found on Y Combinator:\n\n"
      for job in new_jobs:
          message += f"{job['title']} at {job['company']} ({job['location']})\n{job['url']}\n\n"
      send_whatsapp_message(message)
  else:
      print("No new jobs found.")

if __name__ == "__main__":
  main()