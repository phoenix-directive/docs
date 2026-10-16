# SCV - Terra Security Expansion Program Proposal

- **Thread ID:** 7889
- **Author:** Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)
- **Created:** 2022-11-29T23:21:12.455Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 920
- **Reactions:** 1
- **Comments:** 6
- **Source:** https://common.xyz/terra/discussion/7889-scv-terra-security-expansion-program-proposal

---

# Summary

This is a proposal to fund the proactive approach to security benefiting the Terra community, leveraging the expertise and position of SCV. Continuously helping all projects and software within Terra's ecosystem by:

- proactively identifying risks on Terra’s software stack;
- coordinating vulnerability disclosures and remediations;
- actively monitoring external surface for vulnerabilities;
- providing security awareness, training and guidance.


In a nutshell, at SCV, We combine high end security research with a real world attacker mentality approach to reduce risks, fortifying code and implementations for the entire Terra perimeter and software stack for Terra.

The funding would be required to sponsor vulnerability research, small hackathons and continuously scaling our proactive security work dedicated for Terra and on-chain projects.

SCV team is asking _550_000_ Lunas or ~ 900k from the community pool to bootstrap and scale what is described in this proposal. Note that, SCV is a registered company and all considerations were based before tax.


** Based on feedback, we re-worked items this proposal; unfortunately we had to removed the old one to avoid confusing between them two. This new proposal should reflect all changes. **

# About SCV

SCV is a security firm of security researchers and old-school hackers with expertises in various technologies and ecosystems. We do hacking and security for a living. We are absolutely passionate about security and helping the community.

We believe security is an evolving challenge and requires constant vigilance, proactive approach, research and passion. We easily adapt to new environments and are well versed in identifying sophisticates vulnerabilities and maximise it's risk impact while keeping a full integrity all-round from the start.

SCV has more than 15 years of experience in the cyber security industry and have been involved in the hacker culture for much longer. We have a good relationship with security professionals and security researchers in the field.

# What We Do

We are a trusted security provider for Terra, we are working to improve the security posture of the entire Terra ecosystem and perimeter through open-source initiatives, traditional security, audits and innovative security research.

In a nutshell, at SCV, We combine high end security research with a real world attacker mentality approach to reduce risks, fortifying code and implementations for the entire Terra perimeter and software stack for Terra.

We engage directly with TFL, customers, protocols owners and the community. Our goal is to minimise potential attack vectors by identifying and remediating risks and consequentially avoiding it being exploited by malicious actors for financial gain or reputation damage, protecting users and the reputation of our Terra ecosystem.

SCV’s proactive work and security methodology let the team to identify critical vulnerabilities that could result in many project and users losses.

Whether it is Web3 or Web2, there will always be bugs for us to find!

# Significant Past Contributions

Items below describe a few vulnerabilities SCV were able to disclosure and coordinate related to Terra ecosystem. Note that, several others cannot be shared or still in the works.

- **Terra Station Mobile (Android & iOS)** → Lack of double encryption when storing wallet secrets on mobile storage and data grab from other apps that could be installed (Android only).


- **StarTerra Genesis Airdrop **→ Saved the project a ~25M hack in a contract vulnerability that could compromised the entire genesis airdrop allocation.


- **Pylon Protocol **→ Lack of contract permissions allowed anyone to move funds from pools.


- **Anchor Protocol →** Orchestrated an attack to completely takeover and control "[anchorprotocol.com](http://anchorprotocol.com)" apex domain. We also broke into Anchor's mail-list APIs "subscribe for updates", that could result in user data leaked (email address, full name, location and IP). We also could impersonate any account under @terra.money and send e-mails on their behalf.


- **Mirror Protocol** → Identified issues with the oracle price and manipulation;


- **Wallet Leaks** → Identified wallets seed exposure (via API, Github, etc) and successful contact owners and returned about ~700k in total funds. Also help Terra users recovering funds from "hacked" seeds that would be gone to scammers.


- **TFL's/Core Infrastructure **→ Identified several issues related to exposed endpoints, servers and services misconfiguration that could cause a major problem if abused.


# Proposal Motivation

Security is unfortunately not a priority topic for many projects and protocols owners and is often underestimated and overlooked.

SCV understands that, finding reliable and trustworthy people in the industry is challenging, especially due the lack of domain knowledge in the area and the professional skills shortage.

All it takes is a single successful exploit to potential cause irreversible financial and reputation damage and consequentially loss of trust. SCV believes security works the most (reactive vs proactive) when proactive by continuously enforcing the perimeter and reduce the attack surface by actively monitoring and actual finding weak spots long the way.

