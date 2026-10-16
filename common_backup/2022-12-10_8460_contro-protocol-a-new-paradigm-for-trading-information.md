# Contro Protocol | A new paradigm for trading information

- **Thread ID:** 8460
- **Author:** Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)
- **Created:** 2022-12-10T09:56:47.009Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 2588
- **Reactions:** 0
- **Comments:** 10
- **Source:** https://common.xyz/terra/discussion/8460-contro-protocol-a-new-paradigm-for-trading-information

---

# _Enter the Controverse_
  
 
# Summary
 
This grant proposal requests funding to build out a novel decentralized exchange (DEX) **protocol on Terra that enables efficient, scalable and fully decentralized prediction and derivative markets** for the first time. This is made possible by an innovative idea for matching parties taking opposing positions through time that has crucial advantages over both automated market makers and order books. 
 

The protocol will create **new opportunities** for users and thereby **acquire a large number of new users**, from degens and risk managers to political activists and whistleblowers, unlocking a new playing field for decentralized finance and betting linked to our vision: a world in which being honest, wise and speaking up is rewarded, ultimately supporting transparent and intelligent governance by providing the most trustworthy and unbiased source of aggregated collective knowledge.
 

Our minimum viable product (MVP) is a financial product offering binary options and futures on crypto prices. We will make these derivatives **easy to trade for the broadest market**: users only need to communicate their belief in a single transaction – the protocol does the rest.
 

For example, for what will be offered for MVP, such a belief might read as “_BTC price will be_ 
- [Future]: _between 16,500 and 18,500_
- [Binary Option]: _higher than 17,000 –with 70% to 90% probability–_

_USD by the end of next week"_ for futures/options, respectively.

**The protocol then automates buying low and selling high** throughout the week for both SHORT and LONG leveraged exposure on BTC price / for both the TRUE and FALSE binary options, respectively, and depending on the market price moving in and out of price ranges / probability bands. 
 

Shortly after the MVP we will roll out **perpetual futures**. In the longer term (but still 2023), by creating the “Controverse”, we will finally turn to **general prediction markets** and enable everybody to take positions based on their convictions on real-world topics and to share insights publicly.
 

We expect **substantial fee revenue** beginning in 2023 to self-fund future operations and scaling. 10% of the total revenue **will be funded back to the community pool – indefinitely**. 
 
 
 
# Introduction
 
Terra has been the home of highly innovative decentralized applications (dApps) since inception. Lately we are observing lower on-chain activity at best on par with the bear market downturn. 
 

While many teams are currently building for the next generation of dApps on Terra, particular importance should be assigned to a set of “killer apps” that provide major innovation across all blockchains. We are confident that we can deliver such an app.
 

We have developed a novel method for matching traders holding one of two opposing views such as “short” vs “long”, “yes” vs “no”, or “A” vs “B”. Our markets turn out to be more convenient and fairer for retail users as they put the importance on being right and not on being fast, and require fewer transactions, than using order books. They are also more capital efficient and more sustainable than automated market makers (AMMs).
 

Our idea is well-suited for a particularly challenging and interesting type of market: prediction markets of the binary option kind. In such markets users can bet on one of two mutually exclusive future outcomes, say “Biden” or “Trump” win the US presidential election, and earn large returns if they are correct.
 

Furthermore, our idea also fits for _continuous_ prediction markets with two opposing sides: shorts and longs of a "future" derivative (including perpetual futures). This can be achieved with the same protocol with some additional mappings. Instead of probabilities, one predicts prices.
 

Contro Protocol’s focus is on providing a safe, easy, transparent and powerful tool for retail users. Among the many advantages for users over previous protocols are: self-adjusting and limitless liquidity, low required transaction numbers, impossibility of frontrunning, automatic trading strategies (computed and executed by the smart contract) and extremely low required fees. Furthermore, due to the direct user matching, there is no need for liquidity mining and zero risk for protocol default or exploitation.
Some technical details are included in the below sections and in particular in the Appendix. 
 
 
 
# How will the Controverse benefit the Terra ecosystem and its users?
 
For users, the new markets and fair opportunities unlocked by the Contro Protocol are of great utility. The audience for general prediction markets is massive and the market even just for typical derivatives such as perps is huge: A simple estimate (see Appendix) **gives expected revenue of 7-8 digits per year just from perps**. **Significant TVL and liquidity** can be expected from a smooth on-chain perp trading experience competing with dYdX, GMX, etc. alone. However, binary options that allow for immediate returns of multiple 100%, offered at scale and with automated on-chain trading strategies, as well as allowing for endless new markets connected to the real world that do not need external liquidity, are arguably even more exciting.
 

