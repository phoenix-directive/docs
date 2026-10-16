# ALLY Alliance Asset Proposal (Updated)

- **Thread ID:** 15252
- **Author:** Evan_docs (`terra1nhvjgyga4yfkmzv7ts79vu3w2azj6mes0jhccm`)
- **Collaborators:** swgee, telperion3066
- **Created:** 2024-02-09T16:49:17.794Z
- **Last edited:** 2024-02-16T19:50:30.061Z
- **Stage:** discussion
- **Views:** 639
- **Reactions:** 10
- **Comments:** 31
- **Source:** https://common.xyz/terra/discussion/15252-ally-alliance-asset-proposal-updated

---

# Summary

	This is a proposal to add the ALLY token to the Terra blockchain as an Alliance asset, allowing the AllianceDAO NFT contract to stake ALLY to Terra validators and accrue LUNA staking rewards. LUNA staking rewards accrued by ALLY will be distributed to and locked into unbroken AllianceDAO NFTs. The proposed [reward weight](https://docs.alliance.money/concepts/staking#reward-weight) is .003 (0.29% of LUNA staking rewards) with a 0% [take rate](https://docs.alliance.money/concepts/rewards#takerate). By adding ALLY as an Alliance asset, this prop seeks to establish a unique role for AllianceDAO in promoting the adoption and evolution of the Alliance module for Terra and its community. As a leading force driving the success of Alliance throughout Cosmos, AllianceDAO’s ultimate goal is to draw new users and activity back to Terra for the benefit of the Terra ecosystem.

# Benefits to the LUNAtic Community

	Whitelisting ALLY as an Alliance asset and giving LUNAtics opportunities to join and participate in AllianceDAO, including upcoming NFT mints (See [Phase 2 of ](https://alliance-dao.notion.site/alliance-dao/AllianceDAO-Growth-Proposal-ba2c8efd98314b5e9043df6820680f5d)this [recently approved](https://dao.enterprise.money/dao/proposal?address=terra1g0mfrpswewteaf9ky4rlj09wh5njp6u9xxk94uszplw4qz2f9mzq3k27fm&id=14) AllianceDAO governance proposal), presents several benefits to the Terra community, including:

1. **New LUNA Alliances with Other Cosmos Chains:** AllianceDAO will promote the adoption of the Alliance module and the whitelisting of LUNA LSTs as Alliance assets to other Cosmos chains, unlocking more cross-chain yield opportunities for Terra users, similar to the current alliances with Migaloo and Carbon.
2. **Community Growth & Engagement:** As an active participant in the Terra community, AllianceDAO will foster growth and retention of active users on Terra through initiatives such as the [AllianceDAO growth plan](https://alliance-dao.notion.site/alliance-dao/AllianceDAO-Growth-Proposal-ba2c8efd98314b5e9043df6820680f5d), which will give members of Terra NFT communities and general Terra users the chance to become members of AllianceDAO. Furthermore, AllianceDAO plans to host community Twitter/X Spaces and lead engaging activities, such as an upcoming story contest where users can build on the NFT backstory. 
3. **Reduction in LUNA Liquid Supply:** The NFT contract accrues and locks up LUNA in each NFT. Because these rewards can only be claimed once, holders are incentivized to keep their LUNA locked as long as possible, decreasing the amount of LUNA in active circulation and increasing the attractiveness of both the NFTs and LUNA.
4. **Increased Brand/Ecosystem Awareness:** The Alliance brand is tied to and supports the Terra brand (see the recent [Persistence One announcement](https://blog.persistence.one/2024/02/07/persistence-one-to-bring-restaking-to-cosmos/) for an example). Increased adoption of the Alliance module will boost Terra brand recognition, bring awareness to the Terra ecosystem, and show that Terra is continuing to build useful, innovative technology. This will provide positive attention to Terra apps and LUNA.
5. **Novel Terra NFT Use Cases:** While NFTs that generate staking rewards exist, AllianceDAO is the only NFT project with a unique accrual mechanism built specifically for native staking via the Alliance module. Terra will be the first chain to implement NFTs that directly accrue and lock tokens from staking rewards, continuing Terra’s track record of experimenting on the bleeding edge of blockchain-based incentives.
6. **Enterprise DAO Adoption:** As a DAO with the explicit goal of promoting Alliance to other chains and communities, AllianceDAO will also promote Enterprise DAO by demonstrating its features and utility to new communities. This will encourage Enterprise DAO adoption, which means more transaction volume (and more fees paid) on the Terra blockchain, which benefits all Terra ecosystem participants.


# Vision

	On January 17th, AllianceDAO [passed a proposal that solidified its mission](https://dao.enterprise.money/dao/proposal?address=terra1g0mfrpswewteaf9ky4rlj09wh5njp6u9xxk94uszplw4qz2f9mzq3k27fm&id=10) to promote the successful adoption and evolution of the Alliance module across Cosmos. With this goal in mind, AllianceDAO will focus on the following Alliance-specific development initiatives:

- **Education:** Creating educational content and hosting Twitter/X Spaces across Cosmos, initiating discussions, explaining Alliance, and exploring the creation of new cross-chain use cases.
- **Cross-chain Governance:** Actively engaging in and facilitating the adoption of the Alliance module and Alliance asset listings on Cosmos chains, including LUNA liquid staking tokens like ampLUNA, bLUNA, and stLUNA.
- **Community Building:** Harnessing the power of leading NFT and DeFi communities to establish cross-chain community partnerships that further AllianceDAO’s mission, and bring more attention to Alliance and Terra.
- **New Initiatives:** Conceiving new Alliance module use cases, both cross-chain and domestic.


In addition, AllianceDAO has put forth a [growth plan](https://alliance-dao.notion.site/alliance-dao/AllianceDAO-Growth-Proposal-ba2c8efd98314b5e9043df6820680f5d) to benefit the Terra community by whitelisting AllianceDAO NFTs to holders of Galactic Punks, Skeleton Punks, and PixeLions. A portion of NFTs will also be allocated for sale to the general Terra community.

# About AllianceDAO

	[AllianceDAO](https://medium.com/terra-money/introducing-alliancedao-84ab93501f3c) is an NFT project launched by TFL to reward participants of the Game of Alliance (GoA). It is now a fully independent and community-led DAO on Terra. A [Dao Council](https://dao.enterprise.money/dao/proposal?address=terra1g0mfrpswewteaf9ky4rlj09wh5njp6u9xxk94uszplw4qz2f9mzq3k27fm&id=11) was formed to lead the development of the DAO and further participation from community members in different roles is planned. 

	The GoA was an incentivized testnet designed to battle-test Terra’s Alliance module before its mainnet launch, and it ran from February 9th to March 2nd, 2023. During the game, users could stake on different Alliance chains and move their tokens around to optimize rewards as the Alliance asset parameters of assets on each chain changed. Scores were tracked, and participants were assigned a claimable NFT.

	The AllianceDAO NFT project was [launched](https://medium.com/terra-money/alliancedao-is-live-47aea2cdfb79) on December 12th, 2023, and the 1-month claim period lasted until January 12th, 2024. Once the claim period ended, all unclaimed NFTs were sent to the DAO treasury.

# How AllianceDAO NFTs work

	The same [smart contract](https://terrasco.pe/mainnet/address/terra1phr9fngjv7a8an4dhmhd0u0f98wazxfnzccqtyheq4zqrrp4fpuqw3apw9) that minted the AllianceDAO NFTs also minted a TokenFactory asset referred to as “ALLY”. This asset is solely owned by the contract, and will never be transferred to anyone outside of the contract.

	To leverage the power of Alliance, this proposal seeks to add the ALLY token as an Alliance asset on Terra, enabling the token to earn a portion of LUNA staking rewards. Upon the proposal’s passing, the AllianceDAO contract will stake ALLY to Terra validators (initial staking will be based on the same criteria as the [Terra Delegation Committee Phase 1 Recommendations](https://commonwealth.im/terra/discussion/14807-terra-delegation-committee-phase-1-recommendation)) to start earning LUNA rewards. The delegation of the asset will be controlled by AllianceDAO governance. Staking rewards will be collected periodically using [Warp Protocol](https://warp.money/home) and stored in the AllianceDAO contract.

	After the contract collects the staking rewards, each NFT will accrue rewards at an equal rate. At any point, NFT holders can connect their [Station](https://setup.station.money/) wallet to the [AllianceDAO NFT website](https://dao.alliance.money/) and “break” their NFT to claim their LUNA rewards. Importantly, NFT rewards can only be claimed _once_ per NFT. Once an NFT has been broken, no more Alliance staking rewards will accrue to it. Although broken NFTs no longer accrue Alliance staking rewards, they can still be staked to the AllianceDAO on Enterprise to participate in governance.

	Each “unbroken” NFT will receive an equal proportion of the ever-growing Alliance reward pool. As users break their NFTs to claim rewards, the amount of outstanding, unbroken NFTs gets smaller, and their share of the reward pool gets larger.

	For example, if you own one of 10,000 “unbroken” NFTs, your NFT represents 1/10,000 of the pool. If 6,000 people break their NFTs, the number of unbroken NFTs will shrink, and your claim on the pool becomes 1/4,000 of the pool. The longer you hold your NFT without breaking it, the greater the reward will become.

**Links:**

ALLY token address: [factory/terra1phr9fngjv7a8an4dhmhd0u0f98wazxfnzccqtyheq4zqrrp4fpuqw3apw9/AllianceNFT](https://terrasco.pe/mainnet/assets/factory%2Fterra1phr9fngjv7a8an4dhmhd0u0f98wazxfnzccqtyheq4zqrrp4fpuqw3apw9%2FAllianceNFT)

AllianceDAO NFT contract address: [terra1phr9fngjv7a8an4dhmhd0u0f98wazxfnzccqtyheq4zqrrp4fpuqw3apw9](https://terrasco.pe/mainnet/address/terra1phr9fngjv7a8an4dhmhd0u0f98wazxfnzccqtyheq4zqrrp4fpuqw3apw9)

[AllianceDAO NFT contract repo](https://github.com/terra-money/alliance-nft-collection)

[AllianceDAO NFT audit](https://github.com/terra-money/alliance-nft-collection/blob/main/Audit%20Report%20v1.0.pdf)

[AllianceDAO Enterprise site](https://dao.enterprise.money/dao?address=terra1g0mfrpswewteaf9ky4rlj09wh5njp6u9xxk94uszplw4qz2f9mzq3k27fm)

[AllianceDAO site](https://dao.alliance.money/)


#

---

## Comments (31)

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2024-02-10T07:36:29.646Z (edited 2024-02-14T07:53:06.246Z) — 👍 8

As part of the Alliance DAO council, I support this prop.

I expect this it to fly through governance. 

My only reservation is: should we be more bold? Pump the Reward Weight to 0.005? Proposal suggests 0.003.

More LUNA staking rewards going to Alliance DAO NFT holders makes it more financially attractive to become a member of the project.

> **Anonymous (`terra1vejelzded8yhd3hsnvqluuv3kkpjp4gz54px2v`)** — 2024-02-10T14:05:39.431Z (edited 2024-02-12T04:57:41.734Z) — 👍 5
> 
> yup, 0.003 is kinda low.

> **gram (`terra1pxarnnc703ly92e00txk4su2vh0muj4e704kq3`)** — 2024-02-10T16:01:41.121Z (edited 2024-02-12T04:57:52.372Z) — 👍 3
> 
> raise it praise it. we can go higher

> **Anonymous (`terra1dyh999cuqjkhadpfhh878sar73mrzy65695309`)** — 2024-02-10T17:53:44.104Z (edited 2024-02-12T04:58:14.515Z) — 👍 3
> 
> I support this initiative, but I believe increasing the reward rate for the first NFT Alliance asset on Terra to 0.01 is crucial. The current rate of 0.003 is significantly lower than what typically attracts users in the DeFi space, who are drawn to higher APRs and rewards. By offering a more competitive rate, we can generate fomo around this NFT

> **Anonymous (`terra1e3tzzc6hu4l6a73lkm2430ssumyjvw677f6j46`)** — 2024-02-11T21:00:21.163Z
> 
> I agree. Being bold here is the move. It will get more eyes on Alliance DAO and Terra.

**Opa (`juno15j46nt4mfsl3m0dugf8e5zxvjp8hgla4936aws`)** — 2024-02-10T15:14:08.538Z (edited 2024-02-14T07:53:18.292Z) — 👍 4

This is such an exciting development in the Alliance story. 

What is in store for the Alliance DAO, Alliance NFTs, and Alliance Staking opportunities with these development efforts is:

1. futuristic
2. cutting edge DeFi innovation
3. a demonstration of what Alliance features can offer the eager NFT communities across the Cosmos.

**gram (`terra1pxarnnc703ly92e00txk4su2vh0muj4e704kq3`)** — 2024-02-10T16:00:02.752Z (edited 2024-02-14T07:53:27.474Z) — 👍 6

LFGGGG!!

This is a v ery good prop. I support 100% and I think Allnodes should vote yes

Alliance will be very important to the future of LUNA. 

I think it could go higher we could even raise the reward to .01!

**4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2024-02-10T17:24:54.359Z (edited 2024-02-14T07:53:22.751Z) — 👍 3

4719 fully supports this prop.

**Anonymous (`terra1dyh999cuqjkhadpfhh878sar73mrzy65695309`)** — 2024-02-10T18:00:14.519Z (edited 2024-02-17T07:34:32.810Z) — 👍 5

I fully support this prop, but I believe increasing the reward rate for the first NFT Alliance asset on Terra to 0.01 is crucial. The current rate of 0.003 is significantly lower than what typically attracts users in the DeFi space, who are drawn to higher APRs and rewards. By offering a more competitive rate, we can generate fomo around this NFT

**Survivor (`terra1w5cjcvdkl004fzf0gxl8g8wga90kgk7pu2rjna`)** — 2024-02-11T09:49:34.317Z (edited 2024-02-17T07:34:04.645Z) — 👍 5

I agree with the community that high rewards could significantly boost the appeal of AllianceDAO NFTs. Offering substantial rewards is a strong draw for early users, and getting in early often sets the stage for success in such projects. Not only do these rewards provide immediate financial benefits, but they also create a sense of momentum and excitement around the project. This can lead to more people joining and investing, further increasing the project's value and impact. Early adopters not only stand to gain from the initial rewards but also from the potential long-term growth of the project, as their early involvement could grant them a more influential role in the community and decision-making process.

**Anonymous (`terra1f98h23ty0wkxl0xrdd2pdtye7457aphjvull79`)** — 2024-02-11T19:54:47.300Z (edited 2024-02-17T07:33:23.605Z) — 👍 5

**Support this 100%. I believe a reward rate of 0.01 would significantly benefit the Alliance NFTs community because:**
- Higher rewards can create FOMO, leading to a higher price benefit for all NFT holders and the community.
- Setting a higher value encourages long-term holding, reducing the number of NFTs being broken.
- It becomes more attractive to other communities, allowing us to create new strategies for new alliances. Currently, 0.003 is too low to generate interest.

**Anonymous (`terra1rgy034k3kw2dltz7075uhcqcz0enfmqzegxl3h`)** — 2024-02-11T20:05:42.752Z (edited 2024-02-17T07:33:28.793Z) — 👍 3

This proposal is well outlined and touched almost everything AllianceDAO NFT wants to accomplish.
I personally would like to see a higher reward weight though, namely 0.01.
At a RW 0.01 NFTs will get around 2100 luna daily allocation, meaning every NFT ~0.22 luna/day.
There are only 39 wallets that hold more than 1 NFT and still ~8000 NFTs not allocated. As per AllianceDAO´s plan future distribution will also be only 1 per wallet. My argument here is, if we keep the RW at 0.003, we might get less engagement than intended, as most of the holders will eventually have only 1 NFT. Best case scenario at 0.01 all Nfts stays unbroken and a lot of luna outside circulation. :)

**edwinson (`terra142qw5y37henygqjynha073ns28lratpx7edxql`)** — 2024-02-11T22:03:50.580Z (edited 2024-02-12T22:23:39.078Z) — 👍 4

# **I fully support this prop 100%**
But I think RW. 0.003 is too low, raising the RW to 0.006 til 0.01 would be good. NFTs will become more valuable, and attract more new NFT holders for Community Growth.

**mka (`terra1gxt6j7lh9wq4767knwvtsry2wr8qkt452rh2vz`)** — 2024-02-12T05:38:19.004Z (edited 2024-02-12T20:21:29.122Z) — 👍 1

I support the proposal and fully agree with the stated benefits, however, I believe that the proposed RW of 0.003 is very low.  Higher RW will be more effective in enabling and achieving the benefits mentioned in the proposal.

**Anonymous (`terra19v62f65v9kdy05c48v6fgnf4yvrqsjvqqyp8n0`)** — 2024-02-12T11:45:24.122Z (edited 2024-02-15T15:35:03.313Z) — 👍 3

Alliance NFTs should be a tool to attract and unite other communities so giving value to the NFT is a good idea. I also agree with the proposed reward weight because at this time Alliance community still have to prove that is usefull and not just another NFT collection with members that only cares about pumping their bags.

> **Anonymous (`terra19v62f65v9kdy05c48v6fgnf4yvrqsjvqqyp8n0`)** — 2024-02-12T12:25:05.868Z
> 
> I reply myself because i was missing the numbers, what means a 0.003 of reward weight in value accrual? I paste hear a message from [@Evan_docs](/profile/id/132786) on Alliance telegram
> > I calculate ~2130 Luna daily allocated to the collection at .01 RW.  That means each NFT (assuming none are broken) will receive 81 Luna after 1 year. At .005 RW, it would be around half that ~1065 daily allocated to collection, which is around 40.5 Luna per year for each unbroken NFT. At .003 rw, that's 24 Luna/year for each unbroken NFT.
> [https://t.me/The_AllianceDAO/5654](https://t.me/The_AllianceDAO/5654)
> 
> I think 24LUNA per NFT per year is not appealing for outsiders. Having this in mind and also that this LUNAs willl be locked till the NFTs are broken by their owner.... I also support increasing the reward weight.

**Anonymous (`terra1ud0pnytt8nsmrupl9md40xpqp4w5ea3w4se5ht`)** — 2024-02-12T11:45:33.533Z (edited 2024-02-12T22:23:26.191Z) — 👍 2

Supporting that proposal.

I think RW to 0.007 til 0.01 would be best for us loyal holders!

Kind regards from Croatia

**Evan_docs (`terra1nhvjgyga4yfkmzv7ts79vu3w2azj6mes0jhccm`)** — 2024-02-12T22:18:12.578Z (edited 2024-02-14T07:52:10.757Z) — 👍 6

Hello!

I have read all your comments and have taken your suggestions into consideration. I have updated the proposed reward weight to 0.008, in line with the suggestions of the community. Thank you all for your support and continued discourse!

> **swgee (`terra1xq4vkykvae80xtp85gt7s4j4kz92n82kk8am5j`)** — 2024-02-13T00:16:58.127Z (edited 2024-02-13T18:51:01.948Z) — 👍 2
> 
> Looks good to me! Looking forward to AllianceDAO helping to spread Alliance across the Cosmos—and beyond 🌌🤩

> **Anonymous (`terra1f98h23ty0wkxl0xrdd2pdtye7457aphjvull79`)** — 2024-02-13T10:50:55.449Z (edited 2024-02-13T18:50:59.074Z) — 👍 1
> 
> I support this change! Let's get this proposal posted ASAP.

> **Anonymous (`terra19v62f65v9kdy05c48v6fgnf4yvrqsjvqqyp8n0`)** — 2024-02-13T10:54:06.525Z (edited 2024-02-13T18:50:56.189Z)
> 
> LFG! maybe you could also add an explanation, in LUNA numbers, of what means a reward weight of 0.008. Just to let voters know the quantities we are working with at the suggested reward weight.

**mka (`terra1gxt6j7lh9wq4767knwvtsry2wr8qkt452rh2vz`)** — 2024-02-13T13:05:54.719Z (edited 2024-02-14T07:55:28.505Z) — 👍 2

I support the revised proposal

**Anonymous (`terra175qc8zprp4e0tn2d57rsajrw7pr52mvny6hld0`)** — 2024-02-14T07:51:48.317Z

The revised proposal looks great as it can now attract users in the DeFi from terra and from other chains! Totally supported🤩

**Anonymous (`terra1memg2mn3n89e9cznwjhzhk94r0jumrge95tje3`)** — 2024-02-14T20:52:39.038Z

yip

**Anonymous (`terra1my2fdaqu523g2vfv72p43wkaaa8lqf0ks2xt53`)** — 2024-02-15T03:36:13.373Z

Just read the prop, it great, I highly support it, thanks team for hard working !

**CatWifHat Project - iSkitzTV (`osmo1yvzpmy7guxf5k4gnpsdml28kqfwypaaev097lk`)** — 2024-02-15T15:34:31.789Z

Will additional Rewards such as airdrops and other coins be able to be implemented in the future? or is this Luna Specific?

**Anonymous (`terra1kt5wxtdjewnwlg68scjpknxaz0jgvzskxs3lta`)** — 2024-02-15T20:40:54.658Z

Looks great

**Evan_docs (`terra1nhvjgyga4yfkmzv7ts79vu3w2azj6mes0jhccm`)** — 2024-02-16T20:01:45.604Z (edited 2024-02-17T07:26:07.702Z) — 👍 1

Hey all, I just updated the staking reward percentage projection in the prop to account for the  [Whitelist USDC-USDT & ATOM-LUNA LP Tokens as Alliance Assets](https://commonwealth.im/terra/discussion/15329-whitelist-usdcusdt-atomluna-lp-tokens-as-alliance-assets) prop. Should it pass, the actual percentage of staking rewards directed to ALLY will be 0.72%.

**Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2024-02-17T07:28:31.366Z (edited 2024-02-17T16:23:20.496Z)

This proposal is a slippery slope and ERIS will be voting no. I am holding multiple Alliance DAO NFTs and would personally benefit from the passing of this proposal, but still find the proposal inapropiate for the full Terra community.


**1. Deliverables**

Pay first, deliver later, is not something that works. Alliance Dao has existed for some time, yet there has not been any progress regarding new Alliances on Terra.

A far better model is to use deliverables and provide inflation to those parties, that deliver it. This allows multiple parties to participate and incentivize participation, instead of building incumbents. E.g. 0.2% Inflation is shared per Alliance that is being built.

As soon as the proposal passes, there are no incentives for the DAO to deliver the promises, as the rewards are already active.


**2. Alliance building is hard**

As we are with ERIS at the forefront of Alliance building, we have been one of the parties that initiated the talks, supported and brought Alliances with Carbon and Migaloo. We also have pitched it to many more chains and generally many chains do not see any value in allowing restaking of assets especially when one of the assets is LUNA based for economic security. They will still use Alliance for their own use cases which is fine, but not a value driver to the Terra ecosystem.

So the promises made in the proposal are good, but it is questionable if the DAO can deliver the promises. Deliver new alliances first, before giving 2000 LUNA a day to a newly founded DAO with no proven record and based on promises alone. This sets a precedent that any NFT project should be allowed to receive LUNA inflation. 

Create some milestones (that any project or team can deliver) and define reward rate by reaching those milestones. We have had enough "trust me bro" proposals, and at the current point, it is the same for this one. 


**3. Community**

I do like that we want to use LUNA inflation for active community members, so I don't have an issue with even using more staking rewards on DeFi protocols / events or different utilities, but they need to be targeted and based on merit / provable results.


**4. Size**

Some of these points would have been reduced if this discussion and taken feedback by Alliance DAO holders wasn't just "I have Alliance DAO NFTs, I want a higher reward weight". 2000 LUNA a day will provide significant rewards to a selected few people who participated in Game of Alliance. Further the currently passed proposal to allow people who already have 2 Alliance DAO NFTs to buy another one for cheap, further allows insiders significant benefit over the full Terra community.

In comparison ERIS Amplifier - the biggest liquid staking on Terra - currently has 100 LUNA a day in revenue which will be shared with $ERIS stakers when $ERIS launches. This proposal will highlight the fact that it is easier to just launch a NFT project with promises to ask for LUNA rewards, than building real projects and putting in the time and effort necessary. 

It disincentivizes participation and builds incumbents.


**5. TFL affiliation**

Alliance DAO has been created by TFL employees and TFL is currently receiving 50k LUNA per day in staking rewards. Why aren't these rewards partially being used for Alliance DAO. This was one of the points made in the "TFL Community Grant", that TFL will be able to negotiate better terms with enforceable contracts.


**6. Timeline**

Include a timeline with also a fixed reduction / removal of the rewards, if promises are not delivered.


**7. Slippery slope**

As we have already seen with the posted ampROAR proposal by Lion DAO, this can get to a slippery slope real quick. There are multiple projects that have already delivered that are not receiving a reward weight yet. What about Skeletton Punks? What about Galactic Punks? What about GMC? What about Orne? What about SAYVE? What about ...

**Why Alliance DAO?**

> **Anonymous (`terra1rgy034k3kw2dltz7075uhcqcz0enfmqzegxl3h`)** — 2024-02-17T11:13:23.685Z (edited 2024-02-17T15:48:00.685Z) — 👍 2
> 
> Hello oxPhilipp,
> 
> 1.First of all its not a TFL project. there are some tfl employees involved in this from the begining as Alliance module is a tfl product. Its a community dao utilising Enterprise dao governance.
> 
> 2.~2000 luna is distributed equally among 9500 nfts daily. it benefits only few is not true. Alliance dao Nfts were rewarded to the beta testers of Alliance module and more then one wallet from the same ip was avoided and given only 1 nft. in total 10000 nfts were allocated and ~1200 minted. rest sits in dao treasury at the moment. **Please see Alliance Dao growth proposal for futher details**.
> 
> there are only 33 wallets that hold more than 2 Nfts and those were all bought from the market after the airdrop hunters dropped them. another 8000 nfts will be distributed or sold to wl projects of terra and beyond.
>  
> 3. luna rewards per nft is locked untill they are broken and broken nft wont get any rewards. it all comes down to the point where who holds the nfts longer.
> 
> 4. Alliance Nfts are unique contracts and there isnt any nfts you have mentioned has the same contract. Possiblity for building alliance among terra and other cosmos projects increases with this unique contract characteristics.

**POPIAH.luna 🌖 (`cosmos1xam0nkd4qlpwzea2u0rn7yah6uj5w6pz20gmax`)** — 2024-02-23T17:49:45.291Z

Too low, 1% will be just nice...

