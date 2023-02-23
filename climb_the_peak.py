from collections import deque

daily_portion = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
conquered_peaks = []
peaks =[
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
            ]

while True:
    if not peaks or not daily_portion or not stamina:
        break
    current_power = daily_portion.pop() + stamina.popleft()
    if current_power >= peaks[0][1]:
        conquered_peaks.append(peaks[0][0])
        peaks.pop(0)


if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peaks:
        print("Conquered peaks:")
        print('\n'.join(conquered_peaks))