For investors wishing the best for Luna’s price action, **releasing a new type of market that supersedes AMMs and order books for derivative assets for the first time on Terra mainnet** is a move that showcases the innovation strength of the Terra ecosystem. This is going to **increase visibility of Terra as a platform for innovation** and intellectual rigor, and is likely going to **attract more engineering talent to build on Terra** as a consequence, creating positive network effects.
 

The long-term vision of generalized prediction markets is not a pure DeFi product, but one that appeals to a **much larger, not necessarily crypto-native, audience**. To succeed with this vision, additional tech will have to be built to ease the onboarding experience, which will then be available on Terra. **Millions of people who are not interested in finance in particular but rather in what is happening in the world more generally** will be invited to participate. To make this happen, we envision and will push for integration with social apps.
 

Finally, by supporting the funding of Contro Protocol, you support solving the long-standing problem of realizing scalable prediction markets robustly with a completely new approach. This helps **strengthen the web3 narrative in general**: Prediction markets that will work well are necessarily going to **find lots of media interest** and exposure (c.f. the bestseller “The signal and the noise” by Nate Silver, or “futarchy” being the NYT buzzword of 2008). This is because they are a tool for stability and governance, namely a method to crowdsource probabilities which can on the one hand be used for hedging and insurance, on the other hand to guide decision-makers.
 

 
# The Protocol in Practice 
## TL;DR
1. Users express their opinion of future prices, or current chances of events, into a “position book” & stake collateral. 
1. This records the levels at which each user currently wants to go long/short, or bet on A/B, for futures and binary options, respectively.
1. From the position book, the smart contract can work out the market prices which determine who are the “active” users at any moment.
1. For active users, bets are **stream-filled** over time at the current market prices. The collateral slowly decays into the appropriate derivative assets.
1. The current market prices can be interpreted as probabilities (binary options) or price predictions (futures).
## Illustration of user experience
_A reader short on time might want to skip this section_


The following detailed example is for a BTC **future** maturing in one week, which is one of the products available for the MVP. We comment on the **binary option** below.
 

A user, Jane, thinks that BTC will be priced somewhere in between 19k and 21k in one week. This implies that Jane is happy to go 
- 🔼 LONG BTC future price for any price under 19k
- ⬇️ SHORT for any price above 21k.

Furthermore, Jane would rather not trade while the market already prices “BTC in a week” in the gap between 19k - 21k. 

If Jane manages to get either SHORT, or LONG exposure, or both, outside of that gap, and if the price will actually fall inside the 19k - 21k by the end of the week as Jane predicted, she will make a profit (here we will offer mild leverage, such as 4x, to BTC price exposure). 
 

In practice, Jane will set her gap on a chart - reflecting her prediction and uncertainty - and transfer some stablecoin collateral. (This can be done at any moment before the maturity date.)
What happens next requires no intervention from Jane’s side and depends on what beliefs the other users report and when, as the global market price changes in time.
 

_If_ the market price of the BTC future is below 19k at first, Jane’s LONG exposure is building up as her collateral is shrinking. This is happening at a fixed rate per dollar of remaining collateral, and per time. If the market price now raises, first to 20k and ultimately above 21k, Jane is _automatically_ first becoming “inactive” (during this time her collateral is left alone), and then flipping to short. From the latter moment, 
- while Jane still holds previous LONG futures, being SHORT turns out to be equivalent to selling these LONG futures at a profit that becomes available immediately for withdraw or compounding; 
- once all LONG exposure is sold, excess SHORT futures are allocated which will generate profit when the price is falling again. 
 
Depending on the market evolution, this process can reverse and repeat indefinitely until the market matures, generating profits for Jane. If Jane does not update her reported position or collateral size, all of this requires only **a single initial transaction** to set the gap between the levels of 19k and 21k.
 

Effectively, the protocol behaves similarly to continuous dollar-cost averaging for buying low and selling high, for both SHORT and LONG exposure. 
 

The gap between these two prices (19k & 21k) signifies Jane’s uncertainty about the future. A more knowledgeable or more daring user can report a tighter gap and avoid being “inactive” while the price is inside their gap, which allows orders getting filled for longer periods of time. The overall market price is a function of the position book containing the gaps of all users, and has the meaning of aggregated knowledge. 
 

**For binary options, a user reports likelihoods of events with an uncertainty band instead of prices, and instead of going LONG/SHORT she acquires options on A/B** when the market deems the probabilities are smaller than her own prediction, **precisely such that she expects a profit on average.** This is very similar to the futures case above, but can be presented with different UX and appeals to people without any interest in trading charts.
 

