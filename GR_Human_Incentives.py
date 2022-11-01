#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:25:10 2022

@author: agnes0x
"""

import  json
import pandas as pd
import numpy as np
from matplotlib import pyplot

df_input = pd.read_csv('GR15.csv')


"DISHONEST VOTING"

#rating distribution in % and total # of votes
df_rating = pd.crosstab(df_input['Participant_Id'],df_input['Vote'])
df_rating['Total # of votes'] = df_rating.sum(axis=1)
df_rating['%, vote 1'] = df_rating[1]/df_rating['Total # of votes']
df_rating['%, vote 2'] = df_rating[2]/df_rating['Total # of votes'] 
df_rating['%, vote 3'] = df_rating[3]/df_rating['Total # of votes']
df_rating['%, vote 4'] = df_rating[4]/df_rating['Total # of votes']
df_rating['%, vote 5'] = df_rating[5]/df_rating['Total # of votes']
df_rating=df_rating.drop(columns=[1,2,3,4,5])
#flag those who casted the same vote more than 60% of the time
flag_criteria = 0.6
df_rating['Flag_rating'] = np.select([df_rating['%, vote 1']> flag_criteria,
                                      df_rating['%, vote 2']> flag_criteria,
                                      df_rating['%, vote 3']> flag_criteria,
                                      df_rating['%, vote 4']> flag_criteria,
                                      df_rating['%, vote 5']> flag_criteria],
                                     ['1','1','1','1','1'], default='0')


"INCENTIVES"
## Nr of grants reviewed
#VISUAL
#on participant level
df_p_count = df_input.groupby('Participant_Id')['Option'].nunique()
#on user level
df_u_count = df_input.groupby('User_Id')['Option'].nunique()
# user & incentive level
table = pd.pivot_table(df_input, values='Option', index=['User_Id'], columns=['Incentive'], aggfunc=pd.Series.nunique)
table = table.sort_values([2,3,1], ascending=[True, True, True])
ax= table.plot.bar(rot=0, title='Total number of grants reviewed by userID are driven by incentives')
ax.set_xlabel("userID")
ax.set_ylabel("nr. of grants reviewed")



