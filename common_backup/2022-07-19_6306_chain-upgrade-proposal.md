# Chain Upgrade Proposal

- **Thread ID:** 6306
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2022-07-19T00:28:08.924Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 7317
- **Reactions:** 0
- **Comments:** 0
- **Source:** https://common.xyz/terra/discussion/6306-chain-upgrade-proposal

---

_Disclaimer: I am employed by TFL._

This proposal utilizes the Software Upgrade Governance function to enable a smooth chain upgrade. This proposal type halts the chain at a specific height in order for nodes to update their software to the latest version.

The halt height for this proposal is set for **block 890000**, which is approximately **12:00 am UTC on 7/29.**

The following additions are proposed in this update:

**Update 1 - Enable vesting account creation via transaction**

Previously, the only way to create a vesting account was during Genesis. This update will implement the following message: ‘_MsgCreatePeriodicVestingAccount’_, which will allow for the creation of vesting accounts via transactions. 

Functionally, the LUNA airdrop cannot be executed without this update, whereby new vesting accounts can be created when users claim their airdrop.

_PR reference** -** [https://github.com/terra-money/core/pull/52](https://github.com/terra-money/core/pull/52) _


**Update 2 - Vesting schedule adjustment for an exchange wallet incorrectly whitelisted at Genesis**

An exchange with the wallet address _terra1chq5ps8yya004gsw4xz62pd4psr5hafe7kdt6d_ was incorrectly whitelisted during Genesis. The whitelisted address in [genesis-tools](https://github.com/terra-money/genesis-tools/blob/main/src/exchange/terra_wallets.csv) was _terra1chq5ps8yya004gsw4xz62pd4psr5hafe7kdt6_, instead of the actual address which had the letter “d” at the end. This resulted in the exchange receiving zero unlocked LUNA for their Pre-Attack LUNC allocation and also subjected them to the longest vesting period.

This update aims to adjust the vesting period for the Pre-Attack LUNC allocation (for wallet _terra1chq5ps8yya004gsw4xz62pd4psr5hafe7kdt6d_) from ‘1-year cliff, 4-year vesting’ to ‘30% unlocked, 6-month cliff, and 2-year vesting’.

~1.137M LUNA will be unlocked with this update, and the vesting schedule for the remaining LUNA will be adjusted to ‘6-month cliff, 2-year vesting’.

**Address**
**LUNA to Unlock**
terra1chq5ps8yya004gsw4xz62pd4psr5hafe7kdt6d
1,136,894.40

_PR reference -** **_[https://github.com/terra-money/core/pull/60](https://github.com/terra-money/core/pull/60)


**Update 3 - Allow for sending of vesting tokens to the Community Pool via transaction**

This update will implement the following new message: ‘_MsgDonateAllVestingToken_’, which will allow any user to send their vesting LUNA to the Community Pool. 

_PR reference -** **[https://github.com/terra-money/cosmos-sdk/pull/88](https://github.com/terra-money/cosmos-sdk/pull/88)_

---

## Comments (0)

_No comments._
