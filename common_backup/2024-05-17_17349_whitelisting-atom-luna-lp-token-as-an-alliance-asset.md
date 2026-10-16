# Whitelisting ATOM - LUNA LP Token as an Alliance Asset

- **Thread ID:** 17349
- **Author:** PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)
- **Created:** 2024-05-17T22:43:38.565Z
- **Last edited:** 2024-05-29T10:21:52.269Z
- **Stage:** discussion
- **Views:** 922
- **Reactions:** 1
- **Comments:** 1
- **Source:** https://common.xyz/terra/discussion/17349-whitelisting-atom-luna-lp-token-as-an-alliance-asset

---

**Summary**

This proposal is one of a series of alliance whitelists I aim to do in order to jumpstart Terra liquidity again after TFL can no longer provide liquidity due to the SEC regulations. I believe the alliance module is the best tool we have currently, which allows us to incentivize liquidity tokens with a small portion of Luna inflation. The first proposal (Luna - USDT) I did a couple of weeks ago failed due to Astroport LP pools minting CW20 tokens, which are incompatible with alliance currently. I have looked deeply into how we can make it work as soon as possible. And it's quite simple: find a DEX where the LP pools mint native factory tokens, so the bank module recognizes them. (https://docs.alliance.money/guides/create/)

This DEX is URA, which has recently gone permissionless, allowing anyone to open a pool. _Although I originally planned to start with Luna - USDC (Noble) and Luna - USDT (Kava), I have been informed that another team is also working on a solution to bring this liquidity to Terra. As such, I think it is a good idea to hold off the proposals on these pools and jump straight to the ATOM - LUNA pool, of which this team currently has no plans._ I will outline my reasonings below for connecting Terra with Gaia.

Edit: For anyone who thinks this conflicts with ERIS' proposal, I personally don't think so. I see this as more of an intermediate solution. His proposal is complex and it will take time to implement.

**Motivation**



```
Cross-chain interactions: Similar to USDC (and to a lesser extent USDT), linking Luna with Atom opens up many pathways that allows anyone in the Cosmos to buy Luna, as Atom, being the primary Cosmos asset with the largest market cap, is linked, directly or indirectly, with almost any asset and chain. Thus, by providing Luna - Atom liquidity, we connect Luna, and every other Terra asset connected to Luna to the whole Cosmos ecosystem. (Yes, it is even more liquid than Osmo, because Osmo, while obviously very liquid on Osmosis, is not as liquid on other dexes, such as Kujira's. And even on Osmosis, the largest asset bound to USDC is in fact not Osmo, but Atom, with a 2.2M LP pool.) It thus helps massively in addressing fractured liquidity, especially with Station's and TFM's cross-chain swap functions.
```



```
Exchange connectivity: While it is true that Luna is already integrated in most of the largest exchanges, there are some smaller exchanges, that may not have Luna deposit and withdrawal. Atom on the other hand, is likely present on almost every exchange, thus, by having Luna - Atom liquidity on Terra, we greatly increase on- and off-boarding of Luna. We also secure Luna's position of always being connected to the exchanges, regardless of what those exchanges decide for Terra integration itself. Atom thus essentially serves as a gateway coin.
```



```
Layer zero bridges: This is a similar argument I've made for USDC/USDT, which have interchain liquidity through various layer zero bridges. Kava USDT has Stargate, whereas Noble USDC has cctp.money (which isn't exactly liquidity, but it's the same kind of function). Besides these two assets, the most well integrated Cosmos asset in these kinds of DEX's tends to be Atom. Take Thorswap for example. Every user who wishes to enter Cosmos via this route has to go via Atom, and by having Atom-Terra liquidity on-chain, we serve as the first hub through which money can flow into Terra. (Complex IBC transfers and swaps are off-putting for new users, and it has to be as simple and efficient as possible. We cannot expect users to first travel to Osmosis, swap there to a stablecoin, and then again 2 IBC transfers to Terra, and then another swap for Luna. It's nonsensical. They should just be able to straight up buy Luna with Atom with one IBC transfer to Terra.) 
```
Basically, the idea here is to connect Luna with everything, and that's why these 3 assets are arguably the most important, which not unironically, are also the assets put forward by 2 previous proposals, one of which by former TFL member Zion. It is more efficient than putting Luna against every specific asset. All roads should lead to Terra. 


```
Attracting holders of Atom to Terra: By offering Atom holders decent APR, we re-ignite outside interest in Terra, who might be tempted to buy Luna in order to provide Luna - Atom liquidity, and while doing so re-emerge themselves into the Terra ecosystem. Attracting outside interest is key to growing userbase, which requires offering something that is alluring to people who are not already invested in Luna. Atom has potentially the largest userbase in Cosmos.
```


Conclusion: Atom is essentially the "Bitcoin" of the Cosmos ecosystem, and therefore it is in our best interest that we have atleast some Atom liquidity on Terra.

**Alliance parameters**

As with my previous proposal, I aim for pools that still have a decent APR at around 1 million $ TVL at the current price. Here are the calculations :

According to terra.stakebin.io , an extra 277000 LUNA is minted daily. Let's assume a reward weight of 1%:
1% of that is 2770 LUNA daily.
This translates to roughly 1.011M LUNA per year.
Which translates to an APR of 60.66% at the current price of roughly 0.6$ per Luna.
(Now at a price of 3$ per Luna, the APR would increase to 300%, and then it settles at 60% APR again once the pool reaches a TVL of 5M $, which is the interesting part of alliance incentivization...) 

As you can see, this is quite an aggressive reward weight, hence it seems that it is a good idea to start with a lower **reward weight of 0.66%** . This is not excessive I believe, considering Whale's LSD tokens combined are currently receiving 2.5%, and this is I believe a more necessary appliance of alliance now that most of our liquidity has vanished. 

**Info**:  https://alliance-dashboard.terra.money/?selected=phoenix-1 . Here we can see that bWhale with a 1M $ staked, is receiving an APR of 42% at the current price of 0.57$ per Luna, with a reward weight of 0.92% . If we follow these statistics, the APR would actually be slightly lower than my previous calculations. And it would put us slightly above 30% with the 0.66% reward weight at a pool of 1M$ .


**How it will work:**

Once you provide liquidity on the Atom - Luna pool on ura.xyz , you will receive an LP token that has the following denom: 

factory/terra1djk2zl83dspt696ex5crhfacu8vm6934576t4zdd2592fzyahr2qma6guq/ULUN-IBC/-LP

If the proposal passes, then you will be able to stake that token on a Terra validator (with a 0 day period unstaking, which is the norm for all Terra's alliance assets currently), and gain Luna staking rewards as usual.


With kind regards,

(Hope to see some discussion before doing the proposal)

---

## Comments (1)

**mbaejir (`cosmos165hv2wmzcxmw3nfstrsvg8ah3uut45x4errwqk`)** — 2024-05-30T00:30:18.206Z (edited 2024-05-30T00:31:25.580Z)

This is definitely a No from Orbital Command.


You are proposing that a pool with almost no liquidity is incentivised and on a DEX (URA) where the team has just announced that they are giving up and leaving. There is no management plan in place for URA to ensure that it will even be maintained. URA team is not giving either the front or back end code to the community so this all needs to be developed with substantial investment. 

Why did you even take this on chain knowing that there is a much more developed proposal just posted by ERIS that may address this in the future?  

But until there is a substantial plan worked out, it would be completely irresponsible to allocate Alliance rewards to URA and these pools.

