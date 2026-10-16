# Terra Validator Reformation: Forging a Stronger Future

- **Thread ID:** 13870
- **Author:** Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)
- **Created:** 2023-10-27T18:13:38.286Z
- **Last edited:** 2023-10-28T13:12:39.039Z
- **Stage:** discussion
- **Views:** 328
- **Reactions:** 0
- **Comments:** 4
- **Source:** https://common.xyz/terra/discussion/13870-terra-validator-reformation-forging-a-stronger-future

---

**TL;DR:**

This proposal aims to reform Terra's validator ecosystem by addressing structural issues. It suggests reducing the number of validators from 130 to 70, implementing a min commission of 5%. The goal is to combat problems like rent-seeking behaviour, enhance community participation, and reduce network costs. The proposal involves a phased implementation, with potential benefits including lower infrastructure costs, increased staking rewards, and a stronger Terra ecosystem.

## **Introduction**

As part of Terra’s growth and future success, there is a clear need for Validator reform

Primary goal of this proposal is to address the serious structural problems of the current active validator set and to recommend as a solution, that will enable the gradual creation of a quality validator group: 

A group determined fairly and transparently, and composed of validators who are closely aligned and engaged with Terra's success.


**The current validator set has problems resulting from**:

- sub-optimal formation of the active set at genesis
- lack of incentives or mechanism to encourage meaningful engagement by validators 
ie no deterrent to rent-seeking behaviour

**Background:**

- During the Terra2 genesis, a significant proportion of genesis tokens were bonded to genesis validators. The urgency to establish Terra2 caused the onboarding of new validators from outside of the pre-existing Terra1 active set that were not vetted or verified by any formal criteria.  

**This resulted in:**

- imposters impersonating pre-depeg validators
- individuals and entities controlling two or more validators 
- wide-spread Rent Seeking Behaviour (when an entity seeks to gain wealth without any reciprocal contribution of productivity) where validators have no motivation other than to sell validator commissions without a contribution in any other way to the ecosystem
- inactive capital delegated to validators

**Typical behaviour of rent seeking validators include:**
	
- Do not consistently participate in Governance votes at all or in a meaningful way. This includes not voting or regularly voting abstain
- Maximising profit extraction by setting their commission between 15%-25%
- General lack of engagement in validator channels and community channels (even during critical upgrades)

**Impact: **

- Commissions from the 130 active validators at current $luna prices (0.45c) equate to USD $285,750 per month. Rent seeking validators extract their profit and sell $luna creating constant downward pressure on the price. Those that do make a contribution to the ecosystem use those commissions to support the contributions they make. 

- Potential for rent seeking validators with multiple validators to consolidate unhealthy levels voting power

## **Proposed Solution**

**This is comprised of several parts: **

1. A Gradual reduction of the active set from current 130 validators to a target of 70. 
2. Implement a minimum commission of 5%

 
**1._ Validator set-reduction_**

The reduction is scheduled to happen monthly, to allow enough time for delegators to redelegate and allow for the TFL planned community delegation program to start up. For 3 months the active set is being reduced by 20 validator places each month. 

As part of this process, validators ranked below the 70th position in terms of voting power will be automatically inactive, making them unable to sign new blocks. Delegators will need to redelegate to bonded validators at the active set to continue earning staking rewards.

Rational :
- The Terra validator set is overscaled for the current size and usage of the chain.
- Additional validators procure additional infrastructure costs, increasing the LUNA value bleed.


**2. Implement a minimum commission**

Implement a minimum of 5% validator commission.

Validators should change their commission to accommodate the new parameters before the Core upgrade. During the update, validators that have a commission < 5% will be set to 5%

Rational :
- 0% validators draw in delegations and centralise the chain and governance power. After attracting delegates, often these validators later switch to 5% or higher commissions. Current 0% commission validators are all in the top 33%, with Setten reaching 5.5% of voting power and delegations.
- Due to reduction of the validator set, 0% validators will have an increased delegation draw, so the min commission implementation needs to be passed before the set is being reduced.


**Proposal execution phases: **

The implementation of this proposal would be broken down into on-chain proposals as per below:

