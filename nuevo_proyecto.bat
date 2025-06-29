@echo off
set /p name=Nombre del nuevo proyecto:
set /p template=Nombre del repositorio plantilla (por defecto: project-template-python):

if "%template%"=="" set template=project-template-python

cd C:\Users\azher\Projects
git clone https://github.com/azhernan/%template%.git %name%
cd %name%

REM Elimina vínculo al repo plantilla
rmdir /s /q .git

REM Inicia Poetry con nombre personalizado
poetry init --name %name% --no-interaction
poetry config virtualenvs.in-project true

echo Proyecto "%name%" creado y listo.

REM Abre Visual Studio Code
code .
