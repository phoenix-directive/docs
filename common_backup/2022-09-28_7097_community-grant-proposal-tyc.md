# Community grant proposal - TYC

- **Thread ID:** 7097
- **Author:** Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)
- **Created:** 2022-09-28T12:06:22.541Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 2193
- **Reactions:** 1
- **Comments:** 13
- **Source:** https://common.xyz/terra/discussion/7097-community-grant-proposal-tyc

---

# Summary


Sometimes it's all too hard to know if a NFT, wallet, or token is real one, or just some imposter, or even worse the same person multiple times.

The common way to solve this is to force the person to KYC themselves..  but yuk.

we propose a middle ground.. we KYC against twitter. 

People will be able to verify that a NFT actually comes from [@](/terra/account/terra107je4n5hafn0s948qnkzkfdyzf6shd4jdr8kxr)TheMoonMidas or that @wagmigently is on the multi-sig.

# Motivation

I'm tired of people proposing multi-sigs with random wallets that could be anybody, and buying un-authentic NFT clones because I thought they came from the same artist. This should help prevent this.

# Proposal

We are asking for 20,000 Luna to develop this.

The deliverables would be:
- Smart contract system to store wallet/twitter handle, we envision a small fee for established twitter accounts to verify (say over 10k followers or with a blue-tick), which will help with continued running of the services
- Oracle to verify twitter person has posted a signed verification method on their twitter
- A website to put in a twitter handle or wallet to see which is which. 
- A stretch goal is to write a PR for station so that it integrates with it.
- If funding is successful, we will port this to other chains, once we do this, then the service will be free on Luna, as a thank you for the initial grant.



## Who are we:
- We are PFC.  We have been in the Terra ecosystem since early 2021.
- We have build and maintain several smart contracts on the Terra system
- We run a validator which is used to fund IBC relaying,  and running of the STEAK liquid steaking app.


Thoughts? Questions?

---

## Comments (13)

**Anonymous (`terra1p5eswxj03j7z5xj7c5rdv44tl8hmgg058aghjl`)** — 2022-09-28T12:25:27.880Z (edited 2022-09-28T13:15:18.392Z) — 👍 1

Hey,
Seems like a good idea to have some kind of social kyc oracle.

A few important Qs:
- What's the planned oracle account verification flow?
- Is the oracle decentralized or run by a single party (PFC?)
- If decentralized, what will be the incentive mechanism?
- How does it compare with other identity solutions like TNS for example?
- How many man-hours do you estimate this work requires?

More open question: how will this design cause less confusion than without it?
ex: I create an `@PFC_VaIidator` account on twitter (uppercase `i` instead of `l`) and use it in a multisig. Will the system make it more or less confusing that this multisig is legit? Could it introduce a false sense of security?

Thanks!

