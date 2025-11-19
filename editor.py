# editor.py
import os
import pandas as pd
from openai import OpenAI
import config

def read_permit_data(filename="permits.csv"):
    """Reads the permit data from the specified CSV file."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        print("Please run the scraper first to generate the data.")
        return None
    try:
        return pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def create_summary(df):
    """
    Uses the OpenAI API to create a sassy, engaging summary of the most
    interesting permits.
    """
    api_key = config.OPENAI_API_KEY
    if not api_key or api_key == "YOUR_API_KEY":
        print("Error: OpenAI API key is not configured.")
        print("Please set your OPENAI_API_KEY in a .env file.")
        return None

    client = OpenAI(api_key=api_key)

    # Convert dataframe to a string format for the prompt
    permit_data_string = df.to_string(index=False)

    system_prompt = (
        "You are a sassy, slightly snarky local news reporter for Sanford, Florida. "
        "Your goal is to make boring public records sound like unmissable local gossip. "
        "Use a casual, witty, and engaging tone. Never be boring."
    )

    user_prompt = (
        "Here are the latest building permits that were just filed. "
        "Find the top 3 most interesting or gossip-worthy permits from this list and write a short, "
        "engaging newsletter blurb about them. Make it fun and sassy!\\n\\n"
        f"Permit Data:\\n{permit_data_string}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred with the OpenAI API: {e}")
        return None

def main():
    """
    Main function to run the editor.
    """
    print("Starting the editor...")
    permit_df = read_permit_data()

    if permit_df is not None:
        summary = create_summary(permit_df)
        if summary:
            print("\\n--- Sassy Local News ---")
            print(summary)
            print("------------------------\\n")

    print("Editor finished.")

if __name__ == "__main__":
    main()
