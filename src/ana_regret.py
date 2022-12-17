import glob,os
import pandas as pd

# analyze eeg data and compare the patterns between regretted and unregretted item
def regret_anal(band):
    regret_all = pd.DataFrame()
    unregret_all = pd.DataFrame()
    for eeg_norm in glob.glob(f'*_{band}_*.csv'):
        eeg_norm_df = pd.read_csv(eeg_norm)
        
        regret_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D1R','E1R','DR','ER'])].index.tolist()
        print(eeg_norm+'_regret:'+str(len(regret_event_indexes)))
        regret_events = pd.DataFrame()
        for r in regret_event_indexes:
            regret_event = eeg_norm_df[r-20:r].iloc[:,1:].mean(axis='index') # 1 regret event (5 sec)
            regret_events = pd.concat([regret_events,regret_event],axis=1)
        regret_1p = regret_events.mean(axis='columns') # 1 participant's regret events
        regret_all = pd.concat([regret_all,regret_1p],axis=1) # all participant's regret events
        
        unregret_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D1','E1','D','E'])].index.tolist()
        print(eeg_norm+'_unregret:'+str(len(unregret_event_indexes)))
        unregret_events = pd.DataFrame()
        for u in unregret_event_indexes:
            unregret_event = eeg_norm_df[u-20:u].iloc[:,1:].mean(axis='index')
            unregret_events = pd.concat([unregret_events,unregret_event],axis=1)
        unregret_1p = unregret_events.mean(axis='columns')
        unregret_all = pd.concat([unregret_all,unregret_1p],axis=1)
    
    regret_5p = regret_all.mean(axis='columns')
    unregret_5p = unregret_all.mean(axis='columns')
    regret = pd.concat([regret_5p,unregret_5p],axis=1)
    regret.columns = ["regret", "unregret"]
    regret.to_csv(f'../eeg-analysis/regret_{band}.csv')

def main():
    os.chdir('../eeg-normalized')
    regret_anal('alpha')
    regret_anal('low_beta')
    regret_anal('mid_beta')
    regret_anal('high_beta')

if __name__ == '__main__':
    main()