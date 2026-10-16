# Software update: Minimum Commission

- **Thread ID:** 5473
- **Author:** Anonymous (`terra1fza7jd84vy80qwke642rrxejgg3nc7qef7ketk`)
- **Created:** 2022-06-15T15:23:16.014Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 4785
- **Reactions:** 6
- **Comments:** 19
- **Source:** https://common.xyz/terra/discussion/5473-software-update-minimum-commission

---

_**Disclaimer: I am a member of TFL.**_

**Background**
**Currently, costs to run a Validator node can run high when you also include the human resources necessary to maintain optimal performance and court delegations.**

**To cover their costs, Terra validators are able to charge a commission rate on the staking rewards they earn for their delegators. However, there is currently no minimum commission rate set. Therefore, delegators are incentivized to seek the lowest commission rate possible in order to extract the most value from their staking rewards. For validators, attracting delegations thus becomes a race to the bottom as validators are forced to lower their commission rate in order to compete.**

**What is a validator:**
**A validator runs a set of programs which record the ledger of the blockchain to ensure a consensus of correct transactions is always recorded. The distribution of these programs being run across 130 different machines of varying stakes, ensures a permissionless network. These actions from validators are essential, as without validators running dependable operations, the Terra blockchain would not be able to operate in its current form.**

**The minimum machine that must be run for this operation at the time of proposal is:**

**The AWS c6a.4xlarge, or equivalent **
**vCPU: 16 **
**Memory (GiB): 32 **
**Instance Storage: 2TB SSD NVME)**
**Network Bandwidth (Gbps): Up to 12.5 EBS **
**Bandwidth (Gbps): Up to 6.6**

