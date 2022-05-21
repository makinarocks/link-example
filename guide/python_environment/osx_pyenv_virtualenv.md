## MacOS (OSX)

### introduction
- 사용하는 shell은 zsh로 가정하였습니다.
- open source pages
    - [pyenv](https://github.com/pyenv/pyenv)
    - [pyenv-vritualenv](https://github.com/pyenv/pyenv-virtualenv)
    - [direnv](https://github.com/direnv/direnv)

### pyenv, pyenv-vritualenv 설치
```zsh
$ brew install pyenv
$ brew install pyenv-virtualenv
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
$ source ~/.zshrc
```

### pyenv-virtualenv를 사용하여 python 실행환경 만들기
- 아래는 "test-3.7.3-env"라는 virtualenv를 만드는 명령입니다.
```zsh
pyenv virtualenv 3.7.3 test-3.7.3-env
```

### direnv 설치
```zsh
brew install direnv
```

### direnv 설정
- `~/.zshrc`에 다음을 추가해줍니다.
```zsh
# ~/.zshrc
eval "$(direnv hook zsh)"
```
- `~/.direnvrc`에 다음을 추가해줍니다.
```zsh
# ~/.direnvrc
# -*- mode: sh; -*-
# Custom global configuration for [direnv](https://direnv.net/)
# i.e. override/complete the direnv-stdlib:
#           https://github.com/direnv/direnv/blob/master/stdlib.sh
#
# Quick installation of this file:
#    mkdir -p ~/.config/direnv
#    cd ~/.config/direnv
#    curl -o direnvrc https://raw.githubusercontent.com/Falkor/dotfiles/master/direnv/direnvrc
#
# Sample .envrc you can use for Python projects based on the
# layouts defined in this file:
# https://github.com/Falkor/dotfiles/blob/master/direnv/envrc
#
############################ Python ############################
# Workfow based on:
# - 'pyenv' to easily switch to a special version of python
# - 'pyenv-virtualenv' to manage python versions AND virtualenvs
#
# Typical .envrc for your python project using the below functions:
#    if [ -f ".python-version" ]; then
#       pyversion=$(head .python-version)
#    else
#       pyversion=2.7.16
#    fi
#    pvenv=$(basename $PWD)
#
#    use python ${pyversion}
#    layout virtualenv ${pyversion} ${pvenv}
#    layout activate ${pvenv}
#
# Adapted from
#  - https://github.com/direnv/direnv/wiki/Python#-pyenv and
#  - https://github.com/direnv/direnv/wiki/Python#-virtualenvwrapper
#
# Side note:
# It appeared required to reload the pyenv [virtualenv-]init as for
# It May be due to the fact that direnv is creating a new bash
#  sub-process to load the stdlib, direnvrc and .envrc
###

# === Use a specific python version ===
# Usage in .envrc:
#    use python <version>
use_python() {
    if [ -n "$(which pyenv)" ]; then
        local pyversion=$1
        eval "$(pyenv init -)"
        pyenv local ${pyversion} || log_error "Could not find pyenv version '${pyversion}'. Consider running 'pyenv install ${pyversion}'"
    fi
}

# === Create a new virtualenv ===
# Usage in .envrc:
#    layout virtualenv <version> <name>
layout_virtualenv() {
    local pyversion=$1
    local pvenv=$2
    pyenv local ${pyversion}
    if [ -n "$(which pyenv-virtualenv)" ]; then
        eval "$(pyenv virtualenv-init -)"
        pyenv virtualenv --force --quiet ${pyversion} ${pvenv}
    else
        log_error "pyenv-virtualenv is not installed."
    fi
}

# === Activate a virtualenv ===
# Note that pyenv-virtualenv uses 'python -m venv' if it is
# available (CPython 3.3 and newer) and  'virtualenv' otherwise
# Usage in .envrc:
#    layout activate <name>
layout_activate() {
    if [ -n "$(which pyenv)" ]; then
        local pyenvprefix=$(pyenv prefix)
        local pyversion=$(pyenv version-name)
        local pvenv="$1"
        # Below initialization is necessary to recall ;(

        pyenv activate ${pvenv}
    fi
}
```

### how to use
- directory 별로 `.envrc`파일을 만들어서 사용합니다.
- 해당 directory로 이동시에 `.envrc`파일은 direnv에 의해서 실행됩니다.
- pyenv-vritualenv가 active되는 것 뿐만아니라, 각종 환경 변수도 설정할 수 있습니다.
- (기본) `.envrc`에 다음을 추가해 줍니다.
```zsh
pyversion=3.7.3 # your python version
virtualenv=project-template # you project name or what you want to call you virtual env

use python ${pyversion}
# Create the virtualenv if not yet done
layout virtualenv ${pyversion} ${virtualenv}
# activate it
layout activate ${virtualenv}
```
- (추가) flint를 사용할 시에는 `.envrc`에 다음을 추가해 줍니다.
```zsh
export PYTHONPATH="$(git rev-parse --show-toplevel)/assets/flint:${PYTHONPATH}"
```
- `.envrc` 마구 수정되는 것이 방지되어 있다. 다음을 수행해서 direnv의 수행을 허용한다.
```zsh
direnv allow
```
