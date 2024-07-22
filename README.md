# Google Map Scrapper

**Created by:** Karan Parmar
**License:** MIT

## Overview

Google Map Scrapper is a Python script designed to scrape business information from Google Maps. The script allows users to extract data such as business titles, links, websites, ratings, reviews, and phone numbers, and save the extracted data into a specified file format (JSON, CSV, or Excel).

## Prerequisites

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Google Chrome browser: Ensure you have the latest version of Chrome installed.

## Installation

1. **Install Python**: Download and install Python from [here](https://www.python.org/downloads/).
2. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/google-map-scrapper.git
   cd project
   ```
3. **Install Required Libraries**: Install the necessary libraries using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**: Execute the Python script to start scraping.

   ```bash
   python google_map_scrapper.py
   ```
2. **Follow the Prompts**:

   - Enter the Google Maps link you want to scrape from.
   - Select the desired file format for saving the data (1 for JSON, 2 for CSV, 3 for Excel).

## Libraries and Documentation

- **Selenium**: For web scraping automation.
  - Selenium documentation: [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- **Pandas**: For data manipulation and saving in CSV/Excel formats.
  - Pandas documentation: [Pandas Docs](https://pandas.pydata.org/docs/)
- **Python**: General-purpose programming language.
  - Python documentation: [Python Docs](https://docs.python.org/3/)

## Example

```
Enter the link you want to scrape from: [your_google_maps_link]
Select the file format to save the data:
1. JSON
2. CSV
3. Excel
Enter the number of the file format you want: [your_choice]
```

After selecting the file format, the script will scrape the data and save it in the chosen format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
