import numpy as np
import pandas as pd
import datetime
import random as r

def randate():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2021, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = r.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

donor = pd.read_csv("donors.csv")
receiver = pd.read_csv("receiver.csv")
delivery = pd.read_csv("delivery.csv")
donor = donor[['ID']]
receiver = receiver[['ID', 'Accepts']]
delivery = delivery[['employeeID', 'isWorkingForSocialCause']]

d = delivery.to_numpy()
del_worker = [d[0][0]]
for i in d:
    if i[1] == 1:
        del_worker = np.append(del_worker, i[0])
don = donor.to_numpy()
rec = receiver.to_numpy()
x = randate()
stat = ['delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'delivered', 'active']
arr = np.array([['donor', 'receiver', 'delivery', 'category', 'status', 0, x]])
for i in range(220):
    di = r.randint(0,len(don) - 1)
    ri = r.randint(0,len(rec) - 1)
    dwi = r.randint(0,len(del_worker) - 1)
    dai = randate()
    xi = r.randint(0,len(stat) - 1)
    if rec[ri][1] == 'Money':
        temp = [[don[di][0], rec[ri][0], del_worker[dwi], rec[ri][1], stat[xi], r.randint(100,2000), dai]]
    else:
        temp = [[don[di][0], rec[ri][0], del_worker[dwi], rec[ri][1], stat[xi], 1, dai]]
    arr = np.append(arr, temp, axis = 0)
print(arr)
pd.DataFrame(arr).to_csv("donation.csv")
