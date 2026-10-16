# Entropy Beacon Community Funding Grant

- **Thread ID:** 6703
- **Author:** amit (`terra17h4xr6naneyjr6undxjfypjw8atwr26jpgxa52`)
- **Created:** 2022-08-19T22:40:25.092Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 2713
- **Reactions:** 0
- **Comments:** 4
- **Source:** https://common.xyz/terra/discussion/6703-entropy-beacon-community-funding-grant

---

First off, who am I? I’m Amit, a developer and creator of Entropic Labs. I created the Entropy Beacon, including frontend, infrastructure, libraries, and smart contracts. I am also ex-TFL.

# Overview
The Entropy Beacon was developed to provide secure and unpredictable entropy (randomness) on-chain, through a decentralized on-off chain system. One of Terra’s main value propositions is the ease of development, and the community that has sprung up around it. To further this narrative, the Entropy Beacon aims to facilitate the creation of dApps and DeFi games that require a secure source of randomness.

The intention is to make the Entropy Beacon a community utility; “just another” feature that exists on Terra that builders can take advantage of to create the next generation of application development. The project is already fully open-source on our Github page. This proposal requests a grant from the community pool to support development, and subsidize operations of the Entropy Beacon and surrounding infrastructure. This will undoubtedly incentivize development on Terra 2.0, bringing value to the entire ecosystem.

# How Entropy Beacon works
For some context, here's a quick summary of how the Beacon works:
1. Contracts request entropy from the Beacon
2. Off-chain infrastructure generates entropy alongside a “proof”, which allows anyone to verify that the generated Entropy is tamper-free
3. The generated entropy is submitted to the Beacon, verified, and then passed along to the original requesting smart contract.


