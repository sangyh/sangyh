---
author: "Sangy Hanumasagar"
title: "Introduction to Deep Research"
draft: false
date: "2025-02-07"
description: "Notes from YouTube video analysis with speaker diarization"
tags: ["youtube", "transcript", "video-notes"]
categories: ["content-summary"]
series: []
aliases: []
cover:
  image: 
  caption:
---

## Video Information
- Source: https://www.youtube.com/watch\?time_continue\=173\&v\=jv-lpIsnLOo\&embeds_referring_euri\=https%3A%2F%2Fopenai.com%2F\&embeds_referring_origin\=https%3A%2F%2Fopenai.com
- Date Processed: 2025-02-07
- Audio File: Introduction-to-Deep-Research-jv-lpIsnLOo.mp3

## Summary

Summary:

The transcript involves a conversation between four speakers from OpenAI's research and product teams. They discuss various topics about their latest development, Deep Research, a model that performs multi-step research on the internet. Here are the main highlights:

1. Introduction to Deep Research: 

   - OpenAI believes models like Deep Research will help streamline processes and make workers more productive, transforming how knowledge work gets done. 
   
   - The Deep Research model differs from traditional models in that it takes a long time to come up with an answer, and usually, the more time it takes, the better the answer. A limitation of previous models is their inability to browse the internet, an issue that Deep Research addresses.

2. Features and Benefits of Deep Research:

   - Deep Research does multi-step research on the internet, discovering, synthesizing, and reasoning about the content it finds. This allows it to adapt its search approach based on new information uncovered. 
   
   - Deep Research may take longer (from five to thirty minutes) before coming back with an answer. Such autonomous, unsupervised task execution is what OpenAI envisions for future agents. 
   
   - The model can offer applications beyond knowledge work, such as shopping for specific items or formulating content for presentations. It can generate comprehensive and fully cited research papers, resembling the work of an expert in a field.

3. Demonstration of Deep Research:

   - Deep Research provides clarifying questions to ensure it has the correct requirements before embarking on the query. 
   
   - It then synthesizes the information and starts executing the research process. It conducts searches, browses web content (including images, tables, PDFs).
   
   - The model continually updates the tasks as it proceeds with the research, adopting a similar trajectory to how humans solve problems. 

4. Deep Research in Different Fields:

   - Deep Research finds application in various domains, such as product research, market research, and academic research in fields like physics, computer science, and biology. 

5. Performance and Evaluation:

   - Deep Research reaches new performance highs on multiple public and private benchmarks, demonstrating high competence on expert-level tasks and an ability to handle time-consuming challenges.
   
   - Its performance increases with more time and resources dedicated to conducting the research, and though it can hallucinate, it performs the best among models OpenAI has released.

6. Deep Research Rollout Plan:

   - Deep Research plans to launch in pro and is projected to roll out to plus, team, education, and enterprise.

Key Interactions and Discussions:

The speakers began with a basic explanation of Deep Research and its importance to OpenAI's mission. They then did a live demonstration that showcased the model's functionalities, such as clarifying questions and multi-step research on the internet. They also discussed its benefits for various use cases, including both professional and personal situations. The conversations emphasized the model's performance and achievements on different evaluation benchmarks.

## Full Transcript
(Timestamps and speaker identification included)

[Speaker 0 at 592.43s - 598.43s]
hi everyone my name is mark and i lead research at openai today i'm joined by issa and josh from our research team

[Speaker 1 at 598.43s - 598.59s]
and

[Speaker 0 at 598.59s - 602.54s]
also neil from our product team do you guys notice anything strange

[Speaker 1 at 603.24s - 604.54s]
yeah it looks a little different

