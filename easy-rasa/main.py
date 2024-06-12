import io
import os
import pkgutil
import sys

import pandas as pd


def create_rasa_files(csv_path, create_files_path):
    """
    Converts a CSV file created with the specified format to RASA accepted domain.yml format.
    ex: create_rasa_files('nlu_sample_format_for_conversion.csv', create_files_path='./')

    :param csv_path: path where the CSV file is present
    :param create_files_path: path where the nlu.md, domain.yml file needs to be created
    :return: return nothing. A file is created in the path specified via create_files_path
    """
    try:
        csv_path = os.path.join(sys.path[0], csv_path)
        print(csv_path)
        df = pd.read_csv(csv_path)
        print("Reading contents\n", df.head())
    except FileNotFoundError:
        print(f"Error: The file at {csv_path} was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {csv_path} is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file at {csv_path} could not be parsed.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV file: {e}")
        return

    try:
        nlu_file_path = os.path.join(create_files_path, 'nlu.md')
        with open(nlu_file_path, "w") as file:
            intents = list(df.columns)
            for item in intents:
                file.write(f"## intent: {item}\n")
                for sent in df[item]:
                    if pd.notna(sent):
                        file.write(f"- {sent}\n")
    except Exception as e:
        print(f"An error occurred while writing to the nlu.md file: {e}")
        return

    try:
        domain_file_path = os.path.join(create_files_path, 'domain.yml')
        with open(domain_file_path, "w") as file:
            file.write("intents:\n")
            for intent_name in intents:
                file.write(f"  - {intent_name}\n")
            file.write("actions:\n")
            for intent_name in intents:
                file.write(f"  - utter_{intent_name}\n")
    except Exception as e:
        print(f"An error occurred while writing to the domain.yml file: {e}")
        return

    print("Files have been created successfully.")

    return None


def download_csv():
    """
    Calling this function will download the sample csv file that you can use to add NLU examples and run create_rasa_files() function to generate rasa files.
    :return:
    """
    try:
        data = pkgutil.get_data(__name__, "data/nlu_sample_format_for_conversion.csv")
        df = pd.read_csv(io.BytesIO(data))
        print("Sample .csv file created successfully. Please check your current directory")
        df.to_csv('nlu_sample_format_for_conversion.csv')
    except:
        print('File creation failed')
