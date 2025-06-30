# 📹 Player Re-Identification using YOLOv11 and DeepSORT (Single Feed)

This repository contains a complete implementation for **Player Re-Identification in a Single Feed** using a fine-tuned YOLOv11 object detection model and **Deep SORT** multi-object tracking.

The system detects players in a video, assigns unique IDs, and maintains these IDs consistently even when players temporarily leave and re-enter the frame.

---

## 🎯 Task Objective

Given a 15-second sports video (`15sec_input_720p.mp4`), the goal is to:

- Detect all players in each frame using a provided YOLOv11 model.
- Assign a unique ID to each detected player during the initial seconds.
- Track and **retain those IDs across the video**, even when players leave and return to the scene.
- Output:
  - An annotated video with player IDs displayed.
  - A CSV log of tracking details frame-by-frame.

---

## 🛠️ Technologies Used

- **Python 3.11**
- **OpenCV**
- **PyTorch**
- **Ultralytics YOLOv11** (custom trained model)
- **Deep SORT Realtime** (`deep_sort_realtime` library)

---

## 📦 Project Structure

```

player_reid_clean/
├── assets/
│ └── 15sec_input_720p.mp4 # Input video for inference
├── checkpoints/
│ └── best.pt # Custom trained YOLOv11 weights for player detection
├── output/
│ ├── output_tracked.mp4 # Output video with tracked player IDs
│ └── tracking_log.csv # Log of player positions and IDs per frame
├── src/
│ ├── detector.py # YOLOv11 detection module
│ ├── tracker_handler.py # Deep SORT tracker initialization module
│ └── utils.py # Utility functions (video I/O setup)
├── main_pipeline.py # Main pipeline script to run detection, tracking, and logging
├── requirements.txt # Python dependency list
└── README.md # Project documentation

```


---

## ⚙️ How It Works

1. **Detection (YOLOv11)**  
   A custom-trained YOLOv11 model (`best.pt`) detects 'players' in each video frame.  
   Only detections above a confidence threshold (0.5) are considered.

2. **Filtering**  
   Detected boxes are filtered based on:
   - Minimum and maximum area.
   - Valid aspect ratio range.
   - Boxes are clipped within frame boundaries.

3. **Tracking (Deep SORT)**  
   Deep SORT tracks the detected players, assigning consistent IDs over time using:
   - Kalman filtering.
   - Visual and positional similarity.

4. **Output Generation**
   - **Annotated Video** (`output_tracked.mp4`): Players are labeled with their IDs.
   - **Tracking Log** (`tracking_log.csv`): Frame number, player ID, and bounding box coordinates for each detection.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone (https://github.com/Sanjaykumar7777/Player-Tracking-and-Re-Identification-in-Sports-Video.git)

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
3. Run the full pipeline:
   ```bash
   python main_pipeline.py
4. Outputs will be saved to:
    output/output_tracked.mp4
    output/tracking_log.csv

---

## Notes

-This implementation assumes the YOLOv11 model is fine-tuned only for detecting players.

-Deep SORT parameters (like max_age=30) can be adjusted in src/tracker_handler.py for different sports or scenarios.

-Future improvements could include ball tracking, action classification, and multi-camera player re-identification.

