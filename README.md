# csvtorasa
This will convert CSV file to Rasa acceptable file formats.

The standard format to be followed while creating a CSV is shown in nlu_sample_format_for_conversion.csv file. This CSV file is converted  to rasa format nlu.md and domain.yml file.


STEPS TO CREATE nlu.md & domain.yml file:
1. Download the whole repo.
2. Open nlu_sample_format_for_conversion.csv that was downloaded.
3. First rows consist of intent names. Add any number of intents in the first row.
4. The succeeding rows. i.e after the intent names row, add all your training phrases/sentences.
5. save the file
6. Open csvtorasa.py and call the function/method create_rasa_nlu(path, nlu_md_path). Don't forget to specify path to the CSV file using the path parameter, and path where the output nlu.md file needs to be created via the nlu_md_path parameter.



Interested in contributing? Please go ahead and address issues or create one.
