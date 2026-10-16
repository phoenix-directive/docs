# Increase Terra's Governance Quorum from 10% to 33.4%

- **Thread ID:** 8354
- **Author:** zon (`terra1xtlkxkund5xxsj8uj94y6fmx2sf9unkc9l7lpg`)
- **Created:** 2022-12-06T03:37:01.473Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 710
- **Reactions:** 0
- **Comments:** 1
- **Source:** https://common.xyz/terra/discussion/8354-increase-terra-s-governance-quorum-from-10-to-33-4

---

# Increase Terra's Governance Quorum from 10% to 33.4%

## motivation

Since Terra's inception 6 months ago governance quorum has been set to 10%. As the chain matures the governance process should as well to focus on obtaining a larger sampling of stakers when it comes to decentralied decision making.

As of Dec 5th, only 4 validators are required to vote to make a decision on a vote. 

A brief yet telling comparison of quorums:
- Cosmos Hub: 40%
- Terra Classic: 40%
- Osmosis: 20%
- Juno: 33.4%


## proposal

Terra governance should vote to increase the quorum param from 10% to 33.4%. 

> Increasing the value of the quorum subkey will require a larger proportion of the network to legitimize the outcome of a proposal. This decreases the risk that a decision will be made with a smaller proportion of ATOM-stakers' positions being represented, while increasing the risk that a proposal will be considered invalid.  - [cosmos docs](https://hub.cosmos.network/main/governance/params-change/Governance.html#quorum)

All of these are wonderful innit. 

It allows decisions to be made by a larger representative sample of Luna stakers and keeps proposals focused as they needs to garner the attention and discussion from at least 30% - ultimately keeping the chain and the community pool decentralized and secure.

Given that Tendermint is 1/3 Byzantine tollerant, 33.4% is chosen since any number lower would allow a smaller stake participation to halt the chain than consensus' 1/3 bft.

## param changes

these params will push quorum to 33.4% and keep pass threshold and veto threshold constant.
subspace
  gov

key
  tallyparams

value
   {"quorum":"0.334","threshold":"0.5","veto_threshold":"0.334"}
Please discuss below if you have comments, concerns, thoughts. This proposal will be pushed on chain soon™

# 🫡


## please note
Someone has pushed this proposal to vote [here](https://station.terra.money/proposal/3547), however it was done with 30% quorum. This proposal will be pushed on chain in 2-3 days after enough time for discussion and the link will be posted here.

---

## Comments (1)

**Anonymous (`terra1evtktqwv5gqkt0l2edh2pak0m2u9kxkdtke97p`)** — 2022-12-10T23:37:07.759Z — 👍 1

There are problems with this Proposal: 

**Procedural problems:** 

- Only hours after being posted on Agora this became a vote on Station. If a Project put a funding proposal on Agora and listed it for voting only hours later without a few days of discussion time there would be big community push-back. 


- Station vote says “Increase Terra's Governance Quorum _from 10% to 30%_” , while the Agora Proposal says “Increase Terra's Governance Quorum _from 10% to 33.4%_”


- Zon’s name is on the proposal but he admits he was not the person who made or posted this proposal



**Proposal problems:**

The proposal itself is so poorly written it hardly seems genuine. 

The proposal provides zero supporting information or justification on why it should be supported. I can not recall seeing a proposal like this before. 

My guess is that it has been written this way on purpose: it was kept extremely simple assuming that the less explanation provided, the less people will be inclined to think about whether it is a credible proposal or not. In its current form it is not.

The suggestion that a handful of Cosmos chains have a higher quorum and therefore Terra should follow adds no value without explaining why. None of these chains stand out as stellar examples governance.

The proposal only offers this unsupported statement as their case in favour of a yes vote: 

_“It allows decisions to be made by a larger representative sample of Luna stakers and keeps proposals focused as they needs to garner the attention and discussion from at least 30% - ultimately keeping the chain and the community pool decentralized and secure”. _

Yet nothing in this statement will necessarily come about from changing the quorum. They have also made no attempt to explain How it might themselves, as if the logic or causation is self-explanatory which it is not. 

At the time of this post voters are favouring a Yes vote. I can only assume it is because they think the proposal is benign, a no brainer. This is probably quite wrong.

So what is the issue with raising the quorum and does it matter? 

Yes it does matter because quorum changes have a very significant impact on voting behaviour according to all empirical evidence on this topic. 
 
What will the result of a quorum increase be? A net Decrease in voter participation in proposals and engagement in governance, the opposite of what we would hope for Terra’s future. 

Below is summary of conclusions from various academic papers on Participation Quorums that anyone can find with a quick search. This is what the change in Quorum will cause:  

- Participation Quorums create conditions for a “no-show” paradox through which supporters of the status quo may have the possibility to manipulate outcomes by abstaining. 
- Participation quorums create incentives for strategic abstention when the participation quorum is anything other than negligibly low.
- Quorums increase the probability that conservatives (against change) boycott the election, and do so massively (increasing that probability by more than 40 percentage points) in the case of participation quorums.
- Participation quorums give the incentive to strategic voters preferring the status quo, to abstain from voting, thereby looking like indifferent voters.

