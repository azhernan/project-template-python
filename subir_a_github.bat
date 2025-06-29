@echo off
set /p repo_url=URL del repositorio remoto (SSH o HTTPS):

REM Inicializa Git si no existe
IF NOT EXIST .git (
    git init
)

REM Agrega archivos y hace primer commit si no hay commits todavía
git rev-parse --verify HEAD >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    git add .
    git commit -m "Primer commit automático"
)

REM Fuerza rama main
git branch -M main

REM Agrega remote si no existe
git remote show origin >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    git remote add origin %repo_url%
)

REM Sube al remoto
git push -u origin main

echo Proyecto subido a GitHub correctamente.
pause
