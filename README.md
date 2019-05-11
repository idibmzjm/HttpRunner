# apiautotest


[![LICENSE](https://img.shields.io/github/license/apiautotest/apiautotest.svg)](https://github.com/apiautotest/apiautotest/blob/master/LICENSE) [![travis-ci](https://travis-ci.org/apiautotest/apiautotest.svg?branch=master)](https://travis-ci.org/apiautotest/apiautotest) [![coveralls](https://coveralls.io/repos/github/apiautotest/apiautotest/badge.svg?branch=master)](https://coveralls.io/github/apiautotest/apiautotest?branch=master) [![pypi version](https://img.shields.io/pypi/v/apiautotest.svg)](https://pypi.python.org/pypi/apiautotest) [![pyversions](https://img.shields.io/pypi/pyversions/apiautotest.svg)](https://pypi.python.org/pypi/apiautotest)

apiautotest is an HTTP(S) protocol-oriented universal testing framework. Write testing scripts in `YAML/JSON` once, you can then achieve automated testing, performance testing, online monitoring, continuous integration and other testing needs.

Formerly known as `ApiTestEngine`.

## Design Philosophy

- Take full reuse of Python's existing powerful libraries: [`Requests`][Requests], [`unittest`][unittest] and [`Locust`][Locust].
- Convention over configuration.
- Pursuit of high rewards, write once and achieve a variety of testing needs

## Key Features

- Inherit all powerful features of [`Requests`][Requests], just have fun to handle HTTP(S) in human way.
- Define testcases in YAML or JSON format in concise and elegant manner.
- Record and generate testcases with [`HAR`][HAR] support. see [`har2case`][har2case].
- Supports `function`/`variable`/`extract`/`validate` mechanisms to create full test scenarios.
- Supports perfect hook mechanism.
- With `debugtalk.py` plugin, module functions can be auto-discovered in recursive upward directories.
- Testcases can be run in diverse ways, with single testcase, multiple testcases, or entire project folder.
- Test report is concise and clear, with detailed log records.
- With reuse of [`Locust`][Locust], you can run performance test without extra work.
- CLI command supported, perfect combination with `CI/CD`.

## Documentation

apiautotest is rich documented.

- [`User documentation in English (outdated)`][user-docs-en]
- [`中文用户使用手册`][user-docs-zh]
- [`开发历程记录博客`][development-blogs]

## How to Contribute

1. Check for [open issues](https://github.com/apiautotest/apiautotest/issues) or [open a fresh issue](https://github.com/apiautotest/apiautotest/issues/new/choose) to start a discussion around a feature idea or a bug.
2. Fork [the repository](https://github.com/apiautotest/apiautotest) on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request, you will then become a [contributor](https://github.com/apiautotest/apiautotest/graphs/contributors) after it gets merged and published.

## Subscribe

关注 apiautotest 的微信公众号，第一时间获得最新资讯。

![][qrcode_for_apiautotest]

[Requests]: http://docs.python-requests.org/en/master/
[unittest]: https://docs.python.org/3/library/unittest.html
[Locust]: http://locust.io/
[PyUnitReport]: https://github.com/apiautotest/PyUnitReport
[Jenkins]: https://jenkins.io/index.html
[har2case]: https://github.com/apiautotest/har2case
[user-docs-en]: http://apiautotest.org/
[user-docs-zh]: http://cn.apiautotest.org/
[development-blogs]: http://debugtalk.com/tags/apiautotest/
[HAR]: http://httparchive.org/
[Swagger]: https://swagger.io/
[Postman Collection Format]: http://blog.getpostman.com/2015/06/05/travelogue-of-postman-collection-format-v2/
[qrcode_for_apiautotest]: https://raw.githubusercontent.com/apiautotest/apiautotest/master/docs/images/qrcode_for_apiautotest.jpg
