import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

def analayze_employe():
    try:
        current_folder = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        file_path = os.path.join(current_folder,"employee_dataset.csv")
    
        df = pd.read_csv(file_path)
        
        print(f"\n1.Dataset Shape:{df.shape[0]} Rows , {df.shape[1]} Columns")
        print(f'\n2.Columns Available:{','.join(df.columns)}')
        print(f'  Columns Count:{len(df.columns)}')
        print(f'\n3.Data Preview:')
        print(df.head(5))
        print(f'\n4.Basic Statistics:')
        print(df.describe())
        
        if 'Department' in df.columns and 'Monthly_Salary' in df.columns:
            avg_salary = df.groupby('Department')['Monthly_Salary'].mean()
            print(f'\n5.Average Salary by Department:')
            print(avg_salary)
        else:
            print(f'\nError in Finding Average')
    
    except FileNotFoundError:
        print("\nError : File Not Found error!")
    except pd.errors.EmptyDataError:
        print(f"\nThe file {file_path} is empty!")
    except Exception as e :
        print(f"\nError : {e}")
    
analayze_employe()