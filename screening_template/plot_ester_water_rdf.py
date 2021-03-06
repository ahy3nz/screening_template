import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import pdb
import plot_ay
plot_ay.setDefaults()

unit_to_str = { 'angstrom**2': '$\AA^2$',
                'angstrom' : '$\AA$',
                'nanometer' : 'nm',
                'nanometer**2': 'nm$^2$' ,
                'degree': 'degree'}
df = pd.read_csv('rdf_peaks.csv')

bar_width = 0.5

############################
### DSPC ester-water RDF peaks ###
############################
fig, ax = plt.subplots(1,1)
ffabar_vals = []
ffayerr_vals = []
ffa_components = ['ffa12', 'ffa16', 'ffa24']
for component in ffa_components:
    thing = df.loc[(df[component] == 32.0) & (df['DSPC'] == 32.0)]
    ffabar_vals.append(thing['rdf_peak_mean'].values[0])
    ffayerr_vals.append(thing['rdf_peak_std'].values[0])


ohbar_vals = []
ohyerr_vals = []
oh_components = ['oh12', 'oh16', 'oh24']
for component in oh_components:
    thing = df.loc[(df[component] == 32.0) & (df['DSPC'] == 32.0)]
    ohbar_vals.append(thing['rdf_peak_mean'].values[0])
    ohyerr_vals.append(thing['rdf_peak_std'].values[0])


oh_x_vals = 1.5*np.arange(0, len(ohbar_vals), dtype=int) + 0.5
ffa_x_vals = 1.5*np.arange(0, len(ffabar_vals), dtype=int) + 1
xtick_vals = 1.5*np.arange(0, len(ffabar_vals), dtype=int) + 0.75

oh_bars = ax.bar(oh_x_vals, ohbar_vals, bar_width,
                    yerr=ohyerr_vals, label='50% OH, 50% DSPC')
ffa_bars = ax.bar(ffa_x_vals, ffabar_vals, bar_width,
                    yerr=ffayerr_vals, label='50% FFA, 50% DSPC')

ax.set_xticks(xtick_vals)
ax.set_xticklabels(['12', '16', '24'])
ax.set_ylabel("Ester-Water RDF peaks")
ax.set_xlabel("Tail length")
ax.legend(loc=4)
fig.tight_layout()
fig.savefig("ester-water_rdf.png")
plt.close(fig)

