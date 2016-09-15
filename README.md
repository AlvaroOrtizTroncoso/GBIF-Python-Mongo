# GBIF-Python-Mongo
Scripts for using GBIF data in combination with MongoDB and Python

Most of this can be done using plain Bash. However, my long-term goal is to automate some processes, so I'm using GNU Make.

## Dependencies
* Python 3
* GNU Make
* Mongo DB

## Import GBIF occurence data into a Mongo database
1. Download GBIF occurence data as .csv. 
2. Using GNU make, do:

```bash
make -f tools/build import host=<host> db=<db-name> collection=<collection-name> file=<occurences-file-path>
```

## TODO: Measure taxonomic diversity 
There are several possible definitions of taxonomic diversity. The simplest definition is the number of species within a region (species richness).
To create a spreadsheet with species count per taxon grade, do:
1. Download GBIF occurence data as .csv. 
2. Import the data into the local Mongo database as shown above.
3. Using GNU make, do:
```bash
make -f tools/build diversity output=<csv-file-path>
```
This will create a .csv file with species count per taxon grade.

## Run tests
To run all tests, start mongo and then using GNU make do:

```bash
make -f tools/test
```

or, to run test using the "green" test runner, with test coverage do: 

```bash
make -f tools/test green
```

## External links
GNU Make Manual:
https://www.gnu.org/software/make/manual/

"Green" test runner docs:
https://github.com/CleanCut/green/blob/master/cli-options.txt