
'''
This is called every time a report is generated by test_runner. This class will parse the .gcov file and store the coverage information along with the test failure/pass information
'''

class gcov_parser():

    def __init__(self, file_path, num_tests) -> None:
        self.file_path = file_path
        self.init = 0
        self.num_tests = num_tests


    def count_code_lines(self, file_content):
        lines = file_content.split('\n')
        code_line_count = 0
        for line in lines:
            # Split each line on ':' and check if there is code after the split
            parts = line.split(':', 1)
            if len(parts) > 1 and parts[1].strip() != '':
                code_line_count += 1
        return code_line_count


    def parse_gcov(self, execution_number):
        """
        Parse a gcov file and return a list of dictionaries containing line number,
        execution count, and source line.

        :param filename: Path to the gcov file
        :return: A list of dictionaries, each representing a line in the gcov file
        """
        if self.init == 0:
            with open(self.file_path, 'r') as file:
                file_content = file.read()
            
            self.source_code_length = self.count_code_lines(file_content)
            
            # make a new array of dimensions source_code_length x num_test
            self.coverage_data = [[0 for i in range(self.num_tests)] for j in range(self.source_code_length)]
            self.init = 1
        

        coverage_data = []
        filename = self.file_path

        self.lines = []

        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(':', 2)

                if len(parts) == 3:
                    execution_count = parts[0].strip()
                    line_number = parts[1].strip()
                    source_line = parts[2].strip()

                    # Handle non-executable lines and lines with execution count as '#####'
                    if execution_count == '-':
                        continue
                    elif execution_count == '#####':
                        execution_count = 0
                    else:
                        execution_count = int(execution_count)

                    self.lines.append(parts)
                    coverage_data.append({
                        'line_number': int(line_number),
                        'execution_count': execution_count,
                        'source_line': source_line
                    })
                    self.coverage_data[int(line_number) - 1][execution_number] = execution_count
        
        return self.coverage_data
