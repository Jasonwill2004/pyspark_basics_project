# PySpark CSV Data Processing

## Project Overview

This project demonstrates how to use PySpark to process and analyze CSV data. The main tasks include filtering data, grouping and aggregating data, and counting transactions per category. The project is designed to showcase the capabilities of PySpark for handling large datasets and performing complex data transformations.

## Table of Contents

- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6 or higher
- Apache Spark 3.0 or higher
- Java 8 or higher

### Setting Up the Virtual Environment

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd pyspark_basics_project
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that the CSV file (`data.csv`) is placed in the project directory.

2. Run the PySpark script:
    ```sh
    python pyspark_basics.py
    ```

3. The script will perform the following tasks:
    - Load data from the CSV file.
    - Display the original data.
    - Filter transactions where the amount is greater than 150.
    - Group and aggregate data to show total spending per customer.
    - Count transactions per category.

## Features

- **Data Loading**: Load data from a CSV file with headers and inferred schema.
- **Data Filtering**: Filter transactions based on a specified condition.
- **Data Aggregation**: Group and aggregate data to calculate total spending per customer.
- **Data Counting**: Count the number of transactions per category.

## Screenshots

### Original Data
<img width="415" alt="Screenshot 2025-03-21 at 8 23 30 PM" src="https://github.com/user-attachments/assets/79607b30-ba88-4c3e-b422-e5a74321265b" />

### Filtered Data (Amount > 150)
<img width="304" alt="Screenshot 2025-03-21 at 8 23 49 PM" src="https://github.com/user-attachments/assets/9c2e094a-2088-4e3b-87e8-27a9c7742e43" />

### Total Spending Per Customer
<img width="271" alt="Screenshot 2025-03-21 at 8 24 13 PM" src="https://github.com/user-attachments/assets/f5698cac-ebd9-4d0a-a1d3-53f35c33d47c" />

### Transaction Count Per Category
<img width="319" alt="Screenshot 2025-03-21 at 8 24 41 PM" src="https://github.com/user-attachments/assets/b91752ed-e935-45bb-9e9b-c2772ecbe7f3" />

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
