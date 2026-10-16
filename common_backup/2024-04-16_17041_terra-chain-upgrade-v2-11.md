# Terra Chain Upgrade - v2.11

- **Thread ID:** 17041
- **Author:** Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)
- **Created:** 2024-04-16T07:10:18.783Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 575
- **Reactions:** 0
- **Comments:** 1
- **Source:** https://common.xyz/terra/discussion/17041-terra-chain-upgrade-v2-11

---

On April 16th, 2024, Terra’s Pisco testnet was upgraded to v2.11, incorporating new features and bug fixes. This proposal aims to increase the stability of the chain upgrading Terra’s Phoenix mainnet to v2.11. A governance proposal will be sent on-chain for voting and details regarding the time of the upgrade will be included.


## Core Dependency Upgrades

- Alliance: v0.3.5 -> v0.3.6
- CosmosSDK: v0.47.5-terra.0 => v0.47.10-terra.0
- CometBFT: v0.37.2 => v0.37.4

## Features
- Alliance module increases the rounding sensitivity such that we round up more often when there are small discrepancies.
- Implement CosmWasm bindings for Alliance module to enable querying the module from wasm smart contracts.

## Bug Fixes

- Included a bug fix that addresses block production halting temporarily during high traffic periods.
- Alliance module include new rewards calculation algorithms for each alliance and new algorithm distribution for each validator. 
- Execute BlockBeforeSend and TrackBeforeSend bank hooks when minting and burning TokenFactory tokens.
- Recalculate PFM EscrowAccounts to avoid missing funds when sending from one chain to another due a bug that was addressed in the previous release.

Thank you to the community members for reporting these bugs!

## Libraries
Along with the Core upgrade new features have been implemented in the JavaScript library @terra-money/feather.js@v3.0.0-beta-3. These features are mainly related to the newly available queries for Alliance module and the full refact of the API with a better interpretation of the models when querying the chain and creating the messages.

---

## Comments (1)

**Qasim Saleem Qureshi (`cosmos17de5rquzac94s6xjn5pfcylsw8uwsp8syq2c3r`)** — 2024-04-22T10:26:42.634Z

When Cosmos liquidity will land on LUNA? 
Since 2 years LUNA Without cosmos liquidity.
LUNA ecosystem can't fire up without Cosmos liquidity.
Why Cosmos applications/chains or anything needs to come to LUNA as their is no cosmos liquidity on chain? 
AS business perspective its not great option to support LUNA as it does not have cosmos liquidity on its chain
Kindly reduce the unnecessary delays and prioritize Atom-LUNA lp as alliance asset 
https://commonwealth.im/terra/discussion/16993-whitelist-usdcusdt-atomluna-lunausdc-lp-tokens-as-alliance-assets
https://commonwealth.im/terra/discussion/15329-whitelist-usdcusdt-atomluna-lp-tokens-as-alliance-assets

