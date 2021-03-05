# terminalvelocity

[![Build Status](https://travis-ci.org/n8henrie/terminalvelocity.svg?branch=master)](https://travis-ci.org/n8henrie/terminalvelocity)

A fast note-taking app for the UNIX terminal

- Python >= 3.6
- Original author: Sean Hammond, GPLv3
- Modifications in this fork: Nathan Henrie, MIT
- Documentation: https://terminalvelocity.readthedocs.org

## Features

Includes a pyoxidizer build script; the pyoxidizer compiled version to reduces
loading time a fair amount.

## Introduction

Terminal Velocity is a fast note-taking app for the UNIX terminal, that focuses
on letting you create or find a note as quickly and easily as possible, then
uses your `$EDITOR` to open and edit the note. It is heavily inspired by the OS
X app [Notational Velocity](http://notational.net). For screenshots and
features, see the [Terminal Velocity
website](http://vhp.github.com/terminalvelocity).

Note: This is a Python3 fork, minimally modified from
<https://github.com/vhp/terminal_velocity>, which is the currently maintained
Python2 fork of the original at <https://github.com/seanh/terminal_velocity>.
In order to allow `pip` installation as a separate package from the Python2
version, the package name has been changed from `terminal_velocity` to
`terminalvelocity`.

## Dependencies

- Python >= 3.6
- See `requirements.txt`

## Quickstart

1. Install: `python3 -m pip install terminalvelocity`
1. Show options: `tv -h`
1. Run: `tv /path/to/notes_directory/`
1. Quit with `Ctrl c`

### Development Setup

1. Clone the repo: `git clone https://github.com/n8henrie/terminalvelocity &&
   cd terminalvelocity`
1. Make a virtualenv: `python3 -m venv venv`
1. `venv/bin/pip install -e .[dev]`

## Configuration

- TODO

## Acknowledgements

I've done minimal work, just a little refactorying for Python3. All credit goes
to:

- <https://github.com/vhp/terminal_velocity>
- <https://github.com/seanh/terminal_velocity>

Additional contributors will be acknowledged in [AUTHORS.md][].

## Troubleshooting / FAQ

- How can I install an older / specific version of terminalvelocity?
    - Install from a tag:
        - pip install git+git://github.com/n8henrie/terminalvelocity.git@v0.1.0
    - Install from a specific commit:
        - pip install git+git://github.com/n8henrie/terminalvelocity.git@abc123def456ghi789
