# Phoenix Software Upgrade Proposal v2.5

- **Thread ID:** 13551
- **Author:** Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)
- **Created:** 2023-10-02T06:07:29.068Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 305
- **Reactions:** 1
- **Comments:** 3
- **Source:** https://common.xyz/terra/discussion/13551-phoenix-software-upgrade-proposal-v2-5

---

On September 14th, 2023, Terra’s Pisco testnet was upgraded to v2.5, incorporating several new features and bug fixes. One of the notable upgrades is the move to Cosmos SDK 47. This version supports ABCI 1.0 and has official support for the CosmWasm module. Another notable change is the inclusion of the [Protocol-Owned Builder (POB) module](https://github.com/skip-mev/pob) built by Skip Protocol. This Cosmos SDK module gives developers the ability to define how their apps construct and validate blocks on-chain in a transparent, enforceable way, such as providing complete control to Terra to recapture, control, and redistribute Maximal Extractable Vaule (MEV).

Note: We’ve included the POB module in this chain upgrade, but it is not enabled by default. Given that this is a significant change in terms of block production, we will publish a separate governance proposal on-chain to enable the module.

This proposal aims to upgrade Terra’s Phoenix mainnet to v2.5. A governance proposal will be sent on-chain for voting and details regarding the time of the upgrade will be included.
 
Breaking changes: 

- This upgrade will require the use of IBC relayer [v2.4.0](https://github.com/cosmos/relayer/releases/tag/v2.4.0) or later, or any other relayer compatible with IBC-Go v7
- Update [@terra-money/feather.js](https://www.npmjs.com/package/@terra-money/feather.js/v/1.1.1-beta.1) to use the latest protobuf additions
- Update [terra-proto-rs](https://crates.io/crates/terra-proto-rs/4.0.0) to use the latest protobuf additions and extend to implement all message types supported natively by Terra
- [Terra-sdk python](https://pypi.org/project/terra-sdk): library upgraded to be compatible with Terra Core v2.5. TFL has discontinued the maintenance for this library and has entered it into the public domain under an MIT license


Core Dependency Upgrades:

- Alliance: v0.1.2 => [v0.3.2](https://github.com/terra-money/alliance/releases/tag/v0.3.2)
- CosmosSDK: v0.46.13-terra.3 =>[ v0.47.5-terra.2](https://github.com/terra-money/cosmos-sdk/releases/tag/v0.47.5-terra.2)
- CometBFT: v0.34.27-terra.rc.1 => [v0.37.2](https://github.com/cometbft/cometbft/releases/tag/v0.37.2)
- CosmWasm: v0.30.0-sdk469.5 => [v0.41.0](https://github.com/CosmWasm/wasmd/releases/tag/v0.41.0)
- Wasmvm: v1.1.2 => [v1.3.0](https://github.com/CosmWasm/wasmvm/releases/tag/v1.3.0)
- IBC-Go: v6.1.1 => [v7.3.0](https://github.com/cosmos/ibc-go/releases/tag/v7.3.0)
- Packet Forward Middleware: v6.0.2 => [v7.0.0](https://github.com/cosmos/ibc-apps/releases/tag/middleware/packet-forward-middleware/v7.0.0)
- IBC hooks: (Terra Core) v2.4 => [v7.0.0](https://github.com/cosmos/ibc-apps)
- TokenFactory: v0.30.0-sdk469.5 into Terra Core v2.5 (with smart contract hooks. [More info](https://github.com/terra-money/core/blob/release/v2.5/x/tokenfactory/README.md))


Bug Fixes: 

- Fixed an issue with update-client terrad IBC-command (Reported by Synergy Nodes)
- Fixed: Interchain controller params call returns "UnmarshalJSON cannot decode empty bytes: panic” (Reported by Bretheren on Github)
- Fixed a vulnerability regarding Packet Forward Middleware interacting with IBC hooks (Reported by SCV)
- Migrated atlantic-2 IBC channels to increase the unbonding period from 2 days to 5 days (Reported by the Astroport team)


Thank you to the community members for reporting these bugs!

Fork Updates:

Finally, we updated some forks maintained by TFL and partners to use the officially developed libraries. Using officially supported libraries allows Terra to get upstream updates faster and reduces overall maintenance effort on the Core team.

- github.com/terra-money/tendermint => github.com/cometbft/cometbft
- github.com/terra-money/wasmd => github.com/CosmWasm/wasmd
- github.com/terra-money/core/v2/x/ibc-hooks => github.com/cosmos/ibc-apps/modules/ibc-hooks
- github.com/strangelove-ventures/packet-forward-middleware => github.com/cosmos/ibc-apps/middleware/packet-forward-middleware/v7

---

## Comments (3)

**Vini (`terra18ruqkccl5tp493uhvra0u6jylrzq8t8dv5qs4c`)** — 2023-10-04T10:34:09.600Z (edited 2023-10-04T10:34:51.018Z)

Skip POD been archived and moved to a new repository (not sure why or motives). Terra is currently pointing to the archived version which would need to be updated ideally, [https://github.com/terra-money/core/blob/release/v2.5/go.mod#L27](https://github.com/terra-money/core/blob/release/v2.5/go.mod#L27)

For what is worth, SCV will support this core upgrade.

> **Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)** — 2023-10-06T13:03:18.120Z
> 
> Hey Vini, we chose to use this version as it is already in a few main nets in production. The newer module ([https://github.com/skip-mev/block-sdk](https://github.com/skip-mev/block-sdk)) introduces a few new concepts and we've not tested them yet. Will be moving to the `block-sdk` once we have seen some chains implement in production.

> > **Anonymous (`terra16mnrr6w07quansa7a60fmngtfy7s3pvc4d0zda`)** — 2023-10-08T01:14:27.354Z
> > 
> > <!DOCTYPE html>
> > <html lang="en">
> > <head>
> >  <meta charset="UTF-8">
> >  <title>Terra Innovation</title>
> >  <style>
> >   body {
> >    font-family: Helvetica, sans-serif;
> >   }
> >  </style>
> > </head>
> > <body>
> > 
> > <p>
> > I understand your point of view that Terra should wait for other chains to implement something before updating its own library. However, I disagree with this approach. I believe that Terra should be a leader in innovation, development, and implementation of new things and ideas.
> > 
> > **As a reminder, Terra was the first chain to create Anchor, a stablecoin lending protocol that has become one of the most popular DeFi applications in the world. Terra's willingness to innovate and take risks has helped it to achieve significant success.**
> > </p>
> > 
> > <h2>Importance of innovation for Terra's long-term success</h2>
> > 
> > <p>
> > Innovation is essential for long-term success in any industry, and in the world of cryptocurrencies, it is even more crucial due to the constantly evolving market. Chains that do not stay at the forefront of innovation risk falling behind and losing market share.
> > </p>
> > 
> > <h2>Benefits of being a leader in innovation</h2>
> > 
> > <ul>
> >  <li>Attracting new users and developers</li>
> >  <li>Maintaining a competitive advantage</li>
> >  <li>Solving problems that other chains cannot</li>
> > </ul>
> > 
> > <h2>Risks of innovation and how Terra can mitigate them</h2>
> > 
> > <ul>
> >  <li>Conducting thorough testing before implementing new features or functionality</li>
> >  <li>Implementing new features incrementally to allow users and developers to adapt to changes</li>
> >  <li>Providing a feedback process so that users and developers can provide feedback on new features</li>
> > </ul>
> > 
> > <h2>Specific ideas on how Terra can be a leader in innovation</h2>
> > 
> > <ul>
> >  <li>Investing in research and development of new technologies and features</li>
> >  <li>Fostering a culture of innovation among employees and community members</li>
> >  <li>Collaborating with other blockchain projects</li>
> > </ul>
> > 
> > <p>
> > In conclusion, Terra has the potential to lead innovation in the blockchain space by being proactive in adopting new technologies and in creating a culture of innovation, while mitigating the risks associated with these initiatives. This will ensure its long-term success.
> > </p>
> > 
> > </body>
> > </html>

