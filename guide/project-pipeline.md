# Objective of project-pipeline
프로젝트 진행 시 동일한 입출력을 지정하는 것이 첫번째 목적입니다.
동일한 데이터 전처리 과정, 동일한 metric을 산출할 수 있도록 프로젝트 내 통일성을 주어야합니다.
현재 이 목적을 달성할 기본적인 템플릿은 작성되었고 src폴더와 가이드 문서를 참고해 작성하시면 됩니다.

두번째 목적은 첫번째 목표를 달성하는 데 필요한 유틸들을 제공하는 것입니다.
필요한 파일이 없을 경우 오류를 내거나 특정 조건을 만족하지 않으면 로깅이 되지 않도록 하는 등 편의를 위한 기능이 그 예시입니다.
현재는 이 기능을 프로젝트 담당자들이 작성해야 하지만 추후 project-pipeline에서 기능을 지원하고자 합니다.

---

# Project-pipeline Structure
- ml-dev 기본 구조를 명시했습니다.
```
project-template
    L data/
    L src/
        L models/
            L model_ver1
                L trainer.py
                L predictor.py
        L project_paths.py
        L data_downloader.py
        L data_cleaner.py
        L data_spliter.py
        L evaluator.py
        L record.py
        L run.py
```

- 프로젝트 팀은 Data, Evaluation, Logging 코드를 공유해야 합니다.
- 팀원이 서로 다른 전처리 방법, train/test dataset, 평가방법을 사용하는 것을 방지하는 데 목적을 둡니다.
- 팀원은 Model 부분을 자유롭게 수정하여 자신의 모델을 확인할 수 있습니다.

---

# How to setup?
## Getting Started
project-template은 base_path를 이용해 모든 파일들을 실행시킵니다.
따라서, 정상적으로 project-template을 이용하기 위해서 project-template 경로를 환경변수 `PROJECT_PATH`에 입력하는 것을 **권장**합니다.

```bash
export PROJECT_PATH=$(git rev-parse --show-toplevel)
export PYTHONPATH=$PYTHONPATH:$PROJECT_PATH/src
```

## Project path

### `project_paths.py`
프로젝트 진행 중 지속적으로 사용할 path를 이곳에서 미리 지정합니다.
구체적으로 `PROJECT_PATH`, `DATA_PATH`, `NAS_SRC_DIR`를 사용합니다.
`PROJECT_PATH`, `DATA_PATH`는 project-template를 루트 경로로 놓아 이미 결정되어 있으며, `NAS_SRC_DIR`는 새로 입력해주어야 합니다.
입력할 내용은 프로젝트 진행 시 사용할 데이터가 저장된 NAS 경로입니다.

## Data

### `data_downloader.py`
NAS에서 dataset을 다운받습니다.
`python data_downloader.py` 를 실행할 경우 NAS의 데이터를 `$PROJECT_PATH/data/` 에 다운로드 합니다.
이 외의 코드는 수정하지 않아도 됩니다.
**(NAS에 저장된 데이터를 쓰는 프로젝트가 아닌 경우 이 단계는 생략될 수 있습니다.)**

### `data_cleaner.py`
프로젝트 팀에서 공유할 기본적인 전처리 과정을 수행하는 코드를 입력합니다.
- 전처리 과정에서 오랜 시간이 걸리는 작업을 다른 팀원이 미리 수행한다.
- 만약 이 전처리 과정이 오래걸려서 파일화를 하여 팀원과 공유를 하고 싶다면 전처리 된 데이터를 NAS에 올린다.
    - `data_downloader.py`를 수정하여 다른 팀원들이 전처리된 데이터를 이용할 수 있게 한다.

즉, 이 파일은 다운로드 받은 데이터를 전처리를 하기 위한 파일입니다.

- input : project 시작 시 사용하는 기본 raw data.
- output : e.g. `DATA_PATH/data_cleaned.csv`와 같은 형태의 데이터 파일(들)

## Evaluation

