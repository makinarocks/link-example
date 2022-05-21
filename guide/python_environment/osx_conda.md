## MacOS (OSX)

### introduction
- 사용하는 shell은 zsh로 가정하였습니다.
- 관련 페이지
    - [Conda github](https://github.com/conda/conda)
    - [direnv](https://github.com/direnv/direnv)

### conda

다양한 플랫폼에서 사용가능한 패키지 관리자.

- 패키지 저장소 제공
- 가상환경 기능 제공

#### 설치

두 가지 버전 중 원하는 버전을 [여기를](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) 통해 설치한다.

- Miniconda: Conda만 포함된 배포판 **(추천)**.
- Anaconda: Conda와 함께 여러 데이터 분석 패키지들이 포함되어있는 배포판.

#### 가상환경 만들기

다음은 파이썬 버전 3.7.4를 사용하는 "test_conda"라는 가상환경을 만드는 명령입니다.

```shell
conda create --name test_conda python=3.7.4
```

질문이 나오면 y를 선택하고, 생성이 완료되면 다음 명령어를 통해 가상환경을 활성화 시키고, 파이썬 버전을 확인합니다.

```shell
> conda activate test_conda
(test_conda) > python --version
# Python 3.7.4
```

#### 가상환경 관련 명령어

```shell
conda deactivate  # 가상환경 빠져나오기
conda env list  # 생성된 가상환경 리스트 보기
conda remove --name ${ENV_NAME} --all  # 가상환경 삭제하기
```

#### 가상환경 복사

##### Via Conda

```shell
conda env export -n test > environment.yml
# environment.yml 파일의 첫 라인에 가상환경 이름을 적절히 적어준다.
conda env create -f environment.yml
```

간단하고, 파이썬 버전까지 포함해서 가상환경을 export 할 수 있지만, pyenv+pip와는 호환이 안됨.

##### Via pip (recommended)

```shell
conda activate from_env
pip freeze > requirements.txt  # 가상환경 패키지 리스트 생성

conda deactivate

conda activate to_env
pip install -r requirements.txt  # requirements.txt에 있는 패키지 설치
```

파이썬 버전은 requirements.txt에 포함이 안되기 때문에 따로 전달해야 함. pyenv+pip, conda 두 환경 모두에서 사용 가능.

### direnv

디렉토리 별 쉘 환경 설정 사용 가능하게 해줌. 여기에서는 주로, 프로젝트 디렉토리에 들어갈 때 마다, 그에 맞는 (가상)환경을 자동으로 로딩하기 위해 사용함.

#### 설치

```zsh
brew install direnv
```

#### direnv 설정
- [reference](https://graspthegist.com/post/conda-direnv/)
- `$~/.zshrc`에 다음을 추가해서 쉘에 hook을 설정.
```shell
# ~/.zshrc
eval "$(direnv hook zsh)"
```

#### Layout 설정
* `~/.direnvrc`에 다음 내용 추가한다.
    * 디렉토리 별 설정 파일인 `.envrc`에서 conda layout을 사용할 수 있게된다.
    * conda라는 layout은, 주어진 argument에 해당하는 conda env를 activate 한다.

```shell
# ~/.direnvrc
layout_conda() {
  local CONDA_HOME="${HOME}/opt/miniconda3/"  # 경로가 맞는지 확인
  PATH_add "$CONDA_HOME"/bin

  if [ -n "$1" ]; then
    # Explicit environment name from layout command.
    local env_name="$1"
    source activate ${env_name}
  elif (grep -q name: environment.yml); then
    # Detect environment name from `environment.yml` file in `.envrc` directory
    source activate `grep name: environment.yml | sed -e 's/name: //'`
  else
    (>&2 echo No environment specified);
    exit 1;
  fi;
}
```

#### 프로젝트 레포지토리 별 설정

`$REPO_ROOT`로 이동 후 다음을 실행한다. (`proj_env`는 conda 가상환경 이름)

```shell
echo "conda proj_env" > .envrc
# direnv: error /Users/yongsub/work/tmp/.envrc is blocked. Run `direnv allow` to approve its content
```

마구 수정되는 것이 방지되어 있다. 다음을 수행해서 위 명령을 허용한다.

```shell
direnv allow
```

Env 변화를 확인한다.

```shell
echo $CONDA_DEFAULT_ENV
# proj_env

cd ..
echo $CONDA_DEFAULT_ENV
# base (evn name before you entered $PROJECT_HOME will be shown)

cd $REPO_ROOT
echo $CONDA_DEFAULT_ENV
# proj_env
```

#### Env 이름 보이게 하기

프롬프트에서 현재 Env 이름을 보여주는 테마를 쓰고 있는 경우, direnv에 의해 실제 Env는 바뀌지만 프롬프트에 표시되는 Env 정보는 안바뀔 수 있다.  다음을 `~/.zshrc`에 추가한다.

```zsh
# ~/.zshrc
autoload -U colors && colors
show_virtual_env() {
  if [ -n "$VIRTUAL_ENV" ]; then
    echo "($(basename $VIRTUAL_ENV))"
  elif [ -n "$CONDA_DEFAULT_ENV" ]; then
    echo "($(basename $CONDA_DEFAULT_ENV))"
  fi
}
conda config --set changeps1 False
# 색깔이 노랑으로 되어 있는데, 원하는 색으로 바꿔도 됨.
PS1='%{$fg[yellow]%}$(show_virtual_env)%{$reset_color%}'$PS1
eval "$(direnv hook zsh)"
```

`$REPO_ROOT`를 나갔다 들어왔다 하면서, 실제 Env 이름과 프롬프트 맨 앞에 보이는 Env 이름이 같은지 확인한다.

> COMMENT:
>
> - conda activate에 의해 표시되는 프롬프트 상의 Env 이름은 direnv에 의한 Env 변화에 영향을 받지 않는다.
> - 따라서, conda activate, direnv를 섞어쓰면, 프롬프트 상에 서로 다른 env 이름 두 개가 표시될 수 있다.
> - 좋은 해결책이 있는지는 아직 모르겠음.
