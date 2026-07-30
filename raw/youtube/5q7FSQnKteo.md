---
title: "You Can't Hide — mmWave Radar + LoRa Tracks You From Kilometers Away (No WiFi)"
channel: "Electronic Clinic"
video_id: "5q7FSQnKteo"
url: "https://www.youtube.com/watch?v=5q7FSQnKteo"
thumbnail: "https://i.ytimg.com/vi/5q7FSQnKteo/hqdefault.jpg"
captured_at: "2026-07-29T12:06:29.476Z"
published_at: "2026-07-29"
source: youtube
meta_source: "oembed+html"
has_description: true
has_transcript: true
transcript_quality: "good"
transcript_lang: "en"
status: raw
sha256: 09ddc2293c97b48b58e3841c9af4177c8dadede5708d7f9d54ac343f945ee79b
---

# You Can't Hide — mmWave Radar + LoRa Tracks You From Kilometers Away (No WiFi)

- **채널**: Electronic Clinic
- **URL**: [https://www.youtube.com/watch?v=5q7FSQnKteo](https://www.youtube.com/watch?v=5q7FSQnKteo)
- **수집일**: 2026-07-29
- **Video ID**: `5q7FSQnKteo`
- **메타 소스**: oembed+html

![썸네일](https://i.ytimg.com/vi/5q7FSQnKteo/hqdefault.jpg)

## 영상 설명

Download Code & Resources:  "Patrons' early access"
https://www.patreon.com/posts/159735335

Read the Article:
Working on it...
https://www.electroniclinic.com/

Related Videos:
You Can't Hide Part 3:
https://youtu.be/sotLnw5mAoo

Track multiple People in 3D space (digital Twins) using RD-03D mmWave Radar
https://youtu.be/itbygPaOLMQ

RD-03D material penetration test, see through materials
https://youtu.be/RAzKsDblYyk

ESP32 + RD-03 mmWave Sensor, getting started video "multi-human tracking, speed, angle, and distance:
https://youtu.be/cSI9vedf870


mmWave Radar Vs Pets
https://youtu.be/jfPtyIvkfS8

ESP32 + RD-03D mmWave Radar | Real-Time Human Tracking with Distance, Angle & Speed | Wireless Radar
https://youtu.be/ZSrtbVVP9iA

C4001 mmWave Sensor with ESP32 and Arduino " with different tests" 12 meter
https://youtu.be/8ZWTwD66VcI

C4001 mmWave Radar Module 25 meter:
https://youtu.be/5mammWMv7zg

HMMD mmWave Sensor:
https://youtu.be/I508XQrjvDY

Staircase lights that follow you using RD-03E mmWave Sensor and ESP32
https://youtu.be/dfbk7WdBqvU

Rd-03E mmWave Sensor can measure distance and control loads using gestures
https://youtu.be/AeF3XvX2t1Q

Getting Started with C1001 mmWave Human Detection Sensor
https://youtu.be/TL6rvUwu5pM

SMD Soldering Soldering Tutorial:
https://youtu.be/CORLzDxDV4w

See-through walls with a Microwave Sensor, Human detection behind walls:
https://youtu.be/CyZRINdPuks

C1001 mmWave Sensor with ESP32, IoT project
https://youtu.be/Xe2iQmGaYis

Project Description:
*****
Long Range Human Tracking System Using RD-03D mmWave Radar and LoRa | ESP32 TTGO LoRa32 Project

In this video, I show you how to build a long-range human tracking and motion detection system using the RD-03D mmWave radar sensor and TTGO LoRa32 ESP32 boards.

Unlike WiFi or Bluetooth-based systems, this project uses LoRa long-range communication to transmit real-time human tracking data over several kilometers without internet access, routers, or cameras.

The RD-03D mmWave radar can detect and track up to 3 moving targets at the same time. It works in darkness, fog, and even through many non-metallic materials such as cardboard, plastic, glass, curtains, and wood.

 In this video you will learn:

RD-03D mmWave radar wiring with ESP32 TTGO LoRa32
LoRa communication between transmitter and receiver
Real-time human tracking using mmWave radar
OLED radar display interface
Python radar visualization software
Long-range wireless monitoring without WiFi
Portable battery-powered security monitoring system
Real-world testing and practical applications

This project is ideal for:

Remote security monitoring
Smart farms and agriculture projects
Warehouse monitoring
Construction site monitoring
Off-grid IoT applications
Human presence detection systems
Long-range ESP32 projects
LoRa sensor networks


💾 Download Source Code and Project Files:

Both Version 1 and Version 2 source codes, along with the Python radar application and project resources, are available on my Patreon page.

Your support helps me continue creating new electronics, Arduino, ESP32, LoRa, IoT, robotics, and engineering projects for the community.

A huge thank you to all Patreon supporters. Your support makes these projects possible.

*****



Product Links:
*****************
RD-03D mmWave Radar Module
https://amzn.to/4ea3YTE

TTGO LoRa32
https://amzn.to/3QcGkvV

DISCLAIMER: This video and description contain affiliate links, which means that if you click on one of the product links, I will receive a small commission. This helps support the channel and allows me to continue to make videos like this. Thank you for your support!
****************


Website: https://www.electroniclinic.com/
Instagram: https://www.instagram.com/electroniclinic/
Facebook: https://web.facebook.com/profile.php?id=100063900156958
Email: stu_engineering@yahoo.com

#esp32  #iot  #mmwave

## 자막 · 본문 정리

> 언어: en · 구간 206개

You can't hide because what I built today can track human movement in real time from kilometers away without Wi-Fi, without internet, and without a camera.

Sounds impossible? Well, let me prove it. This is the live radar interface, and that dot right there, that's my brother. As he moves, you can see the position updating in real time. And the craziest part, this data is coming from a sensor placed far away and transmitted over long distance. Now, imagine this,

you place this system in a completely remote location, no internet, no infrastructure, and still you can monitor everything in real time. But, here's where things get really interesting. Think about this for a second, most smart systems today depend on Wi-Fi or Bluetooth, but in real life,

that's a big limitation. Bluetooth usually works within 10 to 30 m, and Wi-Fi typically covers around 50 to 100 m. And the bigger problem, many important places don't even have internet access, places like farms, remote warehouses, construction sites, mountain areas. In these locations,

running cables is expensive and sometimes not even possible. So, instead of relying on internet, we use LoRa.

LoRa is built for long-range communication. It can send data over several kilometers using very low power, which means your system stays connected even where everything else fails. Now, that solves the communication part, but what about detection? This is the RD days 03D mmWave radar module. Unlike

traditional PIR sensors, it doesn't rely on heat or light. It uses radio waves to detect movement, and it's not like other mmWave radar modules, you can set its detection mode and track up to three moving targets at the same time. It works in complete darkness, in fog. It can even see through many materials,

cardboard, plastic, hardboard, glass, curtains, even wood, and many more. And it can detect even the smallest movements. It's a true human presence sensor. Standing still, sitting, or even crawling, you can't hide from it. Now, combine both technologies and you get something incredibly powerful, a system that can

detect movement in real time, track presence accurately, send data over kilometers, and work without any internet. On the receiver side, we will monitor important data like XY position, distance, angle, and speed on an OLED display, but that's not all. I have also created a real radar-style interface,

where you can visually see the exact position of the detected person. For those who don't want to use a computer, I have implemented the same radar interface directly on the OLED display, as well. For this project, you will need a pair of TTGO LoRa 32 modules and an RD-03D millimeter-wave radar sensor. I

recommend the TTGO LoRa 32 because it already comes with LoRa and a built-in OLED display, so you don't need to connect any extra components. And the RD-03D mmWave radar, you already know how powerful this sensor is. It can track up to three people in real time at the same time. If you want to learn more about

the TTGO Laura 32 or the RD03D radar in detail, I highly recommend checking out my previous videos. I will add the links in the description below. First, let's start with the transmitter side. Connect the 5-V and ground pins of the RD03D mm wave radar module to the 5-V and ground

pins on the TTGO Laura 32. Then, connect the TX pin of the radar module to GPIO 16 on the TTGO Laura 32. And that's it for the transmitter wiring. Now, on the receiver side, you don't need to connect anything. But, if you want to take it a step further, you can add a buzzer. This

way, whenever motion is detected, the buzzer will alert you instantly. Now, let's go ahead and take a look at the programming. This is the transmitter side program, and this is the receiver side program. First, you need to install the required libraries. So, let's do that.

Simply copy the library name.

Then, open the library manager.

Paste the name here.

And install it.

As you can see, I have already installed it. So, I'm not going to install it again.

Now, just repeat the same steps for the remaining libraries.

Once you have installed all the libraries, you can go ahead and upload the programs.

I'm not explaining the code here because I have already covered it in detail in my previous videos. If you want to learn how to use the RD03D mmWave radar without relying on libraries and how to access data directly from registers, I highly recommend watching my getting started video on this sensor. I've also

explained how to use the TTGO LoRa 32 along with its technical specifications.

You will find all the links in the description below.

Now, for the practical implementation, let's assume the transmitter is going to be installed in a location where power is not available. So, in that case, I'm going to use a 4S lithium ion battery pack, which I actually built a few years ago for my racing drone. Along with that, I will use my custom-designed 5-V

3-A power supply. It can accept input voltages up to 28 V and provides a stable 5-V output. So, it supports a wide input range from 9 V to 28 V. This means you can even power the system directly using a solar panel if you want. But, in my case, I prefer using this 4S lithium ion battery pack because

it makes the entire system portable. So, now it becomes a true on-the-go security system. I can place it anywhere, power it up, and start monitoring instantly.

For this video, I placed the transmitter outside the room, and we will monitor this area. Now, let's power up the receiver side using a standard phone adapter. As soon as I powered it on, the data started coming in. X and Y position, distance, angle, and speed all updating in real

time. The RD03D mmWave radar and the LoRa are working exactly as expected. We can see all the data on the OLED display. X, Y, distance, angle, speed.

But, there's one problem. It takes time to process all this in your head and figure out the actual position. So, to solve that, I designed a radar-style interface. Now, there is no guessing.

You can directly see the exact location of a person in real time. At first, monitoring everything on a computer felt amazing. It looked cool. It felt powerful. And honestly, I really liked it. Seeing all the data live, building that radar interface. It was exciting.

But, then I started thinking, what if you are not sitting at your desk? What if you are out in the real world? Let's say you are in a remote area, maybe a forest or on some kind of field mission where you need to monitor a specific zone and stay alert at all times. In that kind of situation, carrying a

laptop, setting it up, keeping it powered is just not practical. So, I decided to take it a step further. I built version two. Now, you can still monitor everything on your computer if you want that full interface. But, at the same time, you can also see the same radar-style view directly on the OLED

display. No laptop needed, no setup required. And the best part, now the whole system becomes completely portable. You can carry it in your pocket, take it anywhere, and start monitoring instantly. You can download both versions of the code, version one and version two, along with the computer

application from my Patreon page. So, that's all for now. Support me on Patreon for more videos. I hope you like today's episode. Like and share this video with your friends. See you in next episode and thanks for watching.

## 학습 힌트 (자동)

_태그가 없습니다. 설명·자막에서 키워드를 추출하세요._

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._