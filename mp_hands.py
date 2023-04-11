mp_hands.Hands(
    static_image_mode=False,                # 影片流或靜態圖像，先檢測後追蹤
    # 手繪地標模型的複雜性: 0 或 1。地標精度以及推斷延遲通常與模型複雜性有關。默認 1。
    model_complexity=0,
    # max_num_hands=1,                      # 最大手數量
    min_detection_confidence=0.5,           # 檢測閥值
        min_tracking_confidence=0.5)