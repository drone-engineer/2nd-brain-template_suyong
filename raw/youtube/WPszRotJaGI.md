---
title: "Is This DIY EMP Device Actually Dangerous?"
channel: "Skill Make"
video_id: "WPszRotJaGI"
url: "https://www.youtube.com/watch?v=WPszRotJaGI"
thumbnail: "https://i.ytimg.com/vi/WPszRotJaGI/hqdefault.jpg"
captured_at: "2026-07-29T11:46:45.353Z"
published_at: "2026-07-29"
source: youtube
meta_source: "oembed+html"
has_description: true
has_transcript: true
transcript_quality: "good"
transcript_lang: "en"
status: raw
sha256: c4a82685085dfb5bd91f86db22ae594d7a71c781ad47860d0127db736a7f0eeb
---

# Is This DIY EMP Device Actually Dangerous?

- **채널**: Skill Make
- **URL**: [https://www.youtube.com/watch?v=WPszRotJaGI](https://www.youtube.com/watch?v=WPszRotJaGI)
- **수집일**: 2026-07-29
- **Video ID**: `WPszRotJaGI`
- **메타 소스**: oembed+html

![썸네일](https://i.ytimg.com/vi/WPszRotJaGI/hqdefault.jpg)

## 영상 설명

🌏 Get exclusive NordVPN deal here ➵  https://NordVPN.com/skillmake It’s risk free with Nord’s 30 day money-back guarantee!✌
In this video, I built a real, powerful DIY EMP device from scratch! An Electromagnetic Pulse (EMP) can fry and destroy electronic components instantly, and today we are going to test this homemade EMP generator to see if it actually works on old electronics.

If you’ve ever wondered how to make an EMP device at home or how an EMP generator works, this step-by-step video covers the high-voltage circuit, the coils, and the science behind electromagnetic fields. We will be testing this DIY EMP on various devices to see the instant destructive power of a real magnetic pulse.

00:00 - How an EMP Device is Made
00:54 - High-Voltage Transformer for EMP
04:20 - Marx Generator & How it Multiplies Voltage
06:28 - Building a Marx Generator for EMP Pulse Coils
08:28 - Choosing the Best Coil for EMP Pulse Generation
09:37 - Testing the EMP Pulse on Electronic Devices

#EMP #DIY #Electronics #skillmake #Science

## 자막 · 본문 정리

> 언어: en · 구간 91개

Imagine instead of using wires to transfer electricity wirelessly on one side I give a 5 volts to a coil creating a field around it and the second coil picks up that field and turns it back to into power. You can see this exact system in wireless phone charger. What what if instead of 5 volts I feed thousands or millions of volts

into the coil and instead of a second coil I place a phone a calculator a camera it could be any other electronic device as you know all these device are made of circuits and wires they can pick up that field with this much voltage we can fry all of them engineers call it an EMP or

electromagnetic pulse and in this video I'm going to build one first of all This EMP device needs a really high voltage generator. So I decided to make a custom transformer. I found this FR core and took some measurements. Then I designed a layered cylinder around it. I printed it on my

Formlabs printer using clear resin. I really love this printer. It's super precise. And finally, I got this clear print. For the secondary coil, I used a 0.1 mm coated wire. To keep track of the turns, I used this tally counter, but instead of pressing the physical button, I took it out

and soldered the red switch in its place. Now I can count the turns just by spinning a magnet.

For the first section, I was really careful and won 800 turns because if the wire breaks, I have to start all over again. After finishing the first 800 turns, I moved the wire to the next section and did another 800 turns and then again and again. Anyway, after a lot of neck pain and eating bunch of candy,

I repeat this process 15 times. Done. totally 12,000 turns, but I haven't insulated yet.

To insulate the transformer, I use epoxy resin, but I didn't go with the usual 1:22 ratio. I actually used less hardener. It takes longer to cure this way, but it completely coats all the wires. I also put it in a vacuum chamber to remove all the tiny air bubbles.

And for the primary coil, I want nine turns using thick wire. And that's it. Now I have 12,000 secondary turns and nine primary turns. That means whatever voltage I put into the transformer, I'll get 1,333 times at the output. For the flyback circuit, I use a super simple setup with just the MOSFET and the PWM module. Basically, the measure generates the signal at

whatever frequency I set and sends it to the MOSFET gate to boost it. I powered the circuit with a 9V power supply and hook it the output to the transformer. I tuned the frequency to 12.5 KHz with a 70% duty cycle. You have to find these exact numbers track and error and they are

unique to every transformer, but generally it sits somewhere between 10 and 25 kHz.

I love electronics again. Again.

Yes. Me and electricity. We are basically married couple now. For all the circuits, I designed and 3D printed the case. I swapped the old MOSFET heat sink for bigger one. To control the transformer, I added a switch right between the MOSFET gate and the PWM signal. Also, for the power source, I used an 8V battery pack with a charging port.

So far, I've built a high voltage generator, but honestly, that's not enough to create a real EMP pulse. I actually need to something that can store all this energy and in a split second boom release it all. So I'm going to need a capacitor and marks generator circuit. But what is exactly marks generator? Imagine I have a big power source and

six batteries. First I charge them in a parallel and after the full charge I disconnect them. Now each batteries is charged up to the exact voltage of the power source. For the output, I connect them together in series. Instead, now my output is exactly six times the original voltage. Since we

are getting closer to actually generating the EM pulse, I covered my camera in aluminum foil like a mini farat cage to protect it from the pulse. And speaking of protection, as you guys know, for this project, I downloaded a massive amount of data, 3D file, and code every single day. The reality

is any of those could easily be interfected with malware. Luckily, the sponsor of today's video, NordVPN, completely solve this security issue for me. A lot of people think a VPN just for changing your IP address, but it's way more than that. All those files I download could hide malware that

might wipe up my project or compromise my privacy. But NorVPN thread protection feature acts as an invisible shield. It scans and filters the files before they even reach my system. On top of that, when I'm researching new builds, I constantly run into resources that are geoblocked or

restricted in my region. With NordVPN, I have access to thousands of servers worldwide.

You can grab the huge discount on a 2-year plan plus four additional bonus months using my exclusive link getat nordvpn.com/skillmake or just by clicking the link down in the description.

And if you're not totally convinced yet, don't worry because they offer a 30-day money back guarantee. All right, let's back to the project. Now, instead of batteries, I'm using these 15 kW nanopharad capacitors. Also, to get even more power, I soldered them together in series.

But instead of just one, yeah, I need eight of them. I line them up to next to each other and use these resistors to build the parallel path I want. If your electronics are solid, let me know in the comments why I put these resistors between the capacitors.

The parallel path is ready. But you can't have a parallel and the series connection at the exact same time. But Mark uses a really clever trick. Instead of using solid wires between the capacitors for the series path, he uses the spark gaps. So now the transformer charges the capacitor in parallel and the moment they are fully charged, they unleash their energy as a

spark. And that's exactly what creates our series pass between these two pins. Let's test it. Okay.

Yeah, I think I know why it's not working. A mark circuit actually work with DC voltage while my transformer outputs AC. Luckily, solving this is the easiest part of the whole project. I just used these high voltage diodes to build a rectifier and added this straight into the circuit.

Can you see these sparks? They are exactly what creates that series path I was talking about.

To finish it up, I packet the entire circuit inside the case, leaving only the two high voltage outputs sticking out. Now, the only thing is left winding the coil to actually generate the pulse. But there are a few crucial details here. First off, the shape of the coil itself. Usually,

everyone wind these in a standard cylindrical car shape, but I found something way better, the pancake coil. I actually analyzed the magnetic field for both. With a cylindrical coil, a large part of wave just stays trapped inside the cylinder. But with a pancake coil, the pause is

literally shot straight forward. The second point is I only want the pass to travel in one direction along the coil. You talk it naturally generates in a both directions. Well, I actually found the solution in this wireless charging module. Specifically, this shield behind the coil. Look

at this. Right now, the pass is focused on one side to charge the phone. But if I flip it over, the pass actually can't pass through the metal. And that's exactly the point. Metals block the false. So, keeping all these points in my mind, I finally added these piece to it. A pancake coil

with a metal shield right behind it. And for the first test, I tried it out on my digital caliper.

Well, I've always hate math, so I think it's time to destroy this one, too.

Beautiful.

Don't worry.

Next up is this, my lovely Apple Watch. It's worked perfectly and it's in a great condition, but it's a fake.

Next up is my old monitor. It works perfectly, but just for you guys.

See you in the next video. Bye-bye.

## 학습 힌트 (자동)

_태그가 없습니다. 설명·자막에서 키워드를 추출하세요._

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._