import pandas as pd
df = pd.read_csv('sample_employee_data.csv')
salary_sorted = df.sort_values(by= 'Salary', ascending=False)

big_3 = ['USA','UK','China']
def double_salary(row):
    if row['Country'] in big_3:
        return 2 * row['Salary']
    return row['Salary']

df['Salary'] = df.apply(double_salary, axis=1)

df.loc[df.Name == 'Oscar Wright', 'Salary']=0

df = df.set_index('Name')


# gather info on employees older than 30 and salary less than average
median_salary = df.Salary.median()
not_doing_too_well = df[(df.Age >30) & (df.Salary < median_salary)]
















def sqrt(x):
    for i in range(x,-1,-1):
        if i**2 < x:
            return i
print(sqrt(8))