With the amount requested in this proposal in Lunas, SCV can continue to grow, hiring security experts, incentivise security research and increasing our reach within the Terra ecosystem for the community. Growth is vital as Terra expands, particularly with Alliance and other dapps coming aggressively to the ecosystem.

SCV will be expanding the services they offer to continuous monitoring projects on Terra and helping to maintain a bare minimum level of security for them. Some of these include:

- CI/CD misconfigurations;
- GitHub/Gitlab secrets leak;
- dapps security hardening;
- Web Security in general & Weak implementations;
- Best Efforts on CW vulnerabilities, critical/high (if open source);
- CW Contracts fuzzing to find potential vulnerabilities/weaknesses (if not open source);
- Poor Security operations design (ie: contract admins able to tap into funds);
- Terra Core SDK and Tendermint research;
- Common CW pitfalls and how to avoid it; (making audits cheaper as code quality evolves).
- vCISO approach for Terra projects and related.


Funding vulnerability research and providing assurance on services is not an easy task. It requires leadership and knowledge in the area to have the most outcome; finding reliable people is also a challenge, since it is “too easy” to overlook a vulnerability and exploit for own profit at later stage.

We believe SCV is a Terra’s trust security provider that is well positioned in the market to benefit and add value the community and Terra’s projects as a whole. In fact, not only Terra, other Cosmos chains as well since they share often same software stack (Tendermint and CosmWasm).

# **Deliverables**

Security is a pretty hard topic to quantify efforts. As as an example, you can spend months digesting Terra/Cosmos core code and still have no relevant issues to raise; however, it does not simply invalidate the time and effort and of applied methodology approach; It’s indeed an endless process with a great amount of dynamic moving parts.

At SCV, We believe security engagements exercises and code reviews are a constant rather than “do only once and live”. We also mentioned we believe in proactive vs reactive security.

That being said, if this proposal passes, SCV would be able to scale its operations at Terra as described above and provide these following services, free of charge, to each live project related to Terra.

- **Penetration testing on Web and APIs →** We would provide continually security assurance and recommendations on dapps and APIs. SCV would cover all public CVE’s and common exploits based on each technology;


- **APIs/Backend Code Review →** We would code review backend implementations and APIs middlewhere integrations to ensure there’s no risks involved.


- **GitHub/Gitlab monitoring →** Whenever there’s a wrong commit that exposes sensitive content, leading to a risk to the protocol, owner or user, SCV would be the first to know and report;


- **Security Assistance (vCISO) →** We can help with a security related questions and requirements when prototyping an application or an implementation; We can provide guide along the process to ensure all risks and issues are identified in earlier stages;


- **CW Contract Checks →** While we can't comprehensive audits contracts on-demand, we are able to assist with small modifications and security sanity-checks specially prior audits.


- **OSINT →** SCV would watch for our open source intelligence flow and act accordingly on each event. These events can be anything with a risk attached to it, ie: password leaks, new sub-domain added, etc.


SCV would continue to disclose vulnerabilities and interact directly with protocols and their security owners to reduce risks and working on remediations when necessary. Researching results would be published in the form of blogs posts write-up or and vulnerability reports content on SCV’s public Github repository.

# TL;DR Questions

**How this proposal relates to contract audits offered by SCV ?**

Comprehensive audits of contracts would remain offered separately. A comprehensive audit means SCV allocates resources during an agreed time to thoroughly audit and report results. This proposal aims to increase our reach, particularly in other areas including in-house opensource security tooling, security monitoring of the chain and security research.
As an example, TerraPoker has not beed audited. Although, project is open source which permitted us to ensure the code is "appropriate" and safe to use; also added in the watch list for contracts updates/migrations. The contract auditors within SCV are a separate team, the team is funded as a direct result of their contracted work.

**Is SCV profitable ?**

Yes, SCV became profitable last quarter (Q3). We have others money steams such as, validator and CosmWasm audit services. Which none are directly related to this proposal, we cannot funding what we are proposing here without asking for the community fund. We also received ~100k Lunas from the emergency allocation that were used to support company operations and the proactive work we do on behalf of Terra.

**What is proactive security ?**

