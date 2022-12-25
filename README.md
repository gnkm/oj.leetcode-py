# Snippets

## Usage

### Create Python virtual env

```
anyenv install pyenv
pyenv install 3.10.2
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.10.2/bin/python
```

### Prepare

```
poetry shell
poetry install
```

### Start solving

Create some files for a problem.

```
python create_files.py {ID}
```

Created files are following.

```
leetcode/problems
└── no_{ID}
   ├── __init__.py
   └── mycode_01.py

leetcode/tests/problems
└── no_{ID}
   ├── __init__.py
   └── test.py
```

e.g.

```
python create_files.py 12
```

Then, following files are created.

```
leetcode/problems
└── no_0012
   ├── __init__.py
   └── mycode_01.py

leetcode/tests/problems
└── no_0012
   ├── __init__.py
   └── test.py
```
