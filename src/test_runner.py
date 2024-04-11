'''
This file will run the test cases. Given a .cpp file, and it's multiple input commands, and their expected return values,
it will compile the .cpp file, execute the code with the commands, and compare the expected return value with expected and generate a report.
This report will then be parsed by gcov_parser.py everytime a test is run to store the coverage information.
'''
import json
import os
import subprocess
import gcov_parser

class test_runner:
    def __init__(self, test_cases: list[str]) -> None:
        self.test_cases = test_cases
        self.compiled_data = []
        self.project_directory = "/home/beepboop/projects/lightning-2" # todo: change 

        for test_case in test_cases:
            self.compiled_data.append(self._parse_json(test_case))
        
        for test_case_data in self.compiled_data:
            self.run_test(test_case_data)


    def run_test(self, test_case_data: dict) -> None:
        # get the path
        path = test_case_data["path"]
        tests_to_run = test_case_data["tests"]
        gcov_path = test_case_data["gcov_path"]
        compile_script = test_case_data["compile_script"]


        subprocess.run(compile_script, shell=True)


        self.gcov_parser_instance = gcov_parser.gcov_parser(gcov_path, len(tests_to_run))


        self.test_pass_or_fail = []

        for i, test in enumerate(tests_to_run):
            # execute the compile script in bash
            subprocess.run(compile_script, shell=True)

            # run the file, get the return value from the executable
            command = test["command"]
            return_value = subprocess.run(command, shell=True, capture_output=True)


            # compare the return value with the expected value
            expected_return_value = test["expected_output"]
            if return_value.returncode == int(expected_return_value):
                print(f'test {i} passed')
                self.test_pass_or_fail.append(True)
            else:
                print(f'test {i} failed. Expected {expected_return_value}, got {return_value.returncode}')
                self.test_pass_or_fail.append(False)
            

            # generate the gcov report
            gcov_command = test["generate_report"]
            subprocess.run(gcov_command, shell=True)
            

            # parse the gcov file
            self.gcov_parser_instance.parse_gcov(i)

            cleanup_script = test["cleanup"]
            subprocess.run(cleanup_script, shell=True)
        


        self.coverage_data = self.gcov_parser_instance.coverage_data
            

            

            
            






    
    def _convert_to_json_path(self, test_case: str) -> str:
        return f'{self.project_directory}/test_code/{test_case}/test.json'

    def _parse_json(self, test_case: str) -> dict:
        # get the path
        path = self._convert_to_json_path(test_case)
        # parse the file into a dict
        with open(path, 'r') as file:
            return json.load(file)
        
