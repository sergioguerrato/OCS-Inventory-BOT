node exportCSV.js
@echo exporting csv file from OCS...
python emailSender.py
@echo sending emails...
del C:\Users\supor\Downloads\export.csv
@echo off
cls
@echo.
@echo    ******************************************************
@echo    ***                   BOT-OCS                      ***
@echo    ***       Tarefas executadas com sucesso!          ***
@echo    ***                                                ***
@echo    ******************************************************
@echo    ***   Sergio Dpto. TI          ti@company.com.br   ***
@echo    ******************************************************
@echo.
timeout /t 5 /nobreak
