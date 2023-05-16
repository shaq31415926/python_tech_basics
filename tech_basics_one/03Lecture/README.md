# Instructions for creating your gui calculator

## Requirements
- Python3 +

## Instructions

1. Create a virtual environment 

- If you installed python with conda please follow the following steps to create a virtual environment called calc.
```bash
  conda create –-name calc python
```

Activate your environment
```bash
  conda activate calc
```

- If you do not have conda, create a virtual environment using the following steps

i. You need to install the library virtualenv
```bash
  pip3 install virtualenv
```

ii: Create a virtual environment called calc with virtualenv

Window users:
```bash
  python -m venv calc
```

MAC users:
```bash
  virtualenv -p python calc
```

iii. Activate your virtual environment

Window users:
```bash
  .\calc\Scripts\activate
```

MAC users:
```bash
  source calc/bin/activate
```

3. In your activated virtual environment, install the library tkinter
```bash
  pip3 install tk
```

4. Create a script called gui_calculator.py and execute the code that you can copy from [here](https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_one/03Lecture/gui_calculator_demo.py).

5. Run the code

Window users:
```bash
  python gui_calculator.py
```
MAC users:
```bash
  python3 gui_calculator.py
```

