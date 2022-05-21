# Directory Structure

-   directory의 기본 구조를 명시했습니다.

## requirements.txt

-   현재 repo에 사용되는 python package를 적는 곳입니다.
-   아래의 명령어는 현재 directory에서 requirements.txt를 만드는 명령입니다.

```shell
$ pip install pipreqs
$ pipreqs .
```

-   (Tip) pipreqs를 실행하는 폴더가 아닌, argument로 주어지는 폴더를 대상으로 requirements.txt를 생성합니다.
-   (Tip) pipreqs가 못 찾는 것이 있을 수 있습니다. (e.g. pyarrow, xlrd)

## hooks

-   pre commit hook에 관련된 directory
-   license.txt파일에 각 코드에 넣어야할 문장이 있습니다.

## data

-   raw data를 저장하는 directory
-   git에 push 금지!
