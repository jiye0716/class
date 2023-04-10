import cv2
import mediapipe as mp
import math

# 根據兩點的座標，計算角度


def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(math.acos(
            (v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_
# 根據傳入的 21 個節點座標，得到該手指的角度


def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        # [第幾個landmark][0=x,1=y]
        ((int(hand_[0][0]) - int(hand_[2][0])),
         (int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])),
         (int(hand_[3][1]) - int(hand_[4][1])))
    )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),
         (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])),
         (int(hand_[7][1]) - int(hand_[8][1])))
    )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[10][0])),
         (int(hand_[0][1]) - int(hand_[10][1]))),
        ((int(hand_[11][0]) - int(hand_[12][0])),
         (int(hand_[11][1]) - int(hand_[12][1])))
    )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[14][0])),
         (int(hand_[0][1]) - int(hand_[14][1]))),
        ((int(hand_[15][0]) - int(hand_[16][0])),
         (int(hand_[15][1]) - int(hand_[16][1])))
    )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[18][0])),
         (int(hand_[0][1]) - int(hand_[18][1]))),
        ((int(hand_[19][0]) - int(hand_[20][0])),
         (int(hand_[19][1]) - int(hand_[20][1])))
    )
    angle_list.append(angle_)
    return angle_list
# 根據手指角度的串列內容，返回對應的手勢名稱


def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return '0'
    elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return '1'
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return '2'
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 > 50:
        return '3'
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return '4'
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return '5'
    elif f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return '6'
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return '7'
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return '8'
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 >= 50:
        return '9'
    else:
        return ''


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,                # 影片流或靜態圖像，先檢測後追蹤
                       # 手繪地標模型的複雜性: 0 或 1。地標精度以及推斷延遲通常與模型複雜性有關。默認 1。
                       model_complexity=0,
                       # max_num_hands=1,                      # 最大手數量
                       min_detection_confidence=0.5,           # 最低檢測置信度
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
    h = img_rgb.shape[0]  # **
    w = img_rgb.shape[1]  # **
    if results.multi_hand_landmarks:
        # print(results.multi_hand_landmarks)
        # break
        for hand_landmarks in results.multi_hand_landmarks:
            # mp_drawing.draw_landmarks(img, hand_landmarks)
            mp_drawing.draw_landmarks(
                img, hand_landmarks, mp_hands.HAND_CONNECTIONS, hand_LmsStyle, hand_ConStyle)
            finger_points = []  # **
            for i in hand_landmarks.landmark:
                # print(i.x, i.y) #跟畫面的比例 #**
                x = i.x*w
                y = i.y*h
                finger_points.append((x, y))  # landmarks在畫面上的座標
            if finger_points:
                finger_angle = hand_angle(finger_points)  # 計算手指角度，回傳長度為 5 的串列
                # print(finger_angle)                     # 印出角度 ( 有需要就開啟註解 )
                text = hand_pos(finger_angle)            # 取得手勢所回傳的內容
                cv2.putText(img, text, (30, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)  # 印出文字

    cv2.imshow('hand', img)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
