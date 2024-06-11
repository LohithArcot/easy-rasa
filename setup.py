from setuptools import setup, find_packages

setup(
    name="csvtorasa",
    version="0.1.1",
    author='Lohith Arcot',
    author_email='lohith.arcot@gmail.com',
    description='A package that converts .csv file to rasa compatible file',
    long_description='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=2.2.2",
    ],
    entry_points={
        # "console_scripts":[
        #     "csvtorasa = csvtorasa:create_rasa_files"
        # ]
    },
)
