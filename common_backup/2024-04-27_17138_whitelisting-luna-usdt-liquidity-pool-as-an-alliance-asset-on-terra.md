# Whitelisting LUNA - USDT Liquidity Pool as an Alliance Asset on Terra

- **Thread ID:** 17138
- **Author:** PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)
- **Created:** 2024-04-27T14:19:42.356Z
- **Last edited:** 2024-05-15T00:40:35.388Z
- **Stage:** discussion
- **Views:** 832
- **Reactions:** 0
- **Comments:** 6
- **Source:** https://common.xyz/terra/discussion/17138-whitelisting-luna-usdt-liquidity-pool-as-an-alliance-asset-on-terra

---

# **Summary**

This proposal aims to whitelist the LUNA - USDT liquidity pool as an Alliance Asset, enabling it to receive a portion of LUNA inflation as incentives, similar to ampWhale, rSWTH and ampRoar.

### **_Motivation_**

1. Liquidity: We are facing a liquidity crisis now that TFL is forced to withdraw most of their assets Astroport, White Whale and URA. The liquidity was thus provided for us and not naturally grown from the ground up. We need decentralized liquidity.


2. Natural growth: By using the Alliance protocol as incentivization we can effectively grow the pools naturally as LUNA grows in value, because the rewards also increase at a similar rate. This is important because many chains with external incenvitization face liquidity crisis as the ecosystem grows. This is due to the fact that the rewards are not linked to the main token's value. They are paid out in a different token. Thus the size of the liquidity pool depends on the value of that token and also the one who incentivizes instead of the community as a whole.


3. Accessibility: By increasing liquidity we make LUNA more accessible to a wider audience in a decentralized way, which is important for mass adoption. This is also why Tether was chosen for this proposal, because it has a market cap of 110 billion dollars. We are not talking about axlUSDT bridged from Ethereum, we are talking about native USDT that is directly linked through major exchanges like Binance and KuCoin. It is an IBC transfer from the Kava chain, the chain that Tether has chosen to provide USDT to the Cosmos. Kava has now been added to Station v3, which together with the soon-to-be-released mobile version, will make it easy to transport and swap this stoken within people's personal wallets.


4. Consumer trust: UST's collapse caused alot of problems with how Terra Luna is perceived by the public. We can correct this distrust and skepticism and show that we learn from our mistakes by making native Tether the primary stablecoin within Terra 2's ecosystem. Terra 1 had a vibrant ecosystem that unfortunately collapsed due to the fact that the stablecoin that the ecosystem was built around could not preserve its peg under pressure from external forces that did have our best interest at heart. The primary function of a stablecoin is that it can keep its peg at all times. And native USDT (meaning not transferred through a centralized bridge from Ethereum) is the winner in this regard. Using USDT on Terra is no different than using USDT on Ethereum, BNB or Solana. It has a proven track record and everyone trusts it, including merchants. 


Alliance Asset Parameters
LUNA - USDT
Since with Alliance, the pool size is dependant on the value of the LUNA token, it is difficult to calculate exactly how big the pools will grow, because we do not know how big LUNA will grow. So I propose a reward weight of 0.01 and a take rate of 0.
These parameters can be adjusted through later proposals if we find it is ineffective. We do not want to provide more inflation than is needed, because more pools like LUNA - ATOM and LUNA - INJ will follow. We can also adjust the take rate in a later update, allowing LUNA stakers to also earn LP rewards, to more effectively decentralize the liquidity. This way basically all stakers provide liquidity. But let's keep it simple for now.

The DEX that is intended for use on this pool will be Astroport. I am trying to create a PCL pool once Astroport fixes a bug in the decimals.

---

## Comments (6)

**Beatmode (`terra14yrfk4pdtn8p768dylqdhyrmh4udfwgel8skgf`)** — 2024-04-27T15:45:29.421Z

This is a great workaround for now to replace what has been removed for liquidity. Will these funds be returned if TFL is able to resolve everything with their legal issues?

> **PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2024-04-28T11:53:22.909Z
> 
> Your staking rewards cannot be returned. It works exactly like staking LUNA on a validator, except you will then also be able to stake LUNA-USDT liquidity token on a validator.

**Anonymous (`terra1nyau5wrqj500arqf6xncsum7f25dzqzhwl33k7`)** — 2024-04-28T06:18:05.968Z

How about using two pools in Astroport and Ura?

> **PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2024-04-28T11:51:51.368Z (edited 2024-04-30T23:11:46.056Z)
> 
> I am not as familiar with URA, but I can only whitelist one pool. I am not 100% decided yet on the DEX. That depends on how they cooperate.

**0xPhilipp (`cosmos142v8lp8m8fgj3zegg9mzsq9k5n2z2r06cn04h5`)** — 2024-05-04T16:33:40.566Z (edited 2024-05-04T17:01:41.507Z)

I think we need to incentivize LUNA-Stablecoin liquidity. I am just not convinced about the usage of USDT instead of the widely used USDC in cosmos. If we use USDT, we should first engage with KAVA / Tether if they help Terra in the grander scheme of things, e.g. by also deploying KAVA-USDT liquidity to Terra.

Also your calculation is wrong. The daily inflation in LUNA is 250k a day, so 1.2% amounts to 3k LUNA, almost double the amount you expect.

EDIT: Will be voting NO, as the proposal is wrong. Denom must be a factory denom / coin and CANNOT be a cw20 token.

> **PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2024-05-04T18:37:39.832Z (edited 2024-05-14T22:36:49.717Z)
> 
> How do you arrive at 250000? The yearly inflation is 7%, 7% of 730M Luna is 51M yearly extra LUNA. Divided by 365 = 140K daily extra LUNA. (The staking rewards are higher because not all the LUNA is staked.) Please explain how you arrive at those numbers.
> 
> As for USDT vs USDC. Ideally we would have both. But the arguments for prioritizing are outlined above. The trend of Tether looks bullish, while the trend of Circle is looking bearish, thus the potential for monetary inflow into Terra and long term survival is greater for USDT. On the other hand, USDC seems to be favoured by chains such as Solana and has high on-chain volume, thus making it a strong candidate for a payment coin. As you can see, it is too early to pick a side and therefore we should aim to have liquidity for both coins. Do not think of this proposal as a denial of USDC, because I am planning to do either that one or ATOM next. As to your other question, why should Kava deploy the liquidity on Terra, they are just a gateway hub?
> 
> And then the denom. You could be right in this regard. If this turns out to be true, then the solution is URA DEX. URA pools mint factory tokens, which should then be compatible with alliance. Thanks for pointing this out.

