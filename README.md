# GBIF-Python-Mongo
Scripts for using GBIF data in combination with MongoDB and Python

Most of this can be done using plain Bash. However, my long-term goal is to automate some processes, so I'm using GNU Make.

## Dependencies
* Python 3
* GNU Make
* Mongo DB

## Import GBIF occurence data into a Mongo database
Download GBIF occurence data as .csv. Using GNU make, do:

```bash
make -f tools/import host=<host> db=<db-name> collection=<collection-name> file=<occurences-file-path>
```

## Run tests
To run all tests, using GNU make do:

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