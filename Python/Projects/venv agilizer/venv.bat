@echo off
python venv-agilizer.py %*
activate > nul 2> nul && echo "[!] Run activate to finally activate your environment!"
@echo on
