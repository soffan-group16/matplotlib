import os
import sys
import shutil

def main():
    if len(sys.argv) != 2:
        raise IOError("Wrong number of arguments")
    report_file_name = sys.argv[1]
    with open(report_file_name, "r") as report_file:
        string_data = report_file.readline()
    # map(print, string_data.split(","))
    data = set(map(int, string_data.split(",")[:-1]))
    branch_count = max(data)
    data.remove(branch_count)
    missing_branch_id = set([i for i in range(branch_count)])
    print(data)
    print(branch_count)
    print(len(data)/branch_count)
    print(missing_branch_id - data)
    shutil.copy(report_file_name, f"{report_file_name}copy")
    os.remove(report_file_name)

if __name__ == "__main__":
    main()
