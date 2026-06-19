# Air New Zealand Review Analysis

Scrapes, stores, and analyzes 900+ customer reviews from [airlinequality.com](https://www.airlinequality.com/airline-reviews/air-new-zealand) using Python, SQLite, Alembic migrations, and a Groq LLM classification pipeline.

## What it does

- **Scrapes** reviews (author, date, rating, route, travel type, review body) with BeautifulSoup, paginating across all available pages
- **Stores** data in a SQLite database with upsert logic to avoid duplicates; schema is managed with Alembic migrations
- **Classifies** each review into complaint/praise categories (e.g. Flight Cancellation, Cabin Staff Service, Refund Issues) using Groq's LLM API with structured JSON output
- **Visualizes** rating distributions, review volume over time, quarterly 1-star vs 10-star trends, and category breakdowns with Matplotlib and Seaborn

## Tech stack

Python · Pandas · BeautifulSoup · SQLite · SQLAlchemy · Alembic · Groq API · Matplotlib · Seaborn · Jupyter

## Setup

```bash
git clone https://github.com/elenajdata/air_new_zealand_review_analysis.git
cd air_new_zealand_review_analysis
pip install requests beautifulsoup4 pandas sqlalchemy alembic groq matplotlib seaborn python-dotenv
```

Create a `.env` file from the example:

```bash
cp .env.example .env
# then edit .env and add your Groq API key
```

Open `newzelandairlines.ipynb` in Jupyter and run cells in order.

## Notebook sections

| Section | Description |
|---|---|
| Dependencies & imports | Install and import all required libraries |
| Database setup | Connect to SQLite, run Alembic migrations to create the schema |
| Scraping | `scrape_air_new_zealand_reviews(page)` fetches one page of reviews; loop scrapes all pages incrementally |
| Storage | `store_data_in_db()` upserts records using `review_id` as the conflict key |
| Visualizations | Monthly review distribution, quarterly total vs 1-star/10-star trend charts |
| LLM classification | Groq client setup, category definitions, `classify_review()` with structured JSON schema output, pie chart of category distribution |

---

[View repo on GitHub](https://github.com/elenajdata/air_new_zealand_review_analysis) &nbsp;|&nbsp; [Portfolio](https://github.com/elenajdata)
