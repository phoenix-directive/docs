# Proposal: Fibonacci Algorithm in Triplet State (FATS)

- **Thread ID:** 5345
- **Author:** Daniel Mark Harrison (`terra1tnwelfh3e79mv7my9n5f2vx0yuv8gyqu5k2h58`)
- **Created:** 2022-06-08T07:01:15.883Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 4814
- **Reactions:** 9
- **Comments:** 25
- **Source:** https://common.xyz/terra/discussion/5345-proposal-fibonacci-algorithm-in-triplet-state-fats

---

By Daniel Mark Harrison (danielmarkharrison@gmail.com)

**Summary**
The critical error in Do Kwon’s algorithm has less to do with the logic found in mathematics and economics as it does in a rather more theoretical field – quantum physics. Particles in quantum theory move across singlet or triplet states. In singlet form. particles are at 0 (although in reality a little above that) wherein two particles are paired, with one in a grounded state and the other in an excited state or separated, with both particles in an excited or grounded state. Do Kwon’s algorithm operated much the same as a singlet particle beam, with each particle necessarily bound to the other until separated entirely. In triplet states, particles have an alternate option wherein there can be two particles that are paired aside a third separate particle. By configuring an algorithm that conforms to these inherently more stable laws of quantum physics by utilizing a mint/burn particle pairing / separating mechanism on a Fibonacci algorithm and then allowing each coin to mint a third stablecoin priced along the same regressive Fibonacci market making system, I show how in fact both LUNA and USTC have a certain chance of being restored to their former values by cooperating as payments for a stablecoin backed by those and two other Blockchain coins on the Cosmos chain, ATOM and LUNA, to offer investors the most assured recovery of their value.


**Motivation**

This algorithm may sit on top of or in place of the original minting / burn algo and employs some regressive Fibonacci and simple equations to achieve stable distribution, minimal supply interruption / readjustments  to get a proper, strong coin price going again. In addition, I include the new LUNA and ATOM from the Cosmos chain in this proposed backed stablecoin for the sake of inclusiveness and enhanced stability.  In particular, readers are encouraged to note that in April this algorithm would have begun to burn LUNC at a rate of $0.23 per dollar of LUNC sent and that only four nights before the crash,  when LUNC lost its peg, specifically this algo shows how by putting a halt to minting and burning this collapse would have been easily avoided by employing this algo.  

**Proposal**

**Overview**
LUNC supply starts at 7T while USTC supply starts at 11.75B. This is an supply ratio (s) of 1.67, consistent with _f_. The algorithm uses Fibonacci regressive division equations along with a price/supply reduction (r) and price/supply magnifier (m) formula to calculate the most appropriate mint and burn for LUNC and USTC. 

If (s) is <1.67 then LUNC has a burn feature enabled; if >1.67 then USTC has a burn feature enabled _unless_ (r) or (m) are outside the 0.01-1.67 range, in which case there is no burn/mint applied. No two coins can simultaneously mint or burn; while one coin is burning, the other is minting. Note that price and supply is calculated in USD at all times and the system must resolve the token mint/burn quantities therefore with an Oracle. Objectively, the aim is that over time, the formulae help to harmonize and stabilize the supply adjustments of both currencies so that price performance is more consistent and predictable and that the ultimate utility of the coins as minting agents for UST is optimally expressed. 

_**Minting & Burning **_
(r) is expressed to the following formula (note: wherein the price of LUNC > price of USDT reverse the division in the AR – this is so that the burn always takes precedent over any mint in terms of top-heavy dominance, affording the user the greatest possible economy and value):

LUNC Price / USTC Price = x 
LUNC Supply / USTC Supply = y 
x/y = z 
xy = -z

