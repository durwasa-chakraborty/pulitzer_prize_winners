# Pulitzer Prize Winners
Currently, Pulitzer Prize Winners' data is not available through API. This project is a Python-based tool designed to efficiently scrape winners list from categories from specified websites and save them into a structured CSV format. The python tool makes only two HTTPS calls to the website and gets all the cleaning of the data and post processing using internal logic, thus not taxing the website


## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
What things you need to install the software and how to install them:

- python Python 3.x
- pip

## Installation
A step-by-step series of examples that tell you how to get a development environment running.

Clone the repository:

```bash
git clone https://www.github.com/durwasa-chakraborty/pulitzer_prize_winners
cd pulitzer_prize_winners
```

```
python3 -m venv venv
pip install -r requirements.txt
```
### Usage
To run the project, you need to execute the driver script from the src directory:
```
python src/driver.py
```

You can change the URL targeted by the scripts by modifying the URL variable within the relevant Python code file (e.g., src/url_caller.py).

## Contributing
Your contributions are always welcome! 

### Creating Issues
Please use the GitHub issues section to report a bug or request a feature.
- Clearly describe the issue, including steps to reproduce when it is a bug.
- Make sure to mention the expected behavior and the actual behavior.


