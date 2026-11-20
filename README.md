# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nurulnr/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nurulnr/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper front page that sums up the world's news of Friday 20 November 2026 in one image: Russian missiles landing in Poland as Moscow pounds Kyiv, Cyclone Akvan making landfall on India's east coast, Asian stocks sliding with the Nikkei down 4.8% and SoftBank plunging 16%, Ukraine's allies meeting in Berlin, Saudi Arabia intercepting more Houthi missiles, and the GTA 6 launch topping $2.3bn in sales.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` in the grader). It is deterministic: both runs write the same bytes, and it uses no network and no third-party packages. The image is 1024×1024 PNG, 125 KB.

This entry is MIT licensed.
