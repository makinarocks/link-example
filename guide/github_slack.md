# Github & Slack 연동 Guide

- Slack 채팅방 내에서 GitHub Repository의 소식을 업데이트 받을 수 있습니다.

* 스쿼드내 공유하는 Repository의 소식을 스쿼드 채널에서 업데이트 받으세요!
  * 스쿼드 알람 채널을 만들어서 소식만 따로 업데이트 받을 수도 있습니다.





## How to Use(In Slack Chat Room)

1. 채팅방 내에서 `/github` 명령어를 통해 github application을 채팅방에 추가합니다.

```
/github
```

2. 이후에 `/github` 명령어를 다시 치면 사용할 수 있는 명령어를 확인 할 수 있습니다.

```
/github

Need some help with /github?
Subscribe to notifications for a repository:
/github subscribe owner/repository
Unsubscribe from notifications for a repository:
/github unsubscribe owner/repository
Subscribe to notifications for all repositories in an organization:
/github subscribe owner
...
...
```

3. 자주 쓰는 명령어에 대해 아래에서 알아보도록 하겠습니다.



### 특정 Repository 구독 하기/안하기

1. `/github subscribe owner/repository` 명령어로 특정 Repository를 구독합니다.

```
# example
/github subscribe makinarocks/hmc-graph-to-text
```

2. `/github unsubscribe owner/repository` 명령어로 특정 Repository를 구독을 취소합니다.
3. `/github subscribe owner` 로 특정 owner의 모든 Repository를 구독할 수도 있습니다.

### 구독의 Feature 수정하기

* 초기 특정 Repository를 구독하는 경우는 issues / pulls / commits 등 7가지의 소식을 구독합니다.
* 총 12가지 소식에 대해 Customize 할 수 있습니다.

```
/github subscribe owner/repo [feature]
/github unsubscribe owner/repo [feature]

# example
/github subscribe makinarocks/hmc-graph-to-text reviews comments
/github subscribe makinarocks/hmc-graph-to-text commits
```

[참고](https://github.com/integrations/slack#configuration)

These are enabled by default, and can be disabled with the `/github unsubscribe owner/repo [feature]` command:

- `issues` - Opened or closed issues
- `pulls` - New or merged pull requests, as well as draft pull requests marked "Ready for Review"
- `statuses` - Statuses on pull requests
- `commits` - New commits on the default branch (usually `master`)
- `deployments` - Updated status on deployments
- `public` - A repository switching from private to public
- `releases` - Published releases

These are disabled by default, and can be enabled with the `/github subscribe owner/repo [feature]` command:

- `reviews` - Pull request reviews
- `comments` - New comments on issues and pull requests
- `branches` - Created or deleted branches
- `commits:all` - All commits pushed to any branch
- `+label:"your label"` - Filter issues, pull-requests and comments based on their labels.