[Speaker 0 at 605.08s - 793.42s]
well it's because we're here in tokyo so hello from tokyo everyone the reason we're here is later on we're going to do a special event with one of our close partners but this stream is about our next agentic offering i want to first talk about agents as they relate to openai so openai cares about agents because we believe that they're going to transform knowledge work we think that they're going to help enterprises streamline their processes make workers more productive but it'll also be really really important for consumers so last year we launched o one which was the first model in our o series of reasoning models these are models that differ from traditional models in that they think for a long time before they come up with an answer and usually the longer they think the better the answer that they come up with one of the limitations however of these models is that they don't have access to tools and one of the really core missing tools is the ability to browse the internet what this means is that a lot of the things that we use in everyday life are now not accessible to the model so we'd like to announce a next big step we are introducing a capability called deep research what is deep research deep research is a model that does multi step research on the internet and what it does is it discovers content it synthesizes content and it reasons about this this content adapting its plan as it uncovers more and more information so one important feature of deep research why we call it deep research instead of just research is that we've removed latency constraints from the model typically models return fairly quickly but deep research models they can take five sometimes even thirty minutes before they come back with an answer and we think this is a good thing not a bad thing we think it's important for our models to start doing autonomous tasks for much longer in an unsupervised way and this is core to our agi roadmap as well i think our ultimate aspiration is a model that can uncover and discover new knowledge for itself and the first step here is a model that can go and synthesize and understand the models sorry the information on the web what you get from deep research is a comprehensive fully cited research paper essentially something that an analyst or an expert in a field might produce to you now we've talked about usages for knowledge work but there are also many usages for other things that require extensive web browsing for instance oftentimes you may be searching for something very very specific right this also takes a lot of manual labor on the internet you know you might want a specific item that you're shopping for with all these constraints that are tailored for your personal use so it's also very good for that i've also personally used deep research for putting together content for slides that i've used in a presentation so it's very very good across the board across a variety of different use cases finally i'm happy to announce that deep research is launching in pro later today we're gonna soon roll it out to plus and team and then after that to education and enterprise to show you how deep research works we have neil

[Speaker 2 at 793.42s - 861.38s]
sure thanks mark so deep research is in chatchbt later today very excited to show you all how to use it deep research is accessible from a button right here in the beginning of shatchbt and from here you can immediately put in any query and it's gonna send it off to deep research i'm a pm at openai and one of the things that we like to think about is what new features and products should we build one of the things we've been tossing around is should we build a new language translation app and so this is something that i can ask deep research to go and research for me so i'm actually going to type in this query i want to learn a little bit more about all the different markets that i can go off and target so i'm asking deep research help me find ios and android adoption rates the percent of folks who want to learn another language and the change in mobile penetration over the past couple years and give me that difference between the top developed countries and developing countries and i also really want this information in a formatted report with some tables and a clear recommendation on what the best emerging opportunities are for jetbritt so this is a query that would have taken me hours to put together but with deep research i can just immediately kick it

[Speaker 1 at 862.34s - 864.65s]
off is this your actual side project in openai

[Speaker 2 at 864.65s - 1003.35s]
this is my side hustle when i'm not working on deep research so what you'll first see is that deep research comes back with a set of clarifying questions just like a pm just like a pm this is super important because if deep research is going on for five thirty minutes you really wanna get those requirements right and so there's a couple of questions that it's giving to us right now you know how do you want mobile penetration set up do you want overall adoption rates or specific categories so the percentage of folks beyond general interest or really engaged interest these are really good questions that you'd expect an analyst to want to ask you when you're giving them a really tough prompt and so it is really important that you can capture these upfront so i might answer something along the lines of you know i want to look at this as a you know give me penetration as a percentage of users and look at overall usage and then make your best assumptions on the rest you know the model is really good at taking information that's sometimes specified and a little bit more open ended and using that to go off on a mission and get all the information that you need so you can see right now deepresearch has taken all of that and synthesized it and started kicking off its own research process deep research is really good across a number of different knowledge work domains and so we've seen folks being able to use it for market research for different academic areas across physics computer science biology i have been using it myself to try to pm a little bit on the side and we are really hopeful that it will be useful for you too at work and so what you will see over here is deep research pops open a little sidebar and it shows you all the reasoning that it is doing so you can see right now it's identifying you know the top countries it's gathering information and it's starting its process of searching for different information so zooming in over here you've seen that deep research is searching for information opening pages reasoning about what it's seeing under the hood what's actually happening is that the model is conducting searches quite literally opening and browsing the pages and looking through all the different components including images tables pdfs and pulling out all of that information and using that to determine what it does next

