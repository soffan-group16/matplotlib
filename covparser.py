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
    branch_hits = set(map(int, string_data.split(",")[:-1]))
    branch_count = max(branch_hits)
    branch_hits.remove(branch_count)
    missing_branch_ids = set([i for i in range(branch_count)])
    branch_misses = missing_branch_ids - branch_hits
    branch_hit_percentage = len(branch_hits)/branch_count
    output(branch_count, branch_hits, branch_misses, branch_hit_percentage)
    with open(report_file_name + "parsed", "w") as output_file:
        output(branch_count, branch_hits, branch_misses, branch_hit_percentage, output_file)
    shutil.copy(report_file_name, f"{report_file_name}copy")
    os.remove(report_file_name)

def output(branch_count, branch_hits, branch_misses, branch_hit_percentage, file=sys.stdout):
    with file as sys.stdout:
        print(f"branch count: {branch_count}")
        print(f"branch hits: {branch_hits}")
        print(f"branch misses: {branch_misses}")
        print(f"branch hit percentage: {branch_hit_percentage}")


if __name__ == "__main__":
    main()
