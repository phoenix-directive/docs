# Deploy LUNA to the stLUNA liquidity pool

- **Thread ID:** 12174
- **Author:** Anonymous (`terra15rx7anfy3rj2sn5znpq42j5rfl8m8rhk40f997`)
- **Created:** 2023-07-14T12:28:20.838Z
- **Last edited:** 2023-07-21T13:25:02.095Z
- **Stage:** discussion
- **Views:** 121
- **Reactions:** 0
- **Comments:** 9
- **Source:** https://common.xyz/terra/discussion/12174-deploy-luna-to-the-stluna-liquidity-pool

---

## Overview

Recently, Terra governance [passed a proposal](https://station.terra.money/proposal/phoenix-1/4736) to support Terra DeFi by deploying a total of 5M LUNA to ampLUNA and bLUNA liquidity pools. However, that proposal overlooked stLUNA.  

Seeing as stLUNA plays a key role in the Terra DeFi ecosystem, this current proposal seeks to give equal treatment to stLUNA, by deploying 2.5M LUNA to the stLUNA-LUNA Astroport pool.

By supporting several different LUNA LSTs, Terra governance can help make the Terra DeFi ecosystem more vibrant and resilient.

The LUNA being requested would remain the property of Terra governance, and would be stewarded by a multisig controlled by trusted community members. At any time, Terra governance would be free to order the LUNA to be returned to the community pool.


## Justification

In early 2023, Stride contributors were attracted to the Terra ecosystem by the success of Terra’s recovery. In February, Stride deployed its liquid staking to Terra, using an interchain account (ICA) on Terra controlled by the Stride blockchain. All expenses involved were borne by Stride Labs, without any sort of grant from the Terra community.

Since then, stLUNA has become the second biggest LUNA LST, generating transaction fees for LUNA stakers and leading to increased economic activity for Terra. stLUNA currently has a deep liquidity pool on Astroport, externally incentivized by the Stride DAO. stLUNA has been integrated by Cavern protocol on Terra, and has helped to spread LUNA throughout the Cosmos through an integration with the Demex money market. stLUNA is also a stakable token on the Alliance chain Carbon.

While there are many LUNA LSTs, Stride’s stLUNA differentiates itself from the rest through its robust decentralization. stLUNA is issued by the Stride blockchain, which is a Cosmos blockchain governed by the STRD token using Tendermint consensus. As such, the only way to change the Stride code is through an open, transparent, decentralized governance process. No one entity or small group controls the Stride blockchain. Stride is the only LUNA liquid staking provider to use an open, transparent governance system to control code access.

In addition, Stride has cutting edge security features, such as IBC rate-limiting, interchain security, and chain minimalism. The Stride code base has had [three comprehensive audits](https://github.com/Stride-Labs/audits) from separate security firms, and Informal Systems has been retained to provide continuous auditing of all new code.


## Shade Protocol integration

Contingent on Terra governance deploying LUNA liquidity to the stLUNA pool, Shade Protocol plans to add stLUNA as a collateral token for its SILK stablecoin. This would mark the first non-Terra stablecoin backed by a liquid staked token of LUNA, and would bolster LUNA’s profile in the Cosmos.

A key part of Terra’s continuing recovery is popularizing LUNA throughout the Cosmos, both through the spread of Alliance and integrations with existing Cosmos DeFi apps. Stride’s decentralization, high security standards, and large Cosmos user-base make stLUNA a good candidate to help in this effort.


## Details  

If this proposal passes, 2.5M LUNA will be sent to an Enterprise multisig address. The multisig group is currently being formed. Once the signers are ready, their names as well as the multisig address will be added to this proposal. This will happen before the proposal goes onchain.

The LUNA sent to this address would remain the property of Terra governance. The multisig signers would be stewarding the funds on behalf of Terra governance. The signers have bound themselves to follow this specific set of instructions:

Upon receipt of the LUNA, as soon as possible the signers will deploy it to the stLUNA-LUNA liquidity pool on Astroport Terra. They will first liquid stake half the LUNA with Stride, and then add both the stLUNA and LUNA to the pool. They will then hold the resultant LP tokens in the multisig address, without bonding them in the Astroport generator. Once this is complete, the signers will do nothing with the LP tokens, unless ordered to by Terra governance. At any time, Terra governance is free to order the return or transfer of part or all of the funds. This would be done by passing a signaling proposal. The multisig signers are obliged to follow any such orders from Terra governance.


## Final thoughts

Stride’s stLUNA is a key part of the Terra ecosystem, with integrations on Terra and throughout the Cosmos. Providing liquidity to the stLUNA pool will help stLUNA continue to serve Terra, both on the Terra chain and in the greater Cosmos.

Furthermore, by providing LUNA to the stLUNA pool Terra governance will be treating all major LUNA LSTs equally. And if governance treats all major LUNA LSTs equally, LUNA holders will be able to make their own decision as to which they would like to use. It would level the playing field.

Pending community discussion, this proposal will go onchain soon. In the meantime, please ask questions or provide comments.

_Disclaimer: I am an employee of Stride Labs._

---

## Comments (9)

**Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2023-07-14T13:59:43.282Z (edited 2023-07-14T15:22:14.399Z) — 👍 7

Hi John,
 
generally the case you make is a weak one. 
 
Asking for liquidity based on other projects and their contributions seems envious and can be observed as repeated behavior from Stride.
 
Stride does not have Terra's best interests at heart:
 
- Stride actively removed Astroport incentives from Backbone and ERIS liquidity
- Stride makes no progress on the long announced Terra Airdrop
- Stride regularly shows anti-competitive behavior behind closed doors against Terra projects such as ERIS and Backbone. (Cases: Carbon incentives, Injective)
- Stride actively wants to reduce Astroport incentives for the whole community without any backing data except their personal feeling toward Terra ([https://forum.astroport.fi/t/disregard-this-post/1136](https://forum.astroport.fi/t/disregard-this-post/1136))
- Stride validatorset on Terra is more than questionable, with many delegations to non-value providing validators ([https://chainsco.pe/terra2/address/terra1ap70xcsx25u5ke77jmajdkza0lr7jr5mun98zsalzlr7z20hxa8slsnpaa/delegations](https://chainsco.pe/terra2/address/terra1ap70xcsx25u5ke77jmajdkza0lr7jr5mun98zsalzlr7z20hxa8slsnpaa/delegations))
- STRD holders (see also next point) have control over delegations and governance power - not the Terra community.

 
Decentralization of Stride is a sham:
- "Stride DAO" makes decisions without an onchain vote
- Stride Team & Insiders hold more than 50% of the voting power. ([https://www.stride.zone/blog/stride-tokenomics](https://www.stride.zone/blog/stride-tokenomics))
- For security reasons there is less STRD supply in the market than the Stride Foundation delegations, making the chain de facto a proof of authority chain. Nothing decentralized about that, more like an incentivized multi-sig.
- Last time I checked, the LP staking contract (on Astroport) of Stride is held by a single wallet controlled by Stride. That means the whole funds of stLUNA-LUNA in the Astroport DEX can be rugged by that wallet.

 
Stride is not a key part of the Terra ecosystem and needs to show improvements on contributing to Terra before asking for a liquidity grant.
 
**Governance has not decided to treat LUNA LSTs equally**, but that the contributions of ERIS and Backbone Labs are rewarded by providing community owned liquidity.
 
**Your proposal wants to set the precedence for equality, which I do not support**. This will open a pandora's box.
 
So while I have Conflict of Interest - as almost everyone participating in cosmos governance - I urge the community to consider the points made.
 
Best Philipp
 
_Disclaimer: I am part of the ERIS protocol core team and to be frank am a bit allergic to the arrogant attitude._

> **Anonymous (`terra15rx7anfy3rj2sn5znpq42j5rfl8m8rhk40f997`)** — 2023-07-17T13:28:23.583Z
> 
> Hey, Philip. Let me respond to these points, being as objective as possible.
> 
> stLUNA is the second biggest LUNA LST, and has the deepest liquidity pool of all the LUNA LSTs. It is integrated on Cavern, on Demex, and is stakable on Carbon. Also, it will likely soon be integrated with Shade Protocol. stLUNA is clearly an important part of the Terra ecosystem, and is playing an important part in Terra's recovery.
> 
> About decentralization, it's a simple fact that Stride is the most decentralized LUNA LST provider. Stride is a Cosmos blockchain with Tendermint consensus, meaning that all code changes have to be voted on by governance. And governance power, which resides in the STRD token, has been distributed among dozens of entities and thousands of individuals. Objectively, this is more decentralized than Eris and BackBone, for which code access is governed by multisigs.
> 
> And ultimately, Stride is a very different sort of organization than Eris and BackBone. Stride has tens of thousands of users throughout the Cosmos, Stride is independently funded, Stride's contributors are DOXed, Stride contributors work closely with contributors to many other Cosmos projects. And of course, Stride is decentralized, whereas other LUNA LSTs are ultimately run by multisigs.
> 
> Ultimately, we need to ask ourselves: what's best for the Terra ecosystem?
> 
> Stride supports Terra, Stride offers a uniquely decentralized LUNA LST, and ultimately Stride is structed much differently than Eris and BackBone. Should only one sort of LUNA LST be supported by governance, or should multiple sorts be supported? Fundamentally, I think Terra will be stronger with multiple different LUNA LST options.
> 
> More options means more diversity, more resilience, and greater strength.

> > **BackBone Labs (`terra1gw8mesks5uw2gukjfv9xftf5xh0xn8empydw2t`)** — 2023-07-17T15:55:57.388Z — 👍 3
> > 
> > You didn't really address any of these points that @0xPhilipp has raised and glazed over the most important points. Some clarity on the points below and the controlling wallets would be appreciated.
> > 
> > Stride does not have Terra’s best interests at heart:
> > Stride actively removed Astroport incentives from Backbone and ERIS liquidity
> > Stride makes no progress on the long-announced Terra Airdrop
> > Stride regularly shows anti-competitive behavior behind closed doors against Terra projects such as ERIS and Backbone. (Cases: Carbon incentives, Injective)
> > Stride actively wants to reduce Astroport incentives for the whole community without any backing data except their personal feeling toward Terra (https://forum.astroport.fi/t/disregard-this-post/1136)
> > Stride validator set on Terra is more than questionable, with many delegations to non-value-providing validators (https://chainsco.pe/terra2/address/terra1ap70xcsx25u5ke77jmajdkza0lr7jr5mun98zsalzlr7z20hxa8slsnpaa/delegations)
> > STRD holders (see also next point) have control over delegations and governance power - not the Terra community.
> > 
> >  Decentralization of Stride is a sham:
> > “Stride DAO” makes decisions without an on-chain vote
> > Stride Team & Insiders hold more than 50% of the voting power. (https://www.stride.zone/blog/stride-tokenomics)
> > For security reasons there is less STRD supply in the market than the Stride Foundation delegations, making the chain de facto a proof of authority chain. Nothing decentralized about that, more like an incentivized multi-sig.
> > Last time I checked, Stride's LP staking contract (on Astroport) is held by a single wallet controlled by Stride. That means the whole funds of stLUNA-LUNA in the Astroport DEX can be rugged by that wallet.

**BackBone Labs (`terra1gw8mesks5uw2gukjfv9xftf5xh0xn8empydw2t`)** — 2023-07-14T14:01:29.440Z — 👍 6

It did not overlook stLUNA. The previous prop was specifically for teams and projects building on terra. STRIDE is its own chain and does not build anything on the Terra chain for the Terra community. 

IMO Stride needs to form an alliance with Terra chain to chain and not ask for a handout from our community.   

They do not drive value back to our chain in any way.

We will be voting NO and encouraging others to do so as well.

**Heisemberg (`terra13lq28yy2hzmxn3m4t5qgs0mjvgyx9vwmp66zdn`)** — 2023-07-15T11:57:57.900Z — 👍 4

I agree with [@BackBone Labs](/profile/id/97077) and [@0xPhilipp](/profile/id/61123) , before asking for liquidity support, the Terra community, I believe, wants to see your effective contribution to the Terra ecosystem, maybe join its alliance, there are expert people here, and they can understand certain dynamics , among other things, the effort made by backnone and Eris is visible to everyone, I honestly don't see anything of stride ...

**ZorroTicToc (`terra1xmm86htuyljhgxkh5yefkmqavxd9dj5hesv3rn`)** — 2023-07-15T16:15:22.124Z — 👍 4

As a general principle, considering the bear market and following the Luna 1.0 crash and all consequences on a lot of people, I think funding should be restricted to the Terra ecosystem exclusively. So, I look at this unfavourably.

**Sen Com (`terra1jlcqudqhzemqtq7uga53q07cukzju6ddtsrz7v`)** — 2023-07-17T06:48:14.896Z — 👍 3

Dear John,

Let's dive right in, picking up from where we left off on the discussion of the liquidity injection proposal by Backbone Labs and Eris Protocol that passed with overwhelming support.

First, your call for equality is hollow. Nowhere did you provide tangible reasons why you think a uniform approach could benefit the Terra community, especially in the context of Stride's stLUNA.

As for Stride's touted "decentralization," I have conclusively proved this claim to be false, yet, it keeps resurfacing in your proposals and comments. Is this a case of an inability to digest the evidence at hand, John, or are you persisting with this false claim for a different reason?

Lastly, it is profoundly disappointing that you have, yet again, failed to address the additional risk posed by incorporating Stride's stLUNA and its weakening effect on Terra's native protocols. Isn't the purpose of our discussion to address all risks and potential benefits of your proposal?

John, I hope we can use this opportunity to address all points above sufficiently, and I look forward to your response.


Warm Regards, 

Sen Com

**RileyE (`terra17yeg7usw58ykccrgjya542xck87w0apnff37lu`)** — 2023-07-24T21:40:02.439Z — 👍 2

Thanks for your responses, Phillip and BackBone. 

I wanted to chime in with a few clarifications:

Stride contributes positively to Terra:

Stride deployed stLUNA through an interchain account on Terra, for the Terra community. Stride has deployed over $175,000 in external incentives on the Terra blockchain, and used them to distribute incentives for the Terra community. Stride denominated these incentives in xAstro, to best serve the Terra community. Stride collaborates with Astroport on Terra, with Cavern on Terra, and with Capa on Terra. In my opinion, Stride’s greatest contribution to the Terra ecosystem is making available an LST product that’s diversifying to the others, for the community to have a choice. 

The degree of incentive spend and stLUNA’s diversifying product features are made possible by Stride’s app-chain design. In my opinion, Stride’s app-chain design is a strength, not a weakness: If Stride were built as a smart contract, Stride would not be able to maintain deep liquidity for the Terra community and offer safety features like rate-limiting and blockly invariant checks, for the Terra community. 

Stride is distributing an airdrop to the Terra community, to give the community ownership over the protocol. All Stride airdrops have been released sequentially, in the order chains were onboarded, and the Terra airdrop is on schedule as expected. There has often been a considerable lag between the on-boarding of a new chain and that chain’s airdrop becoming claimable. This was the case for the first chains to receive a Stride airdrop, and it contributes to be the case today. Terra is included in the Airdrop Program, so its airdrop will eventually become claimable. Considering developer resources, the Terra airdrop is expected to be claimable by late Q3 / early Q4 2023. Please see the blog for further details: [https://www.stride.zone/blog/stride-airdrop-details](https://www.stride.zone/blog/stride-airdrop-details). 

Stride is decentralized:

Regarding decentralization: as an ICS chain, Stride uses the Cosmos Hub validator set, the oldest and one of the most decentralized delegator and validator sets in the Interchain. If Stride wanted to make a malicious change, it would have to first go through Stride governance and then be executed by Cosmos Hub validators. Very unlikely to happen. Stride’s tokenomics were designed to ensure the community has over 50% voting power. That’s reflected in the link provided. A portion of this majority community share is distributed directly to the Terra community through Astroport incentives and the Terra airdrop. If you want to make the argument that Stride’s governance is like an incentivized multisig, you’d have to apply that reasoning to all Cosmos chains. Stride’s terminal token distribution is similar to most other Cosmos blockchains, including Terra itself (56% of tokens were held by Labs, employees and backers). The reality is that Stride and Terra are decentralized blockchains with hundreds of validators, and many checks and balances. The LP staking contract on Astroport is in the process of being migrated so that it is controlled to Astroport governance. 

Regarding delegations, Stride starts with a neutral copy-staking strategy (balancing delegations across the top 35 or so validators), then moves to a council system to ensure delegations decentralize the chain. Stride contributors don’t run this process, neutral community members of each ecosystem do. 

Stride is not trying to set a precedent for equality, but we believe that an objective analysis of the situation shows that Stride is a strong contributor to the Terra ecosystem and community and is a decentralized, secure LST. 

Protocol owned liquidity for stLUNA/LUNA will make the entire Terra ecosystem stronger.

> **BackBone Labs (`terra1gw8mesks5uw2gukjfv9xftf5xh0xn8empydw2t`)** — 2023-07-25T03:43:03.563Z — 👍 1
> 
> Dear Rob,
> 
> I sincerely appreciate your attention to the matters raised by the community concerning this proposition.
> 
> What continues to perplex me is the rationale behind STRIDE's involvement in creating props in this context. Wouldn't it be more appropriate to propose acquiring $LUNA on STRIDE's chain? Especially considering the substantial financial resources at STRIDE's disposal, which I must emphasize are quite significant.
> 
> $LUNA, being permissionless and open to collaboration, presents an interesting opportunity. However, it seems counterproductive for the community pool to allocate liquidity or funding to another chain that is not built on Terra, has not joined the Alliance module, and emphasizes ICS. These actions by STRIDE appear to diverge from the collective goals we are striving to accomplish on Terra at present. It is important to acknowledge that Terra already hosts thriving LSTs, making it questionable to seek funding redundancy through the CP.
> 
> To be candid, the entire proposal feels rushed, inadequately deliberated, and somewhat coerced.
> 
> Furthermore, I would like to inquire about the timeline for the STRIDE airdrop. Before seeking any favors from the LUNA community, shouldn't we prioritize taking care of their interests?
> 
> Sincerely,
> 
> JG

