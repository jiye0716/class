import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,                # 影片流或靜態圖像，先檢測後追蹤
                       # 手繪地標模型的複雜性: 0 或 1。地標精度以及推斷延遲通常與模型複雜性有關。默認 1。
                       model_complexity=0,
                       # max_num_hands=1,                      # 最大手數量
                       min_detection_confidence=0.5,           # 檢測閥值
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
hand_LmsStyle = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=5)
hand_ConStyle = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=10)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    # print(results)
    if results.multi_hand_landmarks:
        # print(results.multi_hand_landmarks)
        # break
        for hand_landmarks in results.multi_hand_landmarks:
            # mp_drawing.draw_landmarks(img, hand_landmarks)
            mp_drawing.draw_landmarks(
                img, hand_landmarks, mp_hands.HAND_CONNECTIONS, hand_LmsStyle, hand_ConStyle)

    cv2.imshow('hand', img)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
