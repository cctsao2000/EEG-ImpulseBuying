low_beta = readtable('regret/regret_low_beta.csv');
low_beta_r = low_beta(:,2);
low_beta_ur = low_beta(:,3);
low_beta_r = table2array(low_beta_r);
low_beta_ur = table2array(low_beta_ur);
r = topoplot(low_beta_r, 'IB2.loc','nosedir','+Y','electrodes','ptslabels');
caxis([-50, 50]);
saveas(r,'low_beta_re.png');
clf reset
nib = topoplot(low_beta_ur, 'IB2.loc','nosedir','+Y','electrodes','ptslabels');
caxis([-50, 50]);
saveas(nib,'low_beta_ur.png');