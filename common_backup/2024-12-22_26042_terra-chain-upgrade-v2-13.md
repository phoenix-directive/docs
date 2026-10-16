# Terra Chain Upgrade v2.13

- **Thread ID:** 26042
- **Author:** Anonymous (`terra1ytd4m75a4cnv4e7aewkel0z47v0gadayrtg83a`)
- **Created:** 2024-12-22T12:20:31.379Z
- **Last edited:** 2024-12-22T12:24:17.242Z
- **Stage:** discussion
- **Views:** 2509
- **Reactions:** 0
- **Comments:** 0
- **Source:** https://common.xyz/terra/discussion/26042-terra-chain-upgrade-v2-13

---

# **Terra Chain Upgrade - v2.13**

[Changes v2.12..v2.13](https://github.com/phoenix-directive/core/compare/release/v2.12...phoenix-directive:core:release/v2.13)

This chain upgrade contains important upgrades for blockchain stability.


## **Core Dependency Upgrades**



* Recommended Go build Version 1.20.0 -> 1.22.10
* cosmossdk.io/math v1.3.0 -> 1.4.0
* cosmos/cosmos-sdk v0.47.10 -> v0.47.15
* cometbft/cometbft v0.37.4 -> v0.37.13
* terra-money/cosmos-sdk v0.47.10 -> phoenix-directive/cosmos-sdk v0.47.15 [Changes](https://github.com/terra-money/cosmos-sdk/compare/v0.47.10-terra.0...phoenix-directive:cosmos-sdk:upgrade/v0.47.15)


## **Features**



* During Upgrade, burn Axelar assets from Terra Recovery Contract (terra19v058dytxxwdwada9zla0v7my9kjr5z4dtqp9efzn96q79uxdersl7wy9g) and Community Pool
  * **axlWBTC**: ibc/05D299885B07905B6886F554B39346EA6761246076A1120B1950049B92B922DD
  * **axlUSDT**: ibc/CBF67A2BCF6CAE343FDF251E510C8E18C361FC02B23430C121116E0811835DEF
  * **axlUSDC**: ibc/B3504E092456BA618CC28AC671A71FB08C6CA0FD0BE7C8A5B5A3E2DD933CC9E4

Currently this includes:
* Recovery Contract
  * 910,706.647152 axlUSDC
  * 64,710.159582 axlUSDT
  * 0.943493 axlWBTC
* Community Pool
  * 413.154198 axlUSDC
  * 218,335.070000 axlUSDT

Mainnet timeline to be defined. Currently the testnet deployment is scheduled.

---

## Comments (0)

_No comments._
