@ECHO OFF
set FLASK_APP=project.app
set FLASK_ENV=development
set DEBUG=true
@REM set JWT_SECRET_KEY="1cb36505e1924ec58aac929c18588f82"

@REM SET DB_NAME=pharmacy
@REM SET DB_URL=localhost
@REM SET DB_USER=root
@REM SET DB_PWD=aziz123
@REM SET DB_PORT=3306

CMD /k "python -B runDebug.py"