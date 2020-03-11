####### Milestone 3 Python Script
import pandas as pd
import scipy.stats as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")



##Step 1: Import your data set
##-----------------------------------------------------------------------------
manchesterweather = pd.read_csv('ManchesterWeather.csv')

####### Step 2: Analysis of Variance for five population means
##----------------------------------------------------------------------------------------------------------------
print ('Analysis of Variance for five population means - Step 2')
may_data = manchesterweather.loc[manchesterweather['Month'] == 5]['EMXT']
jun_data = manchesterweather.loc[manchesterweather['Month'] == 6]['EMXT']
jul_data = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXT']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXT']
sep_data = manchesterweather.loc[manchesterweather['Month'] == 9]['EMXT']
print (st.f_oneway(may_data, jun_data, jul_data, aug_data, sep_data))
print ('')


####### Step 3: Analysis of Variance for six population means
##----------------------------------------------------------------------------------------------------------------
print ('Analysis of Variance for six population means - Step 3')
jul_data = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXP']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXP']
sep_data = manchesterweather.loc[manchesterweather['Month'] == 9]['EMXP']
print (st.f_oneway(jul_data, aug_data, sep_data))
print ('')


####### Step 4: Plot boxplots to evaluate any significant differences (5 Means).
##----------------------------------------------------------------------------------------------------------------
print ('Boxplots for five population means - Step 4 (NOTE: Boxplots will be saved in a file called step4_5_means.png)')
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib as mpl
import matplotlib.pyplot as plt
may_data = manchesterweather.loc[manchesterweather['Month'] == 5]['EMXT']
jun_data = manchesterweather.loc[manchesterweather['Month'] == 6]['EMXT']
jul_data = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXT']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXT']
sep_data = manchesterweather.loc[manchesterweather['Month'] == 9]['EMXT'] 
data = [may_data, jun_data, jul_data, aug_data, sep_data]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data)
plt.xticks([1, 2, 3, 4, 5], ['May', 'Jun', 'Jul', 'Aug', 'Sep'])
fig.savefig('step4_5_means.png')
print ('')


####### Step 5: Plot boxplots to evaluate any significant differences (3 Means).
##----------------------------------------------------------------------------------------------------------------
print ('Boxplots for five population means - Step 5 (NOTE: Boxplots will be saved in a file called step5_3_means.png)')
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib as mpl
import matplotlib.pyplot as plt
jul_data = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXP']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXP']
sep_data = manchesterweather.loc[manchesterweather['Month'] == 9]['EMXP'] 
data = [jul_data, aug_data, sep_data]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data)
plt.xticks([1, 2, 3], ['Jul', 'Aug', 'Sep'])
fig.savefig('step5_3_means.png')