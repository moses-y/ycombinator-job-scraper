from scraper import scrape_jobs
from database import init_db, insert_job, get_existing_job_urls
from messaging import send_whatsapp_message
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting job scraper")
    init_db()
    existing_job_urls = get_existing_job_urls()
    logger.info(f"Found {len(existing_job_urls)} existing job URLs")
       
    jobs = scrape_jobs()
    logger.info(f"Scraped {len(jobs)} jobs")
    new_jobs = []
       
    for job in jobs:
        if job['url'] not in existing_job_urls:
            if insert_job(job):
                new_jobs.append(job)
       
    logger.info(f"Found {len(new_jobs)} new jobs")
       
    if new_jobs:
        message = "New jobs found on Y Combinator:\n\n"
        for job in new_jobs:
            message += f"{job['title']} at {job['company']} ({job['location']})\n{job['url']}\n\n"
        send_whatsapp_message(message)
        logger.info("WhatsApp message sent")
    else:
        logger.info("No new jobs found")

if __name__ == "__main__":
    main()
