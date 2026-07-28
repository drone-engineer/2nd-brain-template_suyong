---
title: Hunter-Killer 드론 자율 정찰-타격 체계 PRD v2.0
source_type: document
collected: 2026-07-27
sha256: 2e96b900fe3eb54eb61d9f6a6b5bc64ca35e4db7b9352a0bbdc31950e93d061d
original_file: /Users/drone_engineer/.hermes/cache/documents/doc_24fe00fc52db_Hunter_Killer_Drone_PRD_v2.pdf
---

# Hunter-Killer 드론 자율 정찰-타격 체계 PRD v2.0

> 원본: Hunter_Killer_Drone_PRD_v2.pdf (로컬 캐시). 아래는 추출 텍스트.

[PRD] Hunter-Killer 드론 자율 정찰-타격 체계 (통합 제작 가이드 v2.0)
Complete Hardware Wiring, Step-by-Step Setup, and Cursor AI Integration Document
버전: v2.0 (상세 가이드 포함)플랫폼: ROS 2 Humble / PX4 / MAVSDK통합 캐리어 보드: Holybro Pixhawk Jetson Baseboard
💡 쉬운 개요 (중학생도 이해하는 3문장 요약)
1. 정찰 드론(Hunter)이 하늘을 날며 카메라와 레이저(LRF)로 멀리 있는 보물(목표물)의 위치(위도, 경도)를 계산합니다.
2. 무선 인터넷(Wi-Fi Mesh)을 통해 땅에서 대기 중인 타격 드론(Killer)에게 "여기 위치로 날아가!"라고 위치를 알려줍니다.
3. 타격 드론이 정해진 위치로 날아간 뒤, 카메라로 목표물을 찾아 스스로 부딪혀 타격합니다. 
1. 필요 부품 및 공식 구매 링크 (Hardware List)
2. 배선 연결도 (Wiring Diagram)
통합 캐리어 보드(Pixhawk Jetson Baseboard)를 사용하면 대부분 내부 회로로 연결되므로 3가지 외부 포트만 꽂으면 끝납니다.
+---------------------------------------------------------------------------------+
|                       Pixhawk Jetson Baseboard (통합 메인 보드)                  |
|                                                                                 |
|  [ CAN1 포트 ] <========== CAN 케이블 ==========> [ H-RTK F9P GPS 모듈 ]       |
|                                                                                 |
|  [ ETH 포트 ]  <========== 이더넷 케이블 ========> [ Skydroid C13 카메라 ]      |
|                                                                                 |
|  [ POWER 포트] <========== 전원 메인선 ==========> [ 4S ~ 6S LiPo 배터리 ]       |
|                                                                                 |
|  * (내부 이더넷 스위치 회로): Pixhawk 6X <---> Jetson Orin Nano 간 자동으로 고속 통신 |
+---------------------------------------------------------------------------------+
🔌 쉽게 연결하는 3단계 순서
GPS 연결: RTK GPS의 선을 Baseboard의 CAN1 문구가 적힌 곳에 깍 소리가 나도록 꽂습니다.
카메라 연결: Skydroid C13 카메라의 LAN 랜선을 Baseboard의 ETH (Ethernet) 포트에 꽂습니다.
배터리 전원 연결: 배터리 전원 분배판(PDB) 출력을 Baseboard의 POWER 단자에 연결합니다. (Jetson과 FC가 동시에 켜집니다)
부품명 역할 및 기능 공식 링크
Pixhawk Jetson Baseboard Pixhawk 6X FC와 Jetson Orin을 하나로 묶어주는 통합 보드
(선 연결 필요 없음) Holybro 공식몰
Skydroid C13 Gimbal 2K 광학 카메라 + 640 열화상 + 1km 레이저 거리측정기(LRF)
통합 짐벌 Skydroid 공식몰
H-RTK F9P Helical 오차 1~2cm 수준의 센티미터급 초정밀 위성 항법(GPS) 모듈Holybro 공식몰
NVIDIA Jetson Orin Nano 드론 안에서 YOLO 인공지능 영상 분석 및 비전 유도를 수행하
는 미니 컴퓨터 NVIDIA 공식몰
Pixhawk 6X FC Module 드론 모터 4개를 제어하여 균형을 잡고 자동 비행을 총괄하는
주격 제어 컴퓨터 Holybro 공식몰
1. 
2. 
3. 
Hunter-Killer Drone System PRD & Guide v2.0 Page 1 of 3
3. 중학생도 따라하는 단계별 세팅 방법 (Step-by-Step Setup)
[1단계] 컴퓨터 프로그램 설치 및 비행 제어기(FC) 설정
컴퓨터에 드론 조종 프로그램인 QGroundControl(QGC)을 설치합니다.
USB 케이블로 컴퓨터와 Pixhawk 6X를 연결한 뒤 QGC를 켜면 PX4 Autopilot 펌웨어가 자동으로 업데이트됩니다.
드론을 평평한 바닥에 두고 센서 교정(캘리브레이션: Accelerometer, Gyro, Compass) 버튼을 눌러 화면에 나오는 대로 드론을 기울여
줍니다.
[2단계] Jetson AI 컴퓨터 환경 설정 (우분투)
Jetson Orin에 SDK Manager를 이용해 Ubuntu 22.04 LTS와 ROS 2 Humble을 설치합니다.
터미널(창)을 열고 다음 명령어로 PX4와 Jetson이 서로 대화할 수 있는 통신 다리(MicroXRCE-DDS Agent)를 켭니다: 
MicroXRCEAgent udp4 -p 8888
[3단계] 정찰 및 타격 코드 실행
Hunter 드론:ros2 run hunter_pkg target_localizer 명령을 실행하여 C13 카메라와 LRF 레이저가 찍은 목표의 위도/경도를
계산합니다.
Killer 드론:ros2 run killer_pkg terminal_homing 명령을 실행하여 수신된 위경도로 날아간 후, YOLO 인공지능이 화면 속 목
표물을 락온(Lock-on)하여 직충돌하도록 만듭니다.
4. 좌표 계산 및 비주얼 서보잉 수학 모델
Azimuth (방위각) = (Headingdrone + Yawgimbal) mod 360°
Dhoriz = DistanceLRF × cos(|Pitchgimbal|),    ΔLat = (Dhoriz × cos(Az)) / 6378137.0
Errorx = BBoxcenter_x - Cameracenter_x  ⇒  YawRate = -0.003 × Errorx
5. AI 에이전트 전용 `.cursorrules` 개발 규칙
# Cursor Rules for Hunter-Killer Project
- OS: Ubuntu 22.04 LTS | ROS 2 Humble | Python 3.10+
- Hardware: Pixhawk Jetson Baseboard (Pixhawk 6X + Jetson Orin Nano)
- Style: Class-based `rclpy.node.Node`, strict type hinting.
- Fail-Safe: Include try-except blocks in every node triggering RTL on failure.
• 
• 
• 
• 
• 
• 
• 
Hunter-Killer Drone System PRD & Guide v2.0 Page 2 of 3
6. 핵심 ROS 2 파이썬 구현 코드
6.1. Hunter Target Localizer (`target_localizer.py`)
#!/usr/bin/env python3
import math, rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
class TargetLocalizerNode(Node):
    def __init__(self):
        super().__init__('target_localizer_node')
        self.EARTH_RADIUS = 6378137.0
        self.pub = self.create_publisher(PointStamped, '/hunter/target_wgs84', 10)
    def calculate_wgs84(self, lat: float, lon: float, alt: float, dist: float, heading: float, pitch: float, 
yaw_rel: float):
        azimuth = math.radians((heading + yaw_rel) % 360.0)
        pitch_rad = math.radians(pitch)
        d_horiz = dist * math.cos(abs(pitch_rad))
        d_vert = dist * math.sin(pitch_rad)
        d_lat = (d_horiz * math.cos(azimuth)) / self.EARTH_RADIUS
        d_lon = (d_horiz * math.sin(azimuth)) / (self.EARTH_RADIUS * math.cos(math.radians(lat)))
        return lat + math.degrees(d_lat), lon + math.degrees(d_lon), alt + d_vert
def main(args=None):
    rclpy.init(args=args)
    node = TargetLocalizerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
6.2. Killer Terminal Homing (`terminal_homing.py`)
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
class TerminalHomingNode(Node):
    def __init__(self):
        super().__init__('terminal_homing_node')
        self.pub = self.create_publisher(TwistStamped, '/mavros/setpoint_velocity/cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.control_loop)
    def control_loop(self):
        # 화면 중앙 오차 기반 조향
        err_x, err_y = 10.0, 5.0  # 예시 바운딩 박스 오차
        cmd = TwistStamped()
        cmd.twist.linear.x = 12.0  # 12 m/s 초고속 직충돌
        cmd.twist.angular.z = -0.003 * err_x
        cmd.twist.linear.z = -0.003 * err_y
        self.pub.publish(cmd)
def main(args=None):
    rclpy.init(args=args)
    node = TerminalHomingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
Hunter-Killer Drone System PRD & Guide v2.0 Page 3 of 3

---
*raw evidence — immutable. Hunter-Killer 킬체인 하드웨어 참조.*