**The optimal setup includes a Horcrux ([https://github.com/strangelove-ventures/horcrux](https://github.com/strangelove-ventures/horcrux)), a bare metal machine, and virtual machines for sentry operation. **

**Learn more about sentry node architecture here: [https://forum.cosmos.network/t/sentry-node-architecture-overview/454](https://forum.cosmos.network/t/sentry-node-architecture-overview/454)**

**Action**
**We propose that we set the minimum commission rate for validators to 10% in order to ensure all validators are adequately compensated for the service they provide to the Terra network.**

**To do so, we propose that the Terra Core team creates or approves a PR (similar to: [https://github.com/terra-money/core/pull/47](https://github.com/terra-money/core/pull/47)) to add the following parameter to the Terra Core:**

**All validators are set to a minimum commission rate of 10%**

**This floor will allow validators with different business models, or larger network costs, to compete above the 10% mark, while at the same time compensating smaller validators who provide the same level of service to the network.**

**Based on current market conditions:**

**14% - LUNA staking return per year**
**$ 2.6 - Price per LUNA**
**1,000,000 - in LUNA delegations**
**10% - commission on LUNA staking rewards**

**With a 10% min commission rate, the monthly income per 1m LUNA staked to a validator would be: $3,033**

**(.14 * 1,000,000) / 12 = 11,666.67 LUNA/month in total staking rewards**
**11,666.67 * .10 = 1,166.67 LUNA/month in validator staking rewards**
**$2.6 * 1,166.67 = $3,033.34**

**Based on data gathered from validators currently validating on Terra 2.0 (excluding one outlier of $80/month), the average monthly costs to validate on Terra 2.0 at the time of proposal are approximately $3,186.**

**Viewable monthly cost data gathered from validators on the Terra 2.0 Discord: [https://docs.google.com/spreadsheets/d/18v40HmlZDcL8Dk3SOilk6hj5iTFVozHVG7YCLir3m0g/edit?resourcekey#gid=2112147284](https://docs.google.com/spreadsheets/d/18v40HmlZDcL8Dk3SOilk6hj5iTFVozHVG7YCLir3m0g/edit?resourcekey#gid=2112147284)**
**Pending feedback from users and partners, we will potentially adjust this proposal to match the suggested changes. A revised proposal will be communicated once ready to initiate as an on-chain governance vote.**
**Please allow for open discussion regarding the proposal above.**

---

## Comments (19)

**schultzie | Lavender.Five Nodes (`terra1pn3t586r4t0w4w4pncmmdnsl3fqmj625xngs80`)** — 2022-06-15T16:05:05.415Z — 👍 1

We are in support of a minimum commission, and indeed have fought for such on several networks.  

Here's a relevant discussion on the Secret Network: https://forum.scrt.network/t/minimum-validator-commision-discussion/5233

**Arman | NITAWA Systems (`terra150pqxd0j27mjg4yy4fafhkm7gfhsk8xvyx9klh`)** — 2022-06-15T16:12:40.167Z — 👍 1

We've been waiting for this to be implemented in Terra v2. We fully support this minimum commission.

**Garvit (`terra10d8qdmldnugrmpczma2kavgj9f4ugrsdf47aqk`)** — 2022-06-15T18:55:54.361Z — 👍 1

We are fully in favor of this proposal, at Electron Labs

**crytonomenon (`terra1q495w0y3plu8ssyw7fls5433zr65dfra005uzx`)** — 2022-06-15T22:04:11.460Z

A minimum commission based on the current price seems like a bad idea.  If price changes significantly, the minimum either won't cover costs or will seem excessive.

Have you considered a floating minimum based on TWAP?  As price changes, the minimum commission would change with it (up to some reasonable max).  Validators could set their target commission rate, but it would restricted to at least the current minimum.

For example, validators set the following target commissions: 
- Validator A: 0% 
- Validator B: 5%
- Validator A: 20%

If the current floating minimum is 4%, Validator A is forced to 4%, the others are unchanged.  if the floating minimum is 10%, both A and B are forced to 10%.

This will ensure validators are appropriately rewarded while still being reactive to price changes.

-----

I also wonder if there's a way to do min commission that encourages decentralization.  One idea is that for very large validators, part of the minimum commission is redistributed to delegators of smaller validators.  Essentially, once costs are covered and a reasonable profit is made, further profit is taxed.

For example, the biggest validator right now has 20m Luna delegated which is 20x the values used in the post.  Let's say the desired max for a validator is 10m Luna.  The commission earned on the excess 10m Luna would be taxed (at whatever rate seems reasonable) and redistributed to stakers of other validators.  However, if the validator has commission set at 20% (and min is 10%), the portion above the min is not taxed.

This would encourage stakers to distribute more evenly.

-----

Anyways, just some ideas.

> **MoonPlatoon (`terra1akh86cyazxvwz34z4k4656uug3um4vus3tm3xv`)** — 2022-06-15T23:48:08.239Z
> 
> This minimum commission will be governable. if prices rise or fall. we can adjust accordingly. Many other projects have done this flat min. commission and it has been successful. What we are doing is making sure people who are subsidizing their operations here with profits from other chains aren't gathering all the VP because they simply have a 0% commission. Whether long-term or short-term, most people will go for the lowest commission validator. This incentivizes lower cost infrastructure which can lead to degraded performance due to everyone trying to cut costs at every corner. I believe in a free market, but I also believe that we don't live in a free market, so some people will run a validator on the bare minimum with bare minimum support / security etc, while gathering up alot of the voting power. I think that this has long term effects on decentralization and security of the blockchain. Atleast with this people can cover costs of decent infrastructure and be able to pay themselves a livable wage to maintain their node.

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-06-16T00:54:42.279Z

Let me be the contrarian here.

I do not support minimum commissions for several reasons.

1. If someone is basically breaking even at $3k/month, they seriously need to examine their business model. I say this with the experience of running validators on multiple networks for 18+ months, none of which had costed $3k (including time spent)
2. ZERO commission is a great way for a new entrant to enter the market and attract delegations. On terra1 there was a validator running at 0% (NOD games or something) and they provided great value to their delegators for months. The aim of staking is to lock tokens for the security of the network. I see a forced minimum as discouraging delegators staking, especially as interest rates are raising everywhere else.
3. I don't see having only '50' or '80' validators running a chain as a problem. Once the price raises, it will become more profitable for others to validate on the network, and they will join.  My experiences on running new test-nets is that there are 100's of people wanting to run validators.


What I would like to see is a change in redelegation policies. When a validator changes their commission, it should allow people to instantly redelegate, instead of delaying them for 21 days.

I'm also saying this as a validator who has never run at ZERO commission. (I think my lowest was 3%)

We're here for the delegators, not to earn millions of dollars for just keeping a machine or two up.

> **MoonPlatoon (`terra1akh86cyazxvwz34z4k4656uug3um4vus3tm3xv`)** — 2022-06-16T01:38:21.177Z (edited 2022-06-16T01:39:24.388Z) — 👍 1
> 
> How does this stop people from running at 0% commission indefinitely? You can't compete with free. The vast majority of delegators aren't focused on community initiatives as they are becoming rich from staking rewards. Money is a motivator for everyone. delegators included. If it wasn't we wouldn't need a commission at all. While I don't disagree with the option for delegators to be allowed to re-delegate when commission changes, this doesn't stop one or two validators from amassing the most voting power by running at 0% forcing others to either run at a loss or shut down. This has long term ramifications that doesn't help the blockchain. Currently, Luna 2.0 is at a 40 Nakamoto Coefficient, Luna 1.0 was at a 7. Overtime this number will drop due to people losing keys with staked Luna on X validator, going for the highest possible return via lowest commissions, etc. Given enough time a handful of validators could accrue more voting power than the other 49% and then we would be in even more trouble. In 3 years the Nakamoto Co. dropped to 7 on T1. T2 currently requires 22 validators to halt the network. Almost every other cosmos chain requires 6-7 to halt the network. I believe that decentralization is fundamental to the success of any blockchain network and will always personally vote for anything that advances that. I feel that this does that.
> 
> As far as new validators, I understand the concern. However, running at 0% comms. in order to get delegations does what exactly to combat centralization? Assuming they aren't going to run at loss forever, then the moment they up their commission people will just re-delegate to the next 0% comms or their previous validator. That's because there isn't any lasting value in running at 0% comms. unless its perpetual. You'll eventually just have people making new validators running at 0% perpetually or when they up the commission they will run another validator under a different moniker with 0%. I could easily then just up comms on the original validator, I would lose some delegations sure but whatever. I'd then run the other validator @ 0% comms and repeat. Eventually forcing everyone to run at 0%. There are endless game theories that could play out. Atleast with a min. commission, everyone is getting paid for securing the network and there isn't a race to the bottom.

> > **Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-06-16T01:54:46.469Z
> > 
> > some people chase lower commissions.
> > 
> > others chase value produced (podcasts, tools, support, familiar name from another chain, whatever).
> > 
> > If you haven't differentiated your offering, then you're in a race to the bottom (whatever the bottom number is), as you don't provide any extra value to delegators.
> > 
> > Find a way to produce value, and people who like what you do will re-delegate to you.
> > 
> > If people cared about nakamoto indexes they will chose someone under average amount. and tbh.. they will chose some name they recognize.. (which goes back to differentiate).

**Anonymous (`terra17uncwru68z3n0kl543r6rdd5q9jpvwxdxvfe66`)** — 2022-06-16T01:39:53.752Z — 👍 1

I would disagree to this proposal. On top of [@PFC](/terra/account/terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8)'s view as a validator, as a user, a minimum validation fee will be seen as a minimum tax rate to secure the network. The tax rate will be compared against upcoming DeFi protocols which will be able to provide a higher yield on their LUNA compared to the yield to validate the network. 

We do not know what is the exact business model for majority of the validators, with the exception of Bites Digital, Danku, Orbital Command, etc. If they're professional validators, I suspect the running cost will be lower (see PFC's comment above). 

As an alternative, I suggest that if a minimum commission rate is imposed, I would suggest a lower commission rate such as 3% or 5%.

> **MoonPlatoon (`terra1akh86cyazxvwz34z4k4656uug3um4vus3tm3xv`)** — 2022-06-16T01:56:55.383Z
> 
> > The tax rate will be compared against upcoming DeFi protocols which will be able to provide a higher yield on their LUNA
> 
> This proves my point exactly.

**JohnGalt (`terra1wfaxhrq2n0326zkvecc4ad7kgk8cjc48yukgnq`)** — 2022-06-16T02:40:42.639Z (edited 2022-06-16T02:44:24.532Z) — 👍 3

[@crytonomenon](/terra/account/terra1q495w0y3plu8ssyw7fls5433zr65dfra005uzx) Good point about current prices. Prices could go up, or down. At 10% minimum commission, validators will still be incentivized even if prices continue to fall. Downside protection. But price could shoot up. Maybe we should somehow make the 10% minimum commission lapse in 6 months, forcing the community to have another vote to either extend it or change it.

[@PFC](/terra/account/terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8) Minimum commission prevents tragedy of the commons. Yes, people should delegate to community validators and distribute their delegations to prevent centralization. But people acting as individuals won't do this. With no minimum commission, over time validators with 0% or 1% commission who do nothing for the community would amass too much power. Tragedy of the commons.

Minimum commission does a lot of things. It prevents centralization, and network continues to run even if LUNA price declines significantly.

Also, minimum commission would help community validators provide services for the Terra project. Terra has no centralized foundation to subsidize service providers, so many rely on validator commissions. Coinhall, Flipside, Danku, Terra Bites, Setten, Orbital Command, etc. use commissions to support the community. (Speaking of, Terrascope had a validator for Terra 1. They need to fire up a validator for Terra 2, so they can get a steady stream of income to support their work.)  

Validator commission is a decentralized way of funding service providors, but it only works if a minimum commission is in place. When picking a validator, it's a pretty hard choice to pick between paying 10% to support the community or paying 1% to someone who doesn't give a toss about Terra. But choosing between a 10% validator who loves Terra and a 10% validator who doesn't care is an easy choice.         

And at the end of the day, the current staking reward is quite high to begin with. Given that it's 14% APR, paying 10% of that to 1) promote decentralization, 2) ensure network runs regardless of economic conditions, and 3) support important service providers - well, it's not a bad deal.

> **Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-06-16T03:41:08.272Z (edited 2022-06-16T03:41:44.380Z)
> 
> none of this has to do with the tragedy of the commons. (which is who will maintain the public services if no one is being paid directly to do so).
> 
> no one is going to do squat as they just can do nothing and still get 5%. (or whatever the minimum is). 
> 
> That's the game-theoretic optimal choice here (as public infra costs $)
> 
> This is why TFL tried provided grants for people to provide public infra, and why they were encouraging dApps to use dedicated hardware to run themselves. (getting the dApps to pay for the cost of running their dApp)

> > **Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2022-06-16T21:19:27.890Z — 👍 2
> > 
> > 100% agree with [@Terra Watcher](/terra/account/terra1wfaxhrq2n0326zkvecc4ad7kgk8cjc48yukgnq) that:
> > 
> > > Minimum commission prevents tragedy of the commons
> > 
> > The way I see it, a decentralised ecosystem with validators running high quality infrastructure and providing value to the community (educating, creating tools, running relayers, etc.) - is the common (good).
> > 
> > 1. Does a minimum commission support or disadvantage the common?
> > 
> > I would argue it benefits the common. When it is profitable for validators to provide a high quality service, the common benefits - more education, more tools, more relayers, etc.
> > 
> > Maybe validators can spend less time working a regular job and more time in Terra 2.0
> > 
> > A higher quality common benefits every single user of the ecosystem.
> > 
> > 2. Does a minimum commission encourage lazy validators?
> > 
> > It is possible that some validators may:
> > 
> > > do squat as they just can do nothing and still get 5%
> > [@PFC](/terra/account/terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8) 
> > 
> > One of the jobs of community validators will be to highlight parasitic validators so that delegators can make more informed choices and delegate to a validator who provides something they appreciate.
> > 
> > When community validators compete at the same commission rate with less common minded validators, the validator who contributes more to the community wins.
> > 
> > > a minimum validation fee will be seen as a minimum tax rate to secure the network
> > [@Max Callisto](/terra/account/terra17uncwru68z3n0kl543r6rdd5q9jpvwxdxvfe66) 
> > 
> > Interesting observation. I have never viewed validator commissions in this way.
> > 
> > ATM, because there is so much vesting LUNA, staking is our only option. Secondly, even if we could do some other DeFi with our LUNA, 12.5%+ is still a good return.
> > 
> > 3. Do validators even deserve to earn an income?
> > 
> > I think it is entirely reasonable to expect validators (who provide a good service) to receive financial compensation for doing so.
> > 
> > At a 0% commission rate, delegators will receive 14%
> > At a 5% commission rate, delegators will receive 13.3%
> > At a 10% commission rate, delegators will receive 12.6%
> > 
> > By supporting validators with a minimum commission, delegators still benefit from a good rate of return. The entire Terra 2.0 ecosystem benefits from the additional value that validators can provide when they are rewarded financially.

**FatMan (`terra17f7ggjf2xf0n3kqcg6yxxu4wpqs35u2c7e0efl`)** — 2022-06-16T09:05:57.220Z

Don't really have an opinion one way or the other... Just wanted to share some thoughts that came to mind.

- I wonder how the arithmetic used to calculate the minimum commission was derived. There are many assumptions made. The highly volatile price aside, most delegators in the active set have far more than 1M LUNA delegated, so why are we using that as a figure to calculate break-even? 1M seems completely arbitrary. Better candidate figures seem to be average delegated, median delegated, or even minimum delegated.


- There is a fascinating bit of game theory at play here. Validators are voting to increase their own minimum commission, so at what point would they vote no after a fair preponderence of arguments? I presume most validators will vote yes for 10%. What if TFL suggested 15%? 20%? At what point would validators vote not to increase their own earnings given the detriment to stakers? I have no idea, but it's interesting to think about.

**WildCommunist (`terra1q8w4u2wyhx574m70gwe8km5za2ptanny95la5z`)** — 2022-06-16T09:31:38.324Z — 👍 3

I would support minimum commission for few simple reasons:

1. Even if you bring lots of value to the community (RPC,LCD block explorers, stats etc), common folk might not really care about nor look too much into it. Everyday Joe who delegates is here to make money, simple as that. I am saying this from personal and team experience. When we were just building dapps, we really didn't look all thaaat much into validators or what they provided, just their commission value. Also the "oh, you are in the top 5, with 2x delegations than your closes competitor? I'll go with you as others did. You must know what your are doing!"
2. If you amassed a big audience on twitter, tg etc, it would be pretty hard to compete with that.


I would prefer it to be something as mentioned above, every x months we re-evaluate the minimum commission to keep up with the price of Luna.

**JohnGalt (`terra1wfaxhrq2n0326zkvecc4ad7kgk8cjc48yukgnq`)** — 2022-06-16T12:48:09.110Z — 👍 5

[@PFC](/terra/account/terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8) "no one is going to do squat as they just can do nothing and still get 5%. (or whatever the minimum is)."

I would disagree. With a minimum commission, we are forcing delegators to give up part of their staking yield. But they get to choose who to give it to. Thus, delegators evaluate validators based on their contributions to the community. Validators are forced to prove they are supporting community, forced to provide more value to community than their competitors. Danku stops producing high quality educational content about Terra? Delegators will redelegate to Terra Bites instead. Forces validators to compete against each other for the good of Terra.

In reality, validators do squat when they are able to amass a huge amount of delegations and charge a low commission. No other validator can compete with that kind of economy of scale, especially a validator with high opex to support the community.

I do think absence of minimum commission leads to the tragedy of the commons. Decentralization is a common good, high-quality equipment is a common good, and community support is a common good. But, given the choice, people acting in their own interest will go for max value extraction by picking a low commission validator, even if he already has a huge amount of delegations and does nothing for the community. To compete, smaller validators will have to run low-quality equipment to keep costs down, especially the tail end of validators.

[@WildCommunist](/terra/account/terra1q8w4u2wyhx574m70gwe8km5za2ptanny95la5z) Glad you agree on the idea to reevaluate minimum commission percentage every x months. Not sure how that would be implemented technically, but it is quite a good idea. Reopening this discussion every x months would keep validators accountable to the community.

[@FatMan](/terra/account/terra17f7ggjf2xf0n3kqcg6yxxu4wpqs35u2c7e0efl) While validators do vote on behalf of their delegators, delegators have the power to override their validator's vote. Of course, most people don't care, and just let their validator vote for them. But by reopening this discussion every x months, it would repeatedly remind delegators that this is a community decision, everyone is allowed to contribute to the discourse, and ultimately delegators get the final say.

**CapriciousSage (`terra1yxmz0r83s3xy9jn5ywx39xsxtm75esfx896lhr`)** — 2022-06-16T15:47:02.962Z — 👍 4

I believe a minimum is needed (the top validator being at 0% by a wide margin is a good example of why).

It may not need to be as high as 10%, but once we've got the parameter functioning, the process to change it later is much easier to implement with a simple param gov vote.

Either way, I fully agree with [@PFC](/terra/account/terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8)'s comment around ensuring that people can redelegate their luna whenever a validator changes their commission (or at the very least, whenever they increase it).

People have delegated to 0% validators on Terra2, only for that validator to turn around and increase their commissions (as high as 20% without notice in some cases), trapping people with a bait and switch. 

Letting people switch instantly after a change in circumstance is vital to effectively discourage that kind of behaviour.

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-06-17T03:07:37.578Z — 👍 3

as we are talking about 'public goods'

another approach is to take some of the community pool and devote it to those who provide infrastructure (LCD, relayers, and whatnot).

as we don't need a million of either, the pools should be set up so that it can support say 5-10 infrastructure providers doing each.

if 11 do it, then it wouldn't be cost-effective (and one would drop). 
It would also encourage competition. each pool could have metrics associated with it, so they can be maintained.

much better than assuming giving validators more $ will make them do it.
We did this on Terra1 with the TDP. 3 out of the 50 people actually did something. the other 47 did squat in terms of public good, or the betterment of the chain.

(and look.. I would LOVE a minimum commission, it means more money for me, but it isn't the right thing to do)

**CapriciousSage (`terra1yxmz0r83s3xy9jn5ywx39xsxtm75esfx896lhr`)** — 2022-06-30T00:38:38.062Z (edited 2022-07-01T14:04:54.864Z)

**Reminder:** This proposal votes to do two things:

1. Introduce the new 'minimim commission' paramater
2. Set at an _initial _value of 10%


TFL have already completed the software development work - this is just voting on whether they include it in their next planned software update block (693000 - est 15th July).

Once the paramater is in place, the initial value can be changed at a later date through a simple "parameter change" proposal. This change can then be done at any time and does not require a software update.

If you like the idea of a minimum (to end 0% wars and help drive decentralisation) but want the minimum to be a different amount, then you can vote "yes" on this proposal (implementing the patch), raise or vote "yes" on a subsequent proposal to change to 5%, etc.

EDIT: Someone has actually gone and made a prop to set as 5% from the start: [https://station.terra.money/proposal/874](https://station.terra.money/proposal/874)

