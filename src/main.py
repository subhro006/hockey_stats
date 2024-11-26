from scraper import scrape_hockey_data
from scraper import save_html_files
from data_processor import process_hockey_data, save_to_excel

def main():
    # Scrape the data
    html_files, hockey_stats = scrape_hockey_data()
    
    # Process the data
    excel_data = process_hockey_data(hockey_stats)
    
    # Save results
    save_to_excel(html_files, excel_data)

    # Save Zip Files
    # save_html_files(html_files, "C:/Users/pc/Downloads/hockey_stats/src")

if __name__ == "__main__":
    # asyncio.run(main())
    main()
