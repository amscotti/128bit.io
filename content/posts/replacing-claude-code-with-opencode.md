Title: Replacing Claude Code with OpenCode
Date: 2026-11-26 09:30
Slug: replacing-claude-code-with-opencode
Tags: OpenCode, GLM, AI, GitHub, Development
Summary: A year after letting my Anthropic plan lapse, here is how OpenCode, the Z.ai GLM Coding Plan, and OpenRouter powered reviews have worked out for me.

## TL;DR

It has been about a year since I let my Anthropic subscription lapse, and I haven't missed it. Since then I've done my daily coding with [OpenCode](https://opencode.ai/) and the [Z.ai GLM Coding Plan](https://z.ai/subscribe), most recently with the GLM-5.4 model, and the rate limits have been far better than anything I ever got from Anthropic. I'm paying less, I'm getting more usage, and I'm no longer tied to a single company. I also use OpenCode in GitHub Actions for automated pull request reviews on this blog, with models accessed through [OpenRouter](https://openrouter.ai/).

## A Year Without Anthropic

It's been about a year since I let my Anthropic subscription lapse, and it has worked out better than I expected. I haven't gone back, I haven't felt like I was missing out on anything, and I've spent the whole time using a mix of other models that have done the job well for less money. The biggest change for me isn't any one model, it's that I'm not dependent on one company anymore. When a better or cheaper model comes out, I try it that week instead of waiting to see if my vendor catches up.

## Why I Moved Away from Anthropic

I want to be fair, because Claude Code is a capable tool. When I was using it, it caught real bugs, made good suggestions, and improved my pull requests. This was never about it being bad. It was about the plans around it no longer making sense for me.

The first issue is cost and value. The Claude Pro plan is $20 a month and the Max plans run from $100 to $200 a month, and for that money I kept running into usage ceilings and rate limits that reset on a schedule I had no control over. Compared to what other providers were offering for similar or lower prices, with bigger allowances and very competitive models for coding, the Anthropic plans felt like they were priced for a time that had already passed. I don't write code 40 hours a week anymore, so some weeks I barely touch it and other weeks I'm heads down, and paying a premium for a plan that I could still hit the limits on during the busy weeks was hard to justify.

The second issue is the one that bothered me the most. Anthropic updated its terms and put technical blocks in place so that Claude Pro and Max subscriptions only work with Anthropic's own products, meaning the Claude web and desktop apps and the Claude Code CLI. Tools like OpenCode, which had been letting people sign in with their subscription, were shut out. If you want to use an open source coding agent with Claude models you now need to pay separately for API usage, billed per token. I understand the business reasoning, since heavy automated use of a flat rate plan is expensive to serve, but it still means I'd be paying for access that I'm only allowed to use the way Anthropic decides.

I've been around long enough to recognize this pattern. A vendor builds something genuinely good, you build your workflow around it, and then the terms slowly tighten around you. I didn't want my coding agent to be another example of that, so I moved to tools where the harness and the model are separate choices that I get to make.

## OpenCode Has Come a Long Way

[OpenCode](https://opencode.ai/) is an open source (MIT licensed) AI coding agent that runs in your terminal, as a desktop app, or inside an IDE. The project lives at [anomalyco/opencode](https://github.com/anomalyco/opencode) now and has passed 220k stars on GitHub, which tells me I'm far from the only one looking for something provider agnostic.

The current 2.0 releases run on a shared background service that handles sessions, configuration, permissions, and tool execution, so the terminal, desktop app, web client, and the mobile companion apps all see the same state. A few other additions stood out to me:

-   **Code Mode for MCP servers**: Instead of making many verbose tool calls, the agent can run short scripts against your MCP servers, which cuts down on how much context gets used before you've even started.
-   **Background subagents**: Subagents can run concurrently, even on different models, alongside async shell commands and Git worktree tools, which is great for splitting up larger tasks.
-   **Persistent desktop terminals**: Terminal sessions in the desktop app survive restarts and keep their scrollback.
-   **Provider support**: It still works with dozens of providers, so switching models is a configuration change instead of a migration.

Installing it is simple,

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

Or if you prefer a package manager,

```bash
# npm
npm install -g @opencode/cli@latest

# Homebrew
brew install anomalyco/tap/opencode
```

Once it's installed, `opencode upgrade` keeps you current, and running `opencode` in your project directory gets you started. The next step is connecting a provider.

## My Daily Setup: OpenCode with the GLM Coding Plan

For my day to day coding I've been using OpenCode with the [Z.ai](https://z.ai/) GLM Coding Plan for a long time now, and it has worked very well for me. The newly released GLM-5.4 model made it even better. It handles multi-file changes well, keeps track of what it's doing over longer sessions, and I find the results solid for real engineering work. The plan also includes GLM-5.3 and the faster GLM-5.3-Flash, which I'll reach for when I want a quick answer and don't need the full model.

The part that matters the most to me is the rate limits. The GLM Coding Plan gives me far more room than I ever had with Anthropic. I rarely think about usage anymore, and when I'm in a long session I'm not watching a counter or waiting for a window to reset, which was a regular frustration before. At the time of writing, the plans are a Lite tier at $18 a month, a Pro tier at $80 a month, and a Max tier at $168 a month, with a discount of roughly 30 percent if you pay yearly. Usage is measured in credits over rolling five hour windows with a weekly allowance, and requests made during off peak hours are discounted further. That structure fits how I work much better than a flat plan that stops me in the middle of a task.

Z.ai is also happy for you to use the Coding Plan in third party tools. OpenCode, Cline, Cursor, and others are all supported, which is the opposite of the direction Anthropic went. I'm paying for the model usage and I get to use it in the tool I prefer.

Setting it up is easy. OpenCode supports the Z.AI Coding Plan as a built-in provider, so there is no configuration file to edit by hand. You grab your Coding Plan API key from the Z.ai dashboard, run the login command, and pick the provider from the list,

```bash
opencode auth login
```

Choose **Z.AI Coding Plan** (and not the plain Z.AI option, which is the pay-as-you-go API), paste in your API key, and you're connected. You can also do the same thing from inside a running session with `/connect`. After that, use `/models` to pick `GLM-5.4`, or switch to `GLM-5.3` or `GLM-5.3-Flash` whenever you want something different.

## Automated Pull Request Reviews

The other place I use OpenCode is in CI. I wanted automated review on every pull request for this blog, something that runs, reads the diff, and posts feedback as a comment. A flat rate plan isn't a great fit here, since this is a script running on a GitHub runner and the volume is unpredictable, so for this I use OpenRouter. It gives me a single API key that works with hundreds of models, billed per token, so I only pay when a review actually runs.

Getting started is straightforward. Create a key on the [OpenRouter keys page](https://openrouter.ai/keys), add it to your repository as the `OPENROUTER_API_KEY` secret, and you're ready to write the workflow. I prefer writing the workflow by hand over using `opencode github install`, since I like understanding exactly what is running in my repositories.

I have two workflows, each using a different model for a different job. This is the code review workflow, which skips pull requests that only change blog posts,

```yaml
name: OpenCode Review

on:
  pull_request:
    types: [opened, synchronize]
    paths-ignore:
      - 'content/posts/**'

concurrency:
  group: opencode-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  opencode-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v7
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Setup Node.js
        uses: actions/setup-node@v7
        with:
          node-version: '24'

      - name: Install OpenCode
        run: npm install -g @opencode/cli@latest

      - name: Review PR
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: |
          opencode run \
            --standalone \
            --archived \
            --auto \
            --model openrouter/deepseek/deepseek-v4.1-flash-1017 \
            "Review PR #${PR_NUMBER} on this repository.

            Using the gh CLI:
            1. Run 'gh pr view ${PR_NUMBER} --json title,body' to read the PR description
            2. Run 'gh pr diff ${PR_NUMBER}' to see the code changes
            3. Review for: bugs, security issues, performance, code quality, test coverage
            4. Post your review using 'gh pr comment ${PR_NUMBER} --body \"...\"'

            Be thorough but constructive. Flag critical issues prominently."
```

There are a few flags in there worth explaining. The `--auto` flag lets OpenCode run without stopping to ask for confirmation on each tool call, which is what you want in a pipeline, while still respecting any explicit deny rules in your configuration. The `--standalone` flag runs OpenCode with its own private server instead of connecting to the shared background service, which makes sense on a throwaway CI runner. The `--archived` flag keeps these scripted runs out of your session lists, so your history isn't filled with automated reviews.

The other details are about safety and housekeeping. The `if` condition near the top makes sure the job only runs for branches in the same repository, since pull requests from forks don't get access to secrets and I don't want to expose the API key to them. The `concurrency` group cancels an older run if I push again before it finishes.

The content review workflow is similar, but it uses a general reasoning model, DeepSeek V4 Pro, to check blog posts for spelling, grammar, and clarity,

```yaml
name: Content Review

on:
  pull_request:
    types: [opened, synchronize]

concurrency:
  group: content-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  content-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v7
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Setup Node.js
        uses: actions/setup-node@v7
        with:
          node-version: '24'

      - name: Install OpenCode
        run: npm install -g @opencode/cli@latest

      - name: Review Content
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: |
          opencode run \
            --standalone \
            --archived \
            --auto \
            --model openrouter/deepseek/deepseek-v4-pro \
            "Review PR #${PR_NUMBER} on this repository.

            Using the gh CLI:
            1. Run 'gh pr diff ${PR_NUMBER}' to see the changes
            2. If the PR contains blog posts (files under content/posts/), review them for: spelling errors, grammar mistakes, factual inconsistencies, awkward phrasing, broken links, missing or malformed frontmatter
            3. If the PR does NOT contain any blog posts, reply with 'No blog content changes in this PR - nothing to review.' and nothing else
            4. Do NOT review code or workflow files - only review blog post content
            5. Post your review using 'gh pr comment ${PR_NUMBER} --body \"...\"'

            Be thorough but constructive. Flag issues with specific line references."
```

You may notice that this one runs on every pull request instead of using a `paths` filter. That was a deliberate choice. If a workflow is a required status check and it never runs because the paths didn't match, the check stays pending forever and blocks the merge. Running it every time and having the model reply that there is nothing to review keeps the check green for code only changes, and it costs next to nothing.

I like having two different models here, because a fast model for code diffs and a deeper reasoning model for prose are good at different things, and the choice is only a single `--model` line in each workflow. If I decide that GLM-5.4 or anything else does a better job, I change that line and nothing else in the pipeline needs to know about it. To make the reviews mean something, I also added both workflows as required status checks under **Settings > Branches > Branch protection rules** for the default branch.

## What It Costs

A typical review on a small to medium pull request processes somewhere between 10,000 and 50,000 input tokens and produces a few thousand tokens of output. With the models I'm using and the prompt caching that OpenRouter passes along from the providers, that works out to a few cents at most per review, and often closer to a cent. Even on a busy month with dozens of pull requests, I'm looking at well under a dollar or two, which is far less than a subscription would cost for something that runs in the background and sits idle most of the time.

The exact numbers will change as models get repriced and new ones show up, but I don't see that as a problem. Since the model is just a parameter, I'm not tied to any specific price. If something gets more expensive I can swap it out, and if something cheaper and better shows up I can try it the same day.

## Conclusion

After a year, I have two setups that cover what I need, and in both of them I choose the tool and I choose the model. For daily coding it's OpenCode with the GLM Coding Plan, and for automated reviews it's OpenCode with OpenRouter and GitHub Actions. Neither of them requires me to stay inside one company's products or accept whatever the pricing happens to be next quarter, and I'm getting better rate limits for less money than I ever did before.

I still think Claude Code is a good tool, and Anthropic's models are strong, so I'm not saying I'll never use them again. If I need one for a particularly hard problem I can still reach them through an API key or through OpenRouter, and pay for exactly what I use. What I'm not willing to do anymore is pay a monthly premium for a subscription that costs more than the alternatives, gives me less, and can only be used inside the products the vendor decides I should use.

If you're in a similar spot, where your AI subscription is starting to feel more like a leash than a tool, I'd suggest giving OpenCode a try with a provider that welcomes it. It only takes a few minutes to set up, and after that you're the one making the decisions.

## Resources

-   [OpenCode](https://opencode.ai/): the open source AI coding agent
-   [OpenCode on GitHub](https://github.com/anomalyco/opencode): source code and releases (MIT license)
-   [OpenCode Documentation](https://opencode.ai/docs): setup, configuration, and CLI reference
-   [Z.ai GLM Coding Plan](https://z.ai/subscribe): subscription tiers and supported tools
-   [OpenRouter](https://openrouter.ai/): a single API for hundreds of models
-   [OpenRouter and OpenCode Integration Guide](https://openrouter.ai/docs/cookbook/coding-agents/opencode-integration)
