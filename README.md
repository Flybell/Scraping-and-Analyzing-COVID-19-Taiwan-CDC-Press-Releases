#Analyzing Taiwan CDC COVID-19 Press Releases

Each day, the Taiwan CDC (https://www.cdc.gov.tw/) publishes an English and a Chinese press release reporting each day's newly confirmed case(s). The Chinese press release, in particular, contains a rich and largely formulaic paragraph detailing the key characteristics of the confirmed cases, e.g., gender, where they live, how they got infected, symptom progression and onset date, confirmation date. 

The ultimate goal is to use this data to construct a graph database (with neo4j) and visualize/analyze known transmission clusters. Before that, we need to first glean the relevant press releases from the Taiwan CDC site, store them in a clean text file, and extract data for each case. 

