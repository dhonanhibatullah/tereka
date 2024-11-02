import cv2
import os

video_path = "jurang_short.mp4"
cap = cv2.VideoCapture(video_path)

output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_path = os.path.join(output_dir, f"frame_{frame_count:03d}.jpg")
    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames and saved in {output_dir}.")