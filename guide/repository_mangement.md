# Repo 운영
## Project 이름 convention
- Repository 이름: "project-ooo"
  - 띄어쓰기는 '-'을 사용
  - ooo에는 회사이름만 표시 x

- Repository 토픽: Project와 관련있는 키워드를 추가합니다.

    - 예: project, amat, applied, applied materials, live_validation
    - 토픽 추가하는 법:
        - Github의 Repository 최상단 페이지를 간다.
        - 좌측 상단 "Code" 밑에 "add topics"를 누른다.
        - 적절한 키워드를 입력한다.
        - (아래의 빨간 박스 참고)

    <img width="500" alt="add_topics" src="https://user-images.githubusercontent.com/19830562/74056921-bb54af00-4997-11ea-9eb1-a467481843e2.png">



## Issue
- 가장 작은 단위로 생성합니다.
  - 안좋은 예) EDA 하기
  - 좋은 예) 시간을 x축으로 OO column을 y축으로 해서 plot하기
- assignee 지정을 꼭 합니다.
- label은 적절한 것으로 지정합니다.
  - 없을 때는 생성하면 됩니다.
- 적절한 milestone 지정을 합니다.
- 적절한 project 지정을 합니다.

## Milestone
- 작은 목표를 세울 때 사용합니다.
  - issue를 open할 때, milestone을 지정할 수 있습니다.

## Projects
- Project의 진행상황을 보여주는 용도로 사용합니다.
- Tip
  - Auto Configuration을 해두면, issue 생성시 To-Do column에 자동 등록/close시 done colum으로 이동 됩니다.

## Wiki
- 이 프로젝트를 하면서 공유할 것들을 정리하는데 사용합니다.
- Tip
  - Wiki에 바로 글을 쓰면, 사진/그림이 첨부가 Drag&Drop으로 안됩니다.
  - Issue에서 먼저 글을 작성, 사진/그림 Drag&Drop으로 첨부하고 Wiki로 옮기는 것을 추천합니다.

## Settings
- repository를 관리하는 tab입니다.
- Manage access
  - crew는 write권한을 줍니다.
- Branches
  - 공식적인 브랜치는 master, 또는 필요에 따라 master/develop 브랜치로 한정합니다.
  - 아래는 `master` branch에 protection rule을 추가하는 방법입니다.
    - 필요한 경우 다른 branch (develop 등)도 rule을 추가합니다.
  - Add rule을 누릅니다.
  - Branch name pattern에 `master`를 입력합니다.
  - `Require pull request reviews before merging`을 check 합니다.
  - `Include Administrators`를 check 합니다.
  - `Restrict who can push to matching branches`를 check 합니다.
  - create 버튼을 누릅니다.
