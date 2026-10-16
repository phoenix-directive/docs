# Enable IBC transfers for Noble USDC and Kava USDT and inject liquidity from community pool.

- **Thread ID:** 13802
- **Author:** PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)
- **Created:** 2023-10-22T22:19:28.262Z
- **Last edited:** 2023-10-29T12:47:56.208Z
- **Stage:** discussion
- **Views:** 177
- **Reactions:** 0
- **Comments:** 6
- **Source:** https://common.xyz/terra/discussion/13802-enable-ibc-transfers-for-noble-usdc-and-kava-usdt-and-inject-liquidity

---

## Summary
In the last few months the Cosmos DeFi space has finally been injected with native stablecoins (Circle via Noble chain and Tether via Kava chain). These stablecoins should get fully integrated into the Terra Ecosystem and fully IBC transferrable with the Noble and Kava chain, in order for Terra to position itself at the forefront of this evolution

## Motivation
Before the fall of Terra Classic, the Cosmos DeFi ecosystem was thriving thanks to Terra's native UST stablecoin (strong DeFi needs strong stablecoins). Do Kwon therefore nicknamed himself to "stablekwon". But ultimately, due to the fact that this was an algorithmic stablecoin, it was ultimately doomed to enter into a death spiral, therefore leaving the Cosmos without a native USD stablecoin. 

Axelar's wrapped USDC/USDT then took the place of UST, however these were bridged from Ethereum and therefore not truly safe nor practical. Clearly this was only a temporary solution until true stablecoins once arrive to the Cosmos. This recently happened, and we are already seeing alot of liquidity in Osmosis, Kujira and Migaloo. White Whale has been preparing for Noble USDC for quite a while, and they have recently unlocked their axlUSDC - Whale pool on Terra to transfer this liquidity to Noble USDC - Whale on Migaloo. 

The other Terra DEX is Astroport, and there also we are seeing more and more liquidity for Luna - axlUSDC disappearing, for what I argue is the same reason. If you have native USDC on Cosmos (and also directly transferrable to a merchant's Circle account via Noble), there is no more reason to hold wrapped USDC from Ethereum. The Terra chain needs to preserve its stablecoins and on-chain liquidity so therefore it has to open itself up to the new stablecoins. 

On top of that, as I understand it, TFL is focusing on web3 solutions and payments, but in order to do payments succesfully, you need a strong on chain stablecoin and the required liquidity.

## Proposal
1) Open IBC transfers with USDC from Noble and USDT from Kava.
2) Give these tokens a proper denominator/symbol, so they are easily found within the explorers.

and after these steps are completed and pools have opened on Astroport and White Whale

3) Inject 100K liquidity into LUNA/USDT + LUNA/USDC on Astroport and 100K liquidity unto LUNA/USDT + LUNA/USDC on White Whale from community pool to jumpstart on-chain DeFi centered around Luna and the new stablecoin, linking it directly with Noble and Kava, increasing its position within the Cosmos.

## About the team
My name is Niels Sampermans. I am simply an investor into Terra, and therefore I wish to share my vision.

---

## Comments (6)

**Inspiration (`terra13ejj2nzmy2clgqkvx87hy9tpx840ktuj49l2g4`)** — 2023-10-23T23:08:53.687Z (edited 2023-10-25T14:25:54.987Z) [deleted]

_[deleted]_

> **PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2023-10-24T13:51:27.933Z
> 
> What do you mean, natively? They're already in Cosmos. Tether minted native USDT on Kava chain and Circle minted native USDC on Noble chain. You can only have one native USDT and one native USDC in the whole Cosmos ecosystem. The above chains are the Cosmos hubs that were chosen. Native USDT/USDC in Terra are IBC transfers from these 2 chains.

**PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2023-10-25T19:34:28.588Z (edited 2023-10-29T12:50:42.083Z)

**Update:**

