import os
import json
import traceback
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain

def main():
    try:
        # Simulate file input (you can also use open() if needed)
        file_path = "text_files/sample.txt"  # Or a PDF like "text_files/sample.pdf"
        with open(file_path, "rb") as file:
            text = read_file(file)

        # Define inputs
        number = "3"
        subject = "Machine Learning"
        tone = "formal"
        response_json = """
{
  "1": {
    "mcq": "string",
    "options": {
      "A": "string",
      "B": "string",
      "C": "string",
      "D": "string"
    },
    "correct": "string"
  }
}
"""

        # Run the SequentialChain
        response = generate_evaluate_chain({
            "text": text,
            "number": number,
            "subject": subject,
            "tone": tone,
            "response_json": response_json
        })

        # Print raw response
        print("\n=== Raw MCQ Output ===")
        print(response["quiz"])

        # Print review
        print("\n=== Review Output ===")
        print(response["review"])

        # Convert quiz to table data
        print("\n=== Tabular MCQ Output ===")
        table_data = get_table_data(response["quiz"])
        if table_data:
            for i, row in enumerate(table_data, 1):
                print(f"\nQ{i}: {row['MCQ']}")
                print(f"Choices: {row['Choices']}")
                print(f"Correct: {row['Correct']}")
        else:
            print("Failed to convert MCQ output to table.")

    except Exception as e:
        print("An error occurred.")
        logging.error(f"App failed: {traceback.format_exc()}")

if __name__ == "__main__":
    main()