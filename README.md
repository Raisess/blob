# blob

A simple and small blog generator for Github Pages.

## Dependencies

- [Python 3.10.x >=](https://www.python.org/)
- [yacli](https://github.com/Raisess/yacli)

## Getting started

Installing:

```shell
$ git clone https://github.com/Raisess/blob
$ cd blob
$ sudo ./install.py
$ blob help
```

Usage:

```shell
$ blob init my-blog
$ cd my-blog
$ blob post my-post-title
$ blob serve
```

check `http://localhost:8000/blog` in a browser, edit the generated file on the `inputs/` folder,
execute the command `blob generate` and the commit the files to your github repository, have fun.
