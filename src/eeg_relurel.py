import glob,os
import pandas as pd

# analyze eeg data and compare the patterns between relatedted and unrelatedted item
def related_anal(band):
    related_all = pd.DataFrame()
    unrelated_all = pd.DataFrame()
    for eeg_norm in glob.glob(f'*_{band}*.csv'):
        eeg_norm_df = pd.read_csv(eeg_norm)
        
        related_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['R'])].index.tolist()
        print(eeg_norm+'_related:'+str(len(related_event_indexes)))
        related_events = pd.DataFrame()
        for r in related_event_indexes:
            related_event = eeg_norm_df[r-20:r].iloc[:,1:].mean(axis='index') # 1 related event (5 sec)
            related_events = pd.concat([related_events,related_event],axis=1)
        related_1p = related_events.mean(axis='columns') # 1 participant's related events
        related_all = pd.concat([related_all,related_1p],axis=1) # all participant's related events
        
        unrelated_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['U'])].index.tolist()
        print(eeg_norm+'_unrelated:'+str(len(unrelated_event_indexes)))
        unrelated_events = pd.DataFrame()
        for u in unrelated_event_indexes:
            unrelated_event = eeg_norm_df[u-20:u].iloc[:,1:].mean(axis='index')
            unrelated_events = pd.concat([unrelated_events,unrelated_event],axis=1)
        unrelated_1p = unrelated_events.mean(axis='columns')
        unrelated_all = pd.concat([unrelated_all,unrelated_1p],axis=1)
    
    related_5p = related_all.mean(axis='columns')
    unrelated_5p = unrelated_all.mean(axis='columns')
    related = pd.concat([related_5p,unrelated_5p],axis=1)
    related.columns = ["related", "unrelated"]
    related.to_csv(f'../eeg-analysis/relation_{band}.csv')

def main():
    os.chdir('../eeg-rel')
    related_anal('alpha')
    related_anal('low_beta')
    related_anal('mid_beta')
    related_anal('high_beta')

if __name__ == '__main__':
    main()