In all cases, instead of having to carry out constant buy/sell orders (low-level), users report their belief with an uncertainty gap (high level) that is translated into an automatic trading/hedging strategy executed by a smart contract. Meanwhile, slow ordering allows continuous matching of opposing users even if participation number is low. The aggregated market price of all users has the meaning of an aggregated prediction of price/probability for futures/binary options, respectively.
 
 
## Advantages
 
Our market primitive solves all pain points of both order book and AMM prediction markets and has the following advantages:
- Only reward precision and sustained correct expression of controversial opinion/position.
- Transparency of all opinions/positions as they are expressed over time.
- Front-running of limit orders is impossible, because orders are not executed instantly but streamed. - One can show that this is particularly important for prediction markets when new information comes in. This makes prediction markets fair for retail users without special infrastructure and trading bots.
- Every market participant is equal. Buying/Selling, taking a position, market making, liquidity provision are all consequences of expression of opinion/position. There is no extra market making, no separate liquidity providers, no centralized stakeholder setting odds or special accounts having any additional rights.
- Direct user matching: no risk-taking of the protocol leads to low fees, offering fair bets in any market. 
- Most importantly, liquidity scales limitless and adjusts dynamically with participating users, and can freely move to the most inefficient markets. This enables the creation of arbitrarily many markets on any topic without liquidity incentives - if they are interesting, liquidity is a direct consequence of and proportional to participation. 
 
# Go-to-market plan, business model
## Roadmap
 
We have implemented and successfully tested a prototype contract for our novel binary options in CosmWasm while at TFL, and a large part of the core algorithm implementation for MVP is therefore already completed. This dramatically reduces failure risk. The user-facing side of the product still needs to be built; this is what requires funding.   
 
 

**DeFi application (this grant)**
 
- **April 2023**: MVP: Binary options and futures for crypto asset prices
Goal: fully validate the tech/algorithm and UX in production
- **May 2023**: Perpetual futures
Goal: fee income for becoming self-sufficient (see sections below)
 
**Further vision, 2023 (this grant + self-funded)**
 
- General prediction markets and hedges
- Futarchy governance
 
Furthermore: a decentralized DAO (for regulatory reasons) could also run, using the technology developed for Contro, live sports betting markets. Since the continuous ordering of the market algorithm replaces instant gratification (“yolo” behavior) with automated trading strategies, and since the odds are not centralized but fair market odds, even those markets could be seen as a positive development for parts of society. For speculators, smart-contract based markets are less risky and cannot ban users for good performance unlike some centralized betting platforms.
 
 
## Fees
 
Revenue is generated due to trading fees:
For binary options, winners are charged e.g. 1% of their winnings
For futures, a smaller fee is taken at purchase regardless of outcome.
We conservatively estimate the fee revenue to be 7-8 digits per year from capturing just a tiny fraction of the total accessible market. Please refer to the Appendix for more details. 
 
 
## Token
 
We plan to release a token in the future when the product has assumed form. The goal is to create a utility token with attractive tokenomics and extremely low dilution. The tokenomics are constructed to reach a deflationary state.
Of the stablecoin fees collected by the protocol, 
- 50% are distributed to token stakers, depending on lockup duration
- 30% are used for token buy-back and burn to create deflation
- **10% are used to buy Luna to be given back to the Terra community pool** (permanently, i.e. even after grant amount is exceeded)
- 10% enter the protocol treasury to fund operations


We aim to employ a token sale market that our research team has developed and that transitions continuously from a fixed-price sale / minting to a fixed-supply constant-product market over several months. This novel idea to bootstrap a token circumvents the need for liquidity provision in the trading pair of the token against a stablecoin and we expect it to become a new standard for launching crypto projects.


There is not going to be a pre-minted token supply for DAO treasury / team, additional investors or airdrops and incentives. Some dilution to satisfy those needs occurs only during the initial sale phases of the token market and only in unison with increasing token demand. We aim to keep this minimal (< 15% of circulating supply). This new design of a token distribution mechanism ensures that 
- returns are more egalitarian, as the formation of an inflated bubble is prevented at all times. 
- This is particularly important for a bear market release for which initial demand is low.
- Even the total supply can at any time be absorbed by the market module, without putting investors at great risks, since the dilution is bounded and small at all times.
 
 
# Who we are
 
Contro will be fully decentralized and welcoming talent as a DAO. Full decentralization of governance will be completed step by step and as much as legal structures require. We plan to offer public bounties for all tasks and assign them in the open from the beginning. 


