"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """        
		#这是我的解法，虽然简短，但是速度慢
        for x in employees:
            if x.id == id:
                return x.importance + sum([self.getImportance(employees, i) for i in x.subordinates])
				
		'''
		下面方法使用id构建map，访问的很快
		emps = {employee.id: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return subordinates_importance + emps[id].importance
        return dfs(id)
		
		emps = {employee.id: employee for employee in employees}
        dfs = lambda id: sum([dfs(sub_id) for sub_id in emps[id].subordinates]) + emps[id].importance
        return dfs(id) 
		'''