1. **Signal: **Active-set reduction proposal & minimum validator commission **(in 1 week)** 
2. **Execute**: Implement a minimum and maximum commission **(signal & implemented)**
3. **Execute 110**: Active-set reduction parameter change proposal **(signal passed)**
4. **Execute 90**: Active-set reduction parameter change proposal **(signal + 1 month)**
5. **Execute 70**: Active-set reduction parameter change proposal **(signal + 2 months)**


This proposal has been posted on 27.10.2023.

## **Implications **

**1. Reduction of Infrastructure cost**
With the proposed parameters and current delegations, the total monthly infrastructure cost is reduced to ~80.000 USD per month (top 70 validators, min commission 5%). We expect that the real-world cost will be a bit higher, as redelegation happens, but allows for validators to run the chain more cost efficiently.

**2. Increase in Staking APY**
The genesis of Terra has a lot of inactive capital staked with genesis validators. By reducing the validator set size some of the inactive capital / disconnected users will be kept on inactive validators, increasing the APY for active community participants. In the bottom 50 validators there is a total stake of 126 M LUNA that will need to be redelegated.

**3. Value Providing Validators**
We understand that there are validators in the bottom 50 validators that are actively providing value to the Terra ecosystem and we believe that with the planned TFL Community Delegation Program you will be able to keep staying in the active set. This proposal is geared towards improving the overall set and optimising the operating cost of the Terra chain, to make it successful in the long term.

