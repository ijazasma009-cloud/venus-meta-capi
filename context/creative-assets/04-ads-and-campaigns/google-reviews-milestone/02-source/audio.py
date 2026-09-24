# VENUS AESTHETICS - "10,000 VOICES" REEL : sound design + score
# Synthesised to the exact timing map in the creative playbook.
import numpy as np, wave

SR   = 48000
DUR  = 45.0
N    = int(SR * DUR)
L    = np.zeros(N)
R    = np.zeros(N)
RVB  = np.zeros(N)
rng  = np.random.default_rng(7)

def idx(t): return int(t * SR)
def expdec(n, k): return np.exp(-np.linspace(0, k, n))

def add(t0, sig, pan=0.0, send=0.0):
    i = idx(t0)
    j = min(i + len(sig), N)
    if i >= N or j <= i: return
    s = sig[:j - i]
    gl = np.sqrt((1 - pan) / 2) * 1.414
    gr = np.sqrt((1 + pan) / 2) * 1.414
    L[i:j] += s * gl
    R[i:j] += s * gr
    if send > 0: RVB[i:j] += s * send

def lp1(sig, cut):
    c = np.atleast_1d(np.asarray(cut, dtype=float))
    if c.size == 1: c = np.full(len(sig), c[0])
    a = 1.0 - np.exp(-2 * np.pi * np.clip(c, 20, SR / 2.2) / SR)
    out = np.empty(len(sig)); y = 0.0
    for i in range(len(sig)):
        y += a[i] * (sig[i] - y)
        out[i] = y
    return out

def hp1(sig, cut): return sig - lp1(sig, cut)

# ---------------- voices ----------------
def blip(dur, f, amp, dec=18):
    n = int(dur * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * f * t
    s = np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.16 * np.sin(3 * ph)
    click = rng.normal(0, 1, n) * expdec(n, 600) * 0.5
    return (s * expdec(n, dec) + click) * amp

def kick(amp=1.0, dur=0.42, f0=110, f1=42):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 22)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * expdec(n, 9) + rng.normal(0, 1, n) * expdec(n, 420) * 0.28) * amp

def subhit(amp=1.0, dur=2.6, f0=76, f1=33):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 9)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * expdec(n, 3.4) + 0.30 * np.sin(ph * 2) * expdec(n, 7)) * amp

def noiseband(dur, f_start, f_end, amp, curve=1.0):
    n = int(dur * SR)
    cut = f_start + (f_end - f_start) * np.linspace(0, 1, n) ** curve
    return lp1(rng.normal(0, 1, n), cut) * amp

def whoosh(dur=0.55, amp=0.5, up=True):
    n = int(dur * SR)
    cut = np.linspace(300, 7000, n) if up else np.linspace(7000, 300, n)
    s = hp1(lp1(rng.normal(0, 1, n), cut), 220)
    return s * (np.sin(np.linspace(0, np.pi, n)) ** 1.6) * amp

def shimmer(dur=2.8, amp=0.35, base=1320):
    n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for k, mult in enumerate([1, 1.5, 2, 2.66, 3.4, 4.2, 5.6, 7.1]):
        f = base * mult * (1 + rng.normal(0, 0.002))
        out += np.sin(2 * np.pi * f * t + rng.random() * 6.28) * expdec(n, 2.2 + k * 0.55) / (k + 1.6)
    return out * amp

def pad(freqs, dur, amp, atk=1.2, rel=1.6, detune=0.004):
    n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for f in freqs:
        for d in (-detune, 0.0, detune):
            ff = f * (1 + d)
            out += np.sin(2 * np.pi * ff * t)
            out += 0.22 * np.sin(2 * np.pi * ff * 2 * t)
            out += 0.10 * np.sin(2 * np.pi * ff * 3 * t)
    out /= (len(freqs) * 3)
    a = int(atk * SR); r = int(rel * SR)
    e = np.ones(n)
    if a > 0: e[:a] = np.linspace(0, 1, a) ** 1.5
    if 0 < r < n: e[n - r:] = np.linspace(1, 0, r) ** 1.3
    return out * e * (1 + 0.006 * np.sin(2 * np.pi * 4.4 * t)) * amp

def pluck(f, dur, amp):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2 * t) + 0.2 * np.sin(2 * np.pi * f * 3.01 * t)
    return s * expdec(n, 7) * amp

def heartbeat(amp=0.5):
    n = int(0.55 * SR); t = np.arange(n) / SR
    f = 30 + 40 * np.exp(-t * 30)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * expdec(n, 11) * amp

# ==================================================================
# 0.00-3.00  OPENING : no music, one review notification tap
# ==================================================================
add(0.12, blip(0.60, 1180, 0.30), 0.0, 0.30)
add(0.12, blip(0.60, 1770, 0.14), 0.0, 0.25)
add(0.45, pad([55.0], 2.55, 0.055, atk=1.3, rel=0.8), 0.0, 0.05)

