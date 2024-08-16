# MicroPython Stubs: Enhance Your Development Experience

[![Documentation Status](https://readthedocs.org/projects/micropython-stubs/badge/?version=latest)](https://micropython-stubs.readthedocs.io/en/latest/?badge=latest "Document build status badge")
[![Star on GitHub](https://img.shields.io/github/stars/josverl/micropython-stubs.svg?style=social)](https://github.com/josverl/micropython-stubs/stargazers)
[![All Contributors](https://img.shields.io/badge/all_contributors-19-green.svg?style=flat-square)](#Contributions)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black "Black badge")
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/) 
[![Checked with pyright](https://github.com/Josverl/micropython-stubs/actions/workflows/test_stub_quality.yml/badge.svg?branch=main)](https://microsoft.github.io/pyright/) 

<img src="docs/img/colorstubs.jpg"
     alt="pencil stubs"
     width=0%
     height=20%Welcome to the MicroPython Stubs repository! Here, you’ll find a treasure trove of over 3,000 stub files generated by the MicroPython-Stubber tool. Whether you’re just starting out or a seasoned developer, these stubs are designed to supercharge your MicroPython development process.

 What Are Stubs?
Stubs are like cheat sheets for your code. They provide hints, auto-completion, and static type checking, making your life as a developer easier and more productive. Here’s what you can expect from these MicroPython stubs:

Faster Coding: With stubs, you’ll write code more quickly and confidently. No more guessing function names or parameters!

Fewer Errors: Stubs help catch mistakes early. If you provide incorrect arguments, you’ll get immediate feedback.

Code Completion: Say goodbye to endless Googling. Stubs provide context-aware auto-completion, even for board-specific features.

Static Type Checking: By adding typing information, you’ll catch type-related bugs before they cause runtime issues.

DEMO NEEDS UPDATE

Demo using VSCode:
￼

 Installation
 Option 1: Typings Folder (Recommended)
Install the stubs in a typings folder within your project:

pip install -U micropython-<port>[-<board>]stubs --no-user --target ./typings
Enjoy enhanced code completion and type checking!

 Option 2: Virtual Environment (venv)
Activate your virtual environment (if you’re using one).

Install the stubs:

pip install -U micropython-<port>[-<board>]stubs --no-user
Dive into the world of MicroPython development with confidence!

[TIPS]

Requirements File: Consider adding a requirements-dev.txt file to your project with the specified stubs. It’ll help keep your development environment consistent.

More examples:

pip install -U micropython-stm32-stubs --target typings --no-user

# Install stubs for a specific version.

pip install -U micropython-esp32-stubs==1.20.0.* --target typings --no-user

# Install stubs for a specific board.

pip install -U micropython-rp2-pico_w-stubs --target typings --no-user
 S
     style="float: right; margin-right: 10px;" />

Welcome to the MicroPython Stubs repository! Here, you’ll find a treasure trove of over 3,000 stub files generated by the MicroPython-Stubber tool. Whether you’re just starting out or a seasoned developer, these stubs are designed to supercharge your MicroPython development process.

## What Are Stubs?

Stubs are like cheat sheets for your code. They provide hints, auto-completion, and static type checking, making your life as a developer easier and more productive. Here’s what you can expect from these MicroPython stubs:

1. **Faster Coding**: With stubs, you’ll write code more quickly and confidently. No more guessing function names or parameters!
2. **Fewer Errors**: Stubs help catch mistakes early. If you provide incorrect arguments, you’ll get immediate feedback.
3. **Code Completion**: Say goodbye to endless Googling. Stubs provide context-aware auto-completion, even for board-specific features.
4. **Static Type Checking**: By adding typing information, you’ll catch type-related bugs before they cause runtime issues.

<mark>DEMO NEEDS UPDATE</mark>

**Demo using VSCode:**
![demo](docs/img/demo.gif)

#### Installation

### Option 1: Typings Folder (Recommended)

1. Install the stubs in a `typings` folder within your project:
   
   ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user --target ./typings
   ```

2. Enjoy enhanced code completion and type checking!

### Option 2: Virtual Environment (venv)

1. Activate your virtual environment (if you’re using one).

2. Install the stubs:
   
   ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user
   ```

3. Dive into the world of MicroPython development with confidence!

## 

> [TIPS]
> 
> **Requirements File**: Consider adding a `requirements-dev.txt` file to your project with the specified stubs. It’ll help keep your development environment consistent.

More examples:

```bash
pip install -U micropython-stm32-stubs --target typings --no-user

# Install stubs for a specific version.
pip install -U micropython-esp32-stubs==1.20.0.* --target typings --no-user

# Install stubs for a specific board.
pip install -U micropython-rp2-pico_w-stubs --target typings --no-user
```

## Static Type Checking

Take it up a notch! Combine the stubs with Python static type checkers like Pylance, Pyright, or Mypy. You’ll catch errors even before running your code.

For more details how to use the stubs please refer to [the documentation on RTD](https://micropython-stubs.readthedocs.io/en/latest/20_using.html)

##](docs/firmware_grp.md)

<mark>TODO: Add Link</mark>

## Explore Available Stubs

Curious about which versions, ports, and boards are covered? Check out the [online viewer](https://flatgithub.com/Josverl/micropython-stubs/?filename=all_modules.json) or search for [MicroPython stub packages on PyPI](PYPI).

For a comprehensive overview of all stubs, dive into the documentation on [the documentation on read the docs](https://micropython-stubs.readthedocs.io/en/latest/firmware_grp.html).

## Sponsoring

In order to build accurate stubs I need access to a board to flash it with a specific version of micropython an run part of the stubbing software on the board.

You can help me by: 

- running the software and sharing a PR with the generated MCU stubs,

- sending me a spare board you may have,

- or by sponsoring me though Github

## Contributors

Thanks to everyone that has submitted stubs or other relevant pieces of code and information, or published relevant stubs on pypi or github.

Add authors of typings.py

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- prettier-ignore-start -->

<!-- markdownlint-disable -->

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Josverl"><img src="https://avatars2.githubusercontent.com/u/981654?v=4?s=100" width="100px;" alt="Jos Verlinde"/><br /><sub><b>Jos Verlinde</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/commits?author=josverl" title="Code">💻</a> <a href="#stubs-josverl" title="MicroPython stubs">📝</a> <a href="#test-josverl" title="Test">✔</a> <a href="#tool-josverl" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://micropython.org/"><img src="https://avatars1.githubusercontent.com/u/6298560?v=4?s=100" width="100px;" alt="MicroPython"/><br /><sub><b>MicroPython</b></sub></a><br /><a href="#data-micropython" title="Data">🔣</a> <a href="#stubs-micropython" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/loboris"><img src="https://avatars3.githubusercontent.com/u/6280349?v=4?s=100" width="100px;" alt="Boris Lovosevic"/><br /><sub><b>Boris Lovosevic</b></sub></a><br /><a href="#data-loboris" title="Data">🔣</a> <a href="#stubs-loboris" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pfalcon"><img src="https://avatars3.githubusercontent.com/u/500451?v=4?s=100" width="100px;" alt="Paul Sokolovsky"/><br /><sub><b>Paul Sokolovsky</b></sub></a><br /><a href="#data-pfalcon" title="Data">🔣</a> <a href="#stubs-pfalcon" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pycopy"><img src="https://avatars0.githubusercontent.com/u/67273174?v=4?s=100" width="100px;" alt="pycopy"/><br /><sub><b>pycopy</b></sub></a><br /><a href="#data-pycopy" title="Data">🔣</a> <a href="#stubs-pycopy" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pycom"><img src="https://avatars2.githubusercontent.com/u/16415153?v=4?s=100" width="100px;" alt="Pycom"/><br /><sub><b>Pycom</b></sub></a><br /><a href="#infra-pycom" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BradenM"><img src="https://avatars1.githubusercontent.com/u/5913808?v=4?s=100" width="100px;" alt="Braden Mars"/><br /><sub><b>Braden Mars</b></sub></a><br /><a href="#stubs-BradenM" title="MicroPython stubs">📝</a> <a href="#test-BradenM" title="Test">✔</a> <a href="#tool-BradenM" title="Tools">🔧</a> <a href="#platform-BradenM" title="Packaging/porting to new platform">📦</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pfalcon"><img src="https://avatars3.githubusercontent.com/u/500451?v=4?s=100" width="100px;" alt="Paul Sokolovsky"/><br /><sub><b>Paul Sokolovsky</b></sub></a><br /><a href="#stubs-pfalcon" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dastultz"><img src="https://avatars3.githubusercontent.com/u/4334042?v=4?s=100" width="100px;" alt="Daryl Stultz"/><br /><sub><b>Daryl Stultz</b></sub></a><br /><a href="#stubs-dastultz" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://patrickwalters.us/"><img src="https://avatars0.githubusercontent.com/u/4002194?v=4?s=100" width="100px;" alt="Patrick"/><br /><sub><b>Patrick</b></sub></a><br /><a href="#test-askpatrickw" title="Test">✔</a> <a href="#stubs-askpatrickw" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://comingsoon.tm/"><img src="https://avatars0.githubusercontent.com/u/13251689?v=4?s=100" width="100px;" alt="Callum Jacob Hays"/><br /><sub><b>Callum Jacob Hays</b></sub></a><br /><a href="#example-CallumJHays" title="Examples">💡</a> <a href="#research-CallumJHays" title="Research">🔬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RonaldHiemstra"><img src="https://avatars.githubusercontent.com/u/17012831?v=4?s=100" width="100px;" alt="Ronald Hiemstra"/><br /><sub><b>Ronald Hiemstra</b></sub></a><br /><a href="#stubs-ronaldHiemstra" title="MicroPython stubs">📝</a> <a href="#content-ronaldHiemstra" title="Content">🖋</a> <a href="https://github.com/Josverl/micropython-stubs/commits?author=ronaldHiemstra" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cpwood"><img src="https://avatars.githubusercontent.com/u/13966104?v=4?s=100" width="100px;" alt="Chris Wood"/><br /><sub><b>Chris Wood</b></sub></a><br /><a href="#stubs-cpwood" title="MicroPython stubs">📝</a> <a href="#tool-cpwood" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thingslu"><img src="https://avatars.githubusercontent.com/u/34967785?v=4?s=100" width="100px;" alt="thingslu"/><br /><sub><b>thingslu</b></sub></a><br /><a href="#stubs-thingslu" title="MicroPython stubs">📝</a> <a href="#test-thingslu" title="Test">✔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/WerdoxDev"><img src="https://avatars.githubusercontent.com/u/32638453?v=4?s=100" width="100px;" alt="Matin Tat"/><br /><sub><b>Matin Tat</b></sub></a><br /><a href="#test-WerdoxDev" title="Test">✔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/robertoetcheverryr"><img src="https://avatars.githubusercontent.com/u/63941860?v=4?s=100" width="100px;" alt="Roberto Jose Etcheverry Romero"/><br /><sub><b>Roberto Jose Etcheverry Romero</b></sub></a><br /><a href="#test-robertoetcheverryr" title="Test">✔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jdsmith"><img src="https://avatars.githubusercontent.com/u/1379246?v=4?s=100" width="100px;" alt="jdsmith"/><br /><sub><b>jdsmith</b></sub></a><br /><a href="#test-jdsmith" title="Test">✔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mrkeuz"><img src="https://avatars.githubusercontent.com/u/6247921?v=4?s=100" width="100px;" alt="Mr Keuz"/><br /><sub><b>Mr Keuz</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/commits?author=mrkeuz" title="Code">💻</a> <a href="#test-mrkeuz" title="Test">✔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mattytrentini"><img src="https://avatars.githubusercontent.com/u/194201?v=4?s=100" width="100px;" alt="Matt Trentini"/><br /><sub><b>Matt Trentini</b></sub></a><br /><a href="#stubs-mattytrentini" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://andrew-stclair.com/"><img src="https://avatars.githubusercontent.com/u/4944499?v=4?s=100" width="100px;" alt="Andrew St Clair"/><br /><sub><b>Andrew St Clair</b></sub></a><br /><a href="#stubs-andrew-stclair" title="MicroPython stubs">📝</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://gitlab.com/michal.moravec"><img src="https://avatars.githubusercontent.com/u/24276?v=4?s=100" width="100px;" alt="Michal Moravec"/><br /><sub><b>Michal Moravec</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/issues?q=author%3Amishal" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/paulober"><img src="https://avatars.githubusercontent.com/u/44974737?v=4?s=100" width="100px;" alt="Paul"/><br /><sub><b>Paul</b></sub></a><br /><a href="#tool-paulober" title="Tools">🔧</a> <a href="#stubs-paulober" title="MicroPython stubs">📝</a> <a href="https://github.com/Josverl/micropython-stubs/issues?q=author%3Apaulober" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/samskiter"><img src="https://avatars.githubusercontent.com/u/1271643?v=4?s=100" width="100px;" alt="Sam Duke"/><br /><sub><b>Sam Duke</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/issues?q=author%3Asamskiter" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->

<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

I invite everyone that has generated stubs for a board or port not on the current list, or has another contribution, to submit the stubs via a pull request or by just zipping up your stubs and creating an issue. 

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. 

[samples]: https://github.com/josverl/micropython-stubs/tree/main/docs/samples
[Discussions]: https://github.com/Josverl/micropython-stubs/discussions/categories/ideas
[PYPI]: https://pypi.org/search/?q=-stubs&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython
