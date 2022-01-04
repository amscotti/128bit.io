---
title: "Setting Up a Local Python Development Environment"
date: 2017-09-18T18:06:58-04:00
tags:
- Python
- Development
---

Over the past couple months, I've been working on fine tuning my Python skills, part of this has been taking tutorials online along with building some applications. One of the things I’ve been wanting to document, mostly for myself, is setting up a new environment for developing with Python.

I’m using macOS Sierra right now, it seems that most operating systems still comes with version 2.x of Python. It’s always a good idea to be able to control the version of Python you are using. This is good if you are working on a team project or want to test your application with the newer version of Python. I found that “[pyenv](https://github.com/pyenv/pyenv)” is a great tool for this task.


## Python Version

[pyenv](https://github.com/pyenv/pyenv) is a tool that will let you install a desired version of Python, it will also let you manage multiple versions at the same time. For instance, If you have a project using Python 2.7, pyenv will let you switch to that version easily by using the `pyenv local` along with the version you want to use. You can even add a `.python-version` file in your application folder to tell pyenv what version to use for your project. pyenv is a fork of the [rbenv](https://github.com/rbenv/rbenv) and [ruby-build](https://github.com/rbenv/ruby-build) project if you are from the Ruby world, it provides very similar functionality.

I would highly recommend using [Homebrew](https://brew.sh/) to install pyenv and any other tools you would need for your development system. Definitely something to look into that could save you a fair amount of time installing and updating software.

To install with Homebrew,
```
$ brew update
$ brew install pyenv
```
then

```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ exec "$SHELL"
```

Details can be found on the Github page [here](https://github.com/pyenv/pyenv#basic-github-checkout).

So, let’s get Python 3.6.2 installed, which is the latest release at the time of writing this posting. you would run the `pyenv install 3.6.2` command. This will pull the install file down and install it.

To use the newly installed Python you need to set it as your global version, like so.


```
$ python --version
Python 2.7.10
$ pyenv global 3.6.2
$ python --version
Python 3.6.2
```

If you are curious what other versions are available to install you can run `pyenv install --list` to see the complete list.

So, we can now control the version of Python we are using and switch around as needed. Now let’s look into [virtual environments](https://docs.python.org/3/tutorial/venv.html).


## Virtual Environments

Python installs packages globally so you can get into a situation where a project is using an older package when you have a new one installed or vice versa. Virtual environments help avoid conflicts from project to project by installing packages into its own isolated environment. If you are using Python 3.3 or newer, you can easily create a new virtual environment by running `python3 -m venv path` and then when you are ready to work on your project, activate the environment by running `source <path>/bin/activate`.  This will now make it so that Python and Pip are based on the virtual  environment. When you are done working on your project for the day, deactivate the environment by running `deactivate`.

Keep in mind, the environment itself should be something that is easily removed and recreated if needed. You should be saving a list of packages needed for your project to `requirements.txt` and using `pip install -r requirements.txt` to reinstall when setting up a new environment.

[More details at in the Python documentation on virtual environments (venv)](https://docs.python.org/3/library/venv.html)

Here is a great video talking about virtual environments from my local Python User Group in Boston,

{{< youtube _6xgJSVKMhY >}}

[Exploring Virtual Environments in Python](https://youtu.be/_6xgJSVKMhY)

Alternatively, if you're looking for something a bit more powerful than the built in venv module, you can use something like [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) which is a plugin to pyenv tool. After installing, you an use pyenv virtualenv like so,


```
$ pyenv virtualenv 3.6.2 django_project
$ pyenv virtualenvs
  3.6.2/envs/django_project (created from /Users/ascotti/.pyenv/versions/3.6.2)
  django_project (created from /Users/ascotti/.pyenv/versions/3.6.2)
$ pyenv activate django_project
(django_project) $
```

pyenv-virtualenv is a great way to easily create and manage many environments.


## Editors and IDEs

As far as editors, this is really based on the person and what feels right to them. I’m a big fan of [Atom](https://atom.io/) from Github and [Visual Studio Code](https://code.visualstudio.com/) from Microsoft, both are really great editors and have nice plugins for working with Python. I find myself switching back and forth as new versions come out with new features. I do feel that Code seems to have a more consistent release schedule, but that could just be because they open the release notes after every update.

If you are looking a bit more along the lines of an IDE, [PyCharm](https://www.jetbrains.com/pycharm/) is a really great IDE for Python. It’s been my go-to tool for working on Python lately. Besides basic IDE functionality, they do make it extremely easy to work with Python versions, virtual environments, and packages. PyCharm CE is free, and if you find it too much you can always go to something like Atom or Visual Studio Code.


## Until Next Time

Hope this helps people get started looking into doing some development with Python, and get an idea of the tools that are out there that can help you when working on your projects. I know for myself, this will be a posting I look at when setting up new systems in the future.
