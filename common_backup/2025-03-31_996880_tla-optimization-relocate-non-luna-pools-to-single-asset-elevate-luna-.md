# TLA Optimization: Relocate non-LUNA Pools to Single Asset, Elevate LUNA Pools from Single Asset

- **Thread ID:** 996880
- **Author:** PhoenixPinion272 (`terra1wavtmpcsg8ns63ppddjvlvln8na30f5r3frhdq`)
- **Created:** 2025-03-31T04:40:29.472Z
- **Last edited:** -
- **Stage:** discussion
- **Views:** 36
- **Reactions:** 0
- **Comments:** 3
- **Source:** https://common.xyz/terra/discussion/996880-tla-optimization-relocate-non-luna-pools-to-single-asset-elevate-luna-

---

# Summary

This proposal optimizes the Terra Liquidity Alliance (TLA) by redistributing inflation more efficiently. It moves non-LUNA–non-LUNA pools to the Single Asset category and ensures LUNA-Asset pools are categorized correctly to support long-term Terra liquidity and growth.



# Motivation

The TLA currently allows certain pools that do not include LUNA in either slot to receive inflation alongside LUNA-paired pools. These pools provide limited volume, do not support the LUNA token directly, and dilute the effectiveness of inflation distribution.

Meanwhile, some LUNA-paired pools are misclassified, limiting their ability to attract liquidity. These inefficiencies reduce Terra’s economic alignment and undermine its strategic objectives.

# Proposal

**1. Reclassify Non-LUNA Pools to Single Asset**

The following liquidity pools will be moved to the Single Asset category, where they will share a capped 5% of inflation:

USDC–USDT

USDC–EURe

USDC–SOLID

These pools remain active and useful but will no longer draw from the Blue Chip(/Project) inflation category, ensuring LUNA-paired pools retain priority.

**2. Reclassify LUNA Pools from Single Asset to Blue Chip/Project**

Any LUNA–Asset pool currently placed in Single Asset will be moved to either the Blue Chip or Project category, depending on what best suits them. Specifically:

LUNA–arbLUNA → to Blue Chip (or Project, if preferred by Phoenix Directive)

These moves ensure Terra-aligned liquidity is fully incentivized and not diluted by unrelated assets.

_Benefits_
- Prevents external pools from diluting LUNA-focused liquidity, which will increase TVL and volume in these pools.
- Enhances capital efficiency and rewards alignment, leading to easier absorption of value into Terra.
- Simplifies inflation logic across TLA categories


# Conclusion

This proposal addresses a minor but impactful misalignment in inflation incentives. It strengthens Terra’s core liquidity, and ensures LUNA-paired pools are not competing with external pools, but only with other LUNA-paired pools. This prevents excessive extraction that could go beyond the intended 5% in case non-LUNA pools gain the upper hand in Blue Chip/Project. As such, this proposal can be thought of as a vaccin that protects Terra against possible misaligned forces, and as such is completely neutral. This change is non-disruptive, easily reversible, and requires no technical upgrades.

**Important note**

Rose 🌹, one of the most respected members of the Terra community, validator, and key figure within the Phoenix Directive, has already expressed considerable interest in relocating the USDC–USDT pool to the Single Asset category.

---

## Comments (3)

**Rose | Phoenix Foundation (`terra1vzxzwsm0rscya65jg9znu9jls9gtqrv7mc9yh9`)** — 2025-03-31T23:01:10.263Z (edited 2025-04-01T03:56:25.464Z)

Hi Niels,

While I do agree about moving the USDC-USDT pair to the single asset bucket, I don't appreciate that you have signalled my support for this proposal. In the past we have not used chain governance to decide these things and it really isn't necessary. This is part of the Phoenix team's job.

> **PhoenixPinion272 (`terra1wavtmpcsg8ns63ppddjvlvln8na30f5r3frhdq`)** — 2025-04-01T03:56:25.459Z (edited 2025-04-02T15:36:28.742Z)
> 
> Hi Rose! Glad to you see.
> 
> Yeah I was conflicted about that, but since I consider myself a rational actor (or at least I try to be), I’ve learned that in order to have any real chance of passing a proposal on Terra, you need the approval of the Queen of Dragons. And since I had yours, I couldn’t resist including it, even if you don't personally like that. But why not? It’s a compliment, isn’t it? I was so convinced I'd get something. Must have been another one of my cosmic miscalculations. (But maybe it wasn't, cuz the next morning a song played on the radio, Seal - Kiss From A Rose. No joke)
> 
> But in this case, it’s not about you or me. It’s about Terra bleeding and I’m just the doctor. And through extensive diagnosis, I’ve found that the best/safest solution is not to rip anything out, but rather to take the overgrown fungus that’s suppressing Terra’s lymphocyte production in the bone marrow, and reintroduce it into the gut biome, where it can fulfill its natural role as a probiotic, which seems to be the simplest and most effective cure to Terra’s leaky gut syndrome.

**PhoenixPinion272 (`terra1wavtmpcsg8ns63ppddjvlvln8na30f5r3frhdq`)** — 2025-04-02T04:18:44.267Z (edited 2025-04-02T04:24:00.695Z)

Some further clarification. 

I am not attacking the Noble-Kava pair, I am simply saying it is misplaced. It is a pair through which capital can come in easily to Terra. It is quite a useful pair, but so are the Luna-Blue Chip pairs. But fundamentally it is a single asset pair, and it can grow there more effectively precisely because it is far more useful than most of the other single asset pairs. All the while reducing overall selling pressure and increasing blue chip liquidity. To me it is simply a win-win. And hence the title is TLA Optimization.

