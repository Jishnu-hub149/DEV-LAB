import pandas as pd 
data = { 
    'City': [ 
        'Delhi', 'Delhi', 'Delhi', 'Delhi', 
        'Mumbai', 'Mumbai', 'Mumbai', 'Mumbai', 
        'Chennai', 'Chennai', 'Chennai', 'Chennai' 
    ], 
    'Date': pd.to_datetime([ 
        '2024-04-07', '2024-04-14', '2024-05-05', '2024-06-02',    
        '2024-04-07', '2024-04-21', '2024-05-12', '2024-06-09',    
        '2024-04-14', '2024-05-19', '2024-06-02', '2024-06-30'    
    ]), 
    'Temperature': [ 
        35, 36, 38, 40,    
        30, 31, 34, 35,     
        33, 34, 36, 38    
    ] 
} 
df = pd.DataFrame(data) 
df['Month'] = df['Date'].dt.month_name() 
print("Weekly Temperature Dataset:\n") 
print(df) 
monthly_avg = df.groupby(['City', 'Month'])['Temperature'].mean().reset_index() 
pivot_table = monthly_avg.pivot(index='City', columns='Month', values='Temperature').fillna(0) 
print("\nMonth-wise Average Temperature (°C):\n") 
print(pivot_table) 
summer_months = ['April', 'May', 'June'] 
pivot_table['Summer_Avg'] = pivot_table[summer_months].mean(axis=1) 
hottest_city = pivot_table['Summer_Avg'].idxmax() 
max_avg_temp = pivot_table['Summer_Avg'].max() 
print(f"\nCity with highest average temperature in summer (Apr-Jun): {hottest_city} with {max_avg_temp:.2f}°C.") 