> **Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-09-28T12:33:18.625Z (edited 2022-09-28T13:27:00.559Z)
> 
> Incentivizing oracles would require us to charge more, but it's doable.
> 
> I don't see this as a major issue, people run IBC relayers for at a loss, as it's good for the community. 
> 
> But as the verification won't be free, a percentage would go to the people doing the work, so it should cover transaction signing costs.
> 
> 
> The oracle could be decentralized easily.
> 
> It requires N of M oracles signing/verifying the tweet. 
> 
> who the M people are could be gov-voted in via a multi-sig. 
> 
> re: TNS
> I'm not an expert on TNS, but I believe
> TNS does no verification with external mechanisms. it provides 'vanity' names, so doesn't actually solve the core-problem this is meant to address.
> 
> (Also is TNS alive?)
> 
> as for how does this help with twitter fake accounts, systems using this could do basic DD on the twitter account (#followers, is-blue-tick, etc)
> that would be left for the system using this service (or additional phases)

> > **Anonymous (`terra1p5eswxj03j7z5xj7c5rdv44tl8hmgg058aghjl`)** — 2022-09-28T14:18:13.376Z (edited 2022-09-28T14:18:44.872Z)
> > 
> > There's much more involved in having a good/robust/decentralized oracle. some examples:
> > - Incentivization
> > - Penalty system for bad oracle behaviour (related to first point)
> > - Commit-reveal like system to avoid oracle to reply others' votes
> > - etc.
> > 
> > The current proposal is not decentralized enough, in my opinion, to invest the time and money you require. It would only be a slight improvement over storing this information manually in a repo or database (ex: the address indexing done on terrascope in the past).
> > 
> > Also, on the funding, 20k LUNA is ~45k USD. This is 3 months of full-time work for a senior dev in Switzerland (US should be around similar levels). I can't see how developing this smart contract and UI would take that many man-hours.
> > 
> > **TL;DR: I think I'd rather see a full-fledged identity protocol built with proper incentive and decentralization than a half-hearted solution + can't justify the funding requested**

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-09-28T12:34:46.045Z

Phase 2 would verify against a discord or TG handle

**Anonymous (`terra1lxc6c5rnvcfx94x2ejarsr55cmcec6apklkdpw`)** — 2022-09-29T01:56:10.119Z — 👍 1

Idea is good and TBF, pretty useful. but agree with [@Etienne](/terra/account/terra1p5eswxj03j7z5xj7c5rdv44tl8hmgg058aghjl). This proposal lacks technical depth and the amount of LUNA requested is not justifiable. 

Just compare the amount of effort put into this VS the proposal by Amit for Beacon. Although the ask here is very different (20k vs 50k), Beacon had a well thought plan and budget allocation that made sense. 

Would love to see more technical design fleshed out. Right now this sounds more like requesting for 40+k USD to fund a weekend project. Don't think the community will support the proposal in this current state.

**PFC (`terra1equ5u2v89jmantmj0zajsdxhvjc8jdv96mz7ny`)** — 2022-10-04T05:16:51.016Z — 👍 1

apologies for the slow reply, but no laptop, and this site doesn't really work on the phone for me.

I hear you about more detail, I'm used to larger props, where a 10-page deck works.. mea culpa.

Ok..
so firstly this is not a weekend project, neither is this just a piece of code, it will be a running service, with operational elements, and marketing.

To ease your fears about it being a weekender,

It will need on the technical front:
1. UI & front end design
2. backend bot (decentralized either listening to the web-socket, or polling the smart contract at a regular interval), as there is a decentralized aspect, it's not a simple project.
3. Smart contract work. This is near impossible to find, and also in high demand.


While I could go to the local university and hire someone cheap, I prefer working with experienced people, and those experienced people have other things going on, so funding has to be generous (as they will be weighing it up against some defi dApp that they are being approached with).
I am hoping the coolness, community aspect, and goodwill will be sufficient.

On the tech operational front.
1. 1-2 sentries. I'm a firm believer in not having projects weigh down/depend on public infra, so will be spinning up some boxes for this to use.
2. documentation on how to implement this in your dApp, some kind of support process, and so on.


On the marketing front, we will need someone to promote this to other dApps, get it integrated into wallets. As I'm sure you agree, just building stuff and putting it on a URL doesn't get traffic.

I hope this level of detail is sufficient. I'm still traveling so responses will be delayed a bit

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-10-09T22:14:57.605Z

Official Proposal is now up.

[https://station.terra.money/proposal/1502](https://station.terra.money/proposal/1502)

**Anonymous (`terra1xpdyd332ay3w4z3l74zllel56nzxpukjea0au7`)** — 2022-10-10T00:17:12.368Z

I think this is a bad proposal.

I think a No-with-veto burning mechanism for scam proposals is better than KYC.

KYC has its own set of problems that fly into the face of decentralization. For example: Who watches the watchers? (‘Quis custodiet ipsos custodes?’) Making Twitter the arbiter of KYC for Terra proposals (e.g. Twitter-checkmarked) to make proposals for Terra seems a very bad idea. Twitter has a pretty dubious reputation of arbitrarily banning people. I would not trust a Big Tech censorship proponent like Twitter at all to have a say in Terra Governance proposals. We need more decentralization in my opinion, not less.

Instead, just raising the required Luna to make a proposal, thereby raising the cost for the scammers funds that will be burnt with a No-with-veto vote, seems like a much better idea to me.

> **Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-10-10T12:45:34.287Z
> 
> I am not really sure what you mean here.
> 
> While this _could_ be used for governance proposals, it 
> wasn't the initial intention.
> 
> There might be certain dApps that use it that require you to KYC, that would be their choice.
> 
> and as discussed, twitter would be the first mechanism, with discord, TG, and potentially keybase as well.

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2022-10-11T16:03:14.331Z

[https://www.lns.money/](https://www.lns.money/) allows users to purchase .luna addresses as tied to a wallet address and link social media accounts. While working in a different way, this seems to be a way to tie social media identities to a Terra wallet address.

I agree with the **Motivation** for your proposal and support it in that sense, however in my mind, it seems LNS are already on the way to solving this problem.

**Anonymous (`terra19v62f65v9kdy05c48v6fgnf4yvrqsjvqqyp8n0`)** — 2022-11-21T09:52:47.960Z

One month has gone throw from the day your proposal passed. What is the progress on this?

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2022-12-20T22:17:54.383Z

an update.
since this started, it hit a few delays.
but it was progressing.

sadly someone on the osmo chain just launched inside the wallet a service which was nearly identical to this. 

as such I have decided to return the remaining funds back to the community

[https://terrasco.pe/mainnet/tx/A9803B360EF7648C7F4437A907D0BD118A47FCF60BF3B4B8A3108C1B2E25526B](https://terrasco.pe/mainnet/tx/A9803B360EF7648C7F4437A907D0BD118A47FCF60BF3B4B8A3108C1B2E25526B)

**Anonymous (`terra16mnrr6w07quansa7a60fmngtfy7s3pvc4d0zda`)** — 2022-12-21T00:30:49.487Z

A token that stores encrypted data needed to validate a person's identity.
Something similar to soulbound token

