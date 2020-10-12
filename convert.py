from glob import glob
from tqdm import tqdm
import subprocess

svgs = glob("*.svg")
svgs.sort()

for i in tqdm(range(len(svgs))):
    out = "frame%05d.png" % (i+1)
    cmd = ["convert", svgs[i], out]
    subprocess.check_call(cmd)