# ==================================================================
# 3.00-7.20  MULTIPLICATION : taps accelerate, electronic tension
# ==================================================================
tp, gap = 3.02, 0.230
while tp < 7.18:
    prog = (tp - 3.0) / 4.2
    add(tp, blip(0.28, 900 + prog * 700, 0.112 * (0.55 + prog), dec=26),
        (rng.random() * 2 - 1) * 0.65, 0.22)
    gap *= 0.905
    tp += max(gap, 0.050)
add(3.0, noiseband(4.2, 260, 6400, 0.085, curve=1.9), 0.0, 0.25)
for k in range(17):
    add(3.0 + k * 0.25, pluck([220.0, 261.63, 329.63][k % 3], 0.42, 0.052 * (0.4 + k / 17)),
        (k % 2 * 2 - 1) * 0.4, 0.28)
add(3.0, pad([110.0, 164.81], 4.25, 0.072, atk=2.2, rel=0.6), 0.0, 0.12)

# ==================================================================
# 7.20-8.60  FREEZE
# ==================================================================
add(7.20, subhit(0.55, dur=1.25, f0=70, f1=38), 0.0, 0.30)
rev = noiseband(1.25, 400, 3600, 0.10, curve=2.2)
add(7.25, rev * np.linspace(0, 1, len(rev)) ** 2, 0.0, 0.35)

# ==================================================================
# 8.60-26.60  BRANCH RUN : 9 x 2.0s, impact on every match-cut
# ==================================================================
beat = 0.5                                    # 120 BPM, 4 beats per branch
BASS = [110.00, 98.00, 87.31, 110.00, 130.81, 116.54, 98.00, 110.00, 123.47]
for b in range(9):
    t0 = 8.6 + b * 2.0
    add(t0, whoosh(0.55, 0.30, up=(b % 2 == 0)), (b % 2 * 2 - 1) * 0.55, 0.30)
    add(t0, kick(0.85), 0.0, 0.10)
    add(t0, subhit(0.42, dur=1.4, f0=64, f1=36), 0.0, 0.08)
    add(t0 + beat,     kick(0.40), 0.0, 0.08)
    add(t0 + beat * 2, kick(0.52), 0.0, 0.08)
    add(t0 + beat * 3, kick(0.40), 0.0, 0.08)
    for e8 in range(8):
        add(t0 + e8 * (beat / 2), blip(0.10, 5200, 0.028, dec=95),
            (rng.random() * 2 - 1) * 0.8, 0.10)
    add(t0, pad([BASS[b], BASS[b] * 2], 1.95, 0.082, atk=0.05, rel=0.55), 0.0, 0.10)
    add(t0 + 0.06, pluck(BASS[b] * 4, 0.8, 0.048), 0.35, 0.35)
add(8.6, pad([220.0, 329.63], 18.0, 0.028, atk=3.0, rel=2.5), 0.0, 0.16)

# ==================================================================
# 26.60-29.10  COUNTER RACE : accelerating, then two deliberate ticks
# ==================================================================
add(26.60, noiseband(1.85, 500, 5200, 0.078, curve=2.0), 0.0, 0.22)
add(26.60, pad([110.0, 164.81, 220.0], 1.9, 0.072, atk=0.9, rel=0.4), 0.0, 0.14)
tt, g2 = 26.62, 0.115
while tt < 28.38:
    add(tt, blip(0.09, 2400, 0.078, dec=110), (rng.random() * 2 - 1) * 0.5, 0.12)
    g2 *= 0.958
    tt += max(g2, 0.028)
add(28.40, blip(0.36, 1500, 0.160, dec=22), 0.0, 0.34)     # 9,998
add(28.75, blip(0.36, 1380, 0.160, dec=22), 0.0, 0.34)     # 9,999

# ==================================================================
# 29.10-29.62  SILENCE (non-negotiable) : micro heartbeat only
# ==================================================================
add(29.16, heartbeat(0.085), 0.0, 0.05)
add(29.40, heartbeat(0.070), 0.0, 0.05)

# ==================================================================
# 29.62  THE 10,000 HIT  ->  surge on to 10,271
# ==================================================================
pre = noiseband(0.34, 3000, 260, 0.17, curve=1.0)
add(29.28, pre * np.linspace(0, 1, len(pre)) ** 2, 0.0, 0.30)
add(29.62, subhit(1.10, dur=3.4, f0=88, f1=31), 0.0, 0.12)
add(29.62, kick(0.75), 0.0, 0.10)
add(29.62, shimmer(3.2, 0.32, 1320), 0.0, 0.55)
add(29.62, noiseband(0.48, 9000, 1200, 0.115, curve=0.7), 0.0, 0.40)
add(29.62, pad([110.0, 220.0, 329.63, 440.0], 3.6, 0.115, atk=0.02, rel=2.5), 0.0, 0.30)
st2 = 30.10
while st2 < 30.58:                                          # momentum ticks to 10,271
    add(st2, blip(0.07, 3100, 0.045, dec=130), (rng.random() * 2 - 1) * 0.6, 0.14)
    st2 += 0.042
