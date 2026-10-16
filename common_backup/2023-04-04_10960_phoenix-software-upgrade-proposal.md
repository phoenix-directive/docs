# Phoenix Software Upgrade Proposal

- **Thread ID:** 10960
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2023-04-04T17:51:15.241Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 398
- **Reactions:** 0
- **Comments:** 3
- **Source:** https://common.xyz/terra/discussion/10960-phoenix-software-upgrade-proposal

---

_Disclaimer: I am an employee of Terraform Labs_

## **Summary**

On 21 March 2023,** **Terra upgraded Pisco (Terra’s testnet chain) and incorporated several new and important updates, including:

- - Upgrading Cosmos-SDK to v0.46.x
- - Updating Wasm to use v0.30.0
- - Updating IBC and packet-forwarding-middleware from v3 to v6
- - Adding IBC-hooks as a custom module
- - Adding the token-factory module
- - Enabling the ICA-controller module
- - Adding the Alliance module


Following testing, this software upgrade proposal will incorporate these updates into Phoenix-1 (mainnet). 

## **Terra Core v2.3.0 – Upgrade Details**

**Upgrade Cosmos-SDK to v0.46.x**

This update upgrades Terra’s version of the Cosmos SDK to v0.46.x (See **[GitHub](https://github.com/cosmos/cosmos-sdk/releases/tag/v0.46.10)** for release details). Post-upgrade, governance proposal deposits will only be burned for “No with veto” results; others will be refunded. Expect a temporary Phoenix chain halt due to this update, as experienced by the Pisco chain in its similar upgrade. Also, be aware of breaking changes and new endpoints in LCD APIs; consult the **[Terra Core upgrade guide](https://docs.terra.money/upgrade)** for details.


**Update Wasm to use v0.30.0**

This update allows Wasm to use Wasmd now. Wasmd is a Cosmos zone implementation with WebAssembly (WASM) smart contracts enabled based on a cosmos/gaia repository fork. The Wasmd binary functions like gaiad, with the addition of the x/wasm module. It provides compatibility with CosmWasm contracts and supports various interface versions.


**Update IBC and packet-forwarding-middleware from v3 to v6**

This updates the IBC module to a newer version with enhanced functionality.


**Add IBC-hooks as a custom module**

IBC hooks is a middleware that can allow ICS-20 token transfers to initiate contract calls. This allows cross-chain contract calls that involve token movement and can be helpful for cross-chain swaps, among other things.


**Add the token-factory module**

The token factory module reduces contract complexity and allows tokens minted on Terra to be directly staked into Alliance.


**Enable the ICA-controller module**

The Interchain Accounts module is a Cosmos SDK implementation of the ICS-27 protocol, enabling cross-chain account management using IBC. Interchain Accounts differ from regular accounts by being controlled programmatically via IBC packets instead of using a private key. Enabling the ICA controller module will allow Terra to control host accounts on other chains for cross-chain transactions.


**Add the Alliance module**

**[Alliance](https://github.com/terra-money/alliance/releases/tag/v0.1.0)** is an open-source Cosmos SDK module that leverages interchain staking to form economic alliances among blockchains. Through integration, chains like Terra’s can strengthen their decentralized economy by attracting users, liquidity, and developers, augmenting staking yield, and directing monetary policy (L1 token inflation and fees) toward incentivizing desired user behaviors.

Example use cases:

- - Add Liquid Staking Derivatives (LSDs) of Cosmos assets as _Alliance Assets_ to attract user and capital inflows.
- - Set a _Take Rate_ above 0% for _Alliance Assets _to diversify and augment LUNA staking yield.
- - Add native DEX LP tokens as _Alliance Assets_ to incentivize on-chain liquidity for specific pairs.
- - Add soulbound NFTs as _Alliance Assets_ to incentivize native adoption of them.
- - Add native project tokens as _Alliance Assets_ to incentivize project development.


All _**[Alliance Assets](https://alliance.terra.money/alliance#what-are-alliance-assets)**_ and their corresponding _**[Take Rates](https://alliance.terra.money/alliance#the-take-rate)**_ and **_[Reward Weights](https://alliance.terra.money/alliance#how-are-rewards-determined)_ **are decided through governance. As a result, they can be modified at any point, allowing the Terra community to collectively determine how to grow our domestic economy as it evolves.

—

This governance proposal provides a brief summary of the proposed updates. For a more detailed Terra Core v2.3.0 upgrade breakdown, consult the **[upgrade overview](https://docs.terra.money/spec)** in the Terra Docs.

---

## Comments (3)

**4719 (`terra13qjxhnw98lm36rxc9yjakkmulhpv7zctdc5zlz`)** — 2023-04-04T18:09:42.494Z (edited 2023-04-04T18:42:15.922Z)

👍

**Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2023-04-04T18:21:41.059Z

I presume the token-factory parameters will match what is on test-net.
I personally think we should raise the price of tokens to 50luna (from 10).

**Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)** — 2023-04-05T06:47:02.192Z

Hey [@PFC](https://agora.terra.money/profile/id/55765), thanks for the feedback. Some datapoints to anchor the discussion.

Cost to deploy a cw20 token: 0.0054503 LUNA
Cost to deploy a token (factory) on Juno: 1 JUNO
Cost to deploy on Osmosis: 10 OSMO

10 LUNA seems reasonably costly for now.

However, the downsides of having too many native tokens would be that the bank balances endpoint would be slower, which might impact station UX. IMO, we could have this as a separate params update proposal after the upgrade if required.