wherein z is then used to denote the closest Fibonacci number which determines the rate at which USDT is minting per y which is the rate at which LUNC is burning with both confined to a fib range 0.01-1.67.  The Fibonacci formulae utilize the following display (wherein each Fibonacci is regressed across each of the ten first Fibonacci series numbers.

_**Example 1 – Burn & Mint **_
_Wed 8 June 2022_

x: 0.00006716/0.014 = 0.044
y: 434M/142M = 3.05
z: 0.044/3.05 = 0.0144 
z-: 0.044*3.05 = 0.1342

z is closest to 0.0123, so we calculate for a triplet at S#89: f1+f2+f3-f4+f5+f6-f7-f8+f9 to get 0.2427. This is the burn ratio. The mint ratio (z-) is then subtracted from the burn ratio to get 0.2427-0.1342 = 0.1130. So for every dollar of LUNC sent, $0.2427 is currently burnt while the sender is minted $0.1130 of USTC which is sent to the same wallet as the LUNC was sent from. 

_**Example 2 – Mint, No Burn**_
_Apr 25 2022_
When the price of LUNC is _> USTC _then (z) is reversed in order to produce a reliable burn. In this instance, there is an exact marker for (z) which is 0.18 so this can be used as is. There is no mint available for USTC due to the occurrence of a result that lies outside the 0.01-1.67 parameter, so each time a user sends $1 of LUNC $0.18 of LUNC is burnt without any USTC mint. 

x: 97.04/1 = 97.04  
y: 31,306,895,100/18,274,150,903 = 1.71
z: 1.71/97.04 = 0.018 
z-: 1.71*97.04 = _e_ = 1.67 (no mint)

We can see here how an oversupply of either cryptocurrency could clearly have been prevented while USTC rose in price and LUNC’S contracting supply combined with the rising USTC price brought both coins closer together in equilibrium price/supply.

_**Example 3 – No Mint, No Burn**_
May 11, 2022

x: 17.45/0.7994 = 21.82
y: 1,571,559,885/10,718,072,199 = 0.147
z: 0.147/21.82 = 0.006 (no burn)
z-: 0.147/21.82 = 3.2 (no mint)

Notably, the algorithm stops burning and minting completely just before the crash of the LUNC price in mid-May as a result of both the burn and mint results lying outside the 0.01-1.67 parameters. What this would have effectively done is to de-couple the two coins LUNC and USTC several days before massive funds were wasted trying to buy the coins off the market and before the team ultimately relented and manually decoupled the two coins. Once again, the algorithm proves superior as a predictor of the likely course of events and takes action in advance of the worst of the problems – note that at this point, USTC was still worth $0.8, a position which was halved two days in a row consecutively after the market sell-off as a result of continued binding of the two coins. 

**Stablecoin – UST **
I suggest a coin which is in the form of a smart contract that issues (mints) new UST at the price of $1.01 payable in: LUNC, LUNA, USTC and ATOM, and which repurchases tokens on an equalized basis, handing back a proportionate and equivalent share of all coins held in the UST smart contract for the percentage of UST sent back the contract. Once sent back to the smart contract UST are burnt. The discrepancy between locked value – especially as LUNC and USTC begin to rise aggressively as a result of the newly-configured algorithm outlined here and as a result of being held continually inside the UST contract for the most part – will attract arbitrage traders in large quantities. The stablecoin will be sold according to the price of the coins that are used to mint UST and will be sold across the same Fibonacci algorithm inclusive throughout S1-10*f1-f9 as depicted above.

_**Example 4**_
Terry sends 100 LUNC to UST when LUNC is worth $0.01 and receives 99 coins (inclusive of the spread) while Sarah sends 100 ATOM to the smart contract when Cosmos is $5 each and receives 495 USTC. Now LUNC rises 900% over the course of a few days, making Terry’s investment worth a total of $1000. Sarah then sends 300 UST back to the contract and receives $552, with a balance of a further 200 UST priced at a locked value of approximately $0.3 per UST.

---

## Comments (25)

**Levathar (`terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd`)** — 2022-06-08T07:42:08.348Z — 👍 3

Mr. Daniel, I have read messages of yours and its mind blowing the detail you can place in your ideas. Keep in mind that as much as I am reading this, so the masterminds of the attack to Luna/ust are too. Necessary to perform the necessary adjustments and implement fail safe mechanisms to prevent further exploits. It requires a lot of math and thought experiment... but this trully excites me.

Most of us would fail to follow through but surely other scientists and experts can verify and confirm your proposal, eventually help build up the best model for the LunaC/USTC recovery. Kudos to you, Sir!

**Rob.Stat (`terra1fr4yucxw2lupt03z6aajuxd5das53pr25a24cc`)** — 2022-06-08T08:27:58.985Z (edited 2023-06-23T13:24:39.135Z)

.

> **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T09:31:55.597Z — 👍 2
> 
> I have a master’s in computational physical chemistry and, not trying to be rude or anything, but this person doesn't know what they are talking about... For starters, that is not even a proper explanation of a triplet. A triplet is **two** unpaired electrons, it gets the name triplet because it has a spin quantum number of 1 and produces 2(s) + 1 = 3 spectral lines (and this is an intro p-chem level class topic). Also, particles don't move back and forth across singlet and triplet states. The transition from singlet to triplet requires a change in multiplicity and is so highly improbable it is considered a forbidden transition. 
> 
> Not even going to comment on the math - I think I've made my point enough to invalidate the thesis here. What happened with LunaC is not explainable nor fixable via theory of quantum mechanics.

> > **Terrakin (`terra18flrllx2nu5wwaf3stcjhs85wpzkatnae5nxcy`)** — 2022-06-08T09:44:06.719Z — 👍 1
> > 
> > Thanks, was hoping that someone can confirm/reject this thesis.

> > **Levathar (`terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd`)** — 2022-06-08T10:27:12.050Z
> > 
> > Hi there. Thank you for your input. The brain power amassed by these questions are impressive. 
> > The positive outlook of the discussion is that you smart guys can discuss and improve current solutions.
> > As I said above, words and energy of the community is not enough to drive this.
> > We need know how. And fast, before they ditch Classic.

> > **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T10:43:45.158Z (edited 2022-06-08T10:51:44.946Z)
> > 
> > [@Levathar](/terra/account/terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd) - I think you may be missing the point I was making.. this post didn't require much brain power.. it is either a shit post or a seriously confused person..

> > **UncleSam (`terra14kca7s7vh4wyn94n5u0t2q5gt76q8gydzjzce3`)** — 2022-06-08T11:39:02.057Z (edited 2022-06-08T11:40:48.560Z)
> > 
> > Mrs. Lurker, could you please provide us with some proof that you have "master’s in computational physical chemistry" ? If you put it that way, you know your business and say that about others. because a lot of people want their money back, a lot of people have committed suicide. A lot of people believe you can change that.

> > **Daniel Mark Harrison (`terra1tnwelfh3e79mv7my9n5f2vx0yuv8gyqu5k2h58`)** — 2022-06-08T12:17:12.299Z — 👍 5
> > 
> > HI there - thanks for reading the proposal! You are of course completely right that the technical term is doublet for one paired and one unpaired, singlet for paired and triplet for 2 unpaired particles (they don't just have to be electrons btw ... any particles with calculable spin moving in some sort of Brownian motion will suffice) . I am used to reading papers where singlets vs. multuplets are the norm in expression and sorry for being a bit lazy on the syntax there.  (Also on the forbidden transition I was naturally thinking of Oxygen as the logical object of the sentence, but it doesn't just have to be O2 - there actually are a whole variety of other particles can go from singlet to triplet state without dramatic events happening. O2 seemed more intuitive for example than say, Carbene as an example at least - even then the transition wasn't the subject of the point but thanks again for raising it with respect to some  chemicals where indeed probability is low of transition - although not as low as imagined in most cases, and certainly fine with O2).  I actually meant to go more in depth and get into this point so I am so happy you raised it as its the point of the Intro. 
> > 
> > I am not quite sure you understood why I made the analogy and I thank you for bringing this up so I can better explain it :) I find it very reasonable to use the spin analogy given the huge number of finance papers based on this as a starting point to Brownian equations and Merkle Tree probability spectrums of particles vs say, stock price movements, so I was borrowing in a way from classic econ here. A spin is only a hypothetical anyway, and is not an actual physical event per se - just our best theoretical explanation of what's going on so in this way it is academically warranted I think here (and in many other finance papers). So when Do Kwon made his algo and I say he made it in a singlet state architecture what I mean is that the two coins he made were paired. They have no ability to be represented in his model whatsoever as either paired and unpaired (as in doublet state) or as two unpaired assets - I mean LUNC and USTC here naturally. They are always united and in this it is very clear that his algorithm failed on a number of assumptions, but chiefly, that while he was counting supply of USTC and its burn offset to LUNC in units, he was counting the price of LUNC in USD. What happened therefore was when the LUNC lost its peg, and entered about $0.80, all hell broke loose, as the algo was programmed to assume the singlet state of the USTC coin was as such characteristically one of one USD when this was not true - the singlet state of USTC was in fact just that it had a burn impact on another token called LUNC. This unalienable binding indeed meant that Kwon Do transgressed many a rule of chemistry and physics for scientists and ended up splitting the two by depegging out of necessity because of the severe loss to his investors. This indeed in an investment context did transgress a line for many, and they are still upset about that fundamental violation of their financial product. So Kwon Do was the chemist who basically spit the two particles in singlet state  into an unpaired  triplet state which - just as for many investors here with the depegging - you are naturally angry about as it violates what is assumed to be an expected rule (except for cases like O2.)
> > 
> > Now, imagine that both those coins, having a more structured and forecast binding system in the form of a regressive fibonacci equation with transparent and consistently automated rules, could then be represented in the state of minting a new crypto that sold for a dollar each and then sitting in the wallet of that cryptocurrencies' public address until it was claimed back at a higher value (more excited state) later? Would this not achieve what physics professors call a more "stable" state / environment, due to the potential for the paired / unpaired coins as in our world today indeed, where oxygen doesn't spontaneously combust like Kwon Do's model? Indeed it does, and this was the point. The hypothetical physics would then appear to conceptually represent the mathematical equations inherent within the proposed algorithm and also fittingly describe what is a stable environment, like planet Earth, because (but I may be wrong in some cases, I don't know) I had assumed LUNA investors were tired of the unstable atmosphere up there in Jupiter for now and looking for a solution? I hope this has adequately addressed your concerns, and thank you again for your detailed attention to my proposal.