### `data_spliter.py`
다운로드 받은 결과물을 train, test 미리 나누고 싶다면 나눕니다.\
이는 팀원들이 공통된 train/test 데이터를 이용하게 하기 위함입니다.
Data 처리 과정에서 로깅하고자 하는 사항이 있다면 `data_info.json`에 작성합니다.

- input : `DATA_PATH/data_cleaned.csv`(2.1의 output)
- output : 모델 학습에 사용할 데이터와 평가에 사용할 데이터를 분리할 수 있는 정보를 저장
    예시(
    - `DATA_PATH/train_indices.csv`
    - `DATA_PATH/test_indices.csv`
    - `DATA_PATH/data_info.json`

### `evaluator.py`
프로젝트 시작할 때 `evaluatory.py`의 `evaluate()`함수를 정의해야 합니다.
```python
# evaluator.py

def evaluate():
    pass
```
1.3의 output 중 `DATA_PATH/test_y.csv`와
3.1의 결과물 `PROJECT_PATH/src/model/{model_ver1}/submission.csv`를 입력으로 받습니다.
수행 결과물은 `PROJECT_PATH/src/model/{model_ver1}/evaluation_result.json`으로 저장됩니다.

- input :
    - `DATA_PATH/test_y.csv`
    - `PROJECT_PATH/src/model/{model_ver1}/submission.csv`
    - `DATA_PATH/data_info.json`
    - `PROJECT_PATH/src/model/{model_ver1}/model_info.json`
- output :
    - `PROJECT_PATH/src/model/{model_ver1}/evaluation_result.json`

---

## Model specification

### custom model folder 만들기
`PROJECT_PATH/src/models/` 아래에 폴더를 생성합니다. 폴더 이름은 모델의 특성에 맞게 자유롭게 선택합니다.
다만, 커밋된 모델을 업데이트하는 경우는 동일한 이름을 사용하지 않고, 복사하여
- Example: `PROJECT_PATH/src/models/model_ver1`

### `trainer.py`
`trainer.py` 에서는 앞에서 구성한 데이터를 사용하여, 학습된 모델을 생성하고 저장하는 `train()` 함수를 구현하여야 합니다.
```python
# trainer.py

def train():
    ...
```
이 때 모델의 `input`은 [1](#1.-data-download)과 [2](#2.-data-preparation)를 통해 만들어진 데이터 입니다.
학습이 끝난 모델은 `predictee.py`에서 이용할 수 있는 형태로 저장되어야 합니다.
model_ver1의 경우 `preprocessor.joblib` 와 `model.joblib`을 저장하도록 작성했습니다.
모델 제작 과정에서 추가로 mlflow 에 기록하고자 하는 정보(e.g., 하이퍼파라미터)가 있다면 `model_info.json`에 저장합니다.

- input :
    - `DATA_PATH/data_cleaned.csv`
    - `DATA_PATH/train_indices.csv`
- output :
    - `PROJECT_PATH/src/models/model_ver1/preprocessor.joblib`
    - `PROJECT_PATH/src/models/model_ver1/model.joblib`
    - `PROJECT_PATH/src/models/model_ver1/model_info.json`

### `predictor.py`
`predictor.py` 에서는 앞에서 구성한 평가 데이터와 `trainer.py`로 학습된 모델을 사용하여, evaluation 스크립트가 성능 지표를 계산할 수 있도록 submission.csv 를 생성하는 `predict()` 함수를 구현하여야 합니다.
```python
# predictor.py

def predict():
    ...
```

- input :
    - `DATA_PATH/data_cleaned.csv`
    - `DATA_PATH/test_indices.csv`
    - `PROJECT_PATH/src/models/model_ver1/preprocessor.joblib`
    - `PROJECT_PATH/src/models/model_ver1/model.joblib`
    - `PROJECT_PATH/src/models/model_ver1/model_info.json`
- output :
    - `PROJECT_PATH/src/models/model_ver1/submission.csv`

---







# How to run?

### `run.py`

### `record.py`


---

## Support Later

### `replay.py`
