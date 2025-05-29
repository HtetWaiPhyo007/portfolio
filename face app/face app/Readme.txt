===============================
  Face Recognition with DeepFace
===============================

This project uses Python, OpenCV, and DeepFace to recognize faces in real-time using a webcam.
It compares the detected face with pre-stored known face embeddings (e.g., htet.jpg).

このプロジェクトは、Python・OpenCV・DeepFaceを使ってリアルタイムで顔認識を行います。
検出された顔を、保存されている既知の顔画像（例：htet.jpg）と比較します。

------------
📦 Requirements / 必要な環境
------------
- Python 3.8 ～ 3.11（推奨）
- 必要なライブラリ：
    pip install opencv-python deepface numpy

---------------
📁 Folder Structure / フォルダ構成
---------------
face app/
├── app.py              ← メインプログラム
└── known_faces/        ← 顔画像を保存するフォルダ
    └── htet.jpg        ← 既知の顔画像ファイル

----------------------------
🚀 How to Run / 実行方法
----------------------------
1. `known_faces` フォルダ内に顔画像ファイル（例：htet.jpg）を入れてください。
2. ファイル名は英語にしてください（例：htet.jpg、"てっと.jpg" はNG）。
3. ターミナルまたはVSCodeで以下を実行：
   > python app.py

4. カメラウィンドウが開きます。
   - 一致すれば名前が表示されます（例：Htet Wai Phyo）
   - 一致しなければ「Unknown」と表示されます。

----------------------------
➕ Add More Faces / 顔を追加する方法
----------------------------
1. `known_faces/` フォルダに画像を追加してください。
   例：
     - sai.jpg
     - nanda.jpg

2. 複数の画像に対応するために、`app.py` のコードを修正する必要があります。
   → ChatGPTに「複数人の顔を認識したい」と伝えるとコードを書いてくれます！

----------------------
⚠️ Troubleshooting / トラブル対策
----------------------
- "too many values to unpack" → DeepFaceバージョンにより起こる。最新版またはv0.0.79を使ってください。
- 顔が検出されない場合：
    - 鮮明な正面顔画像を使用してください。
    - enforce_detection=False を使うと強制認識されますが、精度が下がります。
- 認識されない場合は、threshold値を0.6 → 0.7くらいに調整してください。