**4. Nakamoto Index**
We expect that the combination of proposals does not have any negative impact on the nakamoto index and can even improve it through the delegation program. We are in contact with [https://observatory.zone/](https://observatory.zone/) to list Terra to also include the infrastructure score in the TFL Community Delegation Program.

# Conclusion
This proposal seeks to address critical challenges within Terra's validator ecosystem. By implementing a series of well-defined changes, including reducing the validator set, enforcing minimum commission limits, we aim to enhance the trustworthiness and fairness of Terra's active-set.

The problems stemming from the Terra2 genesis are significant, but this proposal represents a comprehensive remediation solution. It introduces a phased approach, ensuring community involvement through signalling proposals and governance voting.

As Terra continues to evolve, these changes are vital for maintaining a secure and vibrant network. We look forward to the community's support in implementing these improvements and working together to build a stronger Terra ecosystem.

Thank you for your consideration and collaboration.

---

## Comments (4)

**Chris Amani (`terra1xx8wkyld9gkzqpyxyh8k0tqchsg0fwl02msvut`)** — 2023-10-27T18:22:02.005Z

Can you elaborate on impact to Nakamoto Index and why you think it will have no impact or might even improve it?

> **Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2023-10-27T18:40:43.644Z (edited 2023-10-27T18:43:43.564Z) — 👍 1
> 
> Ideally I would like to get observatory.zone to include Terra as one of the monitored chains to showcase the issue, that a bigger set, not necessarily mean a higher Nakamoto Index or even higher decentralization. A higher focus of delegations to fewer (still 70) validators means they can have better operations, in combination with a Delegation Program, that **rewards and incentivizes** **diversity**, the set is being improved and the Nakamoto Index raises.
> 
> The min commission however will have an immediate positive impact on the Nakamoto Index, as we have seen validators raising to the top spots via 0% commission and currently the top validator has a total voting power of 5.56 % with still raising delegations, starting to make the Terra Validator set top heavy.
> 
> Further reducing the set and activating the community to redelegate, it is a good time to educate about the Nakamoto Coefficient, so they actively can choose to improve it. If we say active wallets of the bottom 50 validators randomly redelegate to validators, they have almost a 75% chance to improve the Nakamoto coefficient. ((70-18)/70)

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2023-10-27T19:16:31.222Z

as it will come as no surprise to people,
I am opposed to this. (this is going to be long.. sorry but there is a lot going on in here)

my main concern is that it adds** no value to the chain**. It just changes who is getting the rewards, and some unlucky chumps who got stuck on lower-ranked validators will get penalized through no fault of their own. it does increase rewards for LSDs as well, as more rewards/APY = higher fees for them.

**but validators are rent-seeking?**

Most validators got into this business to make money. Some for themselves, others for charities. We charge the commission we do and people are free to move off and re-delegate as they wish. The infrastructure I provide as a validator is based on technical concerns, not revenue. I could run it cheaper, but then it would blow up when it is needed.  
We saw this in May 2022 when half the validators failed, because they were doing the bare minimum. I personally adjust my commission rate based on delegations and price. 

Implementing a maximum commission (or minimum) commission is reducing free market choice. No one is forcing you to stake on a 100% validator, and if people want to run a loss-leader for their own purposes (or tax reasons) then why shouldn't they? 

**the initial allocation was flawed**
while the initial allocation wasn't perfect. (and I was a major objector to some of the things that occured at the time), it was good enough, and we need to get over it. 
People who had luna on the old chain had luna on the new one, and had 2-4 years to vest that. Some probably took the long term view to just leave it alone for 4 years. others with very short term views busily just traded and sold. Now we are going to penalize people who took the long term view and happened to land on the bottom 50. 

also why 70 validators? why not 50? or 90? 

**but APY will be higher?? **
most chains have already realized that inflationary tokens are not a good thing, and are working to reduce their inflation amounts. ETH is around 2% yield at the moment I believe. we should be working at reducing our overall APY. People who like inflationary tokens are short-term yield farmers. they are mercenary, and detrimental to the chain in the medium-long term.

**better for decentralization?**
how can less choice be better for decentralization? nakamoto scores are just one way to measure decentralization. but how can less choice be better for anyone? now.. having caps on the maximum voting power would be interesting

# So what should we do?

**the TFL Community grant program**
I think that this is the way forward. we (well TFL or it's delegates) can decide how to allocate the community funds to validators who provide value. The rankings will shift according to that. 

**reduce the inflation amount**
lets get less new LUNA entering into the system. we should be reducing inflation to zero. (over time) and the fees generated by dApps on the chain should be rewarding people who stake.

KUJI is the poster boy for real yield. .. it works. we should move that way, like others are

> **Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2023-10-27T20:13:48.278Z (edited 2023-10-27T20:52:33.793Z)
> 
> I do agree that validators should be able to choose their commission rate how they see fit and want to run their business. However this proposal is very unique to the Terra Blockchain. Much of the genesis delegation is inactive stake, that means that normal factors like redelegation based on commission fee is not working to balance delegation and good behavior is not incentivized enough.
> 
> I believe in the notion that validators do what is best for the chain and only take the fees they require to run their business, so while active wallets will redelegate, hopefully validators like yourself that depend on delegation amount and LUNA price can reduce their commission again to fit their formula due to new delegations. This redelegation process will also give very good insights into how many wallets are really active from genesis.
> 
> Inflation is also one of these heated topics that happen from time to time on chains and also on Cosmos Hub right now. There is one faction, that says if you stake your coins inflation doesn't matter to you and then others are fans of deflationary tokenomics. The protocol I am involved in is generating revenue from yield transformation. Much of that yield is coming for inflation. I think there should be a healthy balance to be struck and certainly it should be evaluated to additionally reduce inflation in a follow up proposal. What we probably all aggree is that Terra is overspending on Economic Security, paying 35 M$ a year to secure 6 M$ TVL is also an issue that need to be balanced, but we first need to see how TFL plans to deploy their capital on Terra so we can calculate the right amount. As far as I have seen in the community or heard in the TFL space is that Growth DAO is engaged in creating some dynamic inflation model, which I am looking forward to seeing.
> 
> The previous (discarded) version of the proposal had included a max commission of 10%, that I received a lot of strongly opinionated feedback that it shouldn't be included. If the community wants to include that, I am happy to add a maximum commission too. 
> 
> Most of the reasons why I think this improves decentralization are shared in the comment below Chris: [https://commonwealth.im/terra/discussion/13870-terra-validator-reformation-forging-a-stronger-future?comment=69156](https://commonwealth.im/terra/discussion/13870-terra-validator-reformation-forging-a-stronger-future?comment=69156)