[Speaker 1 at 1003.73s - 1010.79s]
and it's really cool here you can see it's using the information from onesearch to inform what it searches for in the next step yeah

[Speaker 2 at 1011.00s - 1021.49s]
super cool it's fun to just watch and follow it along sometimes alright cool well while we wait for this one i'll hand over to josh to show us a different way of how deep research can work

[Speaker 1 at 1021.49s - 1142.66s]
thanks yeah so we we've talked a lot about deep research for knowledge work and that's one of the use cases that we're really excited about for this but it's not just for doing your job better it's also useful for things that you might wanna do for fun or at home so one thing i really like to use deep research for is to do research on products that i might wanna buy especially for like larger purchases where like for me if i'm buying something expensive i often will like read every page about it on the internet and you know i wanna if there's like some review somewhere that's on the internet i wanna make sure that i've taken into consideration before i actually make the purchase so we're here in japan and i've heard the skiing is pretty good this time of year but we planned this trip a little bit last minute so i didn't actually bring my skis and i'm wondering if i can actually maybe just buy some skis and you know take a little bit of a ski vacation at the end of this so i want to buy some skis for for skiing in japan and i one thing i like to do also is specify how deep research can format the output so format this as a report with a nice table at the end and just like in neil's example this is gonna come back with some questions that i can choose to answer or not answer so i'll say advanced skier all mountain but powder sometimes i've heard that powder is pretty good here hopefully we'll get lucky fingers crossed this week i'm tall so need long skis long skis and let's do something more fun like maybe i guess it'd be really cool to have like a nice color palette so how about something with with a nice color palette and so i'll kick this off and just like anil's example deep research will go off and do a bunch of research on different websites and the internet and hopefully come back with some good recommendations so i'll hand it off to issa to explain how this all works under the hood

[Speaker 3 at 1142.80s - 1213.64s]
sounds good so deep research is powered by a fine tuned version of our soon to be released o three reasoning model and we trained it using end to end reinforcement learning on hard browsing and other reasoning tasks through that training the model learned to plan and execute a multistep traject trajectory reacting to real time information and backtracking when necessary the final model is able to browse over user uploaded files it's also able to use a python tool for calculations and for creating an images and plots and then it can also actually embed those plots in it in its final response it's also able to embed images from websites in its final response and when it cites its sources it actually cites specific sentences and passages the resulting model is able to complete tasks that would take humans many hours and that are quite complex and it also reaches new highs on a number of both public and private evaluations on humanity's last exam a recently released benchmark from the center for ai safety and scale ai which tests mod the model's capabilities across a range of expert subjects the deep research model reaches a new high of twenty six point six percent accuracy

[Speaker 0 at 1214.10s - 1218.20s]
that's super impressive yeah humanities last final exam too

[Speaker 3 at 1219.30s - 1286.55s]
the this test consists of around three thousand short answer and multiple choice questions across a range of around a hundred different subjects and it's actually really cool if you see the the trajectories and thinking process of the model because it's actually very similar to how a human would solve a problem so if i was given a really hard problem i'd probably do some online research to try and help me figure out the answer and we've seen examples for example in physics where the model has to answer some hard calculation it will look up an equation in an existing scientific paper and help that and use that for answering the question or in a poetry example the model had to identify a very niche poetic meter for a new poem and so we saw it looking up examples of other existing poems and trying to help that use that to help it reason through how to get to the answer on another benchmark gaia that measures models' agentic capability and requires web browsing multimodal capability code execution reasoning over files the model also reaches a new high on all three levels of difficulty

