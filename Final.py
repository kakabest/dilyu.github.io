import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
raw_data['hour'] = pd.DatetimeIndex(raw_data['CRASH TIME']).hour
num_by_year = raw_data.groupby('hour')['CRASH DATE'].count()

plt.figure(figsize=(15, 7))
num_by_year.plot(kind='line', marker='o', color='blue')
plt.title('Number of Collections by Hour')
plt.xlabel('CRASH HOUR')
plt.ylabel('Number of CRASH')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()