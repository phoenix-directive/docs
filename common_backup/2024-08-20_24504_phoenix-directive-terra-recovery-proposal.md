# Phoenix Directive - Terra Recovery Proposal

- **Thread ID:** 24504
- **Author:** Phoenix Directive (`terra1fsgr93reemnty3240kwjxz29qqz5wzaelpukwy`)
- **Created:** 2024-08-20T08:10:41.086Z
- **Last edited:** 2024-08-20T08:32:59.641Z
- **Stage:** discussion
- **Views:** 3107
- **Reactions:** 7
- **Comments:** 4
- **Source:** https://common.xyz/terra/discussion/24504-phoenix-directive-terra-recovery-proposal

---

## **Phoenix Directive - Terra Recovery Proposal**


On July 30, 2024, the Terra blockchain was the target of a malicious attack exploiting a vulnerability in IBC-Hooks. This vulnerability, reported in April as ASA-2024-007: Potential Reentrancy using Timeout Callbacks in ibc-hooks was patched and released in v2.10.6 of the Terra Core.

The patch was later not applied to the release branch for the following v2.11.0 release, leaving Terra vulnerable and allowing the attacker to exploit the issue. The attacker was able to "fool" the blockchain and IBC module into giving them tokens that should not exist by using a contract and carefully crafted messages.

A detailed explanation of the Hooks Exploit can be found here: 
- https://blog.astroport.fi/post/theday-lightning-struck-twice
- https://medium.com/@Rarma_/terraibc-hooks-exploit-21cca87d70a4

Through the Hooks Exploit, the exploiter was able to steal the following tokens on the Terra blockchain:

- 2,192,476 axlUSDC;
- 353,069 axlUSDT;
- 2.047 axlWBTC (worth $ 118,955);
- 53,769,000 Astro (exploiter sold 14,769,000 Astro for 136,338 USDC with the remainder since frozen by Terra and Astroport/Neutron teams to stop additional sales.)

**Impact of the Hooks Exploit on Terra**

The Terra blockchain is currently isolated from other Cosmos chains as it is impossible to bridge in liquidity through Axelar and Axelar related services

The legitimately issued Axelar assets on the Terra blockchain are currently trading at a vast discount and are essentially worthless

Current – and legitimate – holders of Axelar assets on the Terra blockchain are unable to bridge out their assets as the Axelar bridge (for Terra issued assets) has been emptied by the exploiter;

Protocols using Axelar assets on the Terra blockchain, e.g. Astroport and SOLID, can no longer properly function, compromising virtually all economic activity that was taking place on the Terra blockchain up until the Hooks Exploit

**Action Plan**

This proposal aims to make use of the Terra Community Pool to reverse the impact of the Hooks Exploit: 

- Approve the community pool funds needed buy back the stolen assets to reestablish equilibrium and remove the imbalance created by the exploit
- In total, an amount equivalent to $ 3m worth of LUNA will need to be provided from the Terra Community Pool
- Depending on market conditions this means that 12m LUNA will be needed.
- A multisig of well known community leaders has been established to facilitate this action plan
- As the new Phoenix Directive BORG entity is not yet established, OTC sales with market makers will be carried out by the Astroport Foundation acting as a counterparty on behalf of the community
- The OTC or TWAP transactions will be carried out off chain with limited impact on LUNA price
- Any excess LUNA remaining after the execution will be refunded to the Terra Community Pool
- Astro holders will be made whole, by rebuying 136,338 USDC worth of ASTRO on the open market over a period of 30 days
- Burn the 218,335.07 axlUSDT currently in by the Terra Community Pool to reduce the amount of axlUSDT needed to be purchased

This brings the Required Assets to be bought to:
- 2,328,476 USDC
- 134,734 USDT
- 2.047 BTC

**Technical Process**

- Terra Governance transfers 12m LUNA from Community Pool to Terra MultiSig
- Terra MultiSig transfers 12m LUNA to Market Maker CEX account (contract with Astroport Foundation)
- Market Maker converts LUNA to Required Assets (2,328,476 USDC; 134,734 USDT; 2.047 BTC)
- Market Maker transfers nonLUNA assets to Ethereum Multi-Sig (Astroport Foundation)
- Market Maker returns unused LUNA to Terra MultiSig
- Ethereum MultiSig (Astroport Foundation) transfers acquired assets via Axelar to Terra Multi-Sig
- Terra MultiSig returns remaining LUNA to the CP
- Terra MultiSig buys 136,338 USDC worth of ASTRO over the period of 30 days
- Terra MultiSig returns acquired ASTRO to Astroport Assembly
- Terra MultiSig received non-LUNA ibc/… assets will be burnt with the next chain upgrade
		2,192,138 axlUSDC
		134,734 axlUSDT
		2.047 axlBTC

**Terra Multi-Sig 4/5 (DAODAO)**

https://daodao.zone/dao/terra1uh34jacuacgzlc7tmd99txafk29g22zqkdervya9nktzhu2q3hlsenfcyq 

1. André Sardo (Astroport): terra1np5em0379k8hc90chdzfsfgjgtm7xk8d0td77t
2. MB aejir (OC/PD): terra15vwmgac9tlcgkrkjn4rq3r0md003ufsqp64vaw
3. 0xPhilipp (ERIS/PD): terra1vm5azhvaxeanc7auxh02y8jmxrk8tj93f6aywp
4. Sen Com (White Whale): terra1p75vhdn3640vwavl997pe7m7lnqzs9h3a9x3xy
5. David (Community): terra1j00tmfa8el568llp3y96dquc9j2fcczmccnsn0

**Metrics / Context**

The amount of LUNA to be sold represents only a small portion of the 197M LUNA currently held in the Terra Community Pool, ranging from about 5 - 7.5%.

Global trading of LUNA is currently $ 2550m per day, therefore market makers expect that there is adequate liquidity and trading activity to handle managed sales of the 12m LUNA.

LUNA currently has an inflation of 279,000 LUNA per day, or 101m LUNA per year, equating the 12m LUNA to 43 days of inflation

**Summary**

This proposal requires a great deal of commitment from the Terra community.  

Without prompt and decisive action, the Terra blockchain will continue to stay isolated from other Cosmos chains. Users or developers will not take the risk to bring liquidity, economic activity or utility to Terra.

This proposal allows the Terra community to prove to the whole industry that even in difficult times it knows what actions have to be taken in order to ensure the long-term success of the chain, its partners and its users.

---

## Comments (4)

**Windfall_Crypto (`terra10m8gzey5zn72dfnu0a9q7mygjwcadn3fguftzv`)** — 2024-08-20T16:59:03.567Z (edited 2024-08-25T23:10:31.222Z) — 👍 4

Again, the Terra Community will pay the price for the actions (or in this case the gross negligence) of TFL, but this is the only way to go. Sadly, TFL is bankrupt and will not pay for its mistake. The Terra Community is all alone to clean the mess.

Considering the inflation rate on the chain, this proposal only adds 43 days worth of inflation in sell pressure in the books. I think it is manageable.

Sadly, the Terra Community does not have any other choice here. For the chain to survive it needs economic activity, it needs to be able to handle Axelar assets and Wormhole assets (if I am not mistaken, Wormhole has also deactivated transfers to Terra, not only Axelar has done it).

Right now the Terra blockchain is isolated in the Cosmos. Paying back the debt will result in some sell pressure short term, but not going forward with the proposal will result in the chain dying in the foreseeable future in my opinion.

So I prefer some pain now than a certain death later. Hence, I fully support the proposal and hope after that the Phoenix Directive can stop managing TFL's mess after that and will be able to get to work to build us a better future.

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2024-08-21T04:04:12.918Z (edited 2024-08-25T23:10:34.835Z) — 👍 2

Good to see trusted members of the community on this multisig.

Assets on Terra must be rebalanced, otherwise we might as well call it quits now.

IBC Hooks exploit was made possible due to human error at TFL.

Since TFL cannot resolve the situation, the only option is this community pool spend.

**Heisemberg (`terra16vzhe8500360lc8kp4hgapk8rk07ehucsuxa7v`)** — 2024-08-26T14:08:15.114Z

I fully support this proposal, we need people who know Terra, who provide stability and above all who dare, we need to dare to come back stronger

**motionlessflorist51 (`terra1qyqrfwzy0chh4ld6xfdrggetxyhze2sv3mc6ph`)** — 2024-11-11T14:33:33.179Z

It seems the price of all .axl assets was restored. Why not reopening the bridge/channels to be able to deposit again from axelar?

