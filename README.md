# 📚 Book Scraper & Visualizer App

A complete **web scraping + data analysis** project built in Python using [Books to Scrape](https://books.toscrape.com) as a case study. The project scrapes **multiple pages**, 
processes the data into a structured format, and uses **Streamlit** for interactive visualizations and analysis.

---

## 🚀 Features

### ✅ Web Scraping:
- Scrape **title**, **price**, **rating**, and **availability** from all pages
- Convert star rating from class name to numeric format
- Store results in a clean **DataFrame** and exportable CSV

### ✅ Streamlit Visual Dashboard:
- View total number of books scraped
- Top rating by **count**
- **Total, average, maximum, and minimum** price
- **Top 5 books by price**
- **Rating vs Average Price**
- **Bar chart**: Number of books per rating
- **Histogram**: Book price distribution
- **Pie chart**: Availability ratio

---

## 📊 Visualizations

The Streamlit app uses **Plotly** for beautiful, interactive charts:

- 📊 **Bar Chart**: Number of books per rating  
- 📈 **Bar Chart**: Rating vs. average price  
- 🧮 **Histogram**: Price distribution  

---

## 🛠️ Technologies Used

- `requests` + `BeautifulSoup` – Web scraping
- `pandas` – Data handling
- `Streamlit` – Web app UI
- `Plotly` – Visualizations
- `os`, `re` – Utilities

---

## 📁 Project Structure

```bash
book_scraper_streamlit/
├── scraping.py # Streamlit app
├── web scraping.ipynb # Scraping logic
├── Scrap.csv # Scraped data (optional)
├── requirements.txt # Dependencies
└── README.md
```
```bash
git clone https://github.com/yourusername/book-scraper-streamlit.git
cd book-scraper-streamlit
```

## 🐍2. Install dependencies
```bash
pip install -r requirements.txt
```
## 🚀 3. Run the Streamlit app
```bash
streamlit run app.py
```
## 📦 Requirements

```bash
streamlit
pandas
matplotlib
numpy
seaborn
beautifulsoup4
requests
plotly
```

## 📌 Future Improvements
- Add search/filter by book title or category
- Export selected data to Excel or PDF
- Scrape book descriptions or categories

👨‍💻 Author
Developed by [Opakunbi Paul](https://github.com/paulow540)