> > **Iminadaze (`terra1eauq4phzlqqpcc9eh6hl56nd4ws80r7jpcmh2y`)** — 2022-06-08T12:33:02.896Z — 👍 1
> > 
> > I don't care if what happened to UST/Luna can be explained through quantum mechanics or not. What matters here is if a proposal such as this would solve the issue that caused the failure. Perhaps it will, perhaps it won't. The introduction of this proposal here shows that someone is trying to tackle the underlying issue rather than putting up another burn proposal that does nothing to solve the problem of making UST/Luna stable again. I see this proposal as a possible solution or at least a step in the right direction.

> > **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T14:45:04.568Z
> > 
> > [@UncleSam](/terra/account/terra14kca7s7vh4wyn94n5u0t2q5gt76q8gydzjzce3) Mrs.? lol.

**Tuna Money (`terra1auydap0uk2ystpvdnzklvj66wpq5zkcy9jzkly`)** — 2022-06-08T10:04:21.970Z — 👍 1

had a hunch it was serious shit talking.  thanks.

**Levathar (`terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd`)** — 2022-06-08T13:01:13.825Z — 👍 4

I am a mechanical engineer so I am familiar with systems theory, and stability / resonance. 
I think a mathematical model should be built using the code and rigged with the stability proposal by Mr. Daniel above.
Maybe e can configure a testnet where we could throw all the cases towards it and see how it would absorb the inputs.
After all, is the oucome that we want to control, by managing the relashionship of the inputs and the variables.

