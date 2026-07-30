---
title: "Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis"
channel: "GabeFPV"
video_id: "KUZjxxrvsLQ"
url: "https://www.youtube.com/watch?v=KUZjxxrvsLQ"
thumbnail: "https://i.ytimg.com/vi/KUZjxxrvsLQ/hqdefault.jpg"
captured_at: "2026-07-29T12:25:30.730Z"
published_at: "2026-07-29"
source: youtube
meta_source: "oembed+html"
has_description: true
has_transcript: true
transcript_quality: "good"
transcript_lang: "en"
status: raw
sha256: b0602e3c111247e6dd383c0ecaee3dd3e1b5560cedcbc1a61cdea6d1094c8956
---

# Engineering a UAV - Part 2: Conceptual Sizing, Drag Polars, & Constraint Analysis

- **채널**: GabeFPV
- **URL**: [https://www.youtube.com/watch?v=KUZjxxrvsLQ](https://www.youtube.com/watch?v=KUZjxxrvsLQ)
- **수집일**: 2026-07-29
- **Video ID**: `KUZjxxrvsLQ`
- **메타 소스**: oembed+html

![썸네일](https://i.ytimg.com/vi/KUZjxxrvsLQ/hqdefault.jpg)

## 영상 설명

In Part 2, we continue a series of videos diving into all aspects of aircraft design, at a small scale. This video covers Conceptual Sizing, Drag Polars, and Energy-Based Constraint Analysis (all at very basic levels), also touching on the differences between propeller-driven and jet driven performance and how each differs when performing constraint analysis and power sizing. Remember, the target at this stage is the derivation of the design point: Thrust/Weight Ratio, Wingloading, and Design/Takeoff Weight

I also realize that I totally forgot to cover the lift curve in this video, so I'll discuss it in part 3!

I work super hard to take down the paywall to deliver this information in the most digestible manner possible; I make these videos to help people learn about aircraft design, and I hate the institutional paywall. Between full-time engineering and grad school, making these takes nearly 100% of my free time. If you've found these helpful, let me know and we can share a coffee/beer over it!: 
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

00:00 Intro
01:31 Drag Polar Overview
02:20 Wetted Aspect Ratio
06:09 Drag Polar Buildup
10:01 Important Airspeeds
14:01 Turning/Loitering
15:52 Empty Weight Methods
17:29 Empty Weight Estimation
19:37 Conceptual Sizing Loop
21:25 Constraint Analysis
26:16 Design Point Selection
30:47 Summary

## 자막 · 본문 정리

> 언어: en · 구간 901개

This is part two of my seven-part video series where we are together executing a complete engineering cycle for a fixed-wing UAV from the first blank sheet concept to the final flight test data correlation.

This isn't about just building a drone.

This is about learning the actual engineering process and reasons behind why UAVs look the way they do, why they fly the way they do, and why they're designed the way they are, and how to walk through each of the engineering processes, connecting the dots along the way to result in a finished flyable UAV

that successfully flies some mission defined in the early stages.

Last video, I covered mission definitions, requirements, design points, and a few key things to understand about the performative differences between jet-driven aircraft and propeller-driven aircraft, as well as some of the most basic mission analysis equations for both fuel burning

and electric aircraft.

This video, we'll be talking more technically this time about conceptual sizing, including how to arrive at a design point using things like drag polars, weight fraction estimations, and constraint analysis.

All right, with that said, that's enough wasting time. Let's figure out how to predict drag at the conceptual stage.

Finishing off video one, we reviewed propulsion and how to understand how thrust changes.

So, naturally, we now need to understand drag and predict how drag changes because the reason that we require thrust to fly these missions is to overcome the drag that's generated as a consequence of us moving and producing lift to lift our payload.

One of the most important tools for this prediction is called a drag polar. I'll quickly cover this, but if you want more info, I mentioned it in a couple of my other videos, as well. Every shape has a drag polar, and it's really simply the mathematical relationship between the lift something produces and the drag

that it produces at that lift. The drag polar allows for quick determination of an aircraft's efficiency across the range of flight conditions, and it provides key inputs for sizing, for constraint analysis, and for thrust weight ratio calculations, for example.

We use the drag polar in conceptual design to determine the minimum drag and CD naught as well as the L over D ratio, which is really important for range and endurance calculations. A common and super quick method to estimate L over D, which is required for any range or endurance calculation, is what I'll call

wetted aspect ratio approximation.

If we're talking steady level flight, the lift required is known. So, the L over D is really only a function of drag, which is composed primarily of two parts at subsonic speeds, induced drag and profile or parasitic drag.

Physically, this just breaks down into skin friction drag and pressure or form drag.

Now, we could use the wing's aspect ratio as an indication of the wing's efficiency to estimate that L over D.

And for initial numbers in conceptual design, you can choose the aspect ratio from historical data on similar configurations or from intuition.

However, the aspect ratio really only gives insight to the induced drag. And again, that's only half the story. So, how do we estimate parasitic drag then?

What we can do is use a term called wetted area. And while for hand calcs in conceptual design, we typically base performance off the wing alone, an aircraft's parasitic drag depends on the exposed surface area of the entire aircraft, not just the wing.

To get early estimates of the L over D ratio, we can take the ratio of the total wetted area of the aircraft to the wing area, which is referred to as the wetted area ratio.

So, if L over D primarily depends on the wing span and wetted area, we can use a parameter called the wetted aspect ratio, which is the square of the span divided by the total wetted area.

Notice how similar this is to the regular aspect ratio equation.

A perhaps more useful simplification of this equation is that the wetted aspect ratio is also equal to the traditional wings geometric aspect ratio divided by the wetted area ratio.

Now, you're probably wondering, "Gabe, this is conceptual design. I have no clue what my wetted area is." And I would say to that, "Nope, no you don't, nor do I, none of us do." One of the simplest ways to estimate this though, to keep moving forward with your conceptual design and analysis, is

to use historical data trends of aircraft classes that have successfully flown. Again, the act of estimating via historical data regressions is common and a useful skill in conceptual design.

I'll skip the plots and charts of these trends, and I'll just give you these two tables.

On the top, select a wetted area ratio based on the closest configuration to your conceptual design. On the bottom, select a statistical loiter parameter K for the closest configuration.

With these, we can use the following equation for predicting L/D max.

If you're unsure of your aspect ratio, you can literally eyeball conceptual sketches here.

For the UAV I'm laying out, I'll use the wetted area ratio of the single prop configuration and the loiter parameter of the non-retractable landing gear propeller aircraft with my initial aspect ratio guess of nine to come to a final wetted aspect ratio.

Then, I'll use this equation to estimate the maximum efficiency for my aircraft.

Because this will be a propeller-driven aircraft, this L/D max will be used for cruise. Um bookmark this in your head because we'll come back to this.

Another method for estimating the maximum efficiency is what I'll refer to as the full drag polar build-up.

This requires several assumptions, but gives us more information than only the max L/D like the last method did. In fact, this method determines a full drag polar for the conceptual design, which is super useful for us because it can tell us the drag and efficiency or L/D at any lift and therefore velocity.

And this method is particularly useful because like I have here, you can make this a part of the conceptual calculation loop, meaning that when parameters like wing sweep and aspect ratios change, the L/D ratios at different air speeds will be automatically calculated and will automatically update the rest of the

conceptual model in a loop.

To begin, we'll need to estimate the Oswald efficiency factor, which is effectively a wing efficiency knockdown or correction to account for reality.

I discuss this more in depth in this video, but for now, I'll clarify that the span efficiency e sub span can be thought of as your wing's potential if physics were perfect, aka no viscosity, so this will underestimate drag. While the Oswald efficiency e naught can be thought of as

the efficiency of the wing's lift distribution after reality sets in.

Oswald also accounts for the fuselage interference based on historical data.

So, how do we determine the Oswald efficiency factor then?

Here are two equations that are expressed as a function of geometric aspect ratio and leading edge sweep.

Pretty simple, and in my calculations, I just hardcoded a check using the wing sweep that determines which equation to use automatically.

Like I mentioned before, to simplify the calculations, we make a couple of assumptions to get an initial drag polar.

These assumptions can be refined later and will be refined later through higher fidelity analysis and flight testing, but here are the assumptions you have to make and why I've made mine.

For the minimum drag coefficient CD min, a perfect sailplane made from composites might achieve 0.01 to 0.015, and a Cessna 172 achieves around 0.028, and the Raven is around 0.04.

So, for reference, for a cambered wing, CD min will occur at some positive lift referred to as CL min drag, but for wings with only moderate camber, CD naught could be considered as approximately CD min.

For a UAV with likely exposed servo horns, maybe cooling vents, and dirty fixed landing gear, I selected 0.04 as really a baseline for my clean but real small UAV.

For the lift coefficient that produces the minimum drag, CL min drag, I selected 0.2. This will be zero for a symmetric airfoil, anywhere from 0.4 to 0.5 for high-lift airfoils, and 0.1 to 0.2 for semi-symmetric and reflexed airfoils.

0.2 just implies that I'm using some mildly cambered airfoil. Again, rough assumption.

K1 is the total coefficient for controlling the quadratic lift term, and it dictates how sharply the drag increases with the square of the lift coefficient.

And this leads us directly to the next variable, K2, which controls the linear lift term. K2 is the variable that physically shifts the drag bucket left or right to match our airfoils sweet spot. And I compute the zero lift drag coefficient with this equation.

And with all of this, I use the quadratic equation for drag here to calculate the coefficient of drag for an array of lift coefficients.

It's simple to get from here the ratio for lift to drag every lift coefficient, and then to sort for the max here is 14.5.

And then to find at what lift coefficient that max is experienced at, which here is 0.95.

So, do you remember this calculation that we derived at a few minutes ago when estimating L/D max with the wetted aspect ratio?

So, we just found L/D max with a drag polar, and you'll notice that there is about a 5% discrepancy between these derivations.

This comes from the assumption that we made in the drag polar, and the fact that the historical regressions from the wetted aspect ratio L/D max derivations are just that, estimations based on a variety of similar aircraft. At this stage, so early, 5% is all right in the early conceptual

stage as again, we're going to refine these later.

This is our max efficiency and we can easily calculate the air speed required to fly at this speed, but believe it or not, for my mission, the aircraft should not be flying at max L/D.

L/D max gives me a point of minimum drag. If the goal is to cover the most distance per unit of energy or in other words, max range, then this is the speed to fly because it minimizes energy cost per distance flown. However, my mission is not range, my mission is endurance.

I don't care how far I go, I care how long I stay in the air for and to maximize this time, I don't need to minimize drag, but I do need to minimize power.

I'm going to drill it again. Power equals the product of thrust or drag for steady flight and velocity. Because velocity is a multiplier in the power equation, the power required depends on the cube of the velocity, while the drag only depends on the square of the velocity. So, the air speed for minimum power might be

achieved by slowing down to a speed below the speed required for minimizing drag.

For a parabolic drag polar, the max endurance speed occurs at the maximum of a peculiar curve of three halves power of the lift coefficient divided by the drag coefficient, which I'll show you in a sec.

At this speed, we're flying at the lowest point on the power required curve, but the trade-off is that the aerodynamic efficiency actually drops slightly.

But because there's an extra velocity term here in the power equation, right?

P equals TV, the total power required drops to a minimum and this is how we maximize the battery life.

Now, to show you that curve that I just mentioned, you can see here the peak of the CL to the three halves over CD And note that it's an indication of maximum endurance for a propeller-driven aircraft specifically.

As we learned a minute ago, the maximum range for a propeller-driven aircraft occurs simply at the highest value of L over D or equivalently CL over CD here.

And this is the point of minimum drag and therefore minimum thrust required.

So, we've covered the max range condition and the max endurance condition.

But what if your airspeed for your max range is painfully slow?

There's a third critical speed that we call the Carson speed, which offers the mathematical optimum for a {quote} fast cruise.

This speed maximizes the product of velocity and L over D, and flying here means that the most speed for the least penalty in fuel or energy efficiency is experienced, which essentially optimizes the return on investment for energy spent against time saved. And you'll notice the relationships between induced

and parasitic drag in each of these boxes.

To help, again, make this digestible, the condition for max endurance means that you need three times more induced drag than parasitic drag, which means slower flight at a higher angle of attack than you would fly at for max range.

So, theoretically, I want to fly at the max endurance speed right at the bottom of my power curve to get my maximum endurance requirement. But in my case, the speed for max endurance is practically my stall speed. This means that if the aircraft actually flies a speed with a strict adherence to the

drag polar assumptions, there will be basically zero margin for control or maneuvering. So, we want to fly this low maximum endurance speed, but we need to first make sure we can fly at all. So, I tossed the 20% stall margin requirements into my calcs. This basically just bumps the

target safe speed up to what is 39 ft/s here, which technically removes the iterative nature of the sheet to use the max endurance speed in the initial sizing calculation, but I accept the slight penalty in endurance for the ability to actually keep the UAV flying.

It's also worth noting that this isn't typically what these curves look like, but because I made the assumption that the minimum drag coefficient will be relatively high at .04, things changed a little bit in relation to another. This is what the typical clean fixed-wing curves look like.

Okay, so we got the airspeed that we need to loiter at, but we're still not done. Loitering really isn't flying in a straight line, it's flying in circles or patterns. And in my flight plan, I'm not going to be flying a mile-wide circle.

Plus, I want to put these formulas on your radar anyways, so I made a a really basic series of turning calculations to account for the circular loiter.

I've set a relatively arbitrary turn radius constraint of 200 ft because I don't want to go far. And to hold that radius at my new safe speed, I'll have to bank the aircraft.

Basic flight mechanics tells us that the bank angle phi is the arc tangent of the velocity squared over the radius times gravity. Here, that's about 13 and 1/2 degrees.

Here's the catch. Banking increases your load factor. At that 13 and 1/2 degrees, I'm pulling just barely more than 1 G.

It's really small, but it matters mainly for the sake of you learning it because stall speed scales with the square root of the load factor. So, here the stall speed rises from just under 33 to just over 33 ft per second.

Therefore, we have to update our safe speed again to maintain that 1.2 margin against the turning stall speed.

This pushes our final target speed up to roughly 40 ft per second. At this condition, we then re-enter the drag polar. We need a lift coefficient of 1.1 to support the aircraft in the turn, which generates a drag coefficient of 0.078.

This then gives us a turn efficiency or L/D of 14.3.

Finally, we plug this drag and velocity into the power equation and see that the airframe needs about 27 W of power to stay in the air.

Divide that by our propeller and motor efficiencies and we arrive at the number that actually matters for battery sizing, around 42 W of shaft power required. And this is the value that we'll plug into the battery mass fraction equation in a second. All right, to get back on track, we now need

to characterize the weight of our design point. First things first, we're calculating empty weight here. There are two main methods that we can employ here. Roskam classifies these as class one and class two. Class one is intended for rapid weight conversions for sanity checks, and class two is intended for

sensitivity and refinement. If both agree within 5 to 10%, then your conceptual weight estimate is probably acceptable.

Class one involves a statistical empty weight fraction estimation. This estimates the empty weight as a fraction of the gross takeoff weight using historical regressions again.

You use this during early conceptual sizing when geometry is not fixed and when you want quick weight convergence, which is usually more difficult for vehicles that burn fuel weight as they fly, therefore lapsing weight throughout the mission.

Class two, on the other hand, is an individual component weight build-up method estimating the empty weight by the sum of each component. The component weights are estimated using similar formulas derived from historical trends.

You can use class two after your configuration is defined and it's particularly useful when comparing specific design changes and considering details like control surface and landing gear weights. But for the sake of time and to get us moving, I'm just going to proceed with the empty weight fraction

approach. Since I've chosen electric propulsion, I can replace the fuel weight term here with a battery weight term. And since this is unmanned, I can also knock out the crew weight term.

This is where things get a little bit more challenging. We're designing a small UAV, so the conceptual empty weight fraction data for configurations like transport jets, turboprops, business jets, single engine propellers, and subsonic and supersonic fighters do not really apply here.

While Raymer provides specific equations for UAVs, they rely on historical trends that act as a conservative upper boundary, and this artificially inflates the empty weight by roughly 10% for aircraft under 300 kg, which can effectively kill a valid design.

I've selected an alternative method from a paper I found instead because it's derived from a modern market study of 250 actual UAVs, providing a regression that is tuned to the realistic lighter construction of modern drones in the specific class.

And now you're probably wondering, that's awesome, but what design weight do I use?

Well, my friend, this is where the fun begins. Remember a minute ago when I was discussing weight convergence?

It's time to talk about that.

Using the weight equation up top, payload weight is a gimme and is often fixed, and we discussed the concept of a weight fraction via the empty weight fraction, but it's also really useful to use a weight fraction for the fuel, or in our case, the battery weight.

For us to continue down the convergence calculation path, we need to figure out how to estimate the battery weight fraction needed to fly our mission.

This is the equation we need for our electrically driven endurance mission battery fraction sizing.

And if you want to learn more about what each of these terms means, go check out video one. There's a section for this.

When we consider electric aircraft, there's a notably different process for analysis over the course of the mission as there is no weight change due to the fuel burn.

To accommodate for this, the battery fraction can be calculated for both range and endurance missions using the following formulas.

To save time, I'm not going to go through the list of green inputs line by line, but most of these feed the battery fraction calculation.

The loiter speed is derived on the back end as we did earlier from the CL to the three halves over CD curve calculation.

And you can pause the video if you want to read all the others in the table.

So, knowing the battery weight fraction, calculating the battery weight given an initial design weight is simple. And using the same class one empty weight fraction estimation we reviewed a couple minutes ago, we can figure out the empty weight fraction and therefore the empty weight given the initial design weight

guess again.

Now that we know both the battery weight fraction and the empty weight fraction, we can use the equation at the top right to solve for the payload weight fraction.

This will be the max available payload weight for the vehicle under the assumptions we've put forth.

Now with a design weight guess value fixed, the empty weight and battery fractions get fixed to their own values that change with the design weight guess, and that leaves us with a payload weight. The payload weight is going to change as some complicated function of your design weight guess. So, an easy

way to ensure that our aircraft is only sized to lift what we need in payload and no extra is defining a convergence term, which I just call payload convergence error here.

And now I can sit guessing design weights for 5 minutes until I whittle down the design weight guess to result in the intended available payload weight making the convergence error 0% or because I don't want to do that every time I change the parameters in the drag polar or mission definition,

and unfortunately since I didn't script this in Python because I don't want to make all of you learn to code, I just scripted an Excel macro button that converges the design weight for you.

If you're keen, you'll have remembered that early in the video I explained that in sizing a design point is characterized by a thrust-to-weight ratio and a wing loading. And when a gross takeoff weight is defined, also the wing area and thrust.

These two parameters have been at play in many of the calculations we've already seen, just hidden in the background of the math.

Traditionally, to select a design point, you would perform an entire energy-based constraint analysis for the fuel-burning mission from takeoff roll to touchdown and braking.

Here, for an example, I've modified a basic constraint analysis diagram for a design project I worked a while ago.

All this is doing is ensuring that my thrust-to-weight is higher than the minimum thrust-to-weight required for mission phases like dashes, climbs, combats, and and it ensures that my wing loading is low enough to satisfy my landing and field length constraints, but high enough to perform those same

strenuous phases like climbs, accelerations, and combat.

On the top of these slides is an equation that is simply a form of energy balance, specifically equating the time rate of change of the aircraft's specific energy height to its specific excess power, which represents the net propulsive power per unit weight available for climbing or accelerating.

This fundamental relationship mathematically couples the aircraft's instantaneous ability to change altitude and velocity directly to the aircraft's installed engine thrust and aerodynamic drag forces acting upon the airframe.

For more information on this, Jack Mattingly's Aircraft Engine Design Book is a fantastic source.

Considering the takeoff phase first, I'll take a huge shortcut by assuming that the thrust at the takeoff is significantly greater than the drag from both the air and the ground because obviously my UAV has afterburners. No, I make this assumption so that you don't have to sit through the math with me.

So, by assuming that the drag forces are negligible, all the drag terms disappear, and since we're not climbing until we take off from the ground, the rate of change of height also goes to zero.

After a little bit of manipulation and substitution with distance, velocity, and time, we're left with this, which acts just like a line where Y is the thrust to weight and X is the wing loading.

And you want your design point in this feasible design space and this is going to get narrowed down as we continue.

Now that we've taken off, we need to climb to our cruising or loitering altitude.

For a constant speed climb phase, the loiter factor is still more or less one and the energy balance equation reduces to this.

And this form has three behaviors. It has a linear behavior with the wing loading, an inverse behavior with the wing loading, and a constant behavior with the wing loading.

So, this phase looks like this and you'll want your design point to lie in this new constrained feasible design space.

A constant speed constant altitude cruise phase is generally not very constraining.

We can assume a load factor of one, assume the flaps are up, and assume that we're not accelerating or climbing. That leaves us with this equation, which just looks like the climb only without the constant term of the altitude change effects. So, the only difference on the plot will be a constant shift vertically

and a slope change due to a new Q or dynamic pressure due to the cruise speed being different than the climb speed.

For a constant speed constant altitude loitering, we can consider a steady turn, so acceleration and altitude change go to zero and again, no flaps or anything.

The behavior here is essentially the same as for the cruise and climb, just with again, different speed and the effect of the load factor in the equation now. Again, not super constraining.

The last one we'll touch on for this conversation is the approach.

This phase is a little different because if you think about it, the descent and approach for landings is not at all a thrust or drag problem. It's inherently a lift problem.

Therefore, we don't use this long energy equation that we've been using, and instead, we simply use the definition of the lift force. This means that the approach phase appears as just a vertical line on the constraint diagram because it's determined by the landing speed requirement, which sets a fixed

maximum wing loading based on the aerodynamic capability or CL max, independent of the installed engine thrust.

The independence from the thrust-to-weight ratio means that the approach phase is, again, fundamentally a lift problem rather than a thrust-to-drag problem. And you're probably wondering why this leaves us with a super small feasible design space.

Yes, a wing loading of 2 lb per square foot is extremely low compared to other manned aircraft, but it's standard for small UAVs to ensure manageable landing speeds without sophisticated high-lift devices or long runways.

This low value is kind of expected because the stall speed is directly proportional to the square root of the wing loading. Therefore, a requirement for a slow, safe approach speed mathematically forces a maximum allowable wing loading to be very low.

So, now the question is, where do we select our design point? The goal of energy-based constraint analysis is often to find the smallest feasible aircraft.

Long story short, you usually want to select the point of highest reasonable wing loading and lowest thrust-to-weight ratio simply because you don't want more thrust than you need and a heavier engine than you need to meet the mission requirements. However, the regime that we're considering is for a small UAV.

For jets, which have constant thrust and variable weight, parasitic drag is the big enemy. Smaller wings mean less skin, which means less drag, and as fuel burns, the aircraft gets lighter, so naturally you want the highest wing loading possible.

For UAVs like this one that I've been laying out in the video, we have consistent weight, and these usually fly at low speeds where induced drag is the big enemy.

Induced drag is inversely proportional to the span squared, so a smaller wing means a smaller span means higher drag, and batteries do not get lighter throughout the flight.

Moral of the story is that for an endurance focused electric UAV, oversizing the wing by lowering the wing loading to gain span is often the smartest design choice, even if it adds skin friction because it drastically lowers the power required to fight the induced drag.

So, I select a thrust-to-weight ratio of 0.4 and a wing loading of 2 lb per square foot, which really isn't a wing loading as low as it could be, but I really don't want to be lugging around a huge wing when I go to fly.

Now, I should mention that there are actually a few methods to converge here.

On that same project that I changed around to show you here, you can see that I have three goal seeks. Again, I usually script these models on Python, which can easily loop through the three of these to optimize, but Excel isn't on that level, so I have three independent macros that can be called in any order

to converge on that optimized design point. Remember when you asked me, "Gabe, why are you talking thrust-to-weight? This isn't a jet." And I said, "You're absolutely right, and we'll get to that in a minute." Well, that minute has come. Since propeller and piston engine aircraft are usually

designed in terms of engine power rather than thrust, we need to convert the constraint diagram from thrust-to-weight into an installed power requirement by specifying a propulsive efficiency.

Again, jets produce roughly constant thrust across their speed range, so the thrust-to-weight ratio is a stable ratio to design with.

Propellers, on the other hand, do not produce constant thrust. They produce roughly constant power. Therefore, as a UAV like this speeds up, the available thrust drops significantly.

If we size the UAV based on a static thrust-to-weight ratio requirement, we might have a huge amount of excess thrust at takeoff, but might have not enough thrust to climb, to maneuver, or to cruise at high speeds because the thrust available has dropped off.

So, I'll use this conversion to turn my thrust-to-weight ratio to specific power or the power-to-weight ratio.

This also helps a lot when shopping for a brushless DC motor because when you're searching for a motor, you generally buy in ratings of power. Regardless of if you use a gas turbine engine, a piston engine, or a battery-propelled aircraft, wing loading still dictates stall speeds, turn radius, and gust response.

So, the x-axis of the constraint diagram will remain as wing loading.

We can also take this one step further and convert the y-axis into installed power.

This is particularly useful for specking a propulsion system. This tells me that for my specific power selection, I need a motor capable of delivering at least 200 W of shaft power.

But, remember, when searching for a motor, most motors specify input power, and we just determined the output shaft power we need. To account for this, I'll just use my initial motor efficiency assumption to calculate that I really should spec a 250 W motor for this UAV.

If you'll notice, this is still a lot of power compared to actually what's needed to cruise. Cruise and the modified loiter only require around 45 W of mechanical power for this wing loading.

So, the throttle setting will be relatively low for these phases, and I might need to revise the motor efficiency assumption once I understand where on the motor efficiency versus power curve I'm operating at for most of the loiter.

This would usually advise a specific power decrease, but I have maneuvering test plans for this aircraft and constraints not shown on the plot that I would still like to meet. And I need the max power available to still satisfy those minimums.

So far in the series, we've covered how to define a mission and requirements, as well as what a design point is. And we've walked through a high-level overview of conceptual sizing using tools like weight fractions and drag polars and constraint analysis to arrive at a sized aircraft, meaning that we

have a numerical prediction of the aircraft's performance and its capability to meet a specific mission.

We've answered how big, how heavy, and how powerful does this UAV need to be to fly the mission and meet the requirements.

In the next video, we'll act upon all of these as we synthesize the aircraft, constructing a physical configuration and answering what does it look like and how do the parts fit together?

Again, thanks for sticking around and I hope you've learned at least something today.

## 학습 힌트 (자동)

_태그가 없습니다. 설명·자막에서 키워드를 추출하세요._

## 메모

_이 영상에 대한 메모를 여기에 작성하세요._