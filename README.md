# `sql-unit-test`
## Overview
A CLI tool that permits data teams that aren't quite at the point where they can implement dbt to still adopt test driven development best practices.

## Background 
The idea that drove the development of this tool is the notion that we should be writing unit tests for each object in our datawarehouse so that that asset is returning data that matches the expectations of the stakeholders, aka. the business requirements. Furthermore, these unit tests should be retained in some place (ideally a source controlled place) so that we can check if new developments break requirements from past developments.

There are tools on the market that accomplish this goal very effectively (ex. [dbt](https://docs.getdbt.com/)), however, for many organizations, the road to implementing dbt is a long one. In the meantime, it didn't seem like an option to simply opt out of what is (luckily) becoming a fundamental best practice in the data world. 

While it may not be as convenient and quick as declaring tests in dbt, `sql-unit-test` is certainly is a big step in the right direction. 

## Installion

To install sql-unit-test, it is recommended to use pip:

```
pip install sql-unit-test
```

## Usage

### Unit Test Repo Cold setup
This tool is made to be used in a repository with a particular structure. 

The recommended repo structure is one that models the interior structure of your data warehouse. This helps greatly with organizing the unit tests. Here's an example, where our data warehouse contains 3 databases. 

```
.
├───prod # db level
│   ├───sales # schema level
│   │   ├───factOrders # object level
│   │   └───...
│   └───...
│       └───...
├───raw # db level
│   ├───crm # schema level
│   │   ├───customers # object level
│   │   └───...
│   └───...
│       └───...
└───stage # db level
    ├───crm # schema level
    │   ├───stg_customers # object level
    │   └───...
    └───...
        └───...
```


While this is the recommended unit test repo structure, the level at the root of the repository does not necessarily have to be database. It is valid to split up unit tests in any number of ways. The only hard fast requirement to be able to run `sql-unit-test` is that the test directory contains *only* valid sql unit test files. 

### Writing sql unit tests
TODO


### Tool Configuration
To get started using `sql-unit-test` in your unit test repository, create a `.env` folder at the root of the repo. The following values can be set from the `.env`.

```
URI=<valid sqlalchemy uri> 
TARGET_DIR=<path to a valid test dir>
LOG_LEVEL=<CRITICAL/ERROR/WARN/DEBUG/INFO> # override default log level here
```

### Running `sql-unit-test`
Running `sql-unit-test` is simple. 

The most convenient way to run it is by setting up a .env file with your important config values, and then simply cd'ing into the desired target folder within the unit test repo and running `sql-unit-test` in the command line. 

It is also, however, possible to forget about the `.env` file altogether and pass in those config values at runtime. 

Let's take a look at the usage output straight from the command line:

```
PS J:\Justin\internal_tools\sql-unit-test> sql-unit-test --help
Usage: sql-unit-test [OPTIONS]

Options:
  --uri TEXT         A sqlalchemy URI that will override the URI provided in
                     .env.
  --target_dir TEXT  The target directory in which run sql-unit-test. Default
                     is the current directory from which the sql-unit-test
                     command is run.
  --filepath TEXT    A path to a single sql unit test file.
  --help             Show this message and exit.
  ```

Passing in any of these options will also override config values that are set in the `.env`, if one is present in the repo.


## Contributing

### Environment setup
1. Clone the repository in your development environment.
2. Install [poetry](https://python-poetry.org/docs/#installation) if is not already installed in your environment.
3. Run the `poetry install` command to install the project dependencies. 
4. Create a `.env` file at the root of the repo, and put the following values in. 
    ```.env
    APP_ENV = 'dev' # Automatically sets dev uri that points at sqlite db in sample/ and target_dir to be the sample/playlists/ folder, containing a sample unit test.

    LOG_LEVEL = <CRITICAL/ERROR/WARN/INFO/DEBUG> # Used to override default of WARN, if desired
    ```
5. Develop!
6. To run the package use poetry: `poetry run python sql_unit_test/main.py`

### Tests

TODO



 