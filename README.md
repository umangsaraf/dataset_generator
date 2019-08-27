# dataset_generator

## STEP 1: Prerequisites
Prerequisites - install the following:

- chromedriver: Make sure that path to chrmodriver is changed to your own path. Change it from the dump_html.py on line 14. Chromedriver can be installed from http://chromedriver.chromium.org



- Python modules: `pip3 install -r requirements.txt`

- This requires java 8 or above to run. Java 8 can be downloaded from: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

## STEP 2: HTML Dump 
Returns a json file containing HTML of all companies
- Make sure that path to chrmodriver is changed to your own path. It can be changed from line 14 on dump_html.py
`eg. path = r'/Users/umangsaraf/Downloads/chromedriver'`

### Usage
`python3 python3 dump_html.py --inputFile <input_file> --outputFile <output_file>`

Inputs
``` --inputFile -- Name of the file that conatins all the links ```

Outputs
``` --outputFile -- Location and name of the file. Save it with .json extension ```

``` eg. python3 dump_html.py --inputFile testfile.txt --outputFile test_dump.json ```

## Step 3: HTML to CSV
Returns a csv file with scraped data of all companies 

### Usage 
`python3 python3 parseSI.py.py --inputFile <input_file> --outputFile <output_file>`

Inputs
``` --inputFile -- Name of the file that conatins the HTML dump ```

Outputs
``` --outputFile -- Location and name of the file. Save it with .csv extension ```

``` eg. python3 parseSI.py --inputFile test_dump.json --outputFile test.csv ```
