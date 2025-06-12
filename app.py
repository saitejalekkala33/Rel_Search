import os
from dotenv import load_dotenv
from search.utils import setup_logging
from search.loader import Loader

def main():
    load_dotenv()
    logger = setup_logging()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        logger.error("Missing required environment variable: OPENAI_API_KEY. Please set it in your .env file.")
        return

    base_url = input("Enter a base URL to start crawling (e.g., https://2025.aclweb.org): ").strip()
    
    loader = Loader()

    logger.info(f"Fetching all URLs starting from {base_url}...")
    urls = loader.get_all_urls(base_url)
    if not urls:
        logger.error("No URLs found. Exiting.")
        return

    logger.info(f"Found {len(urls)} URLs: {urls}")
    logger.info("Crawling URLs to extract content...")
    crawled_objs = loader.to_crawled_url_objs(urls)

    content_dict = {obj.source: obj.content for obj in crawled_objs if not obj.is_error and obj.content}

    print(f"\nCrawled Content for {base_url}:\n")
    logger.info(f"\nCrawled Content for {base_url}:\n")
    for url, content in content_dict.items():
        logger.info(f"Fetched content from {url}")
        print(f"From URL: {url}")
        print(content) 
        print("\n" + "-"*80 + "\n")
        logger.info(f"\nFrom URL: {url}\n{content}\n" + "-" * 80)


if __name__ == "__main__":
    main()