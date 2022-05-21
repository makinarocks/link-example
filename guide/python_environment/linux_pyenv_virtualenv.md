## Linux(Ubuntu)

### introduction
- 사용하는 shell은 bash로 가정하였습니다.
- open source pages
    - [pyenv](https://github.com/pyenv/pyenv)
    - [pyenv-vritualenv](https://github.com/pyenv/pyenv-virtualenv)
    - [direnv](https://github.com/direnv/direnv)

### pyenv 설치
```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ source ~/.bashrc
```

### pyenv-virtualenv 설치
```bash
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

### pyenv를 사용하여 python 3.7.3 설치
```bash
$ sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev python3-setuptools python3-pip
$ pyenv install 3.7.3
```

### pyenv-virtualenv를 사용하여 python 실행환경 만들기
- 아래는 "test-3.7.3-env"라는 virtualenv를 만드는 명령입니다.
```bash
pyenv virtualenv 3.7.3 test-3.7.3-env
```

### direnv 설치
```bash
$ sudo apt install direnv
```

### direnv 설정
- `~/.bashrc`에 다음을 추가해서 쉘에 hook 및 env이름이 보일 수 있도록 합니다.
```bash
# ~/.bashrc
eval "$(direnv hook bash)"

show_virtual_env() {
  if [[ -n "$VIRTUAL_ENV" && -n "$DIRENV_DIR" ]]; then
    echo "($(basename $VIRTUAL_ENV))"
  fi
}
export -f show_virtual_env
PS1='$(show_virtual_env)'$PS1
```

- `~/.direnvrc`에 다음을 추가해줍니다.
```bash
# ~/.direnvrc
# use a certain pyenv version
use_python() {
    if [ -n "$(which pyenv)" ]; then
        local pyversion=$1
        pyenv local ${pyversion}
    fi
}

layout_virtualenv() {
    local pyversion=$1
    local pvenv=$2
    if [ -n "$(which pyenv virtualenv)" ]; then
        pyenv virtualenv --force --quiet ${pyversion} ${pvenv}-${pyversion}
    fi
    pyenv local --unset
}

layout_activate() {
    if [ -n "$(which pyenv)" ]; then
        source $(pyenv root)/versions/$1/bin/activate
    fi
}
```

# how to use
- directory 별로 `.envrc`파일을 만들어서 사용합니다.
- 해당 directory로 이동시에 `.envrc`파일은 direnv에 의해서 실행됩니다.
- pyenv-vritualenv가 active되는 것 뿐만아니라, 각종 환경 변수도 설정할 수 있습니다.
- (기본) `.envrc`에 다음을 추가해 줍니다.
```bash
# -*- mode: sh; -*-
# (rootdir)/.envrc : direnv configuration file
# see https://direnv.net/
# pyversion=$(head .python-version)
# pvenv=$(head     .python-virtualenv)
pyversion=3.7.3
pvenv=project-template

use python ${pyversion}
# Create the virtualenv if not yet done
layout virtualenv ${pyversion} ${pvenv}
# activate it
layout activate ${pvenv}-${pyversion}
```
- (추가) flint를 사용할 시에는 `.envrc`에 다음을 추가해 줍니다.
```bash
export PYTHONPATH="$(git rev-parse --show-toplevel)/assets/flint:${PYTHONPATH}"
```
- `.envrc` 마구 수정되는 것이 방지되어 있다. 다음을 수행해서 direnv의 수행을 허용한다.
```bash
direnv allow
```
