from ortools.sat.python import cp_model
# based on https://developers.google.com/optimization/cp/cp_solver

def print_all_solns(varList,cpModel,solver):    
    solution_printer = VarArraySolutionPrinter(varList)
    status = solver.SearchForAllSolutions(cpModel, solution_printer)
    # print('Status = %s' % solver.StatusName(status))
    print('Number of solutions found: %i' % solution_printer.solution_count())

def print_optimal_soln(varList,cpModel,solver):
    # idf added
    solution_printer = VarArrayAndObjectiveSolutionPrinter(varList)
    status = solver.SolveWithSolutionCallback(cpModel, solution_printer)
    print('Status = %s' % solver.StatusName(status))
        
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count
    

# You need to subclass the cp_model.CpSolverSolutionCallback class.
class VarArrayAndObjectiveSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        print('Solution %i' % self.__solution_count)
        print('  objective value = %i' % self.ObjectiveValue())
        for v in self.__variables:
            print('  %s = %i' % (v, self.Value(v)), end=' ')
        print()
        self.__solution_count += 1

    def solution_count(self):
        return self.__solution_count
    
    
    