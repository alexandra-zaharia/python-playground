# Packaging a standalone Python script

This is the code accompanying my blog post [Custom logger in Python for stdout and/or file log](https://alexandra-zaharia.github.io/posts/custom-logger-in-python-for-stdout-and-or-file-log).

Run `custom_logger.py` and check the newly created `logs/` directory.

To check what happens when writing to stdout if it is not a true TTY, redirect standard output as follows:

```bash
python custom_logger.py > test.out
```

When you `cat test.out` you will see that the ANSI color codes are not printed because we took that extra step in `test_verbose()` to check whether `sys.stdout.isatty()`.