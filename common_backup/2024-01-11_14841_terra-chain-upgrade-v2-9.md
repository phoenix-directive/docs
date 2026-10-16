# Terra Chain Upgrade - v2.9

- **Thread ID:** 14841
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2024-01-11T11:48:00.607Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 538
- **Reactions:** 3
- **Comments:** 1
- **Source:** https://common.xyz/terra/discussion/14841-terra-chain-upgrade-v2-9

---

This proposal aims to upgrade Terra (phoenix-1) to v2.9. A governance proposal will be sent on-chain for voting and details regarding the time of the upgrade will be included.

**Notable changes**

- Remove of the **[PoB](https://github.com/skip-mev/pob) module**
- Update the **[Fee Share module](https://github.com/terra-money/core/tree/release/v2.9/x/feeshare/spec)** logic to fairly distribute fees to all contracts registered and executed during a transaction. The module previously only distributed fees to the first contract that was executed
- Add the** Async Interchain Query** **module **([Async ICQ](https://github.com/cosmos/ibc-apps/tree/main/modules/async-icq)). Interchain Queries enable blockchains to query the state of an account on another chain
- Enable querying **token-factory** from the LCD with URL-encoded values 
- Extend governance proposal metadata to a maximum of 5100 characters
- Fix an authz bug that prevents claiming of delegation rewards
- Upgrade CosmosSDK from v0.47.3 to v0.47.6
- Upgrade wasmd from v0.43.0 to v0.45.0
- Upgrade wasmvm from v1.4.1 to v1.5.1
- Greatly increase integration test coverage from 19 tests to 46 tests, including old and new modules and IBC transactions


**Breaking changes**: 

- Update [@terra-money/feather.js](https://www.npmjs.com/package/@terra-money/feather.js/v/1.1.1-beta.1) to use the latest protobuf additions
- Update [terra-proto-rs](https://crates.io/crates/terra-proto-rs/4.0.0) to use the latest protobuf additions and extend to implement all message types supported natively by Terra

---

## Comments (1)

**Anonymous (`terra1alxk3fmhcl0ga80gl9yj9zp3ezjm4sdh8a9l9c`)** — 2024-01-11T13:21:50.785Z

I am not so sure about the Fee Share module change and generally the introduction of it.

- It lead to the spam attack being only half as expensive.
- It leads to incentivizing "bad" contract code or UIs with high gas fees.
- The new addition will incentivize contract developers to just add a couple of more contract calls in front of calling other contracts. So e.g. a complex multi-hop swap we are e.g. executing (and paying fees for) will be 1 contract us, and for each hop 1 contract from the DEX. Same for dex aggregators, they get 1 for very complex logic and then 10-20 for the dex.
- It also incentivizes the use of cw20 tokens instead of tokenfactory, as tokenfactory txs are not tracked.

