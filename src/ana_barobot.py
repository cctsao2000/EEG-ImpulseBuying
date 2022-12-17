import glob,os
import pandas as pd

# analyze eeg data and compare the patterns between before robot and  after robot
def before_after_anal(band):
    beforer_all = pd.DataFrame()
    afterr_all = pd.DataFrame()
    for eeg_norm in glob.glob(f'*_{band}_*.csv'):
        eeg_norm_df = pd.read_csv(eeg_norm)
        
        beforer_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D1','E1'])].index.tolist()
        print(eeg_norm+'_before:'+str(len(beforer_event_indexes)))
        beforer_events = pd.DataFrame()
        for b in beforer_event_indexes:
            beforer_event = eeg_norm_df[b-20:b].iloc[:,1:].mean(axis='index') # 1 before-robot event (5 sec)
            beforer_events = pd.concat([beforer_events,beforer_event],axis=1)
        beforer_1p = beforer_events.mean(axis='columns') # 1 participant's before-robot events
        beforer_all = pd.concat([beforer_all,beforer_1p],axis=1) # all participant's before-robot events
        
        afterr_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D2','E2'])].index.tolist()
        print(eeg_norm+'_after:'+str(len(afterr_event_indexes)))
        afterr_events = pd.DataFrame()
        for a in afterr_event_indexes:
            afterr_event = eeg_norm_df[a-20:a].iloc[:,1:].mean(axis='index')
            afterr_events = pd.concat([afterr_events,afterr_event],axis=1)
        afterr_1p = afterr_events.mean(axis='columns')
        afterr_all = pd.concat([afterr_all,afterr_1p],axis=1)
    
    beforer_5p = beforer_all.mean(axis='columns')
    afterr_5p = afterr_all.mean(axis='columns')
    ba = pd.concat([beforer_5p,afterr_5p],axis=1)
    ba.columns = ["before robot", "after robot"]
    ba.to_csv(f'../eeg-analysis/ba_{band}.csv')

def main():
    os.chdir('../eeg-normalized')
    before_after_anal('alpha')
    before_after_anal('low_beta')
    before_after_anal('mid_beta')
    before_after_anal('high_beta')

if __name__ == '__main__':
    main()