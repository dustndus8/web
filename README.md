# Project : Web 만들기

# 기능

Board (제목, 부제목, 내용, 썸네일)

- 게시판 등록
- 게시판 수정
- 게시판 삭제
- 게시글 읽기
- 게시판 목록 읽기
- 게시판 좋아요 기능

Reply (내용)

- 댓글 등록
- 댓글 수정
- 댓글 삭제
- 댓글 목록 읽기
- 댓글 좋아요 기능

User (유저이름, 이메일, 비밀번호, 인증여부)

- Allauth 사용 (회원가입, 로그인, 로그아웃)
- 로그인 한 유저 정보 읽기
- 유저 이름 변경
- 유저 삭제
- 프로필 사진 추가 및 변경
- 프로필 사진 삭제
- 이메일 인증 기능
- 카카오 로그인 기능

# Skills & Tools
![이미지](https://user-images.githubusercontent.com/75442105/176810518-0a09f019-ab2f-454f-aa55-06c632410d26.png)
DB - MariaDB  
Backend - Python, Django  
Frontend - HTML, CSS, JavaScript (Bootstrap 이용)  


# API 설계

| 기능 | Request | API |
| --- | --- | --- |
| 메인화면 | GET | main |
| 게시글 작성 페이지 | GET | board/create |
| 게시글 작성  | POST | board/create |
| 게시글 조회 | GET | board/readGet/<int:bid> |
| 게시글 전체 조회 | GET | board/listGet |
| 게시글 삭제 | DELETE | board/deleteGet/<int:bid> |
| 게시글 수정 페이지 | GET | board/update/<int:bid> |
| 게시글 수정 | POST | board/update/<int:bid> |
| 게시글 좋아요 | GET | board/like/<int:bid> |
| 댓글 작성 페이지 | GET | reply/create |
| 댓글 작성 | POST | reply/create |
| 댓글 목록 조회 | GET | reply/list |
| 댓글 삭제 | DELETE | reply/deleteGet/<int:rid> |
| 댓글 수정 페이지 | GET | reply/update/<int:rid> |
| 댓글 수정 | POST | reply/update/<int:rid> |
| 댓글 좋아요 | GET | reply/like/<int:rid> |
| 유저 정보 조회 | GET | account/read |
| 유저 프로필사진 작성 페이지 | GET | account/createProfile |
| 유저 프로필사진 작성 | POST | account/createProfile |
| 유저 프로필사진 삭제 | DELETE | account/deleteProfile |
| 유저 이름 변경 페이지 | GET | account/updateUsername |
| 유저 이름 변경 | POST | account/updateUsername |
| 유저 삭제 | DELETE | account/deleteUser |
| 유저 로그인 페이지 | GET | accounts/login |
| 유저 로그인 | POST | accounts/login |
| 유저 회원가입 페이지 | GET | accounts/signup |
| 유저 회원가입 | POST | accounts/signup |

# 구성 화면
### 홈 화면
![Untitled](https://user-images.githubusercontent.com/75442105/189790428-2474e9bb-e0fa-4d3b-8fc6-f25e0026f62d.png)  

### 회원 가입
![Untitled (1)](https://user-images.githubusercontent.com/75442105/189790965-caccefb4-766f-4fca-9b3d-30abf4d5c013.png)

### 로그인
![Untitled (2)](https://user-images.githubusercontent.com/75442105/189790562-c984b085-0d9a-4eac-863f-78e59e99d81c.png)  

### 게시글
![Untitled (3)](https://user-images.githubusercontent.com/75442105/189790624-dfb4d6c2-6cf3-4ad2-97cc-1f63ade594b7.png)
![Untitled (4)](https://user-images.githubusercontent.com/75442105/189790687-cac12aeb-9af4-41dd-9aae-833c2dd5a022.png)  

### 댓글
![Untitled (5)](https://user-images.githubusercontent.com/75442105/189790720-336a8d0f-00f0-4d49-84f9-0d6c103416fb.png)  

### 유저
![Untitled (6)](https://user-images.githubusercontent.com/75442105/189791006-fafdd0db-279b-441f-be01-4c2606f61bc8.png)
