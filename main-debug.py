import sys

from apiautotest.cli import main_hrun, main_locust
from apiautotest.logger import color_print

cmd = sys.argv.pop(1)

if cmd in ["hrun", "apiautotest", "ate"]:
    main_hrun()
elif cmd in ["locust", "locusts"]:
    main_locust()
else:
    color_print("Miss debugging type.", "RED")
    example = "\n".join([
        "e.g.",
        "python main-debug.py hrun /path/to/testcase_file",
        "python main-debug.py locusts -f /path/to/testcase_file"
    ])
    color_print(example, "yellow")
