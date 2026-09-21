# webcam-heart-rate

Get your heart rate (BPM) from a webcam video of your face. No sensors, no touching anything.

Each heartbeat changes the color of your skin a tiny bit. You can't see it, but a camera can. This trick is called rPPG (remote photoplethysmography).

I'm building the whole pipeline myself, step by step, and writing down what I learn in [LEARNINGS.md](LEARNINGS.md).

**This is a research project, not a medical device.**

## Status

- [ ] Step 1: see the heartbeat in the green channel
- [ ] Step 2: signal processing baseline (bandpass + FFT)
- [ ] Step 3: POS and CHROM
- [ ] Step 4: small 3D CNN in PyTorch
- [ ] Step 5: real-world tests (light, motion, skin tones, video calls)
- [ ] Step 6: live demo
