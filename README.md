# Macro Tracker CLI

A simple command-line tool to track daily macronutrient intake to assist fitness and health goals. (built using Python)

---

## Features

- Add food or meal entries with calories, protein, carbs, fat, and sodium
- View daily totals for each macro
- Save and load data to/from 'entries.json'
- Displays a random motivational quote on exit

---

## Getting Started

1. **Clone the repo:**
```bash
   git clone https://github.com/everettpotter/macro-tracker.git
   cd macro-tracker
```
2. **(Optional) Create and activate a virtual environment**
- On Mac/Linux
```bash
python -m venv venv
source venv/bin/activate
```
- On Windows
```bash
python -m venv venv
venv/Scripts/activate
```
3. **Run the app:**
```bash
python main.py
```

4. **Use the CLI menu to:**
- Add entries (calories, protein, carbs, fat, sodium)
- View total macros for the day
- Exit with a motivational quote

---

## File Structure

```markdown
MacroTracker/
├── data                    
│     ├── entries.json  # log of entries
│     └── quotes.txt    # random motivational quotes
├── .gitignore
├── LICENSE
├── main.py             # CLI logic and menu system
└── tracker.py          # Add/view logic and JSON handling
```

---

## Next Steps

- Add macro goal tracking (set certain targets for certain categories)
- Calculate weekly averages
- Build Flask or React UI for web version
- Add data visualization for progress tracking

---

## Why this project?
As someone who spends a lot of time training for endurance races and lifting, tracking nutrition is key to steady progress. This tool makes logging meals quick and easy.

---

## DISCLAIMER
All motivational quotes used in this project are sourced from publicly available material and belong to their respective authors. No copyright ownership is implied.
