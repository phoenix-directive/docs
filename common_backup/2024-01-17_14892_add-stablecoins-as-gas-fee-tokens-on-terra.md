# Add Stablecoins as Gas Fee Tokens on Terra

- **Thread ID:** 14892
- **Author:** Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)
- **Created:** 2024-01-17T14:18:08.260Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 565
- **Reactions:** 3
- **Comments:** 13
- **Source:** https://common.xyz/terra/discussion/14892-add-stablecoins-as-gas-fee-tokens-on-terra

---

_Disclaimer: I am a Terraform Labs employee._

### Summary
One of the things users really liked about Terra Classic was being able to pay for transaction fees using stablecoins instead of spending their LUNA (now LUNC). This proposal aims to bring that back by adding stablecoins like axlUSDC and USDC as gas fee tokens on Terra, simplifying the user experience for new users and providing all users with more options when submitting transactions.

### Proposal
On the original Terra blockchain, stablecoins could be used to pay transaction fees. This feature simplified the user experience of interacting on-chain and was a key reason Terra was the blockchain of choice for many first-time users. The Terra community should adopt this feature again with current stablecoins, starting with: 

- **axlUSDC** (IBC denom: ibc/B3504E092456BA618CC28AC671A71FB08C6CA0FD0BE7C8A5B5A3E2DD933CC9E4) and
- **Noble USDC **(IBC denom: ibc/2C962DAB9F57FE0921435426AE75196009FAA1981BF86991203C8411F8980FDB)


If the community approves this plan, more stablecoins can be added in the future, such as Kava USDT.

Gas fees should be set so that LUNA remains the optimal fee token on the Terra blockchain, offering users 2X cheaper fees vs. stablecoins. The benefits of adding stablecoins as fee tokens on Terra include:

1. **Simplified UX & User Onboarding: **Simplifies the blockchain user experience, especially for new users. Stablecoins will allow new users to quickly on-ramp and begin interacting on-chain, with as little friction as possible. This will lead to increased transaction volume over time.
2. **Greater Optionality for Users: **All users gain options. Some users might prefer to pay with stablecoins rather than spend their LUNA for everyday transactions. Now, everyone will have that choice.
3. **LUNA as the Optimal Fee Token: **LUNA will maintain its ability to pay transaction fees on Terra and will become the optimal fee token, as it will be cheaper than stablecoins.


If the community approves of this idea, TFL will start working with Terra validators to add support for stablecoins on Jan. 22nd, beginning with **axlUSDC** and **Noble USDC** and incorporating others in the future. The anticipated go-live date for this feature on Terra and in Station Wallet, allowing time for validators to update, would be **Jan. 26th**.

_Please note that this is a signaling proposal intended to gauge community sentiment. Fee decisions are outside of governance parameters by design, so no on-chain proposal will be posted. Thank you for your understanding._

---

## Comments (13)

**Inspiration (`terra13ejj2nzmy2clgqkvx87hy9tpx840ktuj49l2g4`)** — 2024-01-17T14:35:19.319Z (edited 2024-01-17T15:03:27.684Z) — 👍 1

Hi Zion, is there any chance that as the fee will be 2x in non-luna fee then to consolidate that fee in a smart contract and automatically daily swap that into Luna to create extra buying pressure?

If transactions are 0.004 worth of LUNA x 5.000.000 transactions =  20.000 LUNA daily = 600.000 Monthly = 7.200.000 yearly of extra buying pressure of the token of ~0.72% yearly.

Might sound not much but if we start working on extra burning / buying pressure mechanisms they will start to add up.

Also for Station please remind that adding extra tokens as fee payment will provoke a bit UI friction for newbies as there are many tokens to select, so maybe something like automatically choose fee payment based on balance and as well let the user select favourite token as in previous station version if you want to pay fees in USTC it become an UI madness of token selection every time you want to pay a transaction.

> **Lion King AZ 🦁 (`terra1g74r6fuxc880dj3rrpvetm42wxaz98r55yu4gm`)** — 2024-01-17T14:52:25.547Z
> 
> I agree with this opinion. We should create more pressure on burning/buying

> **swgee (`terra1xq4vkykvae80xtp85gt7s4j4kz92n82kk8am5j`)** — 2024-01-20T21:16:58.582Z (edited 2024-01-20T21:17:12.204Z)
> 
> Good ideas on the Station UI, I will make sure the Station team sees this.

> **Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)** — 2024-01-25T12:16:24.534Z (edited 2024-01-29T17:13:05.748Z) — 👍 1
> 
> Hey Inspiration, thank you for your thoughts. The Station feedback has been relayed to the team, and on your first point, the x/distribution module already distributes denoms equally according to a user's share of the reward pool. So LUNA stakers will receive axlUSDC and USDC paid in fees

**Galactic Mining Club (`terra12ulyfp6uu8wvygc09a3a2j7uc66rcxnkvvzdxk`)** — 2024-01-17T16:49:35.886Z (edited 2024-01-24T18:23:17.149Z) — 👍 3

i think this proposal is great but i also think we should be supporting terra projects who have decentralized stable coins as well. let's support the teams who have delivered on their promises and continue to build. 

i would love to see $solid added to the list of stablecoins available. adding solid will benefit the community and the ecosystem by offering a decentralized stablecoin for users to choose from. solid has proven to be reliable decentralized and controlled and owned by the terra community TFL holds a big bag of capa so this will benefit them too.

capapult is the only defi protocol to have a fully functioning dapp built with a decentralized stablecoin, and they did it in less time then 99% of dapps took to deploy anything. they continue to add new collateral and are working on new products for the terra community. 

support those who deliver and watch terra rise again

> **Welding (`terra1axga8vmadpx38t9766980rwkkzvdtwxwn976fl`)** — 2024-01-18T03:02:13.297Z
> 
> I agree with this comment. I understand that Noble USDC and axlUSDC should be a priority but we have capa aka SOLID thats a stable coin project on terra but being passed up.. I also understand the fact that there should be more liquidity also, but TFL should help in this endeavor and help make a game plan so Solid can actually be used on the blockchain for transactions. Would like to see solid in this group.

**Qasim Saleem Qureshi (`cosmos17de5rquzac94s6xjn5pfcylsw8uwsp8syq2c3r`)** — 2024-01-17T17:41:07.668Z

Totally support it.
Lets fire the terra economy again and make it happen.
LUNA $20 soon

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2024-01-18T12:36:22.739Z

Would love to hear more about why fee decisions are outside the scope of community governance:

> _Fee decisions are outside of governance parameters by design_

Other than this signalling prop, which theoretically you didn't need to post, the community essentially has no say in this, right?

I agree with previous commenters, in order to support a Terra project, $SOLID would be a great addition as a fee token.

> **Anonymous (`terra1hr7svdp2rga9vf3ry95sx7g5wyspgwmg94qac8`)** — 2024-01-23T18:53:22.547Z
> 
> validators are free to charge whatever they would like, and there are some scenarios where setting it lower can be beneficial for certain applications. 
> 
> some chains have a 'minimum' fee, which overrides the minimum set by the validator node, others have dynamic gas (osmo).
> they have pros & cons.
> 
> btw.. [@Zion](/profile/id/45132) .. are you guys going to update the gas config in Keplr/cosmos.directory as well, so other wallets will be able to use USDC's ?

> > **Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)** — 2024-01-25T12:12:58.538Z
> > 
> > Hey PFC, yes we will

**Rebel Defi (`terra17w74x9vrqq4a338ssh9y9r4m9s3f6zef7wy5ms`)** — 2024-01-18T12:52:54.526Z (edited 2024-01-24T18:21:57.890Z) — 👍 1

I guess when there was that spam inscription stuff on Terra, TFL/validators had the flexibility to quickly increase fees.

Waiting on governance would have been a laborious process!

**Qasim Saleem Qureshi (`cosmos17de5rquzac94s6xjn5pfcylsw8uwsp8syq2c3r`)** — 2024-01-23T11:20:26.015Z

Eagerly waiting to use this feature on 26 Jan 2024 on Terra Station.
**Stablecoins as Gas Fee Tokens on Terra**

**Anonymous (`terra1ld4yf48eqex65vdrt3kta23cvrx865zyfkgkka`)** — 2024-01-28T10:04:21.539Z

Update: About 67% of Terra validators have updated their gas fee parameters. To mitigate user fee issues, we will wait to add the new fee tokens to Station until 80% of validators have updated.

