# Stellic Automated Testing (powered by Selenium)

## Pre-requisite

Python 3.8 or greater

## Virtual Environment


### Windows

1. Install virtualenv
    ```shell script
    pip install virtualenv
    ```
2. Create virtual environment called 'env'
    ```shell script
    virtualenv env
    ```
    or 
    ```shell script
    python -m venv env --without-pip
    ```
3. Activate virutal environment
    ```shell script
    env\Scripts\activate
    ```

4. Install requirements inside virtual environment
    ```shell script
    pip install -r requirements.txt
    ```
   
### Run Test Suite

1. To run all tests as a suite and publish a html report, go to the root and run

    ```shell script
    python main.py
    ```
2. To run all test cases
    ```shell script
    python -m unittest testCases
    ```
   
3. To run a specific test case
    ```shell script
    python -m unittest testCases.test_courses
    ```
   
#### For development

Format code using:
1. Black
    ```shell script
    black --config=.black.toml .
    ```
2. Isort
    ```shell script
    isort --settings-file=.isort.cfg pageObjects/ testCases/ utilities/ *.py
    
    ```
3. Pylint
```shell script

```