# Y Combinator Job Scraper

This project is a web scraper designed to extract job listings from the `Y Combinator` website at 10 am East African Time and shoot me a `whatsapp Alert`.

## Project Structure

* `src/`: This directory contains the source code for the project.
	+ `__init__.py`: An empty file that indicates this directory should be treated as a Python package.
	+ `scraper.py`: This module contains the web scraping logic.
	+ `database.py`: This module handles database operations.
	+ `messaging.py`: This module is responsible for sending WhatsApp messages.
	+ `main.py`: This is the entry point of the project.
* `tests/`: This directory contains unit tests for the project.
	+ `__init__.py`: An empty file that indicates this directory should be treated as a Python package.
	+ `test_scraper.py`: This module contains tests for the `scraper.py` module.
	+ `test_database.py`: This module contains tests for the `database.py` module.
	+ `test_messaging.py`: This module contains tests for the `messaging.py` module.
* `requirements.txt`: This file lists the dependencies required by the project.
* `.gitignore`: This file specifies files and directories that should be ignored by Git.
* `README.md`: This file contains information about the project.
* `.github/workflows/scraper.yml`: This file defines a GitHub Actions workflow for the project.

## Setup Guide

To use this project, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Set the `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `YOUR_PHONE_NUMBER` environment variables.
3. Run the project by executing `python src/main.py`.

## Configurations

To use this project, you need to configure the following settings:

* `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
* `TWILIO_AUTH_TOKEN`: Your Twilio auth token.
* `TWILIO_PHONE_NUMBER`: The Twilio phone number.
* `YOUR_PHONE_NUMBER`: Your phone number.