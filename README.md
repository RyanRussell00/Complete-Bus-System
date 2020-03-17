# Complete-Bus-System

Created by Team MS Excel: [Ryan Russell](https://github.com/RyanRussell00), [Illarion Eremenko](https://github.com/nerdromere), [Phillip Ovanesyan](https://github.com/phillipov), [Mitchell Dang](https://github.com/mduw)

## Overview
The Complete Bus System is connected and deployed to Amazon Web Services (AWS). To start the program just run the `UserInterface.py` file using the command: `python3 UserInterface.py`

## User Interface (UI)

### Requirements
* Python 3.x
* Python MySQL Connector ([install instructions here](https://pynative.com/install-mysql-connector-python/))
* Linux, Mac, or Windows OS

### Running the UI
1. Navigate to the `CBS` folder (`Complete-Bus-System/CBS-Programs/venv/CBS`)
2. Open a terminal in that folder and type: `python3 UserInterface.py`

## Automated Testing Program

### Requirements
* Python 3.x
* Python MySQL Connector ([install instructions here](https://pynative.com/install-mysql-connector-python/))
* Linux, Mac, or Windows OS

### Running the Automated Tests
1. Navigate to the `Testing` folder (`Complete-Bus-System/CBS-Programs/venv/Testing/`)
2. Open a terminal in that folder and type: `python3 tests.py`
3. Modify the tests in the directory: `Complete-Bus-System/CBS-Programs/auto-test-files/`

### .Tests Files
* Files containing the queries to be executed must end in the extension: `.Tests` 
* All statements must end with a semicolon ';'
* Multi-line statements are allowed but the line must not break in the middle of words.
* ONLY USE # or -- FOR COMMENTS.
* The query will expect the output at the same position in the expected file.
*   For example: The 3rd query in this file will expect the 3rd line in the 'Expected' file to be its output.


### .Expected Files
* Expected outputs must end in `.Expected`
* Type output EXACTLY as you'd see it on output. No semicolons, no quotes (unless expected),  etc.
* ONLY USE # or -- FOR COMMENTS.
* The queries will expect the output at the same position in the expected file. (line numbers dont matter)
*   For example: The 3rd query in the queries file will expect the 3rd line in this file to be its output.

#### FORMATTING FOR EXPECTED
* **DO NOT END WITH SEMICOLON**
* If expecting multiple columns: Use a comma to seperate values, keep expected result on 1 single line
* Strings: use a single quote around the 'string'
* DateTime: If single digit day/month **DO NOT put 0 in front.**
* DateTime: USE THIS FORMAT EXACTLY: datetime.date(YYYY, (M)M, (D)D) 
* 	Do not put 0 in front of single digit Month or Day
* For NULL values write: None
* Parentheses around expected output is optional