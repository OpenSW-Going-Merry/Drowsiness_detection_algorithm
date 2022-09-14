# Drowsiness detection algorithm <br>
개요: 졸음이란, 자연적인 생리 현상으로써 휴식을 필요로 할 때 나타나는 현상이다. <br> 
그러나 때론 졸음을 이기고 하던 일이나 행동을 지속해야할 때가 있다. <br>
따라서 카메라와 CO2센서를 이용해 사용자의 졸음을 감지하여 여러 상황에 맞춰 사용할 수 있다. <br>

---

## 졸음 감지 알고리즘
1. 멤버
2. 플로우 차트
3. 각 설명

## 1. 멤버
|이름|역할 및 기여|
|:---:|:---|
|이성찬(리더)|모델 생성 및 프로젝트 관리|
|김용희|모델 생성|
|차영민|모델 최적화|
|최준희|CO2|
|임홍균|데이터셋 확장|
|이창원|데이터셋 조사 및 생성|

## 2. 플로우 차트
<img src="https://github.com/OpenSW-Going-Merry/Drowsiness_detection_algorithm/blob/main/img/KakaoTalk_20220913_215504789.png?raw=true" alt="dda"></img><br/>
<img src="https://github.com/OpenSW-Going-Merry/Drowsiness_detection_algorithm/blob/main/img/flow.png?raw=true" alt="dda"></img><br/>

## 3. 디테일
+ 훈련 데이터 셋의 크기가 너무 작아 전이학습을 사용
    * 전이학습: 사전 학습된 모델을 다른 작업에 이용하는 것
+ 얼굴 특징 분석을 위한 모델 생성을 위해 자세, 명암, 인종이 다양한 데이터셋을 사용
    * 이로 인해 에러 발생
    * 1. 다른 부위를 눈으로 예측
    * 2. 복수의 사람이 있을 경우 완전히 다른 곳을 예측
+ 위의 문제를 해결하기 위해 데이터 증강 사용
    * 1. RandomCrop: 원하는 크기만큼 원래 이미지에서 랜덤하게 추출
    * 2. RandomBrightnessContrast: 밝기 및 대비 랜덤하게 변화
    * 3.	Cutout: 랜덤하게 구멍냄
    * 4.	HorizontalFlip: 수평으로 회전 <br>
<img src="https://github.com/OpenSW-Going-Merry/Drowsiness_detection_algorithm/blob/main/img/KakaoTalk_20220914_113451086.png" alt="dda"></img><br>
+ 이산화탄소 측정
    * 센서: MH-Z14A, WINSEN
    * Datasheet: https://www.winsen-sensor.com/d/files/mh-z14a-co2-manual-v1_4.pdf
    * 졸음을 일으키는 이산화탄소의 농도가 있으므로 해당 농도를 기준으로 사용
<img src="https://github.com/OpenSW-Going-Merry/Drowsiness_detection_algorithm/blob/main/img/image.png" alt="dda"></img><br>
    
    
  
    
    
    
    
    
    