Our current contributors include an ex-TFL physicist with 10 years of various significant academic research contributions in theoretical physics and computer science and fellow of prestigious scholarships and the idea was vetted by an ex-McKinsey economist with a law degree and 15+ years of experience who has recently project managed a $15B initiative, and previously by an ex-Goldman-Sachs and an ex-Jump Crypto engineer in manager roles at TFL. While at TFL, we counted two highly talented engineers (they are even smarter), one of which holds several patents and continues freelance work, while the other remains at TFL but is available for advice. We aim to develop a decentralized protocol in the open, granting funds to the best freelancers (e.g. for UX design) as needed.


We have connections to top universities (CS QS ranking world top 10) and leading stipend organizations (due to being alumni) to tap into a deep talent pool outside of the crypto community, if needed.


Finally, we have two of the world's leading crypto law firms that advise most large L1s, decentralized protocols on Ethereum, as well as many betting platforms, eager to work with us. 
 
 
 
# Required runway
 
We aim to set up a project that can withstand regulatory pressure by achieving maximal decentralization. Besides the resulting legal costs, we need to offer competitive grants to source/keep the best talent, because the scale, complexity and novelty of this product simply require it. 


The goal of the grant is to fund reaching perpetual futures being live (ETA: May 2023) and roll out the product with determination and success (including marketing and community management).


A token would be released around this point, after which we expect sufficient traction to keep going based on fees and the resulting token demand. Since the protocol needs no external liquidity and takes no risk **no further costs will arise** that are not directly related to improving the user experience besides moderate operating costs. 
 

We estimate the required costs including legal, audit, tax, the remaining contracts, UX design, frontend, backend, add. decentralization costs, infrastructure, operations, marketing, communication and business development to reach around up to $0.9M including some safety runway. With significantly less, the MVP may potentially already be released by a minimized team, but this risks delays/failure and would limit scope, partnerships and growth.
 
 
 
# Grant Proposal
 
We are asking for 560,000 Luna. To ensure that funding is tied to outcomes, we propose to split this into two equal tranches of 280k Luna, with the second payout conditioned on launching the MVP:
- 280,000 LUNA (50%) of the grant goes towards the immediate manpower costs required to deliver the MVP and legal setup and marketing (ETA: April 2023);
- 280,000 LUNA (50%) will be used for operations and scaling costs for at least a year to work on the grander vision of generalized prediction markets and ease the transition into the self-funded regime.
 
Upon the passing of the on-chain proposal, all funds would be transferred to the following multisig address (reflected on the on-chain community pool spend proposal) to control the above vesting schedule: **terra1re2uhr2dwat4nnj3e45jss7fs2x2fel6n0f9h7**
 

Signers of this 4 of 5 multi-sig (in alphabetic order):
1. Andreas (Contro): terra15mn3ckzm9q34v8ylnlj0e66vgaevtucywqvtcg
2. Etienne (Setten): terra187r45s6turrggw0y56zfz4uw7vmgmq3n5ueuzg
3. GJ (Flipside, Community): terra1ky3ayzkeu9ffcm2h452u3tk3d293gjsnu9gvkj
4. Javier (TFL): terra1hxl0vzppearh6csk4nk5d8flq7fsrl3zl0fxxz
5. Rose (Community): terra1vzxzwsm0rscya65jg9znu9jls9gtqrv7mc9yh9 
 
**Timeline**: as mentioned above in the section “Roadmap”, the MVP is estimated to be ready in April 2023, and perpetuals very soon after in May 2023. Generalized prediction markets including a non-crypto-native-friendly user experience are expected to launch in 2023.   
 
 
# Conclusion
 
