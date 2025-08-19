import pandas as pd 
import numpy as np 
np.random.seed(1) 
employees = [f"Emp{i}" for i in range(1, 31)] 
departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales'] 
work_hours = [] 
for emp in employees: 
    dept = np.random.choice(departments) 
    hours = np.random.randint(30, 51)  # Random work hours between 30 to 50 
    work_hours.append([emp, dept, hours]) 
df = pd.DataFrame(work_hours, columns=['Employee', 'Department', 'WorkHours']) 
grouped = df.groupby('Department').agg( 
    TotalHours=('WorkHours', 'sum'), 
    AverageHours=('WorkHours', 'mean'), 
    EmployeeCount=('Employee', 'count') 
).reset_index() 
pivot = pd.pivot_table(df, index='Department', values='WorkHours', 
                       aggfunc=['sum', 'mean', 'count']) 
pivot.columns = ['TotalHours', 'AverageHours', 'EmployeeCount'] 
pivot = pivot.reset_index() 
top_dept = pivot.loc[pivot['AverageHours'].idxmax()] 
highlight = f" Department with highest average working hours: {top_dept['Department']} ({top_dept['AverageHours']:.2f} hrs)" 
print("=== Department-wise Work Hours Summary ===") 
print(pivot) 
print("\n" + highlight) 
