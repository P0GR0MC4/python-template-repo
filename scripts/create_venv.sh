#!/bin/bash
set -e
echo "==> Tworzenie środowiska venv..."
python3 -m venv venv
source venv/bin/activate
echo "==> Instalacja pakietów..."
pip install --upgrade pip
pip install -r requirements.txt