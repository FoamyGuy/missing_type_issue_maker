import os
from find_missing_type_annotations import find_missing_annotations
from make_issue_description import make_issue_description

KNOWN_PY_FILES = ["setup.py",
                  "find_missing_type_annotations.py",
                  "make_issue_description.py",
                  "run_on_each.py"]

KNOWN_DIRS = [".github",
              "docs",
              "examples",
              "LICENSES",
              "templates",
              ".mypy_cache",
              "test",
              "__pycache__",
              "util",
              "tests"]



repo_files = os.listdir("./")
lib_module = None
lib_package = None

for file in repo_files:
    if file.endswith(".py") and file not in KNOWN_PY_FILES:
        lib_module = file

if lib_module is None:
    for file in repo_files:
        if os.path.isdir(file) and file not in KNOWN_DIRS:
            lib_package = file

mypy_target = None
if lib_package:
    mypy_target = lib_package
    print(lib_package)
else:
    mypy_target = lib_module
    print(lib_module)

print(mypy_target)
missing_types = find_missing_annotations(mypy_target)

if len(missing_types) > 0:
    #print(missing_types)
    make_issue_description(missing_types)

#os.system("ls ./")

