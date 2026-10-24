#!/usr/bin/env python3
"""Detecta cuándo empieza el Reel dentro de la grabación y dónde se repite (bucle) y recorta justo esa parte.
Uso: recortar_bucle.py entrada.mp4 salida.mp4   (entrada ya recortada a 9:16, sin audio)"""
import subprocess, sys, statistics as st
FF="/opt/homebrew/bin/ffmpeg"; src, dst = sys.argv[1], sys.argv[2]; FPS=5; W,H=32,56
raw = subprocess.run([FF,"-nostdin","-v","error","-i",src,"-an","-vf",f"fps={FPS},scale={W}:{H},format=gray","-f","rawvideo","-"],capture_output=True).stdout
n = len(raw)//(W*H); fr = [raw[i*W*H:(i+1)*W*H] for i in range(n)]
def desv(f): m=sum(f)/len(f); return (sum((x-m)**2 for x in f)/len(f))**0.5
def dif(a,b): return sum(abs(x-y) for x,y in zip(a,b))/len(a)
s = next((i for i in range(n-6) if all(desv(fr[i+k])>28 for k in range(6))), 0)
sig = [fr[s+2+k] for k in range(5)]
D = {i: sum(dif(fr[i+k],sig[k]) for k in range(5))/5 for i in range(s+25, n-5)}
fin = n
if D:
    med = st.median(D.values()); cand = [i for i,v in D.items() if v < 0.4*med and (i-1 not in D or D[i-1] >= v) and (i+1 not in D or D[i+1] >= v)]
    if cand: fin = min(cand) - 2
ini_s = max(0, s/FPS - 0.1); dur = max(1.0, (fin - s)/FPS)
subprocess.run([FF,"-nostdin","-y","-v","error","-ss",f"{ini_s:.2f}","-i",src,"-t",f"{dur:.2f}","-an","-c:v","libx264","-crf","22","-preset","veryfast","-pix_fmt","yuv420p",dst])
print(f"inicio {ini_s:.1f}s · duración {dur:.1f}s · bucle {'detectado' if fin<n else 'no detectado (la grabación terminó antes de repetirse)'}")