[Speaker 0 at 1287.01s - 1290.86s]
we've also put together some internal benchmarks that are pretty broad based can you talk about those

[Speaker 3 at 1290.86s - 1411.78s]
yeah for sure so we also put together some expert level internal evals and we have a range of tasks that experts would do in their in their jobs and we have the deep research model out to them and then have the experts rate the responses and the model was able to complete tasks that the experts said would have taken them hours and very you know a lot of manual investigation so we have two graphs to illustrate this so we have on the left pass rates for different estimated economic value ranges and then on the right we have pass rate for different ranges of number of hours to complete a task and what's in and pass rate is the rate at which the model provides a satisfactory answer to an expert level task as rated by that expert so what's interesting from these graphs is that pass rate is more correlated with estimated economic value than it is with estimated number of hours to complete the task which shows us that the things that the model finds difficult aren't necessarily the same things that humans find time consuming so this graph is pass rate on these expert level tasks against the maximum number of tool calls and what this shows us is that as the model is able to spend more time thinking and browsing the performance increases and this is really important because as you know mark described we're moving towards a world where agents are going to be able to take longer and longer and complete harder and harder tasks and so if we give them more time to think and more time to use these tools they should be able to solve harder tasks and then one final internal evaluation is a hallucination evaluation and this model actually performs the best on that eval of any model we've released however it's still possible that it will hallucinate so when you're making reports make sure to check the sources yourself yes and so as we mentioned the deep research model can take a really long time to respond so we generated some examples this morning to show you the range of different things it can do and so we can look through some of them now

[Speaker 2 at 1413.76s - 1417.12s]
nice super long very very long

[Speaker 1 at 1417.12s - 1419.22s]
we have to solve the scrolling through the top problem

[Speaker 3 at 1421.72s - 1457.81s]
okay so this is a finance problem so i'm an investment analyst in the silicon valley vc firm i want to analyze the market for civilian supersonic air travel and prepare a thorough investment memo and then many other specifications and so the model clarifies and we provided some additional requirements for the memo and then the model kicked off the task and as you can see it went and researched for seven minutes used twelve different sources and then came back to us with quite a comprehensive report of the field and you can imagine if you were doing this for your job this would be quite helpful to bootstrap your research as you're doing your initial investigation

[Speaker 1 at 1458.42s - 1463.99s]
yeah hopefully hopefully this works and next time we're we have to come to japan we'll be a little bit less jet lagged

[Speaker 3 at 1463.99s - 1464.63s]
with the

[Speaker 1 at 1464.63s - 1465.47s]
supersonic level

[Speaker 2 at 1465.67s - 1466.57s]
supercenter so

[Speaker 3 at 1468.55s - 1488.76s]
here's another example it's a biology example so we uploaded a paper and we want to find other papers on the same topic this was actually a task from one of our friends at openai who's very advanced in biology so i'm not going to pretend to understand exactly what this says but we wanted to show you the range

[Speaker 1 at 1488.84s - 1492.20s]
weren't paying attention to the hologram we knew it was smart

[Speaker 0 at 1492.20s - 1492.60s]
we wanted

[Speaker 1 at 1492.60s - 1492.84s]
to show you

[Speaker 3 at 1492.84s - 1514.46s]
the range of things it can do so i asked some clarifications we followed up and then this task the model took quite a long time and i was able to find a bunch of different papers that are on the same topic and when we showed this to our friend he said that it was pretty good response so it was a good vote of confidence for the model and then one final example

[Speaker 0 at 1515.08s - 1515.82s]
right here