In summary, the Contro Protocol offers a DEX framework based on a novel way to match traders that brings many unique advantages, is therefore an exciting and highly competitive development in the DEX and derivatives landscape and satisfactorily solves decentralized prediction markets in the form of binary options for the first time. It promises tremendous value for the Terra ecosystem. 
 
 
## About Contro
- **Website: [contr.org](https://contr.org)**
- **Twitter: [@controrg](https://twitter.com/controrg)**
- **Telegram: https://t.me/controrg**

---

## Comments (10)

**Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)** — 2022-12-10T11:07:02.484Z (edited 2022-12-10T11:10:41.759Z) — 👍 2

# Appendices
 
## A1: Questions and Answers
 
_**Why decentralized prediction markets?**_
A prediction market is a market where people can trade contracts that pay based on the outcomes of unknown future events (e.g. who will win a general election). The market prices generated from these contracts can be understood as a kind of collective prediction among market participants. These prices are based on the individual expectations and willingness of investors to put their money on the line for those expectations.
 
A decentralized prediction market is a prediction market that can operate without the control or management of any one central operator. Typically, these markets operate through blockchain-based smart contracts that can self-execute in order to distribute payoffs.
Decentralized prediction markets are among the oldest and most powerful application of blockchains beyond decentralized money, dating back to early projects inspired by Bitcoin [2], forming a motivation for the creation of Ethereum [3] and the basis of the first dApp ICO (initial coin offering) in 2015 with Augur’s REP token. 
 
Prediction markets have been found to be better election predictors than polls [4]. Loud/polarizing voices must “put money where their mouth is” to be heard, and thus opinion manipulation is costly. This idea has seen recurring interest in the past, and we expect it to grow in importance in times of increasing misinformation campaigns and loss of trust facilitated by technical innovation such as AI (enabling increasingly realistic deepfakes) and the partial transition of our lives into the metaverse. At the same time, the need to transparently govern the emerging local structures of the metaverse, such as DAOs, as well as the democratic structures in real life, cries for novel tools: Futarchy based on prediction markets [5] is one of the most promising applications.  
 
The US Department of Defense, Google, Microsoft, Hewlett-Packard, IBM, Intel, Yahoo and many others have investigated the topic and / or run internal prediction markets for better decision making [6], but consensus so far has been that it is necessary to pay for this powerful tool or charge high fees [7]. This is true even in the centralized case. Consequently, the goal of wide-scale adoption of decentralized prediction markets has been unsuccessful to date as well, due to design flaws in the employed protocols together with the general difficulties in obtaining fair, profitable markets with well-adjusted liquidity. 
 
**_Why Terra?_**
First, we are bullish Cosmos in general. More specifically, our protocol uses data structures that CosmWasm offers and the EVM (for example) does not. 
 
Among Cosmos chains, on Terra, TFL and others are building out infrastructure to facilitate the development of decentralized applications, such as Enterprise Protocol and Warp Protocol, Y-Foundry, Apollo and many more. This creates an immensely useful environment for Contro to build out its idea as a DAO. 
 
Terra also has a strong and intellectually capable core community and leadership that has weathered the storm and has experience with running and participating in a leading blockchain full of DeFi innovation. We therefore hope that the Terra community will be excited about its novel ideas. 
 
Finally, the project was incubated by TFL and some of us are grateful for a good time spent at TFL. _We simply like Terra_.  
 
_**Won’t there be a risk for someone to steal the idea?**_
The idea to match traders directly over time is simple but turns out to be surprisingly complex to implement correctly. It e.g. requires numerical algorithms for integration, special data structures, special mathematical functions such as exp(p/q) (for which we have developed a fast and accurate approximation directly on the integers p, q) and many hundreds of lines of tricky logic, and until the code is open-sourced when we have enough traction we do not expect another team to copy and scoop us. 
 
_**Why don’t you raise a seed round instead?**_
This has nothing to do with a lack of confidence in our idea - there are several other good reasons.
- **Decentralization**
Contro must become fully decentralized for legal reasons. Contributors will be paid in crypto by default. Funding by community pool has the advantages that the funds are coming from a decentralized community and are already on a blockchain. On the other hand, money on a bank account registered on some entity would hinder decentralization.  
- **Token**
We feel strongly about offering equal opportunities for every user and have developed a token market that allows for a sustained public sale, well suited for the bear market release. By construction, there are no "premined" tokens to protect investors. Compare this to VCs who would eventually seek to exit with profit, which is at the cost of the public if the value they added is not big enough to compensate sell pressure. 
- **Overhead and bear market**
Given the current bear market, it would require significantly more work to secure funding than e.g. 1 year ago. Drafting this grant proposal has been time well spent for us. On the other hand, preparing a perfect and flashy pitch deck, organizing calls, sit in negotiations and check and sign legal contracts takes away from time and energy we would much prefer spending on building the product.
- **Terra's name**
For the moment, it is still difficult to find VCs willing to support a Terra project.
 
 
## A2: Revenue estimates
BTC and ETH futures alone trade monthly volumes of about 1 trillion dollars each [The Block], and are up over 300% in 2021 wrt. 2020. Much of this wants to ideally move on-chain (currently, dYdX, which is not fully decentralized, makes up about 0.1%). The growth of the market is expected to continue especially in the next bull run. We aim to capture at least a small percentage of this total market, namely low-frequency moderate-leverage trading that is less related to market making and more to actual opinion expression, as well as traders who want protection from liquidations (Note: liquidations are impossible in our protocol - if you are under water, your leverage scales down and your position remains positive - it recovers when the price returns, up to funding rates). We can lower the fees undercutting any competitor because our novel protocol takes no risk and requires no liquidity provider incentives. The simple estimate of 0.1% (fee) of 0.1% (captured volume) of multiple trillion/month gives expected revenue of 8 digits per year. 7 digits are then a maximally conservative estimate.     
General prediction market applications (after May 2023) can yield similar or larger returns and reach a massive audience; for this, more work is required (such as general oracles and better onramps). 
 
 
## A3: Prediction markets and AMMs 
Proper (unbiased) prediction markets are tricky to run because they must guarantee defined payouts for all correct bets. Only under such promise can the market obtain the information we are after: the probabilities for either outcome to happen. For illustration, betting on “head” of a fair coin flip is only profitable if the payout is larger than 2x the investment, and, conversely, from traders taking such bets for at least 2x returns on both sides, “head” and “tail”, we can conclude that the chance of either outcome is 50% (according to the market’s belief). In contrast to guaranteed payouts at the end, common DEX markets for trading assets put the responsibility of “selling the top” on the traders for maximal profit, which makes them easier to run. 
In the case of AMM prediction markets, payouts for winners must come from the liquidity providers, who tend to lose against traders actively taking the winning position (which can actually be easy when important information comes in or shortly before the maturity of the market). In other words, the impermanent loss caused by the extreme price changes that are enforced at maturity is very large. Thus, despite the fact that AMMs have been invented in times before blockchains [1] to enable prediction markets with low trading activity, they turn out to be ill-suited for this purpose.
 
 
## A4: Whitepaper
We are in close contact with the authors working on a scientific-style [whitepaper](https://contr.org/img/whitepaper_red.png) presenting all technical details of their invention, to be submitted to a peer-reviewed journal. (Names/affiliations have been redacted until we have clarity of the legal set-up. Further technical details on the algorithm will be released and all code will be open-sourced when the project is close to completion.)
**References**
[1] Hanson, Robin. "Combinatorial information market design." Information Systems Frontiers 5.1 (2003): 107-119.
[2] Clark, Jeremy, et al. "On decentralizing prediction markets and order books." Workshop on the Economics of Information Security, State College, Pennsylvania. Vol. 188. 2014.
[3] Buterin, Vitalik. "A next-generation smart contract and decentralized application platform." white paper 3.37 (2014): 2-1.
[4] https://iemweb.biz.uiowa.edu/research/longrunaccuracy/
[5] Hanson, Robin. "Shall we vote on values, but bet on beliefs?." Journal of Political Philosophy 21.2 (2013): 151-178.
[6] Arrow, Kenneth J., et al. "The promise of prediction markets." Science 320.5878 (2008): 877-878.
[7] Othman, Abraham, et al. "A practical liquidity-sensitive automated market maker." ACM Transactions on Economics and Computation (TEAC) 1.3 (2013): 1-25.

> **BlackFalcon (`terra1u4l5cswwpamnlu74snh2zv964cz73naeepgszr`)** — 2022-12-10T15:17:14.688Z
> 
> Proposal is well thought out and looks great. But if you look at the history of prediction markets in the blockchain space, they haven’t faired well (ie: Augur, etc..).   They are too complicated and struggle to gain adoption by regular users.  
> 
> I think offering binary options and futures on crypto prices is a good way to start, but I would also HIGHLY encourage you to consider sporting events outcomes and scores.   Prediction markets are an awesome idea, but on politics and prices alone- do not yet have good product market fit.  Sports betting apps however, have amazing main street popularity currently and will attract lots of users to your dapp.  Essentially, you can Trojan horse users into using a broad prediction market dapp if you attract them first with sports.   Sports betting is hot right now.  Use that angle to market the shit out of your dapp.  That’s my 2 cents.   (I’ve been thinking about this a lot)

> > **Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)** — 2022-12-14T16:39:31.476Z (edited 2022-12-14T19:01:21.309Z)
> > 
> > **We're appreciating your comments. Detailed answers below!**
> >  
> > > Proposal is well thought out and looks great.
> >  
> > **Thanks!**
> >  
> > >  But if you look at the history of prediction markets in the blockchain space, they haven’t faired well (ie: Augur, etc..).
> >  
> > **Indeed **
> >  
> > > They are too complicated and struggle to gain adoption by regular users.
> >  
> > **Agreed.** We are seeing a few reasons for the previous lack of adoption of prediction markets (PMs) and in particular binary options, the type of PM that we offer. We are hopeful that we can change the game already here. In summary, we make PMs easy to use in practice (at the cost of complicating the conceptual deep understanding a little). 
> >  
> > 1. **Expectation of profit for regular users**: Users come when they clearly understand how to make money in principle. (This is true even if it turns out to be difficult to win in practice, c.f. leveraged perp trading). Previous PM protocols are hard if not impossible to use in a sustainably profitable way. Contro makes it really simple and convenient for users to "turn wisdom into gold".
> > 
> >  - UX wise, we do not force people to directly trade binary options on the outcomes on a price/probability chart. We think this is not convenient and not intuitive enough for most people.
> > 
> > - Instead, users communicate at a higher level: they only need to slide a bar to set their belief how likely an outcome is between A and B. The slider has an adjustable width signifying their uncertainty that pro users might want to change. From this we _extract_ the fair prices a user would be willing to pay on either side. Note that this is also how a professional market maker would approach making money on binary options. We thus empower regular users to become market makers. All trading then happens automated under the hood, computed by the contract, and in a way that is mathematically rigorously giving +ev if users are right (see [here](https://contro.gitbook.io/docs/prediction-markets/foundations-of-prediction-markets) for some theoretical background on what it means "to be right" when estimating chances). 
> > 
> >  - Furtheremore, risk (variance of win/loss) is greatly reduced here compared to going all in on one side and at once. Contro Protocol can hedge bets as it would buy either side when they are cheaper than a user thinks is the respective fair price. It also spreads out orders throughout such "cheap" periods of time. 
> > 
> >  - Last but not least users are also protected from frontrunning of limit orders on arrival of information that would have changed the limits, unlike for order book exchanges. They do not have to rush updating their believes on big news, which for traditional long-running markets is a constant source of stress that no retail user wants to take on and for short markets is simply an unfair fight against bots/MMs (see [here](https://contro.gitbook.io/docs/prediction-markets/problems-of-previous-prediction-markets/bots-and-frontrunning-in-order-book-prediction-markets)). It suffices when users update on time scales of a few % of the total market duration (e.g. a night of sleep for a 2-week long market, or minutes for a sports game) 
> > 
> > We think that once users understand this opportunity, e.g. from hearsay from those who have made money by using this new tool, they will be excited to use Contro. 
> >  
> > 2. **Low quality of predictions**: AMM-based decentralized PMs are sluggish as state cannot be updated on arrival of new information without the volume of corrective trades being of the order of the total liquidity. Contro protocol, as well as oder books (e.g. Kalshi.com for a centralized offer), allow for instantaneous price jumps without volume and lead to better predictions. Additionally, Contro protocol eliminates most speculation noise and prices are stable even in the thinnest market due to sustained matching of traders based on their opinions, unlike for order books. (Prices are changing only if users change believes, and remain constant while matched trading happens otherwise.)
> >  
> > We are sure that good forecasting drives interest and reporting using our markets as sources will be free marketing for us. C.f. Metaculus, a forecasting platform that has had over 1M predictions on general questions without the gambling aspect. PredictIt has roughly 7 digits daily trading volume on politics (not massive, but a start), and will likely close early next year by order of the CTFC. Kalshi is also under pressure by the CTFC.
> >  
> > Polymarket's current most popular market is about the Republican presential nomination, not the Soccer World Cup. Furthermore, there are studies that show that real PMs (such as ours) are more accurate than prediction platforms that do not reward with real money (e.g. Metaculus) even without the improvments we offer on top to poll precice predictions and uncertainty . 
> > 
> >  We believe strongly that we will have the most accurate predictions (besides the most convenient and powerful user exerperience) and we assume this will drive significant interest from crowds that would not even have been interested in DeFi or betting otherwise.
> >  
> > **3. Lack of appeal to professionals: **
> > Another reason for previous failures which we think is crucial is that for power users, such as professional forecasters or whales, these previous protocols have too little or badly adjusted liquidity if they are based on unsustainably incentivized AMMs. As mentioned in the proposal, order books are also problematic for all but the one fastest trader (which lead to the invention of AMMs in the context of PMs!) and one should not place large limit orders or use a trading bot to trade continuously (this is what Contro Protocol automates), so they also suffer from low liquidity.
> >  
> >  
> > > I think offering binary options and futures on crypto prices is a good way to start, but I would also HIGHLY encourage you to consider sporting events outcomes and scores. 
> > > Prediction markets are an awesome idea, but on politics and prices alone- do not yet have good product market fit. Sports betting apps however, have amazing main street popularity currently and will attract lots of users to your dapp. Essentially, you can Trojan horse users into using a broad prediction market dapp if you attract them first with sports. Sports betting is hot right now. Use that angle to market the shit out of your dapp. That’s my 2 cents. (I’ve been thinking about this a lot)
> >  
> > We agree that the sports betting market is huge (and growing) and attracts users. We have already mentioned sports betting in the proposal as a possible vertical (see Section Roadmap). We think that one reason for the popularity of such markets is that sport fans often have very strong convictions for either side, increasing the controversy. High controversy makes markets interesting and increases volume and liquidity. (This strong connection to the concept of controversy gave us our name.)
> >  
> > We agree that no guesswork is needed to see the opportunity and the pmf for sports betting. 1% of the market means 1B/y in _revenue_ and would seems feasible. While going all in on one side will still be a simple default mode we offer, adding sophistication and expressiveness for an optional "pro mode" will only help make such a product more interesting than competitors.
> >  
> > We in the initial team ideally do not want to have to remain anon. Since the betting market is highly regulated such offers would have to come from the decentralized effort and not from us.
> > Feel free to reach us on Twitter already, while we are setting up the DAO governance structures.

**4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2022-12-12T10:09:16.335Z

This is the most interesting protocol I have seen in a while. The prediction market is huge and if this protocol can capture some of it onchain would be a great value add to LUNA. The BTC example is 🔥🔥🔥 everyone should read it. 
the 10% of revenue to buy back LUNA & deposit back in community pool indefinitely should be a standard for anyone tapping into community pool funding, great initiative by the team. 
The risk/reward here is substantial & i will definitely be in support of it passing. 

Thanks for including my questions during our chats in the FAQ section.

**ShaunOnTerra (`terra1526zhyrd8fzdvzayct9yfnspsdp9uuqhyjmte3`)** — 2022-12-18T00:03:37.047Z

As  per, _**Why don’t you raise a seed round instead?**_ 

I understand the struggle with finding VCs, though curious why not do a launch on valk.. e.g token launch to secure funding like many others? I don't see the risk/reward in favour of the community, while the demand for the dapp to repay the amount is still questionable.

> **ShaunOnTerra (`terra1526zhyrd8fzdvzayct9yfnspsdp9uuqhyjmte3`)** — 2022-12-18T03:14:12.249Z
> 
> To add, there seems to be a fair bit of legal risks towards the community, as it stands Terra 2.0, is not breaking any SEC laws/requirements, i feel this may directly effect the holders if the community was to directly fund this from the community pool, inwhich imo the risk/reward ratio doesn't match for said risks.. though if im incorrect in my assumptions, some feedback on legals would be appreciated.

> > **Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)** — 2022-12-19T20:35:16.729Z
> > 
> > We have commented on the issues raised here: https://twitter.com/controrg/status/1604863093187776513

> **Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)** — 2022-12-19T22:06:58.655Z
> 
> We are skeptical if in the current market situation a token sale restricted to a few days (or even weeks) would have good chances to raise sufficient capital and liquidity. We do plan to release a token when a) more excitement for the product has been built, and b) on a longer timescale (many months, smoothly transitioning from fixed-price sale to constant-product market - expect more on this soon). We have upfront legal costs that somewhat limit the amount of uncertainty we can tolerate here - and a grant matches that need.

**Stakely -Gov (`terra108lmrztvc3pc3w774shgvpry4d3lf79k2nhxrw`)** — 2022-12-19T13:28:01.576Z

Hi,
Since this is a large grant request, I would like to have more details about how you plan to spend the funds for the sake of transparency.
Could you please detail how many people will work in the team that will be fully dedicated to the project, their roles and their dedication?

Many thanks and good luck with the project :)

> **Controverse (`terra18nw0r2xsl05pc9uwrdwxqkn25nc2jfcek72hdp`)** — 2022-12-19T22:47:41.007Z — 👍 1
> 
> Hi, thanks for your kind words and sure - 
>  
> 
> **Bulk costs:**
>  
> 
> - Law firm: 110k for the initial setup period
> - Legal buffer: 50k for continued legal support
> - Audit: ca. 100k
> - Brand design, new landing page: 25k
>  
>  
> **Salaries**
>  
> 
> We have the following 9 positions
>  
> - Senior Research/Algorithms
> - Junior Smart Contracts
> - Senior Smart Contracts
> - Senior Frontend 
> - Senior Backend
> - 2x UX Design
> - Senior BD
> - Comms
>  
> some of which are part-time.  If you need more details send us a msg on Twitter :)

