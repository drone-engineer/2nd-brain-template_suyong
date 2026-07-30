---
title: "I Stole This from the Military"
channel: "Data Slayer"
video_id: "b7IMBHMjNv8"
url: "https://www.youtube.com/watch?v=b7IMBHMjNv8"
thumbnail: "https://i.ytimg.com/vi/b7IMBHMjNv8/hqdefault.jpg"
captured_at: "2026-07-29T12:14:35.992Z"
published_at: "2026-07-29"
source: youtube
meta_source: "oembed+html"
has_description: true
has_transcript: true
transcript_quality: "good"
transcript_lang: "en"
status: raw
sha256: 3df3fafabc509b0bd3a6812c57fb420ab2a41471685b213d3139fdc5504d513f
---

# I Stole This from the Military

- **채널**: Data Slayer
- **URL**: [https://www.youtube.com/watch?v=b7IMBHMjNv8](https://www.youtube.com/watch?v=b7IMBHMjNv8)
- **수집일**: 2026-07-29
- **Video ID**: `b7IMBHMjNv8`
- **메타 소스**: oembed+html

![썸네일](https://i.ytimg.com/vi/b7IMBHMjNv8/hqdefault.jpg)

## 영상 설명

Built with $240 and zero remorse...

I put the newest long-range radio chip on a Raspberry Pi 5 — a $246 build that does what $20,000 military mesh radios do. I'll show you how I built it, how it compares spec-for-spec, and a live field test that proves it works. No subscriptions, no closed firmware, fully open-source.

Build your own $20,000 MANET for $97 👉 https://buildwithparallel.com/products/haven

New OpenWRT/MorseMicro Raspberry Pi 5 Image 👉 https://github.com/buildwithparallel/openwrt-morse-rpi5

MM8108 Halow Chip 👉 https://www.digikey.com/en/products/detail/gateworks-corporation/GW16167/28244003

Watch these next:

I Built a $20,000 Military Router for $106.23
https://www.youtube.com/watch?v=ofR7GFNZzJY

I Built a $40,000 Military Drone for $120.07
https://www.youtube.com/watch?v=bmLE9BT76Pc



🎥 NEW: Unlock MEMBERS-ONLY videos and behind-the-scenes drops 👉 https://bit.ly/4iyBm4I
🛠️ The exact tools and gear I trust (and actually use) 👉 https://amzn.to/44fKDv4
📡 Join the r/ModernRadio community for LoRa, Meshtastic, and off-grid tech builds  👉 https://reddit.com/r/ModernRadio
💬 Get real-time help and connect with other builders on Discord  👉 https://discord.gg/g7h8Jc7Agt
📚 Step-by-step setup guides, templates, and insider resources 👉 https://bit.ly/4ivZDID
🛒 Grab custom gear and tools designed by me 👉 https://etsy.me/4isKwjb
📩 For sponsorships or business inquiries, reach out: macgyvertechnology@gmail.com
🧠 Need expert help fast? Book a 1:1 session and get unstuck today 👉 https://bit.ly/42I10y5

## 자막 · 본문 정리

> 언어: en · 구간 362개

This costs $20,000, and this costs only $246.04.

One of them is a military-grade IP mesh radio. The other is a Raspberry Pi 5 sitting on my desk. But, they do the same thing. Okay, okay, I didn't fast rope into Fort Bragg and pry one out of a Pelican case. But, I did borrow the idea, which is an IP mesh that routes your comms off-grid over long distances

without internet, and I put that on a Raspberry Pi 5. The newest long-range radio chip on the market plus the most powerful Pi ever made working together for the first time ever. I've told absolutely no one about this until now.

This is Haven 2. Cuz here's the thing, a guy in his garage with a 3D printer and a GitHub account can now build a router that outperforms what most people buy off the shelf and overlaps with what the DoD pays vendor rates for in the mesh radio space. Now, Haven 1 shipped earlier this year, and it hit a nerve.

Hundreds of builds, photos in my feed every week, and outreach from people way above my pay grade. But, that setup only ran on the Pi 4. So, I kept getting the same question, "When will this work on a Pi 5?" And in an effort to answer that question, I emailed the Halo chip manufacturer, Morris Micro. And

honestly, they were great about it. One of their lead engineers told me they were working on it and that it will work in their '24 based version. But, then dropped something interesting by saying that a clever developer in the community might be able to pull back the hardware definitions into their current stable

build to get it all working today, which was just enough to bait me into rolling up my sleeves and taking a stab at it.

Now, what that meant in practice was a full back port, pulling driver support for a chip that didn't exist yet in '23.05 out of an OpenWRT '24 tree and using Claude to debug every incompatibility error that was thrown at build time for several days until a stable build was generated. And just to

set the scene, simply building OpenWrt from source is no walk in the park. I don't wish that task upon my worst enemy. It's a CPU dependent task that on a normal computer can take two to three hours per iteration. And I was iterating a lot. But I got the idea of spinning up a virtual machine on GCP with the most

luxurious setup I could. 60 cores, 256 gigs of RAM, and an extreme persistent disk drive that maxes its disk read write times to speed up our builds. So, the machine I ran this on cost six grand a month to run. But I only needed to run it for a few days. That knocked the iteration loop down from hours to

minutes. And finally, we got an Arpi build image that actually booted. But we still weren't out of the woods yet. But first, what is this thing? So, folks in the industry call it a MANET, short for mobile ad hoc network. And underneath the acronym, it's an IP mesh radio with a fully digital architecture. Solid

state, headless, a piece of kit you take with you into the fray, and it gives you and your squad a private network wherever you happen to be. Your end user devices, phones, laptops, tablets, connect to it over standard 2.4 or 5 GHz Wi-Fi, same as any router at your home.

You keep one of these on your person within a couple hundred feet of your phone. But the interesting part is here, sub-GHz 802.11ah Halo. Same neighborhood spectrum as projects like LoRa and Meshtastic in the US, which is why it carries signals like those builds do. Lower frequency than

your home Wi-Fi, which means it punches further. Done correctly, the radio gets you several kilometers of range. Morse Micro actually holds the Guinness World Record for this. They pushed a Halo link out to 10 miles at 2 megabits per second. But here's the kicker, that record was set on their last generation

chip, the MM6108. And this build actually runs the brand new MM8108.

Better range, better throughput, and it drops into the same Haven socket the original module did. So, if you built a V1, this swaps right in. All the radios are bridged, so your devices don't know they're talking over Halo long haul.

They just see Wi-Fi. And any node on the mesh can share an internet uplink with every other node. So, plug in a Starlink terminal or a cellular modem into one of these, and suddenly the whole mesh has backhaul. Most people using a mesh like this run ATAC on top, the open-source mapping app that the military uses for

situational awareness. But really, anything that runs over IP can theoretically run over this. Last week, Amelia and I ran a truly mobile network test. One Haven node in each vehicle with a magnetic Halo antenna on each hood. Each phone joined Wi-Fi from the node in its own car, and we shut off

cellular data, so there was no carrier internet at play. Then we held a FaceTime call on our private mesh while driving 70 mph down the highway. That was awesome. On the protocol side, this thing supports 802.11s, which is the standard Wi-Fi mesh protocol, which works fine. But we also

have support for something called Batman-Adv, which is a smarter routing layer. It supports more types of physical links, and it operates at layer two, which means the whole mesh looks like a single switch to the devices on it. Roaming, failover, multicast, they all just work. And all the Wi-Fi

runs over type three encryption, specifically WPA3-SAE, which is something a lot of home routers sadly still don't support. And while we were upgrading, I went ahead and upgraded the battery supply, too, because why not? V1 ran on two 21,700 cells, totaling about 10,000 milliamp hours of capacity. For context, the

L3Harris military radio battery commonly used here is around 7,000 milliamp hours. In terms of power draw, the Pi 5 is a little hungrier than the Pi 4 was.

You can technically run it on two 21,700s, but you have to power it through the USB-C port because the pogo pins on the GPIO header don't deliver enough current for the new board. So, I swapped in a new WaveShare hat that takes four Molly cells totaling 18,000 milliamp hours of capacity, almost three

times what an L3 Harris battery holds.

From cells you can buy off the shelf, supply chain-wise, the Pi board comes to us out of Wales, and the Halo chip is engineered in Australia. Most of the peripherals are still out of Shenzhen, not perfect, but very likely better than whatever modem came free from your ISP.

Using these devices just feels powerful.

It's the same feeling I felt getting my first MeshTastic node up and running.

Let's actually look at the brain inside the military version, the kind that ships in hardened road cases and lives on radio set decks next to five-figure price tags. Quick sidebar, neither Persistent nor Silvus publishes pricing publicly, so the numbers I give come from someone with access to the DoD

procurement data who reached out with the actual figures. So, yeah, your tax dollars at work. And if transparency matters to you, that's one more reason to pay attention here. Now, Persistent's own spec page lists the onboard computer as 1 GHz quad-core ARM, 2 gigs of RAM, 128 gigs of flash. I don't have a unit

on the bench to confirm the exact system on a chip. These are the numbers published on the website that I'm comparing against. The Pi 5 on my desk is also quad-core ARM, but Raspberry Pi clocks it up to 2.4 GHz, eight times the RAM, four times the storage, and three to four times the per-core throughput at

the same wattage. And when it comes to hardened ruggedization, well, yeah, they definitely have us beat there. Most military radios can survive EMPs and Carrington events. I'm pretty sure if I sneeze on mine, it'll probably combust.

But, we'll get working on an enclosure soon. Interestingly, the MPU5 runs a version of Android on it, which means you can probably play Candy Crush between missions. Haven runs OpenWRT, which is the most popular Linux-based routing OS out there. The other main difference is that military radios are

licensed, so they can do things that we can't. But, I want to keep ours unlicensed if possible and see how far we can push that approach. Now, you might be wondering, why is a cable protruding from the GPIO hat and rerouting into the motherboard? Well, that's how we roll in open-source

country. Improvise, adapt, overcome.

Eventually, we'll improve the form factor. Now, we talked about the device, but what can it actually do? For that, let's head outside. Okay, so I have an interesting setup here to demo what this thing can do. The Haven 2 is here with me, and I'm connected to it over my phone. But, to do anything notable, we

need another node. Now, this thing is compatible with all other Halo nodes. No special specs or requirements needed, which means we can make a micro node using a Chow, attach a FPV camera, put it on Bruno, and suddenly we have some scouting ops we never had before, which is perfect for this test. He runs, and

we should see what he sees. Okay, so we found a kind of open spot here. So, I'm going to set up the Haven 2 right here, and then we're going to put the node on Bruno and have him run around and see if we can't get some footage of him running around over the Halo connection.

So, you can see this guy is streaming video over ATAC. And so, now we just got to put it on Bruno and see if we can get a good shot.

So, I'm going to wrap it in this fabric here, cuz I don't want these battery terminals to touch Bruno. So, I'm going to do that, and then I'm going to use some rubber bands, and we should be good to go. Okay.

Mr. Bruno, you have the cam on you.

Go running to the yonder, Mr. Bruno.

So, we're watching a feed from Bruno right now.

This is cool.

So, the camera went flying off him in about 90 seconds, but Oh my gosh.

Must be hot. He's under the car. Um but it did work.

Um you know, it's just not designed for that kind of thing.

Obviously.

But, um yeah, it worked and we got it running into A-Tac, so that was cool.

Live video feed is up, A-Tac track is up, link always stays locked while he moves through trees and behind structures. That's Bruno cam over Halo on an RPi5 stack we built right here on this channel. Not pretty, not ruggedized, but it works. [music] And I've stacked up enough expensive

experience on this project that committing the notes to the public felt like the right move. So, if you want to build one of these yourself, I've attached all my notes on the new upgrade into the Haven Builders Guide. You can find it in the link below. You certainly don't need that to build one. The code

and schematics [music] are all open. And if you build it and don't like it, cool.

Pull the SD card and flash Home Assistant or Raspberry Pi OS and keep moving. This stack keeps good tech out of the landfill, which is another reason I support it. But, that guide contains my personal notes curated from a year plus of tests, and ultimately it helps support this channel and ensure further

innovation. The whole thing still comes in at a fraction of the price you'd pay for an off-the-shelf device. Oh, and one more thing. Turns out the Pentagon doesn't have a monopoly on the sky, either. Because if you add a $30 USB dongle to the very same pie, suddenly we've got optics on every aircraft

within 200 miles. Okay, so I just plugged a SDR into the Haven and I have it hooked up to this antenna here. Now this is not quite an ADSB antenna, but it's pretty close. ADSB is like 1065 MHz. This is 915. So it should it should suffice for a quick and dirty hot swap here. But now

the question will be is can I get any phones to show up on ATAC? So this guy will connect to the 2.4 on Haven and then the SDR should be able to pick up planes and throw it on a map on this. So we'll see. Okay, so on my phone here, you can see we're connected to Haven.

Now there is no internet, there's no uplink, but that's expected. So the question is now if we go over to ATAC, ooh, here we go.

So I'm just going to plop it down right there and take a look and we see quite a few planes here.

Um we can go ahead and click on one and it will give us information about it. Um uh yeah, just all of the uh sort of details about that aircraft um which is pretty cool here. And again, we don't even have any we don't even have the right antenna going here.

Um and yet it still seems to be working.

Now what's interesting is this guy appears to be getting closer to us. So I wonder if it flies over us if I can get that a shot of that from the sky. And I hear it.

I do hear it. Let me take a look.

Yep.

Right there.

That's pretty cool.

So, that plane right there is literally right here.

And we can see it's going 184 mph.

And um it's uh we're we're getting its ADSB traffic with this antenna right here on the Haven. So, no internet and picking up uh all the airplanes within, I don't know, um maybe 100 mi or so. Pretty cool stuff there. Not bad. Everything I just showed, code, schematics, links, is all

available for free in the description below. All of it is yours. I'd love to see Andro or Ubiquiti say the same thing. For more, click here.

## 학습 힌트 (자동)

_태그가 없습니다. 설명·자막에서 키워드를 추출하세요._

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._