There is no such thing as "perfect code". Everything is hackable over time. SCV continuously looks for new attack surfaces, trying to uncover vulnerabilities, and risks, that could have a major impact on the community. Covering all Terra related technologies including, web2 to web3.
We try to discover new attack vectors and work on remediations before they are discovered by our adversaries. I'm sure you heard about "wallet exploits", "dapps signing malicious transactions", "cosmos core bugs", "contract vulnerabilities", "contracts redressing issues", in the past. These vulnerabilities are not easy to find and take a considerable amount of research, persistence and skill to discover and remediate.
Let's assume there is a vulnerability in Terra Agora where we can simply login as other users, critical right? Or if, there's a way to "execute a contract" but instead, we smuggling another message to "remotely" control users wallets and move out funds. Also critical correct? Or maybe let’s suppose there’s a way to make validators miss blocks and stress pressure the chain ?
Uncovering errors and developing proof of concepts (POCs) is our magic, this is what we do. Finding issues before they have an impact and this is what "being proactive" with security is about.

**How funds would be used ?**

The funding will allow SCV to focus more on proactive security impacting Terra and the Terra community. As a business, with paid employees, we strive to balance our paid work with our passion for helping the Terra community. On average, a good researcher and security professionals costs around ~15k monthly. This funding would allow us to assign more of our security experts time to focus on Terra projects and the greater good of the Terra community.
SCV will initially stake the allotment and use the yield plus a draw down to fund proactive work, incentivise research and hackathons (small hack house) event.
We also want to remind that, SCV was born from the community as a result of our proactive work in the past and preset. Terra and Luna is surely SCV’s best interested, and we’d surely use the funding wisely in pro of the Terra security and it’s community and projects that lives in it.

# Short Conclusion

It's not a secret SCV is completely passioned about Terra and security. We do what we love, we are proud of things we achieved in this ecosystem and we are going to keep it up if the community agrees on this grant or not, we will continue to the same quality of work we have been since we joined Terra.

In our opinion, the community funding should be used to support projects that directly benefits the community and Terra in any way. It’s a challenge to differ legit projects than malicious ones, specially when there’s no history or context around it. 

We also believe past SCV’s actions speaks more than just words. While money is important, it’s not everything; it can be used as a tool as we described all above; Integrity and reputation is all we have in this industry and we are definitely keeping ours intact. Security and work quality would always be SCV's top priority above anything else.

Let SCV work in pro of the community from its own community!

Do you have a skill ? Do you want to learn something new ? Can you contribute in some way

Please reach out !

# Thank you

On behalf of SCV, We appreciate your time reading until the end!

--
Hack the planet - Reference to "Hackers" (1995 movie).

---

## Comments (6)

**Anonymous (`terra1heay4nz54pkn20flf2cu0hlayl4ew9teq6rrz3`)** — 2022-11-30T09:57:58.630Z — 👍 1

Hey Vini, thanks for the further elaboration and clarification that this is a separate scope from your auditing services. 

> The funding will allow SCV to focus more on proactive security impacting Terra and the Terra community. As a business, with paid employees, we strive to balance our paid work with our passion for helping the Terra community. On average, a good researcher and security professionals costs around ~15k monthly. This funding would allow us to assign more of our security experts time to focus on Terra projects and the greater good of the Terra community.

However, I do think that $180k per researcher is on the high end of the pay scale (assuming $990k shared among 5 researchers at a rate of $15k a month). Considering the fact that you are using this to pay existing employees to focus on Terra research, I assume this means that they are being paid on top of their current salary (as you mentioned SCV is currently profitable). Thus, please provide a bit of a clearer breakdown of how exactly the $990k will be spent. 

Would also like to see greater transparency on SCV itself. We don't know who the team are, their backgrounds, etc. $990k is a ton of money and would prefer to not pay it into a blackhole. 

The deliverables that you mentioned are great. But can you elaborate on how you plan to scale along with the Terra ecosystem? A team of 5 researchers (again, am assuming since no clear details were given) might be able to handle the current size of the Terra ecosystem, but in the coming months I'd expect the number of live protocols to grow significantly. 

Would also love to hear what others in the community think, especially and TFL and other protocol leads, since they are maintaining Terra core infrastructure and a number of projects that are live/TBC.


_All opinions are my own and not that of organizations that I represent._

