# Cavern Protocol Audit Proposal

- **Thread ID:** 9591
- **Author:** Cavern Protocol (`terra1ytj0hhw39j88qsx4yapsr6ker83jv3aj354gmj`)
- **Created:** 2023-01-25T11:39:24.196Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 699
- **Reactions:** 0
- **Comments:** 5
- **Source:** https://common.xyz/terra/discussion/9591-cavern-protocol-audit-proposal

---

## Summary
Cavern Protocol is a non-profit organization that aims to provide an efficient lending market on Terra 2.0. Because of its low starting-capital and its non-profit nature, the protocol needs funds to audit its contracts. 

## 1. WHO ARE WE?

**a. The protocol**
Cavern Protocol is a non-profit project that aims to bring the benefit of De-Fi to ordinary and risk-averse people. After the failure of Anchor Protocol, USTC and ultimately LUNC; our team decided to build a new lending protocol on the same model. Similarly to Anchor's money market model, the platform leverages staking rewards of deposited collaterals to make De-Fi more efficient and balanced.

**b. The Team**
We are a small team composed of anonymous Terra builders.

Our long term goal would be to decentralize the protocol, removing the on central pain point the team represents. We have created a group of known Terra builders and members that will have authority over the protocol.

This project aims to create a fully decentralized P2P lending protocol accessible to anyone without any constraint.

Since we are a non-profit project, the only cashflow we get from the platform is fully redirected to running the protocol. So far, we take a small fee on deposits (0.5%). In the last few weeks, we collected a grand total of $240. Those funds will be allocated to the Cavern Price Oracle that burns around 4.32 Luna a day on transaction fees (approximately $10 as of this post). This cost is paid mostly in gas fees to provide prices, and run the protocol.

## 2. WHAT WE NEED

We are a grassroots project and we understand the need for an audit for people to feel safe using the protocol.
Right now, the team is looking at multiple options for the audit:
- SCV Security: $93,500 (They gave a significant rebate already as we are launching on Terra 2.0)
- CertiK: $60,000

From the price point alone, CertiK would be the most cost efficient option but we are concerned that their audit will not be enough. They don't have experience auditing Terra CosmWasm contracts (None that we could find out-there). We feel that this team is better equipped for solidity auditing, and that their Cosmwasm unit and integration auditing experience is more limited. We however think they would also be a great candidate for auditing the protocol.

On the other end, SCV security is very focused on Terra, Cosmwasm and their track record on CosmWasm contracts is very impressive (https://github.com/SCV-Security/PublicReports/tree/main/CW).
They audited a similar protocol (Capapult) and already told us about vulnerabilities we had in our open-sourced code. We trust them to audit the protocol to the fullest extense.

As written above, the protocol costs 4,32 Luna per day to operate. We will not ask for any funds to operate as we already have ideas on how to make the protocol self-sufficient. 

## 3. ROADMAP AND FUTURE PLANS

**Short-term:**
- Get security audit (using funds from a proposal based on this discussion)
- Integrate multiple LSD (ampLuna, bLuna...) as collaterals into protocol
- Decentralize protocol ownership among builders, by creating multi-sig wallet

**Long-term:**
- Integrations with other protocols and cross chains.
- Improve UI and open source the webapp.
- Integrate LP tokens (axlUSDC / Luna for instance) as collateral
- Integrate deposit token aUSDC for liquidation bidding.
- Open-source the backend indexer / worker


## 4. LEARN MORE

Website: https://cavernprotocol.com
Twitter: https://twitter.com/CavernProtocol
Docs: https://docs.cavernprotocol.com
WhitePaper : https://cavernprotocol.com/#/history
Github : https://github.com/CavernPerson

## 5. DISCUSSION

Which company should we choose to audit the protocol ?

We haven't made a choice between the two firms for now and we want to dicuss this choice with the community before moving to a proposal for the community pool. The amount asked from the community pool will depend on the chosen auditor.

---

## Comments (5)

**Anonymous (`terra1heay4nz54pkn20flf2cu0hlayl4ew9teq6rrz3`)** — 2023-01-25T16:37:23.569Z

Unless SCV comes back with a better price I would go for either Certik or A10 as it would not be a wise use of funds. Why?

- Significant rebate and still 1.6x more expensive than the next competitor???
- SCV has already audited Anchor (and Capapult, an Anchor fork) which Cavern is a fork of - this should cut down auditing work by some margin for SCV. 


Glad to hear that the team are working on ways to be self-sufficient! GL.

> **Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)** — 2023-01-25T20:12:28.159Z
> 
> There's always a cheaper mechanic in town. Finding cheaper audit firms isn’t a hard task. I can only speak on behalf of SCV and I can assure you we aim for quality engagements on all audits we provide to our clients.
> 
> We can’t simply attach our name to a protocol or a service we don’t comprehensively audit; Regardless if it’s a fork or not, it has to go through the process. 
> 
> This industry can’t afford any assumptions on “it's secure because it's a fork”.
> 
> As an example:
> 
> On a side note, we are cutting costs the most we can, we are happy to workout with the client and work out specifics around budget if required. On top of that, public reports speak for themselves. 
> 
> SCV is more than happy to work with the protocol at whatever capacity. 
> 
> Good luck with the decision!

**Sasori (`terra1q4j4ucmqz74vxew0kszsxqtmvxqgp5fen248p0`)** — 2023-01-26T04:37:31.323Z

Hey [@Cavern Protocol](/terra/account/terra1ytj0hhw39j88qsx4yapsr6ker83jv3aj354gmj) ,

I understand the positioning that SCV is a well-known brand in Terra, but I honestly think u should remove this bias (since we're all from Terra) especially when it comes to requesting for community pool funds. 

In addition, I frankly do not think the choice is binary. There's are many of smart contract auditors out there. Have u tried approaching Oak Security, Kudelski, and Informal Systems? All of these are equally (if not more) reputed than SCV. 

Although I recognise it's a matter of timing, the proposed audit cost by SCV is greater than the current TVL for Cavern Protocol. Security is important, but conventional wisdom dictates that u wouldn't buy a $1,000 safe to store $100 worth of assets.

While I understand [@Vini](/terra/account/terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c) 's point that there will always be a cheaper mechanic in town, we're talking about community assets here, and thus we should be prudent in our spending. However, if in a group of 5 (or more) audit partners that are similar in standing and audit rigor - why should we pick someone that charges a higher price?

> **Cavern Protocol (`terra1ytj0hhw39j88qsx4yapsr6ker83jv3aj354gmj`)** — 2023-01-26T07:37:26.709Z — 👍 1
> 
> We will come back with more quotes in the next few days. This should shine some clarity on the situation. 
> 
> We have also observed that most investors were reluctant to put funds on the platform because of the lack of audit and a process that is somewhat different to Anchor Protocol. 
> 
> We know auditing the platform will boost our TVL and customer base by a great amount !

**ShaunOnTerra (`terra1526zhyrd8fzdvzayct9yfnspsdp9uuqhyjmte3`)** — 2023-01-28T02:38:20.951Z

pick one Audit, (i prefer SCV) wont be Bias though, i will then vote Yes, (SmartStake) no need for 3 straight away.

