# Terra Chain Upgrade - v2.8

- **Thread ID:** 14354
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2023-12-08T15:50:02.085Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 250
- **Reactions:** 0
- **Comments:** 0
- **Source:** https://common.xyz/terra/discussion/14354-terra-chain-upgrade-v2-8

---

_Disclaimer: I am a Terraform Labs employee_

On December 4th, 2023, Terra’s Pisco testnet was upgraded to v2.8, incorporating several new features and bug fixes. 
This proposal aims to upgrade Terra’s Phoenix mainnet to v2.8. A governance proposal will be published on-chain for voting and details regarding the time of the upgrade will be included.

Notable changes

- Updated the **FeeShare Module** logic to fairly distribute fees to all contracts registered and executed during a transaction. The module previously only distributed fees to the first contract that was executed.
- Added the **Async Interchain Query** **Module **([Async ICQ](https://github.com/cosmos/ibc-apps/tree/main/modules/async-icq)). Interchain Queries enable blockchains to query the state of an account on another chain.
- Enabled querying the **token-factory** from the LCD with URL-encoded values 
- Extended governance proposals metadata to a maximum of 5100 characters.
- Fixed an authz bug that prevented claiming of delegation rewards
- Upgraded CosmosSDK from v0.47.3 to v0.47.6
- Upgraded wasmd from v0.43.0 to v0.45.0
- Upgraded wasmvm from v1.4.1 to v1.5.0
- Greatly increased integration test coverage from 19 tests to 46 tests including old and new modules, and IBC transactions.


Breaking changes

- Update [@terra-money/feather.js](https://www.npmjs.com/package/@terra-money/feather.js/v/1.1.1-beta.1) to use the latest protobuf additions
- Update [terra-proto-rs](https://crates.io/crates/terra-proto-rs/4.0.0) to use the latest protobuf additions and extend to implement all message types supported natively by Terra

---

## Comments (0)

_No comments._
