# test hand
import cv2             # OpenCV套件
import mediapipe as mp  # Mediapipe套件

mp_drawing = mp.solutions.drawing_utils          # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_hands = mp.solutions.hands                    # mediapipe 偵測手掌方法

cap = cv2.VideoCapture(0)  # 開啟鏡頭

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    static_image_mode=False,                # 影片流或靜態圖像，先檢測後追蹤
    # 手繪地標模型的複雜性: 0 或 1。地標精度以及推斷延遲通常與模型複雜性有關。默認 1。
    model_complexity=0,
    # max_num_hands=1,                      # 最大手數量
    min_detection_confidence=0.5,           # 檢測閥值
        min_tracking_confidence=0.5) as hands:  # 追蹤閥值

    if not cap.isOpened():  # 沒開鏡頭的話
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()  # 鏡頭讀出的布林值跟Frame
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = hands.process(img2)                 # 偵測手掌
        if results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks)  # 查看 landmarks
            # break
            for hand_landmarks in results.multi_hand_landmarks:
                # 將節點和骨架繪製到影像中
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        cv2.imshow('hands', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()
