# Seed Osmosis, Astroport Pools With LUNA from Comm Pool

- **Thread ID:** 5835
- **Author:** JohnGalt (`terra1wfaxhrq2n0326zkvecc4ad7kgk8cjc48yukgnq`)
- **Created:** 2022-06-24T16:00:08.748Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 1597
- **Reactions:** 1
- **Comments:** 5
- **Source:** https://common.xyz/terra/discussion/5835-seed-osmosis-astroport-pools-with-luna-from-comm-pool

---

**Summary**

Use the Terra community pool to seed the axlUSDC - LUNA pool on Astroport and the LUNA - OSMO pool on Osmosis. To raise the necessary USDC and OSMO funds, auction LUNA with a two year vest. Also, incentivize said pools with more LUNA. Incentives will mostly accrue to our POL, so they shouldn't be an issue.

**Motivation**

Terra is a decentralized, community-focused project. Thus, it is unfortunate that the vast majority of LUNA trading takes place on centralized exchanges. Low liquidity prohibits individuals and other entities from trading LUNA on DEXes. As we saw with the recent emergency developer allocation of LUNA, developer teams sold their LUNA on CEXes.

Seeding liquidity and adding incentives to the Astroport pool will increase trading volumes, and seeding and incentivizing the Osmosis pool with increase trade activity between Terra and the greater Cosmos ecosystem.

**Proposal**

Withdraw 10MM LUNA from the community pool. Arrange for a total of 5MM from the community pool to be auctioned, 4MM to be auctioned for USDC, 1MM to be auctioned for OSMO. Put the other 5MM aside. Set the auctioned LUNA vesting schedule to coincide with vesting schedules 1 & 2 from the airdrop. Specifically, the 5MM auctioned LUNA vests linearly over 2 years, from 11/24/2022 to 11/13/2024. It would be advisable to time the LUNA auction with a series of Terra protocol launches, or some other good news.

Depending on amounts of USDC and OSMO raised in the auction, pair with LUNA using the remaining 5MM LUNA. Return unused LUNA to the community pool.

Separately, withdraw 1M LUNA from the community pool to incentivize the Astroport and Osmosis pools for 3 months, 800K for Astroport and 200K for Osmosis. Our POL will get most of the incentives, and the ASTRO incentives, too. If we're lucky, we might even be able to convince Osmosis to incentivize their LUNA pool.

**Action Plan**

1. Community discussion, refine plan

2. Develop a method of auctioning LUNA

3. Set up Terra and Osmosis multi-sigs to manage LP positions

**Final Thoughts**

As a rule, we should never spend LUNA from the comm pool unless each dollar's worth we spend creates at least a dollar's worth of value for the project. This plan will meet that criterion. We need DEX liquidity for our project!

---

## Comments (5)

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2022-06-24T16:42:16.660Z

I think this is a very strong proposal. I love the idea of community pool POL!

I wonder what your rationale for 80% Astroport, 20% Osmosis was? Would you be open to a greater share going to Osmosis liquidity?

On Terra 1.0, although I used Osmosis, I was guilty of being a bit too closed off from Cosmos IBC chains. I think now would be a good time to demonstrate that Terra is an integral part of IBC. Perhaps 60% Astroport 40% Osmosis, or even 50:50 would demonstrate how serious we are about working with other chains.

**brianYoon (`terra1w4pr4qqwkc58sq5xsxyruzgu2c4ku3ceaxq34t`)** — 2022-06-25T12:04:51.434Z

Increasing liquidity is a good idea. But why use "OSMOSIS"? Activation is understandable as Astroport is a network within the Luna chain. Can't I just send and receive axlUSDC to the exchange? Currently, the problem of lack of liquidity is that axlUSDC's bridge transmission method is inconvenient. In my opinion, it is enough to support 1. Astroport (100%). 2. You can exchange axlUSDC with the exchange through LunaChain, and having a pair on the axlUSDC/USDC exchange makes it very convenient to trade, which will bring a lot of liquidity. If possible, I would like to be on Binance, which has the most trades.

**Anonymous (`terra17uncwru68z3n0kl543r6rdd5q9jpvwxdxvfe66`)** — 2022-06-26T13:23:35.421Z — 👍 1

Kudos to [@Terra Watcher](/terra/account/terra1wfaxhrq2n0326zkvecc4ad7kgk8cjc48yukgnq) for starting this post. Now that Terra v2 is in its infancy, the main priorities should be:

1. Access to Terra v2 ecosystem
2. Building up liquidity in the ecosystem
3. Increase transaction volumes
4. Improve fees for validators & reduce inflationary emissions


This ties in very well with the first priority, being **Access to Terra v2 ecosystem**. There are two main methods to enter the ecosystem currently. First, being CEX exchanges which is currently listed over more than 10+ exchanges. 

The second will be via bridges & IBC chains. I for one will not think that Astroport will be a good use for the community funds. Astroport could incentivise its own pools with its Astro tokens to deepen its pool. And should the community fund supports Astroport, it should allocate some LUNA to Terraswap & Phoenix DEX as well.

However, seeding the LUNA/OSMO pool will be a good idea to deepen the pool to lower slippages when a swap from one IBC token to LUNA is done. With the Wormhole portal bridge established, we should establish a LUNA/AVAX pool on TraderJoe for the Avalanche chain as well.

Both Osmosis & Traderjoe can be used to farm OSMO & JOE rewards to be recycled back into the community fund.

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-06-30T16:00:33.438Z

Any chance of splitting this into 2 proposals?
each have their own merits, and discussions.

For example is 1M enough for the OSMO/Luna pool ?

**Anonymous (`terra17uncwru68z3n0kl543r6rdd5q9jpvwxdxvfe66`)** — 2022-07-03T15:00:00.463Z

I agree. Splitting the proposals in two will be good. Perhaps we could focus on Osmosis for the first proposal. $1mil will be good for a start since the demand for LUNA may not be as high before dApps launch on Terra v2. Separately, once we agree to allocate the seed capital, a governance on Osmosis will be needed to raise it as an incentivised pool. 

Since Larry, Danku or Smart Stake are validators on Osmosis & Terra, it will be good to have them raise the proposal on Terra's behalf.