1) IBC transfers on TFM from Kava and Noble are working and operational! Thanks to Cosmos Rescue who opened a new Noble relayer (253 (Terra) - 30 (Noble)) since the old relayer (151 (Terra) - 9 (Noble)) was broken. So the default Noble relayer channel still has to be changed to [https://www.mintscan.io/terra/relayers/channel-253/noble/channel-30](https://www.mintscan.io/terra/relayers/channel-253/noble/channel-30) , or fixed.

2) Tokens have been given a proper denominator and symbol. Great job!
[https://terrasco.pe/mainnet/assets/ibc/2C962DAB9F57FE0921435426AE75196009FAA1981BF86991203C8411F8980FDB](https://terrasco.pe/mainnet/assets/ibc/2C962DAB9F57FE0921435426AE75196009FAA1981BF86991203C8411F8980FDB)
[https://terrasco.pe/mainnet/assets/ibc/AC65808D27055D0A44359F4196176B7017C124DE9E866F48BC793C13291BA992](https://terrasco.pe/mainnet/assets/ibc/AC65808D27055D0A44359F4196176B7017C124DE9E866F48BC793C13291BA992)


This leaves only step 3), the **liquidity injection**, which is I suppose is the **actual proposal**. 

- Due to the fact that Migaloo already has a Whale-USDC pool of 164K (USD) and Terra a Luna-Whale pool of almost 100K, White Whale has effectively given USDC holders a corridor to buy LUNA (and vice versa) already. For this reason I decided to ask the White Whale development team to only create a LUNA / USDT pool on Terra of which they responded positively. They have confirmed that they will create it (see discord White Whale, Migaloo governance) as soon as they get confirmation that the liquidity comes (in the form of proposal passing or injection by Terraform Labs)


- I have also opened a LUNA / USDT pool on Astroport ([https://app.astroport.fi/pools/terra14y5l7n04d3pdfs3fmzevmc5vxghtrklstu8jfjqmwnycgnwcylcqaqwvrh/provide](https://app.astroport.fi/pools/terra14y5l7n04d3pdfs3fmzevmc5vxghtrklstu8jfjqmwnycgnwcylcqaqwvrh/provide)) . However, the USDC token is not found on Astroport which I suspect is due to the default Noble relayer channel being used. So I cannot open a USDC pool yet.


So, I wish to alter the actual proposal to this:

The best course of action so that we don't create conflict of interest with our allies WW and Kujira is to primarily focus on USDT. And the best way to grow a pool from scratch with as minimal funds as possible is to incentivize them. I also realize that most of you LUNA holders would rather have something else than LUNA to be used as incentives. This is perfect, as there is also Axelar wrapped ERC-20 USDT in the community pool. The White Whale allows any token to be used as incentives (and those who lock for 1 year get 16x rewards, so most liquidity providers will lock for a year). So the proposal is this.

## **Use 100K USDT.axl as incentivisation on LUNA - USDT (Kava) pool on White Whale DEX to make Terra a great base for Tether on Cosmos**. 

(And FYI, Osmosis has low Luna liquidity, but it is seeing more and more USDT liquidity, by linking Luna with USDT, Luna also becomes connected with Osmosis again. This is a pathway that opens the gates to every other chain.)

**MB aejir (`terra10ql0yxam88pg0a02946pzv36a3w699shl9r3mc`)** — 2023-10-26T02:37:02.756Z (edited 2023-10-26T02:39:14.843Z)

Hi Niels

Full marks for your enthusiasm here. However to state the obvious: 

The community just voted and gave overwhelming support to give TFL a mandate to provide and manage liquidity for the ecosystem. This liquidity will come from their community pool grant and TFL's own treasury. Stablecoin liquidity is a big part of this and will be deployed where it is needed.

There is also widespread support for not accessing the community pool further for a period of time.

You are proposing that the community vote again to allocate further cPool funds for a reason that is clearly within the scope of what TFL has been asked and plans to do. 

Given this, there seems to be no reason to take your proposal to a vote. 

I do however appreciate that you have been joining the community discussions in Telegram recently. Thoughtful contributions should be encouraged. I hope others will also share any ideas or questions on any topic related to Terra's future there. 

Thanks

> **PhoenixPinion (`terra12g5a0p9yylfjcaw3ah83l0ct09gmn7dcwk54qh`)** — 2023-10-26T12:55:26.849Z
> 
> I am glad for the response. Yes, this seems logical. I am not sure yet whether I will actually do the vote. I will wait and see first what TFL is going to do. I do think I have raised awareness about this issue and made people think about which stablecoin to provide the most liquidity for (which after much brainstorming I believe is clearly USDT) and I'm actually already very glad that Step 1) and Step 2) has been fixed already. I didn't need to write a proposal for that though it seems.

**Anonymous (`terra16mnrr6w07quansa7a60fmngtfy7s3pvc4d0zda`)** — 2023-11-29T18:17:42.533Z

upgrade the pools to PCL then we can add liquidity. I guess we have to transfer the USDC from noble to terra through the relayer

