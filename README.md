# TP Software Testing - GL4 2021/2022

## Python unit testing

Can be found under `python-unit-and-int-testing/unit-tests`

* To launch tests and retrieve coverage

  ```bash
  cd python-unit-and-int-testing/unit-tests
  make init
  make unit-tests
  ```


## Python integration testing 

Can be found under `python-unit-and-int-testing/integration-tests`

* To launch tests and retrieve coverage

  ```bash
  cd python-unit-and-int-testing/unit-tests
  make init
  make integration-tests
  ```


## e2e testing 

Can be found under `e2e-tests/cypress/integration/scrap.spec.js`

* To launch tests (scrapping)

  ```bash
  cd e2e-tests
  npm install
  node_modules/.bin/cypress run
  node_modules/.bin/cypress open . # To debug
  ```

## UAT 

Example can be found under `uat-example`

> Full guide can be found [here](https://usersnap.com/blog/user-acceptance-testing-example/)
