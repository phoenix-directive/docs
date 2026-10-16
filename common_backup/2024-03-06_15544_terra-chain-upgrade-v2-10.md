# Terra Chain Upgrade - v2.10

- **Thread ID:** 15544
- **Author:** 0xPhilipp (`cosmos142v8lp8m8fgj3zegg9mzsq9k5n2z2r06cn04h5`)
- **Created:** 2024-03-06T14:12:31.242Z
- **Last edited:** 2024-03-06T21:53:36.869Z
- **Stage:** discussion
- **Views:** 1366
- **Reactions:** 1
- **Comments:** 1
- **Source:** https://common.xyz/terra/discussion/15544-terra-chain-upgrade-v2-10

---

This proposal aims to upgrade Terra (phoenix-1) to v2.10. A governance proposal will be sent on-chain for voting and details regarding the time of the upgrade will be included.

### Notable changes

https://github.com/terra-money/core/compare/v2.9.4...v2.10.2

- Upgrade Alliance from v.0.3.2 to version v0.3.5 fixing rewards distribution bug with multiple alliances, improve amino encoding models, enabling the modification of reward weight ranges for an existing alliance and introducing simplified queries for rewards and unbonding delegations

- Upgrade PFM from v7.0.1 to v7.1.3 fixing a known bug categorized as mid severity.

- Enable WasmVm 1.5 features (https://medium.com/cosmwasm/cosmwasm-1-5-946fd3024f1d)

- Remove legacy code that forces vesting on genesis event (https://github.com/terra-money/core/pull/241)



### Alliance



With the launch of the ALLY and ampROAR alliances, a reward miscalculation issue in Alliance Module has been found. The upgrade to 0.3.4 is consensus breaking and contains the fix. https://github.com/terra-money/alliance/releases/tag/v0.3.4



**Due to the high rewards currently going to ampROAR stakers it is considered to put the proposal on the chain within the next 3 days.**

---

## Comments (1)

**jgnft (`cosmos1ejlamgn4270dmgmzc3z9sc9zkxtyfsh3qdznc2`)** — 2024-03-06T19:15:15.180Z (edited 2024-03-07T13:31:31.486Z) — 👍 1

Let's do it tomorrow. 

Will the lost rewards be reissued for the current Alliance stakers or are they a wash?

