---
title: "OpenIPC AI Object Detection Step by Step Tutorial"
channel: "MarioFPV"
video_id: "6jtqfoxwoxw"
url: "https://www.youtube.com/watch?v=6jtqfoxwoxw"
thumbnail: "https://i.ytimg.com/vi/6jtqfoxwoxw/hqdefault.jpg"
captured_at: "2026-07-29T11:04:49.516Z"
published_at: "2026-07-29"
source: youtube
has_transcript: true
transcript_lang: "en"
status: raw
sha256: c55a967f7dbbe9ffb9171ed0e44466eca9edabc78dc4ac94d0dda9818e40f048
---

# OpenIPC AI Object Detection Step by Step Tutorial

- **채널**: MarioFPV
- **URL**: [https://www.youtube.com/watch?v=6jtqfoxwoxw](https://www.youtube.com/watch?v=6jtqfoxwoxw)
- **수집일**: 2026-07-29
- **Video ID**: `6jtqfoxwoxw`

![썸네일](https://i.ytimg.com/vi/6jtqfoxwoxw/hqdefault.jpg)

## 자막 · 본문 정리

> 언어: en · 구간 51개

Hello everyone and welcome to another OpenIPC video tutorial.

In this video I am going to show you how to install the OpenIPC AI object detector.

First thing we need to do, is enable the OSD on the ground station. We go to telemetry.

We enable the GS rendering and on the display we select the GS rendering as well.

Now we need to restart in order to have the effect. So let's do that and we will continue.

And after the restart, we can see now that we have OSD. But if you see here, you can tell the difference. There is no transparent background. It's only the letters. So that's how you know that the OSD is running on the ground station.

Next thing we want to do is disable the adaptive link and we also need to restart. Okay, you can see that we have now fixed bit rate 8 Mbps.

Then we need to reduce the mlink to 2000 to have better latency.

And then we reduce the video bitrate to 4 Mbps.

We will increase the TX power to maximum and then reduce the MCS index to only 1.

Okay, these are the settings that we need to change. And now we need to run some commands. We need to execute 9 commands.

Of course, these files that we copy into specific locations, we have to download them and the link you will find it in the video description. So, you can download all the files and then extract the zip file and navigate to the Command Prompt Window to the location that you extracted all the necessary files. And then you split the screen

and you execute the first command. Copy paste. Enter. Yes. Enter.

And this command will kill the Majestic streamer, remove the Majestic streamer completely and create some folders that we will need. Next command.

Copy. Paste.

Copy. Here is the YOLO V8.

some more files. Here is the venc, the new encoder, and the settings.

And now with this command we give proper rights to the venc and also we convert DOS to Unix the JSON file the settings of venc.

And now some files that we need to send to the drone to the camera. And now we need to edit two files. Two files only. Two, three, four, five. /usr/bin/wifibroadcast.

Scroll down and here on start_telemetry we comment this line and we paste this command instead.

Escape, upper lower dot, x, Enter. And then second file is in init.d folder in /etc folder and it is the Majestic loader. But this time we don't have a majestic. So we have venc. We replace the Majestic to venc which is the new streamer and add this command.

So this command will need to load every time we reboot the camera.

It is the driver of the IPU. Escape, upper lower dot, x, Enter and we reboot.

And if we see on the camera, we should have Object Detections. You can see those green with very good latency. Yep, it's absolutely fine.

And that's it. Thanks for watching.

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._