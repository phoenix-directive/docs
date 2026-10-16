# Alliance Follow-on Proposal

- **Thread ID:** 12477
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2023-08-01T19:53:23.911Z
- **Last edited:** 2023-08-11T10:56:07.075Z
- **Stage:** discussion
- **Views:** 213
- **Reactions:** 5
- **Comments:** 9
- **Source:** https://common.xyz/terra/discussion/12477-alliance-follow-on-proposal

---

_Disclaimer: I am an employee at Terraform Labs_

## **Summary**

This is a follow-on proposal to execute the ideas proposed in the **[Alliance Signaling Proposal](https://agora.terra.money/discussion/11500-alliance-signaling-proposal)** that **[passed](https://station.terra.money/proposal/phoenix-1/4726)** on June 8th, 2023. To recap, the approach outlined in the Alliance Signaling Proposal aims to:

- Incentivize the adoption of the Alliance module and the formation of mutually beneficial economic alliances between $LUNA and other Cosmos ecosystems
- Cross-pollinate users and liquidity between Terra and allied chains


To accomplish this, the Terra community voted to allocate 3% of LUNA staking rewards to the first ten Cosmos chains that:

- Integrate the Alliance module
- Whitelist at least one $LUNA Liquid Staking Token (LST) as an Alliance asset with a positive yield (i.e., the total $ value provided via the RewardWeight exceeds the total $ value of $LUNA LSTs acquired via the TakeRate)


On Terra, we proposed whitelisting LSTs representing each of these chains’ native tokens as Alliance assets. The portion of the combined 3% RewardWeight each LST is to be allocated will be dynamically calculated based on the yield the allied chain offers to $LUNA LST Alliance stakers. The higher the APR, the higher the RewardWeight the allied chain’s LSTs will be allocated on Terra. Multiple LSTs can be added as Alliance assets for each allied chain, and the rewards distributed to each LST for a given chain will be uniformly distributed.

Since the Alliance Signaling Proposal was approved, TFL has developed the smart contracts outlined in the proposal that:

- Mint a virtual staking token ($VT) to be added as a Terra Alliance asset and awarded a RewardWeight that gradually increases to a maximum of 3%. This token will represent the total amount of $LUNA staking rewards that can be distributed to all LSTs for each of the first ten chains that meet the above requirements
- Pull in $LUNA LST yield data from allied chains via an oracle contract and dynamically calculate and distribute the portion of the total RewardWeight to be allocated to each chain's tokens from $VT
- Allow users to stake and claim $LUNA staking rewards on Station using allied LSTs (e.g., $ampWHALE, $bWHALE, $rSWTH, etc.)


**[FYEO](https://twitter.com/goFYEO) **is currently auditing the smart contracts. We will share the full audit report for transparency once the audit is complete and TFL has remediated any bugs identified.

**In line with the objectives of the Alliance Signaling Proposal, this proposal aims to:**

1. Whitelist $VT (We will provide a link once the audit is complete and the token has been minted) as an Alliance asset with a RewardWeight of 3% and TakeRate of 0%
2. Incrementally increase $VT’s RewardWeight by ~47% each month for six months from 0.3% to its final target of 3%
3. Whitelist the LSTs for the first two chains that have met the eligibility requirements into the Alliance protocol to begin dynamically distributing rewards to stakers
4. **Carbon: $rSWTH **
5. **Migaloo: $bWHALE and $ampWHALE**


We will split this Agora post into two on-chain proposals that can be voted on simultaneously: one to achieve points (1) and (2) and another to accomplish point (3). 

## **Implementation**

Earning Boosted Yield on Terra

Following this proposal’s approval, the protocol that dynamically calculates and redistributes Alliance rewards from $VT to whitelisted tokens will be incorporated into Station’s backend, allowing users to stake allied LSTs and earn an additional yield on top of native staking yield via $LUNA staking rewards. 

User Flow:

1. User stakes their native tokens with their preferred LST provider on an allied chain, and IBC’s them to Terra using the Send button on Station
2. User stakes their LSTs via the **[Quick Stake](https://station.terra.money/stake)** tab on Station’s Stake page, which will interact with this new protocol on the backend
3. $LUNA rewards are streamed to the user every block, which they can claim directly from the Stake page


![](https://lh6.googleusercontent.com/OgRC_pRcCUz3jTuAeMdTCOZN1vy6CQ95GGeaT3rDgixfhM8uOy4zKJZNuutONmKB9HeA9oeHX2WallOSsJJOZ_WAbgTwkIye9B6N1MT_KNPPGoNyJZcqN0DjnJ52pmY2rJllvsfmgv-_-BoVUqLsaVY)
_Image 1: Quick Stake on Station’s Stake Page_

Validator Selection Criteria

Terra validators seeking to receive virtual Alliance delegations must meet the following criteria:

- Positioned in the active validator set
- Commission rate less than 20%
- Voted on the last three governance proposals
- Is not jailed at the block in which the contracts updates the delegations
- Must have been in the active set for at least 100K blocks before the block height when the user is looking to delegate (approximately one week)


The smart contracts will split delegations equally among all eligible validators and review them programmatically every 28 days (unbonding period).

Timeline

After FYEO completes the smart contract audit on Aug. 3rd and TFL resolves any bugs, we will deploy the contracts and append links to $VT, the contracts, and the audit report to this post. We will then publish both proposals on-chain.

Following both proposals being approved, there will be a seven-day period before staking rewards start flowing into the contracts. During this time, users have the opportunity to stake allied LSTs on Terra to qualify for a boosted yield, although rewards will not be distributed until the seven-day period has concluded.

Additional Information

For more details on proposal implementation, including what happens when new Alliances are formed, allied chains cease rewarding $LUNA Alliance stakers, or validators are slashed, jailed, or tombstoned, please see the original **[Alliance Signaling Proposal](https://agora.terra.money/discussion/11500-alliance-signaling-proposal)**.

—

This proposal aims to execute the ideas proposed in the Alliance Signaling Proposal. By supporting and incentivizing economic alliances between Terra and other Cosmos ecosystems through a dynamic reward system, we seek to foster cross-pollination of users and liquidity, improving the overall strength of $LUNA and creating a more united, interconnected blockchain ecosystem.

---

## Comments (9)

**Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2023-08-02T13:14:57.658Z (edited 2023-08-05T22:40:44.139Z) — 👍 2

I am in support of this proposal. 

I would have liked to see a mechanism to allow users to vote on the delegations, so we have active capital deciding who receives delegations, but I understand that the additional implementation complexity might not be ideal.

I think that 20% max commission rate is a bit high and randomly chosen. These are the criterias for the current quick stake feature in station and I would prefer to have the same criteria for both quick stake and alliance quick stake:

1. **Discard top 33% by Voting power.** -**query total luna staked, remove validators from list from highest quantity of luna bonded until 33% of bonded luna is accounted for** 
2. **Query for slashing events in last 1,200,000 blocks** -**remove any validators who were slashed** 
3. **Remove any validators over 5% commission**


I propose that we find some common grounds between the proposed and the existing quick stake feature and use the same criteria for both features:
1. Not bottom 10 validators (risk of dropping out of the set)
2. No slashes since the last rebalance (~28 days)
3. Max commission 10%
4. Must have been in the active set for at least 7 days
5. Not jailed

> **BackBone Labs (`terra1gw8mesks5uw2gukjfv9xftf5xh0xn8empydw2t`)** — 2023-08-02T15:16:58.421Z
> 
> We agree with these proposed adjustments.

> **MB aejir (`terra10ql0yxam88pg0a02946pzv36a3w699shl9r3mc`)** — 2023-08-05T11:06:47.928Z (edited 2023-08-05T22:53:11.497Z) — 👍 1
> 
> Hey Philipp
> 
> Apart from the first criteria (top 10% by voting power excluded - and since removed), I think your recommendation for some reasonable criteria for validator eligibility is needed and should be included in the proposal. 
> 
> 
> I do think that a seperate discussion is also needed on how to improve the active validator set including how to incentivise increased validator engagement and contributions on Terra. Its a worthwhile topic for the Ideas & Suggestions section or a seperate proposal and discussion.

> **4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2023-08-06T06:44:58.501Z — 👍 1
> 
> I think validator eligibility & criteria should be a separate discussion & prop as there are different opinions on these parameters & we shouldn’t delay the alliance prop waiting for validators to agree on acceptable parameters for all.

> **Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)** — 2023-08-08T10:08:09.936Z — 👍 1
> 
> Hi Philipp,
> 
> Ideally, we should have a better mechanism that allows users to vote on delegation. (Something similar to how ampLUNA does it). However, in the interests of time and complexity to implement this, we have chosen to go with a simpler solution. One thing, 20% does seem a little high given that quick stake uses 5%. we will update the proposal to use 10% as you suggested. 
> 
> Agree with [@4719](/profile/id/65121) that the validator eligibility & criteria should be a separate discussion. The current values were chosen so that it isn't too restrictive in terms of picking validators which might cause more friction to get this up. Willing to re-open this discussion right after this proposal to fine tune the criteria further.

**BackBone Labs (`terra1gw8mesks5uw2gukjfv9xftf5xh0xn8empydw2t`)** — 2023-08-02T15:15:16.376Z

This is a big YES for us at BBL. 

It is time to show the true power of "Alliance"

**4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2023-08-03T11:16:51.985Z

I fully support the proposal. We will be voting YES.

**MB aejir (`terra10ql0yxam88pg0a02946pzv36a3w699shl9r3mc`)** — 2023-08-05T09:44:20.837Z

This proposal looks good. Lets get it done and get Alliance into top gear.

**Anonymous (`terra147k94m5sr5gz7e905vhpkrr5y8u52yspkt4hjk`)** — 2023-08-07T14:37:29.212Z — 👍 1

This is what we need for Terra to grow.
PFC supports this, and will vote YES

