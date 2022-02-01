# beancount-stubs

<p align="center">
    <a href="https://github.com/jmgilman/beancount-stubs/actions/workflows/ci.yml">
        <img src="https://github.com/jmgilman/beancount-stubs/actions/workflows/ci.yml/badge.svg"/>
    </a>
    <a href="https://pypi.org/project/beancount-stubs">
        <img src="https://img.shields.io/pypi/v/beancount-stubs"/>
    </a>
</p>

> A package containing stub files for the [beancount][1] package.

## Usage

Install the package:

```shell
$> pip install beancount-stubs
```

Run `mypy`:

```shell
$> mypy .
```

The `mypy` binary will automatically detect the stubs included in the installed
package and use them when asserting against the beancount package. Note that
many of the subpackages in the beancount package do not have stubs and `mypy`
will complain about the missing stubs. To disable this error on an unsupported
package, use the following syntax:

```python
from beancount.ops import validation  # type: ignore
```

## Support

The following subpackages/modules are currently supported:

* `beancount.loader`
* `beancount.core.*`
* `beancount.query.numberify`
* `beancount.query.query`
* `beancount.query.query_compile`
* `beancount.query.query_execute`

## Contributing

Check out the [issues][2] for items needing attention or submit your own and
then:

1. [Fork the repo](https://github.com/jmgilman/beancount-stubs/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

[1]: https://github.com/beancount/beancount
[2]: https://github.com/jmgilman/beancount-stubs/issues
