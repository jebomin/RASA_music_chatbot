# RASA_music_chatbot
## 📂 프로젝트 소개
라사를 사용한 음악 추천 챗봇

## ⏰ 개발 기간
2023.11.13~2023.12.09

## ⚙ 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/Rasa-5A17EE?style=for-the-badge&logo=Rasa&logoColor=white">

## ▶️ 실행 방법
### 1. 필요한 api 설치
아나콘다 프롬포트에서 가상환경 생성 후 설치</br>
```bash
pip install rasa==3.6.4
```

### 2. 실행
visual studio code에서 해당 파일을 다운로드 받은 후 터미널에 다음 명령어 입력</br>
```bash
ran run actions --port 6000
rasa train
rasa shell
```

## 📷 결과화면
### 🗂️기본 데이터 베이스
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/c431f4bf-adde-49ba-b13f-eb32b0b45ee6"><br/>
### 1. 장르 별 음악추천
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/3e90768b-fdb7-4901-936c-b2ec7a198b0e"><br/>
### 2. 가수 별 음악추천
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/6960732e-2bd7-4c8b-acc8-92bf31781ad0"><br/>
### 3. 가사 별 음악추천
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/078d5f51-0e11-4251-8b03-cdcbe53396a7"><br/>
### 4. 기분 별 음악추천
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/83b3a3d3-5489-49d7-9312-dcadcd8b5e54"><br/>
### 5. 사용자가 음악 추천하고 해당 내용이 데이터베이스에 잘 반영되었는지 확인
#### 5-1) 장르를 물어봤을 때
<b>✅결과 창</b><br/>
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/a627504a-7fa2-4636-99ed-ed20000b068b"><br/>
<b>✅바뀐 데이터베이스</b><br/>
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/b5b7dcd2-3b71-4213-80d4-264af06f145d"><br/>
#### 5-2) 가수를 물어봤을 때
<b>✅결과 창</b><br/>
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/fcd84dc6-2b7c-43c8-b151-0e0fa41a937f"><br/>
<b>✅바뀐 데이터베이스</b><br/>
<img src="https://github.com/jebomin/RASA_music_chatbot/assets/42407430/e655b0dd-95e8-4dea-8e00-da9da1fc476d"><br/>
### 6. 이스터에그
