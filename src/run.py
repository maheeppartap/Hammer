from gcov_parser import gcov_parser
from test_runner import test_runner
from dstar import dstar
from dstar import dstar_node
from kulczynski import kulczynski
from simple_matching import simple_matching

import os

project_directory = "/home/beepboop/projects/lightning-2"

def main():
    tr = test_runner(["t1"])
    coeff = simple_matching()
    # # now we have coverage data
    dstar_instance = dstar()
    ret_val = dstar_instance.analyze(tr.coverage_data, tr.test_pass_or_fail, coeff)




if __name__ == "__main__":
    main()