# TODO
    [ ] Complete these document!
    [ ] Github - Add teammates for read-only access to my repo.
    [ ] Figure out Slack/Discord group for teammates (Does Github have native chat?)
    [ ] VSCode Git Integration!
------------------------------------------------------------------------------------

# Set-Up

_I'm making the effort to be more "modern" and use VSCode. We'll see how this goes._
*Do not take this as a recommendation or endorsement!*

* MacBook Pro (13-inch, Mid 2012) running macOS 10.15.7 - Catalina.
* Visual Studio Code (1.52.1)
* Python 3.9.1

## OSX Preparation

I ran all recommended updates before preceding, which took quite sometime. I did install [iterm2](https://iterm2.com) to suplement/replace the default terminal app - though I'm not planning on using much for this adventure.

## Python Installation

I resorted to using [HomeBrew](https://brew.sh)...

```
# Probably not recommended from a security standpoint, but...
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
sudo brew install python3
```

## Visual Studio Installation

* [Official Directions](https://code.visualstudio.com/docs/setup/mac)

```
Installation
Download Visual Studio Code for macOS.
Open the browser's download list and locate the downloaded archive.
Select the 'magnifying glass' icon to open the archive in Finder.
Drag Visual Studio Code.app to the Applications folder, making it available in the macOS Launchpad.
Add VS Code to your Dock by right-clicking on the icon to bring up the context menu and choosing Options, Keep in Dock.
```

I used the Shift-Command-P to "Install 'code' command in PATH" rather than edit the .bash_profile and .zprofile.

Ran through the [VSCode Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) to get things marginally running...

* [Python Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Command-Shift-P (aka Command-Palette) - "Python:Select Interpreter"
* Created Example "Hello.py" to verify tools were installed. (Did not complete tutorial.)

## Github

* Generated new key for my MacBook account
* Created new empty-ish repository, with simple README.md and now this file.

