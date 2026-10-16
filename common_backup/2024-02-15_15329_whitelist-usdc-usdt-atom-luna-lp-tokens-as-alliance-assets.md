# Whitelist USDC-USDT & ATOM-LUNA LP Tokens as Alliance Assets

- **Thread ID:** 15329
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2024-02-15T09:55:55.702Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 910
- **Reactions:** 2
- **Comments:** 20
- **Source:** https://common.xyz/terra/discussion/15329-whitelist-usdc-usdt-atom-luna-lp-tokens-as-alliance-assets

---

_Disclaimer: I am a Terraform Labs employee_

## **Overview**

This proposal aims to establish deep stablecoin and Cosmos token liquidity on Terra by whitelisting **USDC - USDT** and **ATOM - LUNA** Liquidity Pool (LP) tokens from [Astroport](https://app.astroport.fi/pools) as [Alliance assets](https://docs.alliance.money/alliance#what-are-alliance-assets), with room to expand to other liquidity pools—such as TIA - LUNA, DYDX - LUNA, and more—in the future.

Check out this [3-minute explainer video](https://www.youtube.com/watch?feature=shared&v=Xoe9hTzKyeo) or read the [Alliance Docs Overview](https://docs.alliance.money/overview/) for a brief overview of how Alliance works.

**Note**: A USDC - USDT liquidity pool doesn’t yet exist on Astroport’s Terra deployment, and the current ATOM - LUNA pool is XYK, which is less capital efficient than Astroport’s [Passive Concentrated Liquidity (PCL)](https://docs.astroport.fi/docs/learn/astro-pools/passive-concentrated-liquidity-pools/passive-concentrated-liquidity-pools-intro) pools. If this proposal passes, TFL will collaborate with Astroport contributors to create a stableswap USDC - USDT pool and an ATOM - LUNA PCL pool ahead of adding the Alliance assets. 

## **Proposal**

Whitelisting LP tokens from pools containing USDC, USDT, and ATOM—assets with a collective market capitalization of **$129 billion**—as Alliance assets, and offering APRs that rival top-performing pools for these assets within Cosmos (excluding DEX swap fees), will attract a broad base of users to Terra. Motivating these users to contribute liquidity for these pairs and stake their LP tokens on Station in exchange for LUNA rewards presents several benefits to the Terra ecosystem, including: 

- **User & Capital Inflows: **Millions of dollars will flow into the Terra economy from users within and beyond Cosmos.
- **New DeFi Apps:** Terra ecosystem builders will benefit from robust stablecoin and Cosmos token liquidity, providing fertile ground to build powerful new DeFi applications.
- **Increased Transaction Volume: **DEX aggregators will route stablecoin and ATOM token swaps through Terra, increasing transaction volumes.
- **Brand Awareness & LUNA Alliances: **Showcasing Alliance in this way will boost Terra/Alliance/LUNA visibility within the industry and provide a powerful example of how Alliance can be utilized to strengthen decentralized economies, opening the door for future Alliances between LUNA and other chains.
- **New Assets & Low Slippage: **Terra users will benefit from an expanded range of crypto assets to trade, coupled with the advantage of minimal slippage, regardless of trade size.


Alliance is one of the most powerful weapons of growth in the LUNAtics’ arsenal. Redirecting a portion of LUNA staking emissions toward cultivating deep stablecoin and ATOM token liquidity on Terra has the potential to meaningfully strengthen and expand the Terra economy, attracting millions in user and capital inflows, assisting in the creation of novel applications, increasing transaction volumes, improving brand awareness, catalyzing the creation of strategic LUNA alliances, and providing users with access to new assets with low slippage.

## **Alliance Asset Parameters**

- **USDC - USDT**
- Target staked LP value: **$10M**
- Target APR (when $10M USDC - USDT LP tokens are staked): **40%** (not including DEX swap fees)
- [Reward Weight](https://docs.alliance.money/alliance#rewards): **0.065**
- [Take Rate](https://docs.alliance.money/concepts/rewards#takerate): **0%**
- **ATOM - LUNA**
- Target staked LP value: **$1.5M**
- Target APR (when $1.5M ATOM - LUNA LP tokens are staked): **20%** (not including DEX swap fees)
- Reward Weight: **0.05**
- Take Rate: **0%**
- Target APRs are set to rival top-performing pools for these assets within Cosmos (excluding DEX swap fees), and Reward Weights are set to account for fluctuations in LUNA’s price
- Once the target staked LP value for each Alliance LP asset is hit, all unused LUNA will be returned to native LUNA stakers
- Reward Weights and Take Rates can be adjusted anytime through a Terra governance proposal. The initial 0% Take Rate is set to maximize the total amount of staked LP tokens, but in the future, as the ecosystem grows, the Terra community may elect to set a non-zero Take Rate, enabling LUNA stakers to earn LP tokens as part of their staking rewards
- Similar to allied Liquid Staking Tokens (LSTs) on Terra (e.g., ampWHALE, rSWTH, etc.), allied LP tokens will have a 0-day unstaking period


## **Architecture & UX**

To enable LP Alliance staking on Terra, TFL would build a similar open-source architecture to the one that allows for dynamic reward allocations to allied liquid staking tokens on Terra, as was created for the [Alliance Signaling Prop](https://commonwealth.im/terra/discussion/11500-alliance-signaling-proposal). This smart contract protocol would interact seamlessly with the Alliance module, enabling the distribution of LUNA staking rewards from the Alliance module to users who stake whitelisted Alliance LP assets on Station Dashboard. As mentioned above, rewards in LUNA exceeding the target APRs for Alliance LP assets, not including DEX swap fees, would be sent back to native LUNA stakers. This distribution would occur once the target value for staked LP assets is reached, and it would be carried out through an account that manages the distribution on behalf of the smart contract protocol.

The APR earned by Alliance LP stakers would be proportional to the total amount of LP tokens staked for that asset (i.e., the APR decreases as the amount of LP tokens staked increases). If, for example, the total value of staked USDC - USDT LP tokens on Terra hits the target staked LP value of **$10M**, the protocol would distribute a **40%** **APR** to LP stakers (not including swap fees), sending excess LUNA beyond this back to native LUNA stakers. If, instead, the total value of staked USDC - USDT LP tokens on Terra was **$20M**, the protocol would distribute a **20%** APR to LP stakers. Before the target staked LP value is hit for a given Alliance LP asset, the APR offered to Alliance LP stakers would exceed the target APR.

Contract Intialization

1. TFL creates a smart contract that mints a virtual Alliance LP token called ALP. This token represents the total amount of LUNA rewards to go to allied LP tokens (e.g., USDC - USDT, ATOM - LUNA, and any future whitelisted pools)
2. Terra governance passes a proposal that whitelists ALP as an Alliance asset with a Reward Weight of .115 and a Take Rate of 0%


User Experience

If this proposal passes and Alliance LP positions are added to Station, TFL will publish video and screenshot tutorials on how to stake Alliance LP tokens. For now, here is a brief overview of how staking and unstaking would work:

Staking
1. A user provides liquidity to the USDC - USDT or ATOM - LUNA pools on [Astroport](http://hyperlink) using [Station Extension](https://setup.station.money/), receiving LP tokens in return and earning swap fees for that pool (which are automatically claimed when the user withdraws their liquidity on Astroport)
2. The user’s LP position will show up and can be staked by clicking _Stake_ under the _Available To Be Staked_ section on the [Stake page](https://station.money/stake) on Station Dashboard v3 (set to be released soon), which will interact with this new smart contract protocol on the backend. 
3. LUNA rewards are streamed to the user every block, which they can claim at any time by clicking on the _Claim All Rewards_ button on Station’s Stake page


Unstaking & Withdrawing Liquidity
1. A user clicks _Manage_ under the _Staked Assets_ section on Station’s Stake page on Station Dashboard for the LP position they wish to unstake 
2. The user clicks _Unstake_, enters the amount they wish to unstake, and then clicks _Submit_, sending their liquid LP tokens and any unclaimed rewards to their Station wallet
3. The user withdraws their liquidity on Astroport’s [Pools page](https://app.astroport.fi/pools), sending their tokens and any swap fees earned to their Station wallet


Adding New LP Tokens as Alliance Assets

1. Terra governance votes in Alliance assets to be eligible for LUNA rewards, specifying the [Reward Weight](https://docs.alliance.money/alliance#rewards), [Take Rate](https://docs.alliance.money/concepts/rewards#takerate), target staked LP value, and target APR—multiple assets can be added in a single proposal
2. Station and the smart contract protocol add the new Alliance LP tokens, enabling staking for these assets via the Stake page on Station Dashboard
3. The smart contract protocol automatically distributes LUNA rewards to the new Alliance LP asset stakers, and once the target value for the staked LP asset is reached, the account that executes on behalf of the protocol would send excess LUNA beyond the target APRs to native LUNA stakers


Validator Selection Criteria

Terra validators can receive virtual Alliance delegations by meeting the following criteria:

- Positioned in the active validator set
- Commission rates between 5% and 10%
- Voted on five out of the last ten governance proposals
- Have voting power <4%
- Is not jailed at the block in which the contracts updates the delegations
- Must have been in the active set for at least 100K blocks (approximately one week)
- Not be a CEX or custodial validator


The smart contracts will split delegations equally among all eligible validators and review them programmatically every 21 days.

What Happens When a Validator Gets Jailed, Slashed, or Tombstoned

1. A validator that’s been jailed is penalized via temporary removal (for one week) from the pool of validators that can have virtual Alliance assets staked to them 
2. Virtual tokens that have been slashed do not impact LP tokens in the protocol, meaning that users who stake LP tokens do not lose funds. Although, as has always been the case, validators (and their corresponding native LUNA delegators) who are slashed lose a small amount of LUNA as punishment for double signing, extended downtime, or missed consensus votes
3. If a validator is tombstoned, they are permanently removed from the pool of validators that can have virtual Alliance assets staked to them 


—

This signaling proposal aims to gauge community sentiment toward the ideas mentioned above. If passed, TFL will publish two future proposals on Commonwealth: one to incorporate ALP as an Alliance asset and another to whitelist USDC - USDT and ATOM - LUNA as Alliance assets.

---

## Comments (20)

**svsct (`terra129cwyx95tdylfaztuzxy792lvygg4z7d5r797d`)** — 2024-02-15T10:24:54.689Z (edited 2024-02-15T10:37:21.844Z) — 👍 1

we liked it

**Qasim Saleem Qureshi (`cosmos17de5rquzac94s6xjn5pfcylsw8uwsp8syq2c3r`)** — 2024-02-15T10:36:19.951Z (edited 2024-02-15T17:49:00.314Z) — 👍 2

Totally support the above proposal.
Waiting to move to next step **ASAP**
> TFL will publish two future proposals on Commonwealth: one to incorporate ALP as an Alliance asset and another to whitelist USDC - USDT and ATOM - LUNA as Alliance assets.
Community is waiting since 1.5 months of whitelist USDC - USDT and ATOM - LUNA as Alliance assets.
⌛️⌛️⌛️
** Waiting and Waiting**

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2024-02-15T10:50:21.357Z

**Overall in support of this proposal.** High APR on stablecoin LP will attract yield farmers from across Cosmos.

We should not be surprised if this mercenary capital chooses to farm and dump LUNA.

For this reason, as well as educational reasons surrounding the Alliance module, I wonder if a small Take Rate would be appropriate. A Terra Community Pool DAO would need to be established.

1. This would build up Terra Community Pool POL.
2. It would educate yield farmers about how the Alliance Module operates. I think this could be beneficial for adoption of Alliance throughout Cosmos. Take Rate & Reward Weight are challenging concepts to understand.


Proposal states:
> A user provides liquidity to the USDC - USDT or ATOM - LUNA pools on [Astroport](http://hyperlink/) using [Station Extension](https://setup.station.money/)

AFAIK, Astroport works with Leap & Keplr wallets as well. Is there a specific need to interact with Astroport with Station wallet. If so, could further explanation be provided.

**Anonymous (`terra1x5juwsn2rsf4l42mvkd97c2nf709q4tzvmj6tv`)** — 2024-02-15T11:07:11.727Z (edited 2024-02-16T11:13:53.794Z) — 👍 10

Hi there

I love some of the sentiment behind this prop (particularly the goal of achieving deep stable coin liquidity on terra). However I have a number of concerns

1) 11.5% of inflation seems a lot and I think you specify that in order to change it, it would require another governance prop. Is there any specific reason we are giving 5% inflation to $ATOM holders for example?

2) I am curious as to why astroport has been selected? Many of the community have been geo-blocked by their product, only a few months ago they were considering moving their core governance to $NTRN (indeed they are only one prop away from doing that again). Migaloo have already WL Alliance LPs and continuing to deepen relationships with White Whale would benefit LUNA holders because they share a portion of their inflation with ampLUNA and bLUNA stakers. Similarly $URA is only built on terra and is touted as the community DEX. To the best of my knowledge they too haven't geo-blocked anyone. What would astroport give back to to the $LUNA community for the obvious volume this is going to bring?

3) Thirdly and finally, without a take rate, how does the basic $LUNA staker benefit? Your asking the community to dilute their staking rewards by a further 11.5% for the promise of increased volume. My concern is that will people choose to bond their tokens up for 21 days when they can get significantly better APY being liquid, Does that benefit validators and the security of the network?

**ANDYB (`terra143kcg4pnlsrpmtjmkkz9kxymxwh6xew4q5gz96`)** — 2024-02-15T12:46:21.850Z (edited 2024-02-16T11:13:14.381Z) — 👍 10

I would vote** Against **the proposal in it's current format, even though I am a huge fan of alliance and the opportunities it offers if used in the correct way and with the interest of the Terra community as it's main focus.

In the format laid out, I see a very aggressive allocation of inflation to the LP pairs of a single DEX that assumes it will achieve the targets of capital attraction and building awareness of the Terra/Alliance visibility without being incentivized in any way to achieve them or penalized if it does not. As I see it, Astroport will be the only party benefiting from this proposal without any risks assumed while the LUNA stakers bear the risk of alliance farmers dumping their LUNA without generating any additional trading volume or on-chain activity.

Another issue I see is that the second objective (attracting new DeFi apps) will also be undermined by this subsidy of sort to the biggest DeFi player on Terra. This will not only put them in favourable position against the current (albeit small) competition but will also deter new players from entering.

I would suggest the following revisions:

- Whitelist the LP pairs as Alliance assets and allow the LP of any DEX that creates the pairs to be staked as Alliance assets. Such action will boost the competition between DEXs and force them to work harder to attract liquidity.
- Require all DEXs that want to be listed on alliance to share part of their inflation/rewards with the LUNA community - e.g. via direct LUNA staking rewards, require them to allow LUNA staking via Alliance (like White Whale) or allow them to earn airdrop points (like URA)
- Ask all DEXs to include clear and visible information that the additional yield of the LP staking is powered by Alliance/Terra and create clear expectations how they will promote Terra/Alliance on their socials
- Reduce the initial allocation of inflation by half and release the second half if the results match the expectations.

**Anonymous (`terra1f98h23ty0wkxl0xrdd2pdtye7457aphjvull79`)** — 2024-02-15T17:50:09.167Z

I fully support this proposal and trust that it will proceed without any further delays.

**Anonymous (`terra12629f3upv4ltattegp6tzc7uwssq5wfdy7824f`)** — 2024-02-15T19:22:19.084Z (edited 2024-02-16T21:30:09.742Z) — 👍 11

I agree with the sentiment of this proposal. Staking LPs to the chain is a truly fascinating concept and seems to be working well for Migaloo who I believe were the first to do this. 

Despite this, two main issues spring to mind when reading the proposal:

**1. Why Astroport?**
Migaloo and WhiteWhale have shown consistent support for Terra and its community. Not only has the WhiteWhale DEX shown unwavering support the Migaloo chain was the first to integrate Alliance and already uses the alliance tech to showcase its ability to stake LPs, ecosystem tokens and soon BTC and ETH.

**Solution:** Allow WhiteWhale USDC/USDT LPs to be staked. Either solely WhiteWhale LPs or divide the by to and allow both WW LPs and Astroport LPs to be staked. This allows for more projects and users to benefit and helps recognise the Alliance between the Terra and Migaloo communities.

**2. No reward for LUNA stakers.**
Astroport will get risk-free liquidity on their part and users will likely use the pools to farm and dump, as per the usual for liquidity incentives.

**Solution:**  I believe a take rate should be introduced to reward LUNA stakers. Not only will this diversify Terra staking rewards it will also be a big selling point to for users to stake and earn a stable, yield-bearing asset.

**Crypto Snack (`cosmos1fcq6d5d2pxvutj06umua0c6su8vq086hhncrzn`)** — 2024-02-15T19:48:58.361Z (edited 2024-02-17T14:12:29.493Z) — 👍 9

**In the current version of the proposal, I am voting against it!**
It's not necessary to incentivize specific liquidity pools for individual DEXes.

If anything, I would secure equal Alliance Inflation for all prioritized DEXes on Terra to be distributed equally. The volume of, for example, USDT-USDC on Astroport with $5k volume in 24 hours raises the question of why a larger liquidity would even make a difference for that specific DEX. Then, we might as well give all other DEXes the chance to distribute the Alliance Inflation equally. 

I believe Terra should approach a proposal that addresses all DEXes on Terra and not go for DEX-specific proposals for Alliance Assets.

Please completely rework it in this form!

**Anonymous (`terra1kt5wxtdjewnwlg68scjpknxaz0jgvzskxs3lta`)** — 2024-02-15T20:36:39.443Z (edited 2024-02-18T14:50:02.472Z) — 👍 7

I only see astroport as dex here, somehow they have turned their backs on Terra. But white whale + ura was there and does everything. So I think it's unfair to attribute it to astroport alone. If you see that Mars apollo etc. are all on neutron, it's not fair to terra.

**EverydayGuy (`terra1hppefqufuetxkyzhvrmw5p27kh3myyzrac6tn3`)** — 2024-02-15T21:17:31.467Z (edited 2024-02-16T11:12:05.700Z) — 👍 5

My only input is to add my voice to the rest of the community that says we need to focus on the apps and teams that deserve it, that have risen together from the ashes in solidarity.

Rethink working with Astroport when possible. Don't fade the Moon, it always rises

**Anonymous (`terra174echl95gxagu523ey6yupqz6kllahmlr374zu`)** — 2024-02-15T22:50:07.178Z (edited 2024-02-16T11:14:43.206Z) — 👍 3

This proposal leaves out the other dexes that are on Terra and uses Astroport which is on Neutron?

**Anonymous (`terra1m753uer4mzysev8h359cxpq86uvr0rzhkfdl7w`)** — 2024-02-15T23:07:39.183Z (edited 2024-02-16T11:11:55.550Z) — 👍 3

Great idea, which will certainly bring enormous benefits to the entire Cosmos ecosystem! Incentivized stable pools are among the most sought-after destinations in crypto and what is proposed here will result in a lot of attention and TVL. 
 Whitelisting LP tokens only from Astroport, however, will result in all other dexes slowly dissipating into obsolescence. 
 A little less picking sides, a little more WAGMI please! :)

**Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2024-02-16T09:44:09.468Z (edited 2024-02-18T07:43:52.241Z) — 👍 3

There is a couple of considerations I would like the proposer to integrate before putting this on-chain.

**1. Allow users to choose the DEX they are comfortable with.**

Similar to how the balancing mechanism for ampWHALE & boneWHALE staking works in the Alliance Hub Contract, that balances rewards based on user deposits. This will eliminate any discussion about favorism and allow users to decide which DEX they support. The oracle would work similar to the one used for ampWHALE / boneWHALE, that the staked underlying LP value in dollar is measured and based on that amount, the rewards are distributed. This allows a sharing of liquidity across Astroport, WW, Uranus and whatever innovative DEX that might launch in the future.

**2. Post it as 2 Proposals**

Please post each of the LP tokens and reward weight as separate proposal. I see the utility in incentivizing ATOM - LUNA liquidity. However I don't see a valid reason for building up USDC-USDT liquidity, except only for farming LUNA for whales, so attracting mercenary capital. I would like to see you go more into the detail for the USDC-USDT LP liquidity requirements. 

Astroport came to the conclusion to heavily cut incentives on their USDC-USDT pool due to low usage and that there aren't even many use cases for USDT in Cosmos.

**3. Take rate**

I think this proposal is missing a key point that is quite important for the utility of alliance, and this is the take rate. In the best scenario for the community the community pool will start acquiring chain owned liquidity. This means that spent incentives have a permanent effect. The idea was to run a **community** delegation program that stakes 150M LUNA to start aquiring alliance LP assets for the community pool. With instead TFL running the Delegation Program, it still makes sense to use this mechanism to build up permanent chain liquidity. (With a pledge from TFL to give Alliance Assets to the Community Pool)

Details here:
https://commonwealth.im/terra/discussion/11300-unleashing-the-power-of-alliance-a-framework-for-economic-growth

Without the take rate, the proposal will turn LUNA to a farming coin.

**4. TFL Provided Liquidity**

Based on the "TFL Community Proposal", TFL advertised vast external capital available to be deployed to Terra, and one of such mentioned assets was stablecoins. So I assumed that TFL wanted to deploy this liquidity without the requirement of incentives from Terra Stakers. With the recent ch. 11 bankruptcy filling it I understand that the promised liquidity needs to be aquired otherwise, but it opens up follow up questions regarding the TFL 150M LUNA grant.

> **Rose | Phoenix Foundation (`terra14cmsxkl9ynpvrqnqnvd7dv8ecnrdserhn3seme`)** — 2024-02-18T00:30:15.232Z
> 
> That is a good point. A LUNA/USDC pair might be better, maintaining demand for LUNA instead of it becoming a farm & dump coin.
> 
> >  However I don’t see a valid reason for building up USDC-USDT liquidity, except only for farming LUNA for whales

**4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2024-02-16T11:04:21.808Z (edited 2024-02-16T21:22:52.126Z) — 👍 2

Overall in support however I think a take rate is necessary in order to offset the farm & dump of LUNA that will surely happen due the attractive APYs.

**Rose | Phoenix Foundation (`terra14cmsxkl9ynpvrqnqnvd7dv8ecnrdserhn3seme`)** — 2024-02-17T23:34:06.020Z (edited 2024-02-18T00:19:40.689Z)

I like the idea, and would support an Astroport LP.

Is USDC/USDT going to be a useful LP pair though? Agree that we need native stablecoin liquidity, and I'm keen to use noble USDC here so it can be sent to/from EVM chains with cctp.money. But there are no other pools on Terra with either of these tokens at present. So how would this pool be used? For example, if I want to trade LUNA to noble USDC, I would still have to swap to axlUSDC, and then I'm stuck. I would send the axlUSDC to Osmosis to swap it to noble USDC.

@Chris Amani suggested a third pair could be added: https://twitter.com/fleece_cannon/status/1758596187941478791

I would think about adding something with high liquidity+volume paired with noble USDC, such as LUNA. axlUSDC could also make sense, though there are 'transmuter' pools on other chains that swap these for no fee. Then again - it removes the need for the USDC/USDT pool unless you specifically want to get Kava USDT.

AxlUSDC/Kava USDT, or LUNA/USDT could be options. For now they would mostly be used as hops to get USDC out of the other pool, USDC/USDT, but at least then all the pools are useful. Hopefully in future Kava USDT is more widely accepted.

> **Rose | Phoenix Foundation (`terra14cmsxkl9ynpvrqnqnvd7dv8ecnrdserhn3seme`)** — 2024-02-18T00:35:33.769Z (edited 2024-02-18T00:38:29.264Z)
> 
> After reading Philipp's comment about LUNA becoming a farming coin for whales with stablecoins, my preference would be to have 2 pairs: <br>
> LUNA/ATOM <br>
> LUNA/USDC
> 
> But if there is a genuine reason for USDC/USDT, I would suggest <br>
> LUNA/ATOM <br>
> USDC/USDT <br>
> LUNA/USDT
> 
> This way at least the third pair still maintains demand for LUNA.

**Qasim Saleem Qureshi (`cosmos17de5rquzac94s6xjn5pfcylsw8uwsp8syq2c3r`)** — 2024-02-20T14:41:16.254Z (edited 2024-02-20T14:43:23.621Z)

⌛️⌛️⌛️
**Waiting and Waiting** to proceed to next step. @Zion

**jgnft (`cosmos1ejlamgn4270dmgmzc3z9sc9zkxtyfsh3qdznc2`)** — 2024-02-20T22:42:03.574Z

I will only support this prop if all terra dexes are included. If it is an Astro-only prop, NFTswitch will vote NO.

Wagmi or nothing. 

🏴‍☠️✊🏻

**PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2024-03-14T11:11:03.994Z (edited 2024-03-25T13:52:44.888Z)

This is a great proposal to bring permanent native stablecoin and ATOM liquidity to Terra and I fully support it. However, there also to be a liquidity pool that links LUNA to either USDC or USDT. For this reason, I would recommend a third pool, LUNA - USDT. Many Cosmos chains already have USDC pools, and a USDT pool would be something unique to Terra.

Also, for this proposal to work, the Kava chain must first be fully integrated in Station v3. I have no idea what the current state of this is, but I'm sure TFL is working on it.

As for the concern about Luna farmers, I think the benefits far outweigh the negatives, and therefore will positively affect Luna's price regardless. And as for which DEX to use, personally I would go for URA, but Astroport or White Whale will work too.

In conclusion, the best proposal I have heard in recent months. What are we waiting for?

