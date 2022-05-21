# pre-commit guide

## 설치
- repo root에서 아래의 명령어를 실행한다.
```shell
$ ./hooks/install.sh
```

## 기본적으로 설정되어 있는 pre-commit 설명

### trailing-whitespace
- line 끝에 붙는 whitespace가 있는지 check하고 지워주는 작업을 하는 pre-commit입니다.

### end-of-file-fixer
- file끝에 비어있는 한줄이 있는지 check하는 pre-commit입니다.

### mixed-line-ending
- line끝에 LF, CRLF 등이 올수 있습니다.
- 이것을 맞추어주는 작업을 하는 pre-commit입니다.

### check-added-large-files
- large file을 추가했는지 check하는 pre-commit입니다.
- large file은 현재 1MB으로 setting되어 있습니다.
    - `--maxkb=1000` setting값을 바꾸면 check하는 크기를 바꿉니다.
- git-lfs로 track되는 file은 check하지 않습니다.

### requirements-txt-fixer
- requirements.txt안에 있는 package의 이름을 sort하는 pre-commit입니다.

### black
- 현재 black pre-commit은 **disable** 되어 있습니다.
- python code format을 check하는 pre-commit입니다.
- 이것을 켜고 싶은 경우 `.pre-commit-config.yaml`에서 `#`을 제거합니다.
- black pre-commit은 git repo의 `project.toml`파일의 설정값을 이용합니다.
- `project.toml`파일을 상황에 맞게 수정하면 됩니다.
- !!주의!!
    - black은 자동 수정이 default입니다.

### flake8
- python code format을 check하는 pre-commit입니다.
- 현재 project-template에는 pre-commit으로 flake8을 사용합니다.
- flake8 pre-commit은 git repo의 `.flake8`파일에 설정값을 이용합니다.
    - `max-line-length`: line 길이를 제한합니다. (현재는 E501에 의해 무시됨)
    - `ignore`: 무시하고 싶은 rule을 설정합니다.
        - `E203`: [Whitespace before ':'](https://www.flake8rules.com/rules/E203.html)
        - `E226`: [Missing whitespace around arithmetic operator](https://www.flake8rules.com/rules/E226.html)
        - `E266`: [Too many leading '#' for block comment](https://www.flake8rules.com/rules/E266.html)
        - `E501`: [Line too long (82 > 79) characters](https://www.flake8rules.com/rules/E501.html)
        - `W503`: [Line break occurred before a binary operator](https://www.flake8rules.com/rules/W503.html)
- flake8은 자동 수정하지 않습니다.

### reorder-python-imports
- python import의 순서를 정렬하는 pre-commit입니다.

### add-trailing-comma
- 자세한 설명은 [링크](https://github.com/asottile/add-trailing-comma)를 참고합니다.
- line마지막에 comma를 넣어줍니다.

### license-checker
- `.py, .ipynb`파일에 makinarocks license가 있는지 check하는 pre-commit입니다.
- developed by @minhwan-rocks

## 요청
- 이외 쓸모 있는 pre-commit은 사용해 보고, project-template에 추가해 주세요.
