---
title: "Engineering a UAV - Part 1: Mission Definition, Requirements, & Design Point"
channel: "GabeFPV"
video_id: "geljbqJz1ro"
url: "https://www.youtube.com/watch?v=geljbqJz1ro"
thumbnail: "https://i.ytimg.com/vi/geljbqJz1ro/hqdefault.jpg"
captured_at: "2026-07-29T12:24:42.292Z"
published_at: "2026-07-29"
source: youtube
meta_source: "oembed+html"
has_description: true
has_transcript: true
transcript_quality: "good"
transcript_lang: "en"
status: raw
sha256: ba6897a653b9a0ac19da9db483b7be96e67f6f1c7ef4c0ca69aa48f14270a9a4
---

# Engineering a UAV - Part 1: Mission Definition, Requirements, & Design Point

- **채널**: GabeFPV
- **URL**: [https://www.youtube.com/watch?v=geljbqJz1ro](https://www.youtube.com/watch?v=geljbqJz1ro)
- **수집일**: 2026-07-29
- **Video ID**: `geljbqJz1ro`
- **메타 소스**: oembed+html

![썸네일](https://i.ytimg.com/vi/geljbqJz1ro/hqdefault.jpg)

## 영상 설명

In Part 1, we begin a series of videos diving into all aspects of aircraft design, at a small scale. This video covers Mission Definition, Requirements, and Design Points, also touching on how thrust changes throughout flight and a few other small, but important, topics for the design process. 

I make these videos to help people learn about aircraft design, I hate the institutional paywall. Between full-time engineering and grad school, making these takes nearly 100% of my free time. If you've found these helpful, let me know and we can share a coffee/beer over it!: 
https://buymeacoffee.com/gabefpv

(BTW, if you want black borders on the video instead of gray, click on the gear icon on the bottom right of the video and turn off 'Ambient Mode')

Important Sources:
AIAA: Raymer, D. P., Aircraft Design: A Conceptual Approach, 6th ed., American Institute of Aeronautics and Astronautics, Reston, VA, 2018.
Keane, A. J., Sóbester, A., and Scanlan, J. P., Small Unmanned Fixed-wing Aircraft Design: A Practical Approach, Wiley, Hoboken, NJ, 2017.
Finger, D. F., "Comparative Performance and Benefit Assessment of VTOL and CTOL UAVs," Proceedings of the International Micro Air Vehicle Conference and Flight Competition (IMAV), 2017.
Sztajnbok, I., et al., "Drag Characterization of a Fixed-Wing Unmanned Aerial Vehicle (UAV) with COTS Avionics through Flight Testing," 2025.
Finger, D. F., Bil, C., and Braun, C., "Drag Estimation of Small Fixed-Wing UAVs," The Aeronautical Journal, Vol. 122, No. 1248, 2018.
"Flight Testing Small Electric Powered Unmanned Aerial Vehicles," Technical Report/Paper.
Mattingly, J. D., Heiser, W. H., and Pratt, D. T., Aircraft Engine Design, 2nd ed., American Institute of Aeronautics and Astronautics, Reston, VA, 2002.

Timestamps:

0:00 Intro
01:50 What is Design?
05:25 Conceptual Design
07:31 Preliminary Design
08:57 Detailed Design
10:16 Sizing & Synthesis
12:00 Who's the Customer?
14:10 Requirements
19:49 Conceptual Sizing
25:18 Electric Propulsion Fundamentals
27:09 Thrust Lapse
30:36 Summary

## 자막 · 본문 정리

> 언어: en · 구간 852개

I'm kicking off a seven-part video series where we are together going to perform a complete semi-professional engineering cycle for a fixed-wing UAV.

That meaning from the first blank sheet concepts to the final flight test data correlation. If you look at a typical hobbyist workflow, it usually starts with a rough idea or a cool drawing on paper that they think will achieve some specific performance. And the idea then moves straight to CAD and building with

little to no engineering actually performed. And that ends with a flight test that works mostly by accident. We are not doing that. I'm going to walk us all the way through the real phases of an aircraft design program scaled all the way down to the scale of a fixed-wing UAV.

This isn't about just building a drone.

This is about learning the actual engineering process behind why UAVs look the way they do, why they fly the way they do, and why they're built the way they are, at least at non-production volumes. And we'll be focusing on how to walk through every one of these processes, especially connecting the

dots along the way to result in one finished flyable UAV that successfully flies some mission designed in the really early stages like in this video.

So, if you're wondering where all of the other videos are right now, I'm intentionally publishing them as I work on them as I get time to work on the project because I want you to see and learn from how assumptions change. In other words, I don't want to have already have flown the thing and gone

back and changed all my calculations so they're 100% right from square one from this video. I want us to together work through how we reflect back on discrepancies in calculations and how we adjust those moving forward. Because it in reality, your design or your program is going to have assumptions that are no

longer valid at some later stage.

All right, with that out of the way, that's enough wasting time. Let's jump right into the first video. Before diving into the technical design work, I think it's worth being precise about what exactly we mean by design. Because a lot of confusion in really any engineering project comes from skipping

the step. And I know before you skip ahead to the meat of the conceptual design and the fun stuff, I really encourage you to hunker down for at least a couple of minutes to learn these fundamentals.

I understand that topics such as what is design may seem mundane and kind of unnecessary, but I just need you to trust me.

If you don't have at the very least a good understanding of the groundwork like this, you're going to have a much tougher time following through and actually engineering a proper solution.

John Anderson defines design as the intellectual engineering process of creating on paper a flying machine that either meets a set of requirements or explores new concepts and technologies.

Raymer shortens this a bit further stating design is the creation of the geometric description of something to be built.

And it can be further simplified into design is about creating something with a purpose.

The common denominator across all of these is intent. Design is not optimization in isolation. It's not CAD.

It's a purposeful response to a defined need. Design begins with an explicitly identified need and that need ultimately limits and shapes the solution space.

Mattingly frames this very clearly.

First, design is driven by need. If there's no operational need, then there is no design problem. Just analysis really for its own sake.

Often times this will be portrayed in something referred to as a concept of operations or a CONOPS.

Second, design problems do not have unique or optimal solutions, which in simpler terms is just saying that for a given set of requirements, many legitimate aircraft can exist.

The final configuration is always a compromise between competing objectives like performance, weight, cost, and risk. And because of that, the process must be systematic. You really cannot rely on intuition alone once the design space becomes multi-dimensional.

Design is also inherently iterative. So, early assumptions will be wrong in one way or another, and the process of design requires looping back, sometimes repeatedly, as those assumptions are reviewed and corrected. And I think that's an important note for this series because you'll see a series of

assumptions made during the conceptual design in this video that will either get refined later or ignored for now, and the analysis and flight testing will ultimately reveal the consequences of leaving those alone.

I've purposely left some parameters as rather ambiguous assumptions to demonstrate exactly this and to show you how you can still design a great aircraft or UAV in this case without all the right answers from square one. Finally, aircraft design is fundamentally interdisciplinary.

Aerodynamics, propulsion, structures, controls, manufacturing, and operations, they they all interact with each other.

You can't optimize in isolation one without affecting the others, and this is why conceptual design is not about every single small detail, but more about bounding the problem correctly, uh identifying the dominant drivers, and narrowing your solution space before committing to one

geometry or one high-fidelity analysis.

Every aircraft design project and effort begins in the conceptual design phase.

This is where a wide range of candidate configurations are explored, and where both design concepts and top-level requirements are traded against one another.

During conceptual design, engineers will evaluate multiple layouts of aircraft and compare the performance and feasibility of those and gradually narrow down towards a single well-balanced configuration.

The process typically involves close interactions with customers or stakeholders to converge on a realistic and internally consistent set of requirements.

At this stage several fundamental questions are addressed relating to the overall configuration, the approximate size and weight, and the basic performance capability of what you're building.

The design space at this stage is really intentionally broad and the aircraft concept will evolve as assumptions are tested and refined. So, that means an important aspect of conceptual design stages is that it is a very fluid process. As we gain more understanding on certain aspects of the design and improvements

through trade studies, the conceptual design will change.

Nothing is frozen and the design changes repeatedly, and this is where a lot of the fun is for aircraft designers.

In a more professional setting, the design may very well experience week-by-week changes to the configuration, ultimately building into a sort of design evolution experienced by the conceptual design.

Conceptual design also uses the requirements that were set to guide the development of the overall aircraft configuration and arrangement. So, typically this includes the wing geometry and the tail geometry, as well as a fuselage shape, and the internal placement of payloads and major systems.

In this video, though, we'll be reviewing the derivation of a conceptual design point.

That is, the aircraft's gross weight, the wing loading, and the thrust and power requirements.

So, once conceptual design has converged onto a viable configuration, we then move into what we call preliminary design. And this is where the aircraft starts to become real.

In preliminary design, the major configuration decisions are mostly fixed and the wing planform, the tail layout, the propulsion concepts, the overall layout of the aircraft are no longer moving fluidly.

Now, the focus shifts from exploring ideas to validating them.

This is where aerodynamics, where propulsion, where structures, and where controls are analyzed in a much greater detail and higher fidelity tools start to come into play.

This is also where CFD, more refined weight estimates, stability and control analysis or S&C, and subsystem sizing really begin to dominate.

The goal now is to verify that the conceptual design actually works and works when subjected to more realistic assumptions.

By the end of preliminary design, the program typically reaches what we call a go or no-go decision. And if the design survives this phase, the configuration is effectively frozen, meaning that really only minor changes are allowed moving forward. Once the configuration is frozen and the preliminary design

work and verification have been performed, we enter detailed design.

At this point, the question is no longer does this aircraft work, but how do we build it? Detailed design focuses on the exact geometry, the materials, the structural layouts, and the system implementations. And here is where every major component is designed down to a manufacturable level.

So, structural members are sized and designed, control systems are finalized, things like wiring and plumbing are routed, and tolerances are specified.

This is also where drawings, models, and production data are generated. So, testing ramps up significantly during this phase, naturally.

These include structural testing, system integration tests, and again high fidelity simulations that all support risk reduction before the actual hardware is built.

By the end of detailed design, the aircraft is fully defined and the program transitions into full-time fabrication and assembly and flight testing.

So, up to this point we've been talking about conceptual design specifically at a very high level, what it is, why it's fluid, and how requirements and trade studies slowly narrow the design space.

But now the question becomes, how do we actually start putting numbers to this?

Kicking off conceptual design, this is where sizing and synthesis comes in. And together these two form the core of conceptual design.

Sizing is where we stop talking abstractly about configurations, and we start solving for the physical scale of the aircraft, including how big it is, how heavy it is, and how much thrust or power it needs to meet the mission.

Synthesis on the other hand, then takes those numbers and translates them into actual aircraft layouts, turning the wing loading, the weight, the power into geometry and arrangements, and ultimately the integration of various subsystems into one single cohesive aircraft.

So, before we worry about the detailed geometry or subsystem integration, we first need to size our aircraft and establish what's called a design point.

In aircraft design and energy-based constraint analysis as we call it, the specific combination of primary design parameters is often referred to as a design point.

This really allows the aircraft to meet all critical performance requirements, and that point is found on what we call a constraint diagram where the region of feasible solution bounded by curves for various requirements like takeoff, climb, and cruise is at its optimum. The design point ultimately dictates the

necessary sizing of the wing and the necessary sizing of the engine to satisfy, again, the early mission requirements.

Once that numerical foundation is in place, we can then move into synthesis, which translates those numbers into the actual aircraft layout, but everything starts here with sizing.

Now, before we start crunching numbers and getting into the fun stuff, we have to address who's the customer or the stakeholder.

Usually in a university or a corporate setting, the customer is the scary person sitting across the table from your team telling you that you need to carry 500 passengers or fly for 24 hours or something crazy.

They're usually the source of your pain because they're usually the source of your constraints.

And I know some of you're probably rolling your eyes right now thinking, "Gabe, I'm building this in my garage.

I don't have a customer." So, I'm going to tell you this. Stop right there.

This is exactly the first trap of conceptual design.

In engineering, the customer isn't just the person writing the check, but they're also the source of your constraints and requirements.

For a Global Hawk, the customer is the Air Force demanding 30 hours of loiter time.

For an airliner, maybe it's the airline demanding specific seat mile costs.

But, for this project, you you are the customer.

And this is where most hobby designers fail. They skip this step because it feels like corporate fluff.

But, if you don't sit down and honestly act as your own customer and explicitly demand specific needs, speeds, payloads, ranges, or field lengths, then you aren't designing the aircraft. You're just gluing foam together and hoping that it does something cool. So, for this series, I need you to put on your

customer hat first, write down exactly what you demand from this machine.

And only then are you allowed to switch back to the engineer and designer mode to figure out how to build it. To be a good engineer, you have to first be a strict customer. You have to stop saying, "I want it to fly fast." or "I want it to fly far." and start giving yourself rigid rules to

design against. And we call those rules requirements.

Before we touch geometry, CFD, or component selection, we need to be very explicit about what this aircraft is required to do and just as importantly, what it is not required to do.

When designing an aircraft, even at a small UAV scale, and especially when the aircraft is a product, this is extremely important to define the requirements correctly.

Systems engineering will teach you that good requirements are something called SMART, S-M-A-R-T, which is an acronym for specific, measurable, attainable or achievable, realistic or relevant, and traceable.

For example, "The UAV shall have good performance." is neither specific nor is it measurable. Good is undefined and cannot be measured. "The UAV shall loiter for a long time." is neither measurable nor traceable.

"The aircraft should be below 500 lb if possible." is non-binding and ambiguous.

The words should and if possible make it optional, and the weight type isn't specified, and operational or regulatory trace is informal rather than explicit.

All right, with a few examples of bad requirements, and now knowing that a good requirement is SMART, let's go through a few basic requirements that I've set myself for the UAV project.

Nothing complicated and intentionally minimal. They're not certification level, and they're not marketing driven.

First is the payload. 2 lbs. That's the only thing this aircraft exists to carry.

For most operational aircrafts, particularly those intended to deliver transportation, sensing, or services, the design is fundamentally driven by a useful payload requirement. That's how you make money. Everything else, structures, propulsion, batteries, fuel, aerodynamics, is sized around that constraint.

Second, endurance. 45 minutes.

Not range, not loiter plus dash, just total usable endurance.

I could have defined a range requirement just as easily, but for this UAV, my mission will revolve around a local ground station or area of interest where I'm standing. So, the time that the aircraft is capable of keeping the useful payload in the air above that area of interest is critical to me,

instead of how far the UAV can travel away from me. Keep in mind that the endurance and the range are not interchangeable requirements.

They are governed by different optimization conditions, even though they share common aerodynamic and propulsive variables, and we will get into detail about this later in the video. Endurance is maximized by minimizing the power required, while range, on the other hand, is maximized by minimizing the

energy per distance or, equivalently, maximizing the lift-to-drag ratio.

Third, takeoff and landing. 250 ft. This is a hard constraint that immediately pushes me towards wing loading limits and low-speed lift capability.

The field length and surface type were chosen to allow my UAV to rely minimally on runway infrastructure, really only requiring grass fields to take off.

Fourth is replicability, meaning no exotic systems. I want only commercial, off-the-shelf, readily available electrical components. And this matters because it bounds my efficiency assumptions if I'm using batteries and power densities. And it prevents me from designing an aircraft that only

works with custom PCB boards and requires me to do a bunch of electrical design because I suck at that. I'm not an electrical engineer.

And last but not least, but something that should be written out on requirements, is that the UAV needs to be controlled remotely. Meaning the hard set requirement is the aircraft shall support remote controlled and autonomous operations.

With just these five requirements, we can make a series of assumptions that will allow us to determine the required wing loading and power loading and initial drag polar and a first-order weight estimate. This is really when we can start to have fun and brainstorm and draw concepts and conceptual

developments.

A perfect example of a common mistake is the propulsive architecture on this UAV.

As the designer and the engineer, my judgment advises an electric propulsion system rather than a combustion engine.

However, this should not be a requirement whatsoever. This is a design choice and I made this to fulfill the requirements.

It's more common than you think for management or customers to wrongly turn engineering decisions into requirements, which makes the engineers job way more difficult.

Okay, finally, let's start digging into the details of conceptual design.

What I'm going to lay out here is basically the conceptual design feedback loop. And the key idea is that we're trying to solve the aircraft using only a few high-leverage parameters. And these are most commonly thrust-to-weight ratio and wing loading because those two numbers capture a huge amount of top

level performance behavior.

And I know you're probably thinking again, when is Gabe going to get to the design and the numbers and the fun part already?

And I don't blame you at all. This is a complicated process though with a lot of extremely coupled variables and parameters and it's a lot easier than you think to get lost in the loop of well, this affects this which might increase this which then decreases the original thing slightly after I tried to

increase it.

Just trust me here, please and track through the technical flow of sizing with me. Starting at the top, we'll first pick a notional configuration.

Nothing detailed yet, just enough to decide I am a tractor propelled twin boom fixed landing gear piston engine aircraft kind of thing.

Now, we'll need several critical inputs to get our technical design started from there. On the left first for propulsion, we have the thrust lapse and the fuel flow rate or for electric architectures, you can mentally substitute available shaft power versus air speed and energy draw versus time.

For combustion aircraft, the propulsion model is what tells you how the installed thrust changes with altitude and Mach number and also how expensive it is in fuel flow to produce said thrust.

Moving to the middle for aerodynamics, we need to generate a drag polar and lift curve.

We use these to determine the aircraft's aerodynamic behavior in a compact way.

Now, to the right, we can estimate the empty weight of the aircraft from historical weight regressions because we won't know the weight of the aircraft until we design the details of the full thing. And by then, it's way too late to change the conceptual design point.

This, you'll notice, is a common theme in conceptual design and it's really an important skill for an engineer, which is the ability to make educated assumptions and to use historical data to guide future designs.

You'll never know all the details this early. No one does.

I think what really sets strong conceptual designers apart is the quality of their initial assumptions and the rigor of their estimates, which can really place the conceptual design within about plus or minus 20% of the final aircraft rather than relying on rough guesses that miss by maybe plus or

minus 30 or 40%.

With propulsion, aero, and weight models in hand, we do what we call energy-based constraint analysis, which I'll jump to later in this video.

Conceptually, this just takes your point performance requirements like takeoff field length, climbing performance, cruising performance, turning performance, operational ceiling, whatever else matters, and it turns each of those into a curve on a plot of thrust-to-weight ratio versus wing

loading.

Performance constraints become boundaries, and the feasible region is where all constraints are satisfied simultaneously. But, here's the trap.

Conceptual analysis gives you ratios, not actual aircraft size. And that's why we need to perform mission analysis, and this is a piece that a lot of people skip mentally.

Constraint analysis might tell you that your design point is, say, a thrust-to-weight of 0.35 and a wing loading of 18. And that's great, but it still doesn't tell you the weight, the wing area, or the thrust individually.

And that's exactly why mission analysis exists. It provides the additional equation needed to back out the actual values, and it does it by iterating the fuel or energy required versus the fuel or energy available until the design converges and satisfies the basic mission requirements in parallel with

the performance constraints. The major output here is the weight of the fuel required to fly the mission. And notice the blue arrow labeled weight fractions, tying the mission analysis back into the design point. The two are related, and because the weight changes throughout the mission as the fuel burns,

or for electric architectures, as stored energy is depleted, but weight doesn't change there. The fuel weight change changes the required lift coefficient, and therefore the drag that you experience, and therefore the thrust required, and therefore the energy use.

So, what we end up with is an iterative sizing loop.

Energy-based constraint analysis is performed to advise a design point of instantaneous thrust-to-weight ratio and wing loading.

And these data points are fed into the mission analysis and change what we call betas, or mission phase weight lapses, which occur because the weight of the aircraft lapses, or changes from takeoff weight as the fuel burns throughout the mission.

This is important because as you burn fuel, your aircraft gets lighter and less lift is needed, which means that less drag is experienced.

Once we know that we've converged all of these betas, or these weight fractions, for each phase of the total mission, we can figure out the mission fuel fraction, and use that with the takeoff weight guess to compute the fuel weight required to fly the entire mission.

Okay, that's a ton of information. So, to step back, the end product of this whole design loop is a design point, meaning a consistent set of takeoff weight, wing area, and thrust-to-power.

So, now in the next sections, we're going to build each of these blocks just enough to be useful.

And this includes the propulsion model, the drag polar, and the weight estimate, and then run a constraint analysis, picking a design point, and finally closing the design loop with mission analysis.

For fuel-burning aircraft, the sizing begins with an estimation of the fuel burned using a ratio between each mission phase's starting and ending weight that we call a mission segment weight fraction.

On the other hand, for electric aircraft, a similar methodology can be used, but the Breguet equations cannot be used because there is no fuel burn, so no change in weight, and hence no integrated weight change over the mission segments.

What we can do, however, is define the required battery mass for each segment, and this is called the battery mass fraction.

Raymer mentions that the battery mass fraction can be thought of as similar to the propellant mass fraction for rocket analysis, and similar to the propellant mass fraction, the battery mass fraction required to obtain good performance and range is high, but keep in mind that this performance

can only be ensured if the empty weight is kept low.

Here is the generic battery mass fraction equation for some runtime endurance.

This is based only on the motor power setting and is therefore independent of any flight conditions.

Propeller efficiency isn't in yet because again, it only calculates the battery mass required to output some shaft power to any device. With a little bit of manipulation, we can derive the following equations for the battery mass fraction from loiter time and cruise range.

A quick side note for flight testing, if you extract telemetry logs from a flight controller, the power you are seeing is the input power. It is not this output power.

We can also use the rate of climb equation to derive the battery mass fraction required for climb, and this is using a similar structure to the generic endurance battery mass fraction equation at the top.

You can see that in the loiter, in the range, and climb equations for calculating the battery mass fraction required, L over D is in the denominator, which means that as our aircraft gets more aerodynamically efficient, the battery mass fraction required for the same loiter time, for

the same cruise range, or for the same climb rate, decreases. The total battery mass fraction can then be the sum of the various mission segment battery mass fractions, and can be used to solve for the aircraft design weight utilizing the empty weight fraction and the payload weight.

We'll discuss the empty weight fraction a bit more in depth later.

Now, onto thrust lapse. I'm going to go through this quickly. And basically, a lapse just means a decrease, by the way.

For this discussion, there are two important sources of thrust lapse: a lapse due to air speed, and a lapse due to altitude. To preface this, the thrust of a propeller aircraft is proportional to the inverse of the air speed, and in jet and air-breathing aircraft, the thrust lapses, or decreases, with

altitude, and is roughly constant with speed until compressibility effects take over. For propeller-driven aircraft, as forward air speed increases, the angle of attack of the blade decreases, and you eventually hit a speed where your propeller will create zero thrust, no matter how fast it's spinning.

This means that the thrust lapses with air speed for propellers. That is the physical mechanism behind the lapse. The mathematical side of that explanation is that because electric motors and piston engines are roughly constant power devices at high throttle, and because power equals thrust times

velocity, if power is constant and the air speed increases, the thrust will also decrease.

So, the reason the thrust drops to satisfy the power equals thrust times velocity equation is because the blade's angle of attack is decreasing.

The trap that a lot of newer designers fall into is one of static thrust, aka bench testing, which exists only when the aircraft's velocity is zero.

A lot of hobby airplane designers are used to looking at motor charts that say 2 kg or 2 lb of push or pull, but that's static thrust. That number only exists when the aircraft's velocity is zero, basically, when you're bolted to the bench. The second you start moving, that number is no longer true.

This happens because of something called the advanced ratio, which compares your forward speed to your rotational tip speed in the propeller. As that increases, your blade's angle of attack drops.

And that causes the thrust coefficient to slide down the efficiency curve until it hits zero.

On this note, you'll never have a more abusive and demanding load on your motor than when you're static testing like this because the angle of attack on every airfoil cross-section on the blades are greater than they will ever be when flying.

I've got a deep dive into rotorcraft aeromechanics on my list of future videos. I just need more time in the day to get to that.

Now, on to the altitude thrust lapse.

For design, it's important to know that for piston engines, the power produced is relatively proportional to the mass flow of air into it.

By the definition of mass flow, the density of the air plays a big role.

Naturally, the higher the aircraft is, the lower the air density, and therefore the lower the power available is.

Raymer mentions that at an altitude of 20,000 ft, a piston engine has less than 50% of its power available as it does at sea level.

Luckily, one of my engineering decisions, not a requirement, engineering decision, to satisfy the UAV requirements, is to incorporate purely electric propulsion, meaning that this aircraft will not experience the adverse effects of decreasing air density on the available power output of an engine.

It will, still, however, experience the lapse in thrust due to the altitude increase.

Okay, now that we understand our thrust and how it changes, we need to predict the drag and how that changes.

This moves us from the propulsion box into the aerodynamics box. Remember that this is conceptual design, and we don't need nor do we have supercomputers or wind tunnels yet.

We just need mathematical approximations based on history, based on empirical regressions as well as our engineering judgment and textbook theory to get started and to kick off this design loop.

All right, thanks for roughing this one out. In part two, we'll get started straight away with drag polars and then move into sizing. So, I'll see you in the next video and as always, feel free to reach out to me with any questions you have.

## 학습 힌트 (자동)

_태그가 없습니다. 설명·자막에서 키워드를 추출하세요._

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._