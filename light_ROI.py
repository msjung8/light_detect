import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('images/lights.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print(image.shape)

# 임계값 설정
threshold_value = 252

# 임계값 이상 = white, 이하 = black -> cv2.THRESH_BINARY 사용
_, thr_binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# 임계값 처리된 이미지 show
cv2.imshow("threshold binary image", thr_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 연결된 컴포넌트 찾기 
# num_labels : 객체 수 + 1 (배경)
# labels : 객체 번호
# stats : N행 5열, N은 객체수 + 1 (num_labels), 각 정보 5열에는 x, y, width, height, area (면적, 픽셀 수) 순으로 담겨있음.
# centroids : N행 2열, x,y 각 객체별 무게중심좌표 - ROI 그릴 때 사용
# connectivity=8 : 8방향 이웃 연결관계 (대각선 포함) 
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thr_binary, connectivity=8)

# 각 컴포넌트의 면적 계산 - ROI 면적 TOP 5개만 추려낼 것이므로 모든 객체의 면적 데이터를 저장함
areas = stats[:, cv2.CC_STAT_AREA]

#print(areas) # 면적을 찍을 경우 나오는 결과
#[189172      2      1      2      2      3      8     10      2      1
#      2      1      1     26     16      1      3      1      1      1
#      1      4      5      7      3      4      5      3   1563      1
#      1      1      1      1     16      2      2      3      2      1
#    114      4      3      3     11      3      1     33     37      2
#      1      5   1570      2      1      3      1      1      1      2
#      1      1      2      5      2      1      2      1      1      1
#     17      1    526      1     15     11      1      6      1      3
#      1]

# TOP5 정렬을 위해 면적을 기준으로 컴포넌트를 내림차순으로 정렬
sorted_indices = np.argsort(areas)[::-1]


#print(sorted_indices) # 상위 면적 Top5의 객체별 index를 구함. -areas를 해도 되고 areas[::-1]로 해도됨. (내림차순 정렬 시)
#[ 0 52 28 72 40 48 47 13 70 34 14 74 44 75  7  6 23 77 22 63 51 26 41 21
# 25 79 27 42 43 16 24  5 45 37 55 64 36 66 49 62 59 10 35  8  3  1 53  4
# 38 69 67 15  2 68 73 12 11  9 18 71 76 17 46 19 20 50 54 56 39 57 58 33
# 32 31 30 29 78 60 61 65 80]
# 상위 5개의 컴포넌트에 대한 ROI 그리기

for i in range(1,6): #5개 상위 객체에 대하여 idx, left, top, width, height 정보를 구함 idx로는 객체번호, 해당 번호로 stats행에 넣어 열의 좌표구함
    idx = sorted_indices[i]
    left = stats[idx, cv2.CC_STAT_LEFT]
    top = stats[idx, cv2.CC_STAT_TOP]
    width = stats[idx, cv2.CC_STAT_WIDTH]
    height = stats[idx, cv2.CC_STAT_HEIGHT]
    
    #각 stat에서 얻은 정보를 통해 image에 cv2.rectangle로 사각형을 그려넣음 -> 5개.
    cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)

# 결과를 화면에 표시
cv2.imshow('Top 5 LIGHT AREA with ROI Drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
