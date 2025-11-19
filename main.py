# main.py
import scraper_permits
import editor

def main():
    """
    Main function to run the entire Civic Pulse pipeline.
    """
    print("Starting the Civic Pulse pipeline...")

    # Step 1: Run the scraper to get the latest permit data
    scraper_permits.main()

    # Step 2: Run the editor to create a summary
    editor.main()

    print("Civic Pulse pipeline finished.")

if __name__ == "__main__":
    main()
