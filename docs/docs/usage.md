## The `sql-unit-test init` command
The idea is to create one place for all of your sql unit tests. Follow the steps below to initialize a sql unit test project folder:

1. If you don't already have a folder to hold your unit tests, create one and cd into it.

    ```cmd
    mkdir <your folder name>
    cd <your folder name>
    ```

2. Then run the following command:
    ```cmd
    sql-unit-test init
    ```
    Once the initialization is complete, you should see the following output:
    ```
    =======================================================================================================================
                                                    SQL Unit Test
    =======================================================================================================================


                                Project successfully initialized in <your folder name>!
    ```
3. You should see three new objects in your directory: a `.gitignore` file, a `.sql-unit-test` folder, and a `sql-unit-test.yaml` configuration file.

## Configuration
The following configuration values can be set by a user. (* = required)

- `app_env`: This doesn't need to be touched unless you are a developer contributing to `sql-unit-test`.
- `uri*`: This is a valid sqlalchemy uri string that points to the database which holds the objects you want to run unit tests against. 
- `target_dir`: This is the directory in which to execute the `sql-unit-test run` command. *Default is the current working directory.*
- `log_level`: This value overrides the log level used. *The default value is `WARN`.*

The most convenient way to set these values is in the `sql-unit-test.yaml` at the root of the project. They can also be set at runtime by passing in the value as an option to the `sql-unit-test run` command. (ex. `sql-unit-test run --uri 'sqlite:///sample//test_database.db'`)

Below is the order of operations that `sql-unit-test run` takes to find the proper config:

1. Checks for config values passed to the command as options.
2. Checks for `sql-unit-test.yaml` in current working directory.
3. Walks up the folder hierarchy until it finds `sql-unit-test.yaml` in the project root or times out after searching for 1 second.
4. Uses defaults for non-required config values.

Therefore, the `uri` config value must *either* be passed as an option at runtime *or* be present in the `sql-unit-test.yaml`, as it is required and has no default value.

## Unit Test Repo Cold setup
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

## Writing sql unit tests
TODO

## `sql-unit-test run`
Running `sql-unit-test` is simple. 

The most convenient way to run it is by setting up `sql-unit-test.yaml` the file with your important config values, and then simply cd'ing into the desired target folder within the unit test repo and running `sql-unit-test` in the command line. 

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

Passing in any of these options will also override config values that are set in the `sql-unit-test.yaml`.
