# Scraping Taiwan CDC COVID-19 press releases

## Intro
Each day, the Taiwan CDC (https://www.cdc.gov.tw/) publishes an English and a Chinese press release reporting that day's newly confirmed case(s). The Chinese press release, in particular, contains rich and largely formulaic paragraphes detailing the key characteristics of the confirmed cases, e.g., gender, where they live, how they got infected, symptom progression and onset date, confirmation date. The formulaic style of these press releases make it easier to wrangle data with basic regular expressions.

This repo is part of a larger Natural Language Processing project to extract and analyze transmission cluseters in Taiwan based on CDC press releases. The ultimate goal is to use this data to construct a graph database (with neo4j) and visualize/analyze known transmission clusters. Before that, we need to first glean the relevant press releases from the Taiwan CDC site, store them in a clean text file, and extract data for each case.

## About this repo

Two scripts, two method modules, two unit tests (for the methods).

### The Execute.py script
This script crawls and downloads press releases that are related to COVID-19.
It produces a set of text files, one for each press release, with the following format:

title based on the year-month-date of the press release:

\d\d\d\d-\d\d-\d\d.txt

body:

title of the press release

date of the press release

text content of the press release

### The Process_Data.py script
Here, it gives you a "taster" of the type of data that can be extracted from these files.
The script creates a "daily_new_cases.txt" file that prints out the total number of new confirmed cases reported in each day's press release (Note that the first few days have "N/A" because the writing style has not yet taken its current formulaic shape. Data from these files need to be retrieved manually).

## Instructions
1. Download all the files into the same folder.
2. Make sure you have the following libraries installed: beautifulsoup & request

In command line & your virtual environment:

`$ pip install requests`

`$ pip install beautifulsoup4`

3. Run "Execute.py"
4. For a teaser analysis, run "Process_Data.py"
