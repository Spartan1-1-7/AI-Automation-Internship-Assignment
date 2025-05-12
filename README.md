# AI-Automation-Internship-Assignment

## Overview
This repository contains two tasks completed as part of an AI Automation Internship assignment. Each task focuses on solving a specific problem using automation, data analysis, and integration with APIs.

---

## Task 1: YouTube Video Search and Analysis Automation

### Description
This task involves building an automation system that:
- Accepts text or voice input from the user.
- Searches YouTube for relevant videos using the YouTube API.
- Filters the search results based on video length and recency.
- Analyzes video titles using OpenAI's ChatGPT to determine the best video.
- Integrates with Telegram for user interaction.

### Setup Instructions
1. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Save the necessary API keys in a `.env` file. The required keys are:
   - YouTube Data API v3
   - OpenAI API
   - Telegram Bot API

   Example `.env` file:
   ```env
   YOUTUBE_API_KEY=your_youtube_api_key
   OPENAI_API_KEY=your_openai_api_key
   TELEGRAM_BOT_API_KEY=your_telegram_bot_api_key
   ```
3. Run the `bot.py` script to start the automation.

---

## Task 2: Amazon India Soft Toys Data Analysis

### Description
This task focuses on scraping, cleaning, and analyzing product data for soft toys from Amazon India. The goal is to derive actionable insights from the data.

### Steps Performed
1. **Data Scraping**:
   - Scraped data for sponsored soft toys, including:
     - Title
     - Brand
     - Reviews
     - Ratings
     - Price
     - Image URL
     - Product URL

2. **Data Cleaning**:
   - Removed duplicate entries.
   - Converted values to appropriate formats.
   - Handled missing data.

3. **Data Analysis**:
   - **Brand Performance**: Identified top-performing brands and high-rated but less frequent ones.
   - **Price vs. Rating**: Assessed the relationship between price and ratings.
   - **Review & Rating Distribution**: Analyzed popular and trusted products.

4. **Visualization**:
   - Presented findings using visualizations for deeper insights.

### Setup Instructions
1. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the `task_2.ipynb` notebook to execute the analysis.

---

## Repository Structure
```
README.md
Task_1/
    bot.py
    data.csv
    requirements.txt
    youtube_search.py
Task_2/
    requirements.txt
    cleaned_sponsored_soft_toys.csv
    sponsored_soft_toys.csv
    task_2.ipynb
```

---

## Notes
- Ensure that the required API keys are valid and have sufficient quota.
- For Task 2, the data files (`sponsored_soft_toys.csv` and `cleaned_sponsored_soft_toys.csv`) are included for reference.
