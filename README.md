
SSRF 공격방식에 대한 이해를 돕기 위한 데모 어플리케이션

"/" API는 Fronend 서버의 역할을 수행하는 API이다. 웹 브라우저를 통해 해당 API로 접근하여 데모를 진행한다.

"/ssrf" API는 Backend 서버의 역할을 수행하는 API이다. 요청을 받으면 Backend서버(Server-side)에서 QueryString상의 URL로 요청을 보내고, 응답 내용을 반환한다.

실행 방법:
```
python3 -m venv .venv
.venv/bin/pip3 install -r requirements.txt
sudo .venv/bin/python3 app.py
```
- 80번 포트에 대한 binding권한이 필요하므로 root 사용자로 실행 합니다.