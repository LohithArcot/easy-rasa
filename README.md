# Easy-Rasa

## Why?
To make it easier to create rasa`nlu.md` and `domain.yml` file.
## What is it?
This package helps you convert a preformatted `.csv` file to Rasa acceptable file formats.

The standard format to be followed while creating a `.csv` is shown in `nlu_sample_format_for_conversion.csv` file. This CSV file is converted  to rasa format `nlu.md` and `domain.yml` file.

Run command `download_csv()` to download sample file that you can fill.

```
from easy-rasa import download_csv
download_csv()
```
This will download a preloaded file called `nlu_sample_format_for_conversion.csv`. Search the directory where you ran the `download_csv()` command to find the file.
Fill the `.csv` file by follwing these instructions:
- First rows consist of intent names. Add any number of intents in the first row.
- The succeeding rows. i.e. after the intent names row, add all your training phrases/sentences.
- save the file

### STEPS TO CREATE `nlu.md` & `domain.yml` file:

- Call the function/method `create_rasa_nlu(csv_path, create_files_path)`. Don't forget to specify path to the CSV file using the path parameter, and path where the output files need to be created via the `create_files_path` parameter.

```
from easy-rasa import create_rasa_files
create_rasa_files(csv_path, create_files_path)
#csv_path and create_files_path can both be ./
```
Check the directory (create_files_path) to file respective `nlu.md` and `domain.yml` files.
