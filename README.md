# Work Order Automator

## CS312 (Fall '23) – Group Project

### Overview

The **Work Order Automator** is a Python-based tool developed as part of a group project in CS312. This system automates the process of analyzing electronic repair orders and converting them into structured work orders. By extracting key customer and device information, the project aims to improve efficiency in handling repair requests.

### Features

- **Automated Data Extraction**: Parses customer orders to extract:
  - Customer details (name, contact information)
  - Device specifications (brand, model, serial number, color, age)
  - Reported issues and symptoms
  - Testing results (failures, pre-existing damage, additional observations)
  - Storage location or depot transfer details
- **Structured Output**: Converts unstructured customer inputs into a structured format suitable for generating work orders.
- **Interactive User Input**: Guides users through missing information collection via command-line prompts.

### Installation

1. Clone this repository:
2. Navigate to the project directory:
3. Ensure you have Python installed (version 3.x recommended).
4. Install any dependencies (if applicable):

### Usage

Run the main script to input and process repair orders:

The program will prompt for relevant details and save the structured output to `customer_device_info.txt`.

### File Structure

- main.py – Primary script handling data extraction and structuring.
- Software.py – Alternative implementation of the order processing logic.
- requirements.txt – (To be added if any external dependencies are required)
- README.md – Documentation for the project.

### Future Improvements

- Integrating with a database for long-term storage of work orders.
- Implementing a GUI or web interface for user-friendly interaction.
- Automating work order generation as PDF documents.
- Enhancing error handling and data validation.

### Contributors

This project was developed as part of a group effort in **CS312 (Fall '23)**. Team members worked together to design, develop, and test the functionality of the Work Order Automator.

### License

This project is open-source&#x20;

