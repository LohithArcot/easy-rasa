from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="easy-rasa",
    version="1.0",
    author='Lohith Arcot',
    author_email='lohith.arcot@gmail.com',
    description='A package that converts .csv file to rasa compatible file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=2.2.2",
    ],
    entry_points={
        # "console_scripts":[
        #     "easy-rasa = easy-rasa:create_rasa_files"
        # ]
    },
)