[Speaker 3 at 1515.88s - 1567.71s]
okay so i'm sure everyone's had this moment where you can't remember the name of the restaurant that you went to in tokyo ten years ago or the name of the tv show that you're looking for and so this example might seem a bit contrived but that's we wanted to show how good the model is at finding this needle on a haystack pieces of information so the prompt is there's a tv show that i watched a while ago i forgot the name but i do remember what happened in one of the episodes can you help me find the name here is what i remember in one of the episodes two men play poker one folds after another tells them to bet and then a little bit more detail about the story and the only additional information we're able to provide was i think it was five to ten years ago but i'm not really sure and the model is able to do online research and figure out like through reading a bunch of different sites and reasoning about the contents of those sites the actual tv show episode that we're thinking of

[Speaker 1 at 1567.95s - 1568.60s]
wow which is

[Speaker 3 at 1568.60s - 1569.15s]
pretty cool is that

[Speaker 1 at 1569.15s - 1570.69s]
the right answer was that the one

[Speaker 3 at 1571.03s - 1579.35s]
that is a tv show so now i'll hand back to neil and josh to check-in on the task that you guys kicked off at the beginning

[Speaker 2 at 1579.35s - 1594.93s]
yeah absolutely thanks ysa so we'll take a look at the original task over here it actually looks like the task is still going on right now but in the meantime while we've kicked it off it's already looked at twenty nine different sources and gone through a lot of different information oh wow okay perfect great timing

[Speaker 1 at 1594.93s - 1595.76s]
great timing great

[Speaker 2 at 1596.45s - 1663.69s]
so deep research just put together its full analysis it took us eleven minutes and in that process it looked at twenty nine different sites really in-depth and as you can see live on this livestream it gave us a perfectly formatted report here you can see the mobile market analysis for mobile adoption and language learning we got a nice introduction our different adoption trends everything put together in a really great report style where you can see mobile penetration over time and a ton of different data and as you go down you can see it not only has information over here but also different table formats and ways that it's presented the the data in a way that's super digestible so one of the other things that's really cool about this model is that you're able to click in and see all the different sources that it's able to cite over here you can see every citation that the model's encountered and also different sites that it might have encountered that it didn't necessarily put into the final output but it wants to let you know that it found along the way yeah awesome well great let's check-in on the skis let's check-in on the skis alright

[Speaker 1 at 1665.38s - 1731.78s]
so scrolling up here what i like about this is wow this did a lot of research this is the kind of thing that i would probably like have to spend all afternoon just you know you know for for my own sanity to make a good purchase to read every single thing that's written about it but this does a pretty good job of actually just doing like hitting all the sites that i would hit and consolidating this all in format that's a lot easier to digest than you know doing my own searches and it also provides a table at the bottom here that just gives kind of like the high level comparison across the specific things that i i mentioned that i wanted for for this purchase we i find that deep research works really well if you're like very very specific about the the type of answer that you're looking for both in terms of what information that you want what comparisons you wanna see and and anything about the format that you want the final output in because the model is able to take all of those things into consideration and and and think about them all as it does its searches and puts together its final report so this sort of passes the sniff test for me because the top recommendation here is actually the skis that i own at home which is kind of cool

[Speaker 2 at 1731.78s - 1732.13s]
oh so

[Speaker 1 at 1732.22s - 1738.19s]
i love that i'll i'll take a closer look at this and and maybe maybe plan a little bit of a ski trip after this

[Speaker 2 at 1738.19s - 1740.27s]
alright let's go this weekend

[Speaker 1 at 1740.27s - 1746.43s]
yeah so yeah as you can imagine there's a lot more that we can do with this technology so i'll hand it back over to mark to talk through

[Speaker 0 at 1746.43s - 1793.38s]
where we're going with this awesome yeah just to recap deep research is available later today on pro and we're soon gonna bring it to desktop and mobile but again what we're launching today is just scratching the surface of what you can imagine us doing with deep research today we have a deep research agent that browses the web but you can imagine that same deep research agent connecting to custom contexts right or really just kind of enterprise storages of data again deep research is important to our agi road map we believe in agents that think longer and longer more autonomously to solve very difficult tasks and we believe that this you know the ability to work on a task for thirty minutes really does motivate a lot more compute investment so we're excited to see what you guys do and please share with us thank you so much
