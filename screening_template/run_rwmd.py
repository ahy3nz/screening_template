import os
import json
import numpy as np
import operations
import script_utils

################
## Script to iterate through folders, write rwmd files, and submit
################

index = json.load(open('index.txt','r'))
n_nodes = 3
jobid = [None] * n_nodes
curr_dir = os.getcwd()
for i, name in enumerate(index.keys()):
    os.chdir(os.path.join(curr_dir, name))
    rwmd_submission = operations.write_rwmd_lines(tc_groups=['non-water', 'water'],
                                t_pairs=[[305, 455], [305,455]], cooling_rate=1000,
                                gro='npt_500ps.gro', top='compound.top')
    with open('rwmd_chain.pbs', 'w') as f:
        body = 'cd {}\n'.format(os.getcwd())
        body += rwmd_submission
        script_utils.write_rahman_script(f, jobname='{}_rwmd'.format(name), body=body)
    jobid = operations.submit_job('rwmd_chain.pbs', jobid, n_nodes, i)
