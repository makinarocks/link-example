# Project Template update

## Why?
- project-template는 완성된 repo가 아닙니다.
  - 버그가 존재할 수 있습니다.
- 그래서 project-template는 매 달 version이 update 됩니다. (노력중입니다.)
- project-template로 repo를 만들면, 만든 시점의 project-template version을 사용하게 됩니다.

## How?
- patch파일을 제공하고 있었지만, 사용하기 어렵습니다. (현재는 삭제했습니다.)
- [reference](https://stackoverflow.com/questions/56577184/github-pull-changes-from-a-template-repository/56577320#56577320)
  - Thanks to @rightx2
- 현재 repo에서 branch를 만듭니다.
```shell
$ git checkout -b apply-template-patch
```
- (처음 update의 경우) git remote를 활용하여 project-template를 등록합니다.
  - (TIP) git은 multi remote를 지원합니다.
```shell
$ git remote add template https://github.com/makinarocks/project-template.git
```
- template의 변경사항을 받습니다.
```shell
$ git fetch --all
```
- project-template의 최신 버전으로 update 합니다.
```shell
$ git merge template/master --allow-unrelated-histories
```
- conflict이 생기지 않았다면, 성공입니다!
- conflict이 발생하면, conflict을 해결한 뒤 merge를 완료 합니다!
