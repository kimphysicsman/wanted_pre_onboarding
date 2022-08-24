# 📢 원티드 - 프리온보딩 지원 선발과제

## 0. Info

> 개발기간 : 2022.08.24  
> 기술스택 : Python3, Django, Django-REST-framwork  
> 개발자 : [김동우](https://github.com/kimphysicsman)

<br />

## 1. Structure

> wanted_pre_onboarding _(main)_
>
> > ㄴ user _(사용자 기능)_  
> > ㄴ company _(회사 기능)_  
> > ㄴ jobpost _(채용공고 기능)_

<br />

## 2. Modeling

> User - _사용자_  
> Company - _회사_  
> SkillSet - _사용기술_  
> JobPosition - _채용포지션_  
> JobPost - _채용공고_  
> Apply - _채용공고 지원_

<br />

## 3. 요구사항

### 1) 채용공고를 등록합니다.

> DRF Serializer를 이용한 create 기능 구현
>
> > request data 예시
> >
> > ```Json
> > {
> >    "company_id": 0,
> >    "jobposition":"백엔드 주니어 개발자",
> >    "salary":1000000,
> >    "skillset":"Python Django",
> >    "area": "서울",
> >    "country": "한국"
> > }
> > ```

### 2) 채용공고를 수정합니다.

> DRF Serializer를 이용한 update 기능 구현
>
> > request data 예시
> >
> > ```Json
> > {
> >     "jobpost_id": 9,
> >     "company_id": 1,
> >     "jobposition":"프론트 주니어 개발자",
> >     "salary":2000000,
> >     "skillset":"Javascript React",
> >     "area": "도쿄",
> >     "country": "일본"
> > }
> > ```

### 3) 채용공고를 삭제합니다.

> model.delete()를 이용한 오브젝트 삭제

### 4) 채용공고 목록을 가져옵니다.

> #### 4-1. 사용자는 채용공고 목록을 아래와 같이 확인할 수 있습니다.
>
> > response 예시
> >
> > ```JSON
> > [
> >    {
> >        "id": 1,
> >        "company": "원티드",
> >        "skillset": [
> >            "Django",
> >            "Python"
> >        ],
> >        "jobposition": "백엔드 개발자",
> >        "salary": 40000000,
> >        "area": "서울특별시 송파구",
> >        "country": "한국"
> >    },
> >    {
> >        "id": 2,
> >        "company": "삼성",
> >        "skillset": [
> >            "Java"
> >        ],
> >        "jobposition": "데브옵스",
> >        "salary": 38000000,
> >        "area": "경기도 수원시",
> >        "country": "한국"
> >    },
> >  ...
> > ]
> > ```

> #### 4-2. 채용공고 검색 기능 구현(선택사항 및 가산점요소).
>
> URL : .../jobpost/search?search=Django
>
> > response 예시
> >
> > ```JSON
> > [
> >    {
> >        "id": 1,
> >        "company": "원티드",
> >        "skillset": [
> >           "Django",
> >            "Python"
> >       ],
> >      "jobposition": "백엔드 개발자",
> >       "salary": 40000000,
> >       "area": "서울특별시 송파구",
> >       "country": "한국"
> >   },
> >   {
> >        "id": 7,
> >        "company": "원티드",
> >        "skillset": [
> >            "Django",
> >            "Python"
> >        ],
> >        "jobposition": "백엔드 주니어 개발자",
> >        "salary": 1000000,
> >        "area": "서울",
> >        "country": "한국"
> >    }
> > ]
> > ```

### 5) 채용 상세 페이지를 가져옵니다.

> response 예시
>
> ```JSON
> {
>    "id": 1,
>    "company": "원티드",
>    "skillset": [
>        "Django",
>        "Python"
>    ],
>    "jobposition": "백엔드 개발자",
>    "salary": 40000000,
>    "area": "서울특별시 송파구",
>    "country": "한국",
>    "content": "원티드의 백엔드 개발자 채용공고",
>    "other_jobpost": [
>        1,
>        5,
>        7
>    ]
> }
> ```

### 6) 사용자는 채용공고에 지원합니다(선택사항 및 가산점요소).

> request data 예시
>
> ```JSON
> {
>    "user": 1,
>    "jobpost": 1
> }
> ```
