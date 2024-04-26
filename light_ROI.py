import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('images/lights.png')

print(image.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 임계값 설정
threshold_value = 252

# 임계값 이상인 픽셀을 흰색으로, 이하인 픽셀을 검은색으로 변환
_, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# 연결된 컴포넌트 찾기
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

# 각 컴포넌트의 면적 계산
areas = stats[:, cv2.CC_STAT_AREA]

# 면적을 기준으로 컴포넌트를 내림차순으로 정렬
sorted_indices = np.argsort(-areas)

# 상위 5개의 컴포넌트에 대한 ROI 그리기
for i in range(5):
    idx = sorted_indices[i]
    left = stats[idx, cv2.CC_STAT_LEFT]
    top = stats[idx, cv2.CC_STAT_TOP]
    width = stats[idx, cv2.CC_STAT_WIDTH]
    height = stats[idx, cv2.CC_STAT_HEIGHT]
    
    cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)

# 결과를 화면에 표시
cv2.imshow('Top 5 Light Sources with ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
