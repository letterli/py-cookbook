# simple python version management

pyenv lets you easily switch between multiple version of Python.

## install

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

## config

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

## reload shell

exec $SHELL -l

## apply

pyenv version                   # looking for waht python version are use now

pyenv install --list            # list python version for install

pyenv install python-version    # python version

pyenv uninstall python-version  # uninstall python version

pyenv versions                  # list python version installed

pyenv local python--version

pyenv global python-version



