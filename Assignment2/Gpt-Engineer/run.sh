python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python game.py

pytest test_game.py
