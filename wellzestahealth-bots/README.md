# Wellzesta bots

Here, we have all source code to send messages to user through DotMessage. It's written in python and we keep all modulirized by services dispatchers.

## Setup

```bash
$ make setup
```

## Activate environment

```bash
$ source activate wellzestahealth-bots
```

## Install other dependencies (environment must be activated)

```bash
$ make install
```

## Start scheduler

```bash
$ make scheduler
```

See Makefile to know other commands

## Updating scheduler

open `src/executors/scheduler.py` to edit


```
├── LICENSE
├── Makefile           <- Makefile with commands like `make install` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── environment.yml    <- The requirements file for reproducing the conda environment
│                         
│
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── executors      <- Python commands to run from makefile
    |  |
    |  ├── scheduler   <- Scheduler
    |
    ├── models         <- Classes to interact with GraphQL API
    |
    ├── services       <- All dispatchers to send DotMessages
    |
    └── utils          <- Files to help develop 
```

## Contributing

We would :heart: your contributing!

[Follow github guides for forking a project](https://guides.github.com/activities/forking/)

[Follow github guides for contributing open source](https://guides.github.com/activities/contributing-to-open-source/#contributing)

[Squash pull request into a single commit](http://eli.thegreenplace.net/2014/02/19/squashing-github-pull-requests-into-a-single-commit/)

## License

Wellzestahealth Bots is released under the [MIT license](https://choosealicense.com/licenses/mit).