More detailed information can be found in the [documentation](%5B%3Chttps://entropiclabs.io/beacon/docs/how-it-works%3E%5D(%3Chttps://entropiclabs.io/beacon/docs/how-it-works%3E))

# Comparison to existing solutions
Existing solutions on Terra 1.0, notably, Terrand, were simply not secure enough, or random enough to be used by any application involving the transfer of real funds. Terrand worked by publishing the results of Cloudflare’s [League Of Entropy](%5B%3Chttps://www.cloudflare.com/leagueofentropy/%3E%5D(%3Chttps://www.cloudflare.com/leagueofentropy/%3E)) beacon to the blockchain. This was both inefficient, insecure, and predictable for two major reasons:
- Once the latest “round” of entropy from the League Of Entropy is published, anyone can access the “seed”. This means that anyone can extrapolate the results of contract executions that use Terrand as their randomness source, before calling the contract. TLDR: They can predict “random” results.
- The League of Entropy only publishes a new “round” of entropy every 15-20 seconds, or more. For unpredictable randomness, there needs to be new “rounds” of entropy for every single contract execution requiring randomness.


Foreign solutions on other chains include [Chainlink’s VRF](%5B%3Chttps://chain.link/chainlink-vrf%3E%5D(%3Chttps://chain.link/chainlink-vrf%3E)). Whilst obviously not being available on Cosmos-based chains such as Terra, Chainlink’s VRF is also encumbered by the tokenomics of their LINK token. Requests for randomness to Chainlink VRF either require “subscription management”, or some sort of payment in LINK tokens. This is expensive while also hampering the developer experience of anyone who wishes to use Chainlink. The Entropy Beacon, on the other hand, only requires gas fees to be paid by the calling contract, all of which is handled using LUNA instead of a third-party token. If this proposal passes, an additional “protocol fee” that is used to cover the cost of running an off-chain worker will be set to zero and subsidized.

# Future Development
We are currently working on tooling that will enable developers to use Beacon seamlessly on LocalTerra. This will require a “mock beacon” system to be created which allows developers to test contracts that utilize the Beacon on LocalTerra using tools that make such development easy. The defining feature of the Terra ecosystem has been the development experience, and bringing the beacon to a state where we are able to seamlessly integrate it into the Terrra developer experience is a major goal.

In addition, it is possible that the cryptography libraries that are at the foundation of the Beacon system can be used in creating novel applications that connect on- and off-chain experiences. The continued development of the Entropy Beacon will help to battle-test these libraries and provide support for any that wish to use it.

# Grant Proposal
Utilities like these are often encumbered by the need for profit. Entropy Beacon was created with ease-of-use and low fees in mind, and as such has zero profit opportunity. We are not interested in acquiring VC funding that will undoubtedly require monetization, and therefore fees, of the system. This is why this proposal requests the use of community funds to provide funds for development and infrastructure costs. In addition to this, a significant incentive can be created by subsidizing beacon costs.
To these ends, a total of 50,000 LUNA is requested from the community pool. This will be broken down approximately:
- 40% - The establishment of a decentralized subsidization pool for anyone hosting workers. This will step in to compensate workers allowing for the “protocol fee” of the Beacon system to be eliminated, easing the use of the entire system. In addition, these funds are planned to be the basis of a “vault” that will be used to provide future utility, such as flash loans, on Terra.
- 10% - Some basic infrastructure costs to bootstrap usage. Since we expect that volume on the beacon will be low in early stages, running a worker may not be considered profitable or worthwhile to any member. To prevent the possibility of attacks stemming from long delays, we will be hosting workers on servers that we own and pay for, likely at a loss. This will help to pay for said servers over a long period of time. If it turns out that these funds ever become unnecessary, we will deposit this into the subsidization pool.
- 50% - Funding development, past and future. This project _will never be profitable_ since we strive to make the best community tool possible. As mentioned earlier, implementing monetization will only serve to add friction to the developer and user experience. As such, these funds will help support development for the medium-term future.


Glad to answer questions and iterate on community feedback.
## Useful Links
- Entropy Beacon: [https://entropiclabs.io/beacon](https://entropiclabs.io/beacon)
- Documentation: [https://entropiclabs.io/beacon/docs/](https://entropiclabs.io/beacon/docs/)
- Twitter: [https://twitter.com/Entropic_Labs](https://twitter.com/Entropic_Labs)
- Github: [https://github.com/EntropicLabs](https://github.com/EntropicLabs)

---

## Comments (4)

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2022-08-20T16:19:33.371Z

I support this proposal on principle. Love the idea of OSS tools being built to provide tooling to help the Terra ecosystem grow.

That Entropy Beacon will never be profitable means the only way it will be developed is if someone funds it. The Community pool seems the logical choice.

Question checklist:

1. Does this tool benefit the ecosystem?
2. Is the ask reasonable?
3. Do we believe team can deliver?

> **amit (`terra17h4xr6naneyjr6undxjfypjw8atwr26jpgxa52`)** — 2022-08-20T17:00:30.793Z — 👍 1
> 
> Addressing #3 - We’re already live on mainnet and testnet, albeit with a few kinks in the developer experience as we don’t have a LocalTerra version yet, and hosting the backend workers isn’t as smooth as we’d hoped. Both of these are in the works.

**Anonymous (`terra1lxc6c5rnvcfx94x2ejarsr55cmcec6apklkdpw`)** — 2022-08-21T00:24:45.286Z

Great that you are releasing this as a public good. One question, how does this compare to a solution that uses Band Protocol to request for a random seed. (if it is integrated to Terra)?

> **amit (`terra17h4xr6naneyjr6undxjfypjw8atwr26jpgxa52`)** — 2022-08-21T03:23:08.361Z (edited 2022-08-21T03:24:14.596Z) — 👍 1
> 
> To put it simply, this can be used today, and Band Protocol can't. Since not many details are available about the Band Protocol VRF, I'm not sure I can elaborate further.
> 
> In addition, as stated many times, we don't plan on monetizing this resulting in a system that is in all likelihood cheaper and more ergonomic than a monetized alternative.

