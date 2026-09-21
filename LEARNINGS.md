# Learnings

Notes to myself, one section per step. Written before I move on.

## Step 1: see the heartbeat

### How a video is stored

A video is just a lot of still pictures shown one after another. Each picture is a **frame**.

**fps** = frames per second. Ours is about 29.3, so we get a new picture every ~0.034 s.

One frame is an array of numbers: `height x width x 3`. Ours is `480 x 640 x 3`. Each pixel has 3 numbers (red, green, blue), each from 0 to 255. So the video is a 4D block: `frames x 480 x 640 x 3`.

Careful: OpenCV gives the channels as **BGR**, not RGB. Easy to mix up. So "green" is index 1 either way, but red and blue swap.

Our video is uncompressed (1.4 GB for 53 s). That's good for us. Compression throws away tiny color changes, and tiny color changes are the whole thing here.

### What PPG is

PPG = photoplethysmography. Big word, simple idea: shine light on skin, measure how much comes back. A finger pulse oximeter does this with its own LED.

Every heartbeat pushes a wave of blood into the small vessels under your skin. More blood under the skin = more light absorbed = skin looks a tiny bit darker. Blood drains away = a tiny bit brighter. That goes up and down once per beat.

rPPG is the same thing but "remote": the light is just the room light and the sensor is the webcam. The change is very small (less than 1% of the pixel value), so you can't see it with your eyes. But averaging thousands of pixels makes it show up.

### Why green

Blood (hemoglobin) absorbs green light strongly. Red light mostly passes through and goes deeper, so the blood changes it less. Blue barely gets under the skin, so it mostly bounces off the surface.

Green is also good on the camera side: most camera sensors have 2 green pixels for every 1 red and 1 blue, so green is the least noisy channel.

So: green has the strongest pulse and the cleanest signal. It's not perfect though. Light changes and head movement also change green, which is why Step 3 uses all 3 channels.

### Ground truth

A separate finger pulse oximeter was worn while the video was recorded. Its readings are the "answer key". We never feed it to our algorithm. We only use it at the end to grade how close we got.

### What we build in Step 1

1. Load the video and the ground truth.
2. Find the face in every frame (MediaPipe FaceLandmarker gives 478 points on the face).
3. Pick skin regions: forehead + both cheeks (no eyes, mouth, hair, so nothing that moves a lot).
4. Average R, G, B over those pixels -> 3 numbers per frame -> 3 signals over time.
5. Plot green next to the ground truth pulse. If we see the same wave, it worked.