add(30.64, pluck(659.25, 1.4, 0.055), 0.0, 0.40)

# ==================================================================
# 31.00-36.60  HERO VFX : swell, explode, reform, resolve
# ==================================================================
add(31.00, pad([146.83, 220.0, 293.66, 440.0], 3.0, 0.095, atk=1.0, rel=1.2), 0.0, 0.28)
add(32.70, whoosh(0.90, 0.27, up=True), -0.4, 0.40)
add(32.70, noiseband(1.25, 6000, 900, 0.088, curve=0.8), 0.0, 0.34)
add(33.90, whoosh(1.20, 0.21, up=False), 0.4, 0.42)
add(33.90, pad([130.81, 196.0, 261.63, 392.0], 2.6, 0.100, atk=1.2, rel=1.1), 0.0, 0.26)
add(35.60, shimmer(2.6, 0.21, 1050), 0.0, 0.45)
add(35.60, pad([130.81, 261.63, 392.0], 1.8, 0.105, atk=0.35, rel=1.0), 0.0, 0.26)

# ==================================================================
# 36.60-42.20  TREATMENT MONTAGE : warm emotional swell
# ==================================================================
for fr, t0, d in [([174.61, 261.63, 349.23], 36.60, 2.0),
                  ([130.81, 261.63, 329.63], 38.60, 2.0),
                  ([196.00, 293.66, 392.00], 40.60, 1.6)]:
    add(t0, pad(fr + [f * 2 for f in fr[:2]], d + 0.5, 0.112, atk=0.9, rel=0.9), 0.0, 0.30)
add(36.60, pad([87.31, 130.81], 5.7, 0.072, atk=1.6, rel=1.5), 0.0, 0.12)
for k in range(8):
    add(36.60 + k * 0.70, kick(0.20, dur=0.30), 0.0, 0.08)
    add(36.60 + k * 0.70, blip(0.12, 3400, 0.018, dec=80), (k % 2 * 2 - 1) * 0.5, 0.16)

# ==================================================================
# 42.20-45.00  END FRAME : resolve + branded sonic tail
# ==================================================================
add(42.20, pad([130.81, 196.00, 261.63, 392.00, 523.25], 2.8, 0.125, atk=0.5, rel=2.0), 0.0, 0.34)
add(42.20, subhit(0.55, dur=2.6, f0=70, f1=33), 0.0, 0.10)
add(42.20, shimmer(2.6, 0.14, 1046), 0.0, 0.45)
add(43.30, pluck(523.25, 1.5, 0.070), -0.25, 0.42)
add(43.54, pluck(659.25, 1.5, 0.055), 0.25, 0.42)
add(43.78, pluck(783.99, 1.6, 0.045), 0.0, 0.45)

# ==================================================================
# REVERB : FFT convolution with a synthetic hall impulse
# ==================================================================
ir_n = int(1.5 * SR)
ir = rng.normal(0, 1, ir_n) * np.exp(-np.linspace(0, 7.5, ir_n))
pre_n = int(0.012 * SR)
ir[:pre_n] *= np.linspace(0, 1, pre_n)
ir = lp1(ir, np.linspace(7000, 900, ir_n))
ir /= (np.abs(ir).sum() / 22)

def fftconv(sig, imp):
    n = 1 << int(np.ceil(np.log2(len(sig) + len(imp) - 1)))
    return np.fft.irfft(np.fft.rfft(sig, n) * np.fft.rfft(imp, n))[:len(sig)]

wet = fftconv(RVB, ir)
L += wet * 0.55
R += np.roll(wet, int(0.011 * SR)) * 0.55

# ==================================================================
# MASTER : bus compression, soft limit, 16-bit stereo
# ==================================================================
def compress(sig, thr=0.42, ratio=3.2, atk=0.004, rel=0.16):
    a = np.exp(-1 / (atk * SR)); r = np.exp(-1 / (rel * SR))
    ab = np.abs(sig); envd = np.empty(len(sig)); e = 0.0
    for i in range(len(sig)):
        c = ab[i]
        e = (a * e + (1 - a) * c) if c > e else (r * e + (1 - r) * c)
        envd[i] = e
    g = np.ones(len(sig)); m = envd > thr
    g[m] = (thr + (envd[m] - thr) / ratio) / envd[m]
    return sig * g

L = compress(L); R = compress(R)
peak = max(np.abs(L).max(), np.abs(R).max(), 1e-9)
L *= 0.89 / peak; R *= 0.89 / peak
L = np.tanh(L * 1.05) * 0.95; R = np.tanh(R * 1.05) * 0.95
f = int(0.35 * SR)
L[-f:] *= np.linspace(1, 0, f); R[-f:] *= np.linspace(1, 0, f)

st = np.empty(N * 2); st[0::2] = L; st[1::2] = R
pcm = (np.clip(st, -1, 1) * 32767).astype('<i2')
with wave.open('audio.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('audio.wav written  %.2fs  peak=%.3f' % (DUR, max(np.abs(L).max(), np.abs(R).max())))
