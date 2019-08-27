# -*- coding: utf-8 -*-
import json
from datetime import date
from pathlib import Path

NOW_DIR = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR.joinpath('templates')

print(BASE_DIR)
print(TEMPLATE_DIR)

person = {"name": "Light", "location": "HangZhou"}
today = date(2019, 8, 27)
some_file = Path.joinpath(NOW_DIR, 'study_slot.py')

print(some_file.read_text())
