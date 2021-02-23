import os
import sys


class Coverage:
    def __init__(self, branch_count, function_name):
        try:
            self.test_mode = int(os.environ["COV_TEST"])
        except (KeyError, ValueError):
            self.test_mode = 0
        if self.test_mode:
            self.branch_count = branch_count
            self.function_name = function_name
            self.log_list = [False for _ in range(branch_count)]
            self.reports_folder = os.environ["COV_REPORTS_PATH"]

    def log(self, id):
        if not self.test_mode:
            return
        if id >= self.branch_count:
            print(f"Id {id} to large", file=sys.stderr)
            return
        self.log_list[id] = True

    def report(self):
        if not self.test_mode:
            return
        with open(
            f"{self.reports_folder}{self.function_name}.report", "a"
        ) as output_file:
            output_file.write(f"{self.branch_count},")
            for id, log in enumerate(self.log_list):
                if log:
                    output_file.write(f"{id},")
