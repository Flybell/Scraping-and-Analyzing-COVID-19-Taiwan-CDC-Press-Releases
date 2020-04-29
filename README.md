# Analyzing Taiwan CDC COVID-19 Press Releases


## Intro
Each day, the Taiwan CDC (https://www.cdc.gov.tw/) publishes an English and a Chinese press release reporting each day's newly confirmed case(s). The Chinese press release, in particular, contains a rich and largely formulaic paragraph detailing the key characteristics of the confirmed cases, e.g., gender, where they live, how they got infected, symptom progression and onset date, confirmation date. 

The ultimate goal is to use this data to construct a graph database (with neo4j) and visualize/analyze known transmission clusters. Before that, we need to first glean the relevant press releases from the Taiwan CDC site, store them in a clean text file, and extract data for each case. 

## About this repo

### The Execute.py script 
This script crawls and downloads press releases that are related to COVID-19.
It produces a set of text files, one for each press release, with the following format:

title based on the year-month-date of the press release: 

\d\d\d\d-\d\d-\d\d.txt 

body:

title of the press release

date of the press release

text content of the press release 

### The Process_Data.py will be continuously updated in another repo
Here, it gives you a "taster" of the type of data that can be extracted from these files. 
The script creates a "daily_new_cases.txt" file that prints out the total number of new confirmed cases reported in each day's press release (Note that the first few days have "N/A" because the writing style has not yet taken its current formulaic shape. Data from these files need to be retrieved manually).