> **Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)** — 2022-12-01T18:19:51.311Z
> 
> Hi Ian, thanks for your input.
> 
> I agree with you on the high end pay, good security professionals are normally well paid due the nature of the work they provide. As We mentioned in the past, finding security professionals is usually not hard; finding reliable ones is the key criteria here, there are a few things SCV definitely cannot afford to have and the lack of integrity is surely one of those items. 
> 
> As far as the spending goes, it would be used to scale up our proactive work and actually commit to deliverables we listed in this proposal; There are a lot of variables to consider when researching and unfortunate it cannot be “back and white” due too many moving parts along the process or the actual underlying technology we meant to be researching on. I understand the logical way of thinking would be to list exactly items in detail, however, it unfortunately does not work that way. As an example, We could say we’d spend months researching Tendermint or Cosmos modules perhaps, but the reality is that it would still be vague and subjective. As a company, it is one of our jobs to control the spending and redirect efforts where we believe we would get the best outcome for Terra as a whole. I also believe SCV’s methodology and past execution reflects exactly this reality since we proved to be reliable, passionate about Terra, and skilled in cyber and crypto security.
> 
> In terms of demand, security is not quantitative. We have an everyday routine on Terra that helps us identify attack surfaces and internal label stuff to “work next” or redirect research efforts to. Even if Terra grows 10x, we can still cope with demand on services we listed there. The approach we take on those services are proactive and requires a lot of monitoring and tooling we have in-house that facilitates the process as a whole. In summary, It is also one of our jobs to determine which projects or components require the most of our attention in the sense of “most exposed or vulnerable”.
> 
> Once again, I appreciate you taking the time to weigh on this proposal with your considerations.
> 
> Thank you.

**Anonymous (`terra16dxhluqdax72rpgrqc2qx4f68rj933wfc2rsjt`)** — 2022-12-05T15:38:14.504Z

Hello Vini! 

Imho, your work in SCV and this proposal is very important for Terra protocol and community. I have no doubt about your good intentions for Terra. My unconditional "trust" - is my personal opinion, which based on your (Vini) work as validator in Terra.

but I would agree with IAN in all point he has mentioned. _550k Luna - _is a huge grant._ _in general we are not against it, but it need to be more transparent. The best way will be to add some milestones, separate this grand into 4-5 tranches, add multisig wallet with 2 member of TFL (as the main responsible organization in Terra) , and SCV make some report at least to TFL. and after this reports next payment will be processed.

I understand the research side of your work (as soon as I spent 7 years in science research studies). you could spend a lot of time and do huge work with no "positive" result. in security field under "positive" result i mean - finding any vulnerabilities. But and "negative" result - is a good result too for us. it mean there is no security breaches.and due to that, will you give any kind of warranties after your research?

> **Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)** — 2022-12-05T21:47:59.761Z
> 
> Thanks for your input [@sw33 | pro-nodes75](/terra/account/terra16dxhluqdax72rpgrqc2qx4f68rj933wfc2rsjt) 
> 
> We do understand where you are coming from with the milestone approach, although it’s impractical to justify or quantify what would be a “milestone” to start with. A milestone would normally be pre-defined once you know items you want to achieve in a particular time frame window or due date; which works fairly differently for this proposal since everything it's dynamic and requires constant attention and efforts as projects and technologies emerge. An example of that (fresh example) could be Skip.Money. They went live on Terra testnet this week and are planning to go mainnet next week, SCV reported a few things directly to the team which wouldn’t be “classified” as “milestone” or nor directly related to TFL. However, it does relate to Terra’s security as a whole since we are dealing with consensus (could potentially result in chain halts). In summary, not all vulnerabilities are public or need to be reported to TFL directly, hence it's hard to track “milestones”. Not to mention, TFL shouldn’t be involved in every aspect of Terra or take part in our research. We believe this is a great way to enforce decentralisation as well. 
> 
> Our goal is to minimise any kind of exposure and reduce security risks which we believe it’s been working out since we got into Terra. Due to the nature of how security actually works – nothing is 100% safe – we cannot unfortunately provide any warranties at any kind. We believe everything is hackable overtime as technologies and attack vectors become more sophisticated too. That being said, we believe the best way to imply security is via a proactive rather than a reactive approach, and this is what we are aiming to continue offering for Terra and related projects.
> 
> Once again, we appreciate your input here. 
> Best Regards

> > **Anonymous (`terra16dxhluqdax72rpgrqc2qx4f68rj933wfc2rsjt`)** — 2022-12-06T09:12:05.582Z
> > 
> > thank you for response! Once again, i understand your point. And have no arguments not to agree with you.
> > but in this case we will vote - abstain. the main reason - we would like to see another way of financing. may be 2 separate proposals, both with 0.5 amount of luna, you are asking now.
> > And if this proposal was made by someone else but not you (Vini), we would vote - No. As it was said before - you have community reputation.
> > Bc somebody asking almost 1kk $ with no feedback, no warranties and at one payment.

> > **Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)** — 2022-12-06T11:22:09.806Z — 👍 1
> > 
> > Thank you! appreciate your input here.

