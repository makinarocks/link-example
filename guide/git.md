# Git

## 반드시 check!! (자신의 이름, 이메일로 바꾸어서 실행)
- signed-off를 위해서 꼭 설정해야 합니다.
```shell
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

## pre commit hook 설정
- [pre-commit guide](pre_commit.md)를 참고합니다.

## submodule
- makinastyle, flint를 submodule로 등록하기 위해서 아래 명령어를 사용한다.(repo를 만든 사용자만 한다.)
```shell
$ git submodule add https://github.com/makinarocks/flint.git assets/flint
$ git submodule add https://github.com/makinarocks/RLocks.git assets/rlocks
$ git submodule add https://github.com/makinarocks/makinastyle.git assets/makinastyle
```
- submodule이 등록된 repo는 아래의 명령어를 사용하여 clone을 받으면 된다.
```
$ git clone --recursive [repo 주소]
```
- 이미 clone이 된 경우에는 아래의 명령어를 사용하면 된다.
```
$ git submodule update --init
```

## add
- commit에 필요한 line들만 추가합니다.
```shell
$ git add -p [파일이름]
```
- 변경사항 전체를 add하는 것은 좋지 못한 습관입니다.(절대 하면 안되는 명령어)
```shell
$ git add .
```

## commit
- 실행하는 데 문제가 없는 단위로 commit 합니다.
- commit 내용에는 어떤 것을 update했는지 add했는지를 적습니다.
- sign-off를 항상 넣는 것을 추천합니다.
```shell
$ git commit -s
```

## branch
- 코드 작성전 branch를 만듭니다.
- branch에 자신의 이름을 적는 것은 좋지 못합니다.
- branch를 만들어야 하는 경우
  - issue가 생겨서 해결해야 하는 경우
  - 새로운 기능을 개발하는 경우

## tag
- tag는 milestone을 달성시 만듭니다.
- 배포/deploy전에 만듭니다.
