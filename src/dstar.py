from coefficient import *

class dstar:
    def __init__(self):
        pass

    def analyze(self, coverage_data, pass_fail_data, coeff: coefficient):
        # make sure the coverage data and pass_fail_data are the same length
        assert len(coverage_data[0]) == len(pass_fail_data)
        
        # n_f are the number of fails in pass_fail_data
        self.n_f = pass_fail_data.count(False)
        
        # n_p are the number of passes in pass_fail_data
        self.n_p = pass_fail_data.count(True)

        # n is the total number of tests
        self.n = len(pass_fail_data)

        self.coverage_nodes = []
        for statement in coverage_data:
            node = dstar_node(statement, pass_fail_data)
            node.s = self.n_p
            node.f = self.n_f
            node.all_test_case_data = statement
            self.coverage_nodes.append(node)
        
        for node in self.coverage_nodes:
            node.score = coeff.calculate(node)
                
        for i, node in enumerate(self.coverage_nodes):
            if node.score > 0:
                print(f'statement {i+1} has score {node.score}')

        print(f'{len(self.coverage_nodes)}')



class dstar_node:
    def __init__(self, statement, pass_fail_data) -> None:
        self.ncf = 0    # ncf: failed test cases that covered the statement
        self.nuf = 0    # nuf: failed test cases that did not cover the statement
        self.ncs = 0    # ncs: passed test cases that covered the statement
        self.nus = 0    # nus: passed test cases that did not cover the statement
        self.nc = 0     # nc: total number of test cases that covered the statement
        self.nu = 0     # nu: total number of test cases that did not cover the statement
        self.s = 0      # s: total number of passed test cases
        self.f = 0      # f: total number of failed test cases
        self.score = 0
        self.pass_fail_data = pass_fail_data
        self.all_test_case_data = []
        self.populate(statement, pass_fail_data)
    
    def populate(self, statement_data, pass_fail_data):
        # print(f'pass_fail_data: {pass_fail_data}')
        # print(f'statement_data: {statement_data}')
        for i, statement in enumerate(statement_data):

            if pass_fail_data[i] == False and statement > 0:
                self.ncf += 1
            
            if pass_fail_data[i] == True and statement > 0:
                self.ncs += 1
            
            if pass_fail_data[i] == False and statement == 0:
                self.nuf += 1
            
            if pass_fail_data[i] == True and statement == 0:
                self.nus += 1
            
            if statement > 0:
                self.nc += 1
            
            if statement == 0:
                self.nu += 1

        
        return
            

