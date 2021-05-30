[![python-pipenv](https://github.com/sinlov-auto-action/python-testing-park/workflows/python-pipenv/badge.svg?branch=main)](https://github.com/sinlov-auto-action/python-testing-park/actions/workflows/python-pipenv.yml)

# this is python test code park

- repo: [https://github.com/sinlov-auto-action/python-testing-park](https://github.com/sinlov-auto-action/python-testing-park)

## env

- run on [python pipenv](https://pypi.org/project/pipenv/)

## dev

```bash
pipenv install --three
```

### want proxy of pipenv

just make file `.env` at root of project

```env
PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/
```

> PIPENV_PYPI_MIRROR can change to another URL of proxy 

### simple test run

- code at [tests/test_main.py](tests/test_main.py)

```bash
$ pipenv run test_main
```

