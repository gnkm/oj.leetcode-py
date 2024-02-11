# Snippets

## Usage

### Create Python virtual env

```
asdf install python 3.11.7
poetry use env $HOME/.asdf/installs/python/3.11.7/bin/python
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

Make some files for contests.

```
python create_files.py 12 --problem_type contests
```

Then, following files are created.

```
leetcode/contests
└── no_0012
   ├── __init__.py
   └── mycode_01.py

leetcode/tests/contests
└── no_0012
   ├── __init__.py
   └── test.py
```
