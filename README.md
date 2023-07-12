# IMDB-Scraper 👨‍💻

IMDB-Scraper is a Python-based web scraping tool that allows users to scrape movie information from the IMDb (Internet Movie Database) website. The scraper is capable of extracting various details such as title, genre, runtime, vote count, certification, and more, based on the user's input for the required genre.

## Features

- Scrapes movie information from IMDb based on user's input for the genre.
- Retrieves details such as title, genre, runtime, vote count, certification, and more.
- Provides a simple and intuitive command-line interface for easy interaction.
- Saves the scraped data in a CSV file for further analysis or processing.
- Handles pagination automatically to scrape multiple pages of results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/IMDB-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd IMDB-Scraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `main.py` script:

   ```bash
   python Scrapper/main.py
   ```

2. Follow the prompts to enter the desired genre and specify the number of pages to scrape.

3. The scraper will start fetching movie information from IMDb based on your inputs.

4. Once the scraping process is complete, the scraped data will be saved in a CSV file named `imdb.csv` in the project directory along with the datetime.

5. You can open the `imdb.csv` file using any spreadsheet software to view and analyze the scraped data.

## Example

Here's an example of how to use the IMDB-Scraper:

```bash
$ python Scrapper/main.py

Enter the genre you want to scrape: Action

Scraped data saved in imdb.csv.
```

## Contributing

Contributions to the IMDB-Scraper project are welcome and encouraged! If you have any ideas, improvements, or bug fixes, please submit a pull request. Before contributing, make sure to review the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](PUBLIC). Feel free to modify and distribute this code as per the terms of the license.

## Acknowledgments

The IMDB-Scraper project was inspired by the need to extract movie information from IMDb easily. Thanks to the IMDb website for providing a rich source of movie data.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the project maintainer at [shavilyarajput50@gmail.com](mailto:shavilyarajput50@gmail.com).
