# Terra Chain Upgrade - v2.12.1

- **Thread ID:** 24445
- **Author:** Anonymous (`terra16qtc3vuc8fum7rsx0k3ps3vfyj9ru3vwrwztfz`)
- **Created:** 2024-08-16T03:18:13.249Z
- **Last edited:** 2024-08-22T16:27:39.977Z
- **Stage:** discussion
- **Views:** 1155
- **Reactions:** 6
- **Comments:** 0
- **Source:** https://common.xyz/terra/discussion/24445-terra-chain-upgrade-v2-12-1

---

This post aims to propose an upgrade of Terra’s mainnet (phoenix-1) to version [2.12.4](https://github.com/terra-money/core/compare/release/v2.11...v2.12.4). A governance proposal will soon be sent on-chain for voting, and we will provide details about the timing of the upgrade.

We’re pleased to share that this upgrade has already been successfully implemented on our testnet (pisco-1).


# Key Changes


## Update Validator Minimum Commission Rate
This upgrade includes an important follow-up to [Proposal 4803 - A 5% Global Minimum Commission for Validators](https://chainsco.pe/terra2/governance/proposal/4803), which was approved by governance. We will be updating all current validators with commission rates below 5%, and new validators will now be required to maintain a minimum commission rate of 5%. A special thanks to Philipp from Eris Protocol for submitting the pull request that made this possible.

## Burning of Assets
In accordance with Terraform Labs’ (TFL) bankruptcy court order (you can find more information in our [X post](https://twitter.com/terra_money/status/1814250793270218949)), TFL will be burning all LUNA it currently holds. However, the LUNA received from the community pool is currently locked in a [vesting contract](https://chainsco.pe/terra2/address/terra19yxffalxzu88n5lnj40trehpryemqsz7pnnwxp8v73hxz0rl2u9q5qqwh4). This upgrade will enable us to directly burn all assets within that contract.

Additionally, TFL possesses another [wallet](https://chainsco.pe/terra2/address/terra1885dgdvn5u8sjfaefvr39arssaxgqmd29ht0aa) with significant LUNA holdings. While we have the option to transfer these funds to the community pool via the donation function, this wallet has been compromised and we have been unsuccessful at donating the funds. Therefore, we believe that the best course of action is to make use of the upgrade to burn all assets associated with it.

Finally, this upgrade will also address the issue of [illegally minted assets](https://chainsco.pe/terra2/address/terra1wrve5z5vsmrgy6ldcveq93aldr6wk3qmxavs4j) in the attacker’s wallet resulting from the IBC exploit by ensuring the complete removal of these remaining assets.

## Removal of Blacklist Functionality
As part of the emergency chain upgrade during the IBC exploit. a code change to implement a transaction blacklist to prevent the attacker from further withdrawing funds was added. With the [IBC bug fixed](https://github.com/terra-money/core/commit/af1485c03aeeafe41eee786dc42c4c53060b87ab) and the illegally minted funds burnt, we can now remove the blacklist functionality.

---

## Comments (0)

_No comments._
