from typing import List
import subprocess


def find_missing_annotations(path_to_module: str) -> List[str]:
    _found_missing_annotations = []
    try:
        success_output = subprocess.check_output(["mypy", path_to_module, "--disallow-untyped-defs"]).decode()
        print("No missing types found")
    except subprocess.CalledProcessError as e:
        output = e.output.decode()

        for line in output.split("\n"):
            if line.endswith("Function is missing a type annotation"):
                _found_missing_annotations.append(line.split(": error: ")[0].replace("__", "\_\_"))

    return _found_missing_annotations

if __name__ == "__main__":

    found = find_missing_annotations("../Adafruit_CircuitPython_ImageLoad/adafruit_imageload")
    print(found)