Create the model ---> Get a server ---> create the network ---> make it run

**lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T13:43:57.314Z (edited 2022-06-08T14:23:18.823Z) — 👍 3

[@Daniel Mark Harrison](/terra/account/terra1tnwelfh3e79mv7my9n5f2vx0yuv8gyqu5k2h58) 

> thanks for reading the proposal! You are of course completely right that the technical term is doublet for one paired and one unpaired, singlet for paired and triplet for 2 unpaired particles (they don't just have to be electrons btw ... any particles with calculable spin moving in some sort of Brownian motion will suffice)

Brownian motion does not have anything to do with electron transition theory.. Brownian motion is really specific to gases and liquids & it describes random motion of particles.. not their electronic spin. The triplet/doublet/singlet states you are describing are primarily relevant for spectroscopy and understanding vibrational relaxation, density of states, spin decoherence, etc. Brownian motion is also classical mechanics not quantum mechanics - those are like different worlds because Einstein wasn't a quantum fan. 

I do understand a bit better where you were going with the analogy though.. electron decoupling.. trading pair decoupling. Its a bit obscure, but I can see it.. though the extent of the analogy kind of ends there.. i.e. there are no equations or lessons from electron transition theory that would be applicable to solving this problem... and you weren't really proposing to use any of those anyways so to describe this proposal with a meme - I would go: [https://knowyourmeme.com/memes/pepe-silvia](https://knowyourmeme.com/memes/pepe-silvia)  & recommend simplifying it a little bit to remove the quasi-quantum-economic abstraction layer? 

> Finance papers based on this as a starting point to Brownian equations and Merkle Tree probability spectrums of particles vs say, stock price movements

Brownian motion is based on a general stochastic algorithm-  it is just a probability distribution curve with a time interval (grossly simplifying this for brevity). That does not necessarily mean that physics relates to finance.. its more that statistics is always statistics. 

You sound like you are some type of scientist maybe & I am definitely not trying to be dismissive here, but just want to be contentious around the fact that people in here lost life savings because of a failed theoretical model and extrapolating quantum theory outside its realm of application and doing so improperly is not going to be a solution for anyone.  & I apologize for assuming you were shit posting before... just trying to contribute what I can on this forum and help weed out potential spam posts and when I saw inaccurate science in the first few sentences - I flagged it. 

I don't really understand your application of Fibonacci here either. If you can write a simulation for it though I would definitely offer to peer review it.

> **Anonymous (`terra12l7n9fq5jz9dmxzxay2297uassm7v924dt6jcn`)** — 2022-06-08T13:57:47.990Z
> 
> Your college degree doesn't count here when you are trying to spam with negative manners, there is someone who has put all their thoughts to save the UST community.   And that was the low bar,  you setup by flagging. 
> 
> You have nothing just to backup with civilize manner. But does flagging someone, will that solve the problem here? If you think he is wrong, prove it the way you learned from the college you earned the master degree. 
> 
> Or ask him to debate with examples to solve there is problems in this. So we can move forward with this proposal and why it cannot/can be done.

> > **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T14:37:17.637Z (edited 2022-06-08T14:46:18.074Z)
> > 
> > See below - I have been fighting for the UST community pre-terra 2.0 launch. I posted the proposal I wrote in the old governance channel on May 13th. 
> > 
> > Also, it is not a low bar to flag a post for factual inaccuracies. Me doing so is pointing out that the author may not be credible. Would you have preferred I not stated anything at all?
> > 
> > >  If you think he is wrong, prove it the way you learned from the college you earned the master degree.
> > 
> > I believe the responsibility is on the author to prove that he is right rather than me to prove that he is wrong.

> **Daniel Mark Harrison (`terra1tnwelfh3e79mv7my9n5f2vx0yuv8gyqu5k2h58`)** — 2022-06-09T07:14:06.306Z
> 
> First of all let me state that it was my true intended purpose to help here and salvage the LUNC and USTC coins. Having reviewed your analysis however and having questioned overnight (always good to go to bed first!) my insufficient knowledge on stochastic equations I have to admit that you have a point. Thank you for saving this community from unnecessary heartbreak before it was too late. You did a good thing, and I thank you from the bottom of my heart. I will now formally withdraw the proposal so that it is not for consideration. God Bless, Daniel.

**lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T14:06:36.905Z (edited 2022-06-08T14:42:35.523Z) [deleted]

_[deleted]_

> **Anonymous (`terra12l7n9fq5jz9dmxzxay2297uassm7v924dt6jcn`)** — 2022-06-08T14:27:20.300Z
> 
> why do you wanna hijack someone's proposal with yours, how about you create your own and get on with it... if you know how it works here... if you have been long enough. I would say, you are making another bad move.

> > **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T14:41:01.448Z (edited 2022-06-08T14:43:23.427Z) — 👍 1
> > 
> > My proposal is dated and was written pre-terra 2.0 launch. The only reason I posted it was to provide credence that I have actually be in these forums proposing solutions as well, but I have removed it as I don't want it to be interpreted as me trying to hijack this one.. and I would state your negative manners comment above is quite hypocritical given your responses here. We are all working towards the same goal. Open discussion and critique is important in achieving that.

**Levathar (`terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd`)** — 2022-06-08T15:33:42.234Z — 👍 2

Lets continue a sane discussion here, I can feel the emotions lurking but we need to be rational when others are not. Only by brainstorming we will succeed. 
I would very much would like to taste the math - it has been a while since I dwelled with system models - but I cannot stop feeling atracted to it.
As solid we can build here, the stronger the result will be. 
After all, we need to send a message out there, while the fire is spread out (prices keep falling every day) that everything we are fighting for have a bright future.
A true scientific white paper to back this up would be probably our best shot.

**Anonymous (`terra12l7n9fq5jz9dmxzxay2297uassm7v924dt6jcn`)** — 2022-06-08T16:19:04.561Z

[@lurker_dev](/terra/account/terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky)  your outdated one doesn't work, that's why it became outdated remember. You were not adding any contribution at all here. Better take it somewhere... Let other people with skills come to discuss this math issue. You have no valid for open discussion let alone proof to debate with OP.

> **lurker_dev (`terra19f3cn5r2ef0h6drfg9xhjcp9cge3fvrwj9x6ky`)** — 2022-06-08T18:39:27.951Z
> 
> > no valid for open discussion let alone proof to debate with OP.
> 
> meanwhile OP: 
> 
> > HI there - You are of course completely right that the technical term is doublet for one paired and one unpaired, singlet for paired and triplet for 2 unpaired particles
> 
> lol... no proof to debate, but yet I was right 🤔. 
> 
> Also, not sure what your deal is - but if you want a solution, maybe don't tell people with math backgrounds that they should let other people with skills come to discuss the math issue...?

**blackCoffeeBrewer94 (`terra18ccajzy6897vnmgdnywdrm0w2ks25rcpukp3pw`)** — 2022-06-08T17:56:07.409Z — 👍 2

I appreciate the attempt to offer analogies to other disciplines and the attempt to apply mathematic principles to bring stability back to USTC and LUNC. One interesting takeaway here IMHO is this statement: "I suggest a coin which is in the form of a smart contract that issues (mints) new UST at the price of $1.01 payable in: LUNC, LUNA, USTC and ATOM," I am glad that lurker_dev was able to offer some constructive criticism on this and that we might have a chance at making things work again.

**Levathar (`terra1eyxaxae55jkqcrke5yyp9ma3rvm5wgegkx72zd`)** — 2022-06-09T14:25:31.190Z — 👍 1

The  onversation stopped. Why?

> **Daniel Mark Harrison (`terra1tnwelfh3e79mv7my9n5f2vx0yuv8gyqu5k2h58`)** — 2022-06-11T11:32:32.247Z
> 
> No, but it needs shifting now. Forget the math and the physics, we will do that after we get the basics right first. I jumped the gun and I am glad someone here was kind enough to point it out to me (plus how bad at science I am - I am a B student at best in that!)

