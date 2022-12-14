import glob,os
import pandas as pd

# analyze eeg data and compare the patterns between discount and limited edition
def discount_edition_anal(band):
    discount_all = pd.DataFrame()
    edition_all = pd.DataFrame()
    for eeg_norm in glob.glob(f'*_{band}_*.csv'):
        eeg_norm_df = pd.read_csv(eeg_norm)
        
        discount_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D'])].index.tolist()
        discount_events = pd.DataFrame()
        for d in discount_event_indexes:
            discount_event = eeg_norm_df[d-20:d].iloc[:,1:].mean(axis='index') # 1 ib-discount event (5 sec)
            discount_events = pd.concat([discount_events,discount_event],axis=1)
        discount_1p = discount_events.mean(axis='columns') # 1 participant's ib-discount events
        discount_all = pd.concat([discount_all,discount_1p],axis=1) # all participant's ib-discount events
        
        edition_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['E'])].index.tolist()
        edition_events = pd.DataFrame()
        for e in edition_event_indexes:
            edition_event = eeg_norm_df[e-20:e].iloc[:,1:].mean(axis='index')
            edition_events = pd.concat([edition_events,edition_event],axis=1)
        edition_1p = edition_events.mean(axis='columns')
        edition_all = pd.concat([edition_all,edition_1p],axis=1)
    
    discount_5p = discount_all.mean(axis='columns')
    edition_5p = edition_all.mean(axis='columns')
    de = pd.concat([discount_5p,edition_5p],axis=1)
    de.columns = ["discount", "limited edition"]
    de.to_csv(f'../eeg-analysis/de_{band}.csv')

def main():
    os.chdir('../eeg-normalized')
    discount_edition_anal('alpha')
    discount_edition_anal('low_beta')
    discount_edition_anal('mid_beta')
    discount_edition_anal('high_beta')

if __name__ == '__main__':
    main()