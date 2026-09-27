# Effect format and review

Version 1 `.cfeffect` files are UTF-8 JSON. See [effects/](effects/) for working examples. Only the app's built-in ring, rays and glow renderer is available. There are no scripts, executable code, downloaded textures, shaders, sound files or external URLs in the format.

Limits: 64 KiB per effect, 1–6 layers, 1–80 elements per layer, at most 240 elements total. Radius 8–600, line width 0.5–16, opacity 0.05–1, and cycle duration 0.5–8 seconds. Colors use `#RRGGBB`. Motion is `expand`, `contract`, `orbit` or `pulse`. IDs contain only ASCII letters, digits, `.`, `_` or `-`, up to 100 characters. Names and creator names are at most 60 characters; descriptions and credits at most 240. Control characters are rejected. Catalog version 1 is limited to 100 unique effects and 512 KiB.

Each effect includes `version`, `id`, `name`, `authorID`, `author`, `summary`, `license`, `credit` and `layers`. Each layer includes `kind`, `motion`, `color`, `count`, `radius`, `width`, `opacity` and `period`. The effect's `authorID` is not a verified identity on imported files. Catalog maintainers map it to a stable creator identity during review so app blocking remains useful.

## Submission rules

- Submit only effects you created or are authorized to adapt and redistribute. Retain existing credits and license obligations. The supported data licenses are CC0-1.0 and CC-BY-4.0; licenses apply to the effect data itself.
- No harassment, hate, sexual content, impersonation, private personal information, spam or misleading titles/credits. The catalog is intended for a general audience.
- Test the effect on a real Mac, including long holds, release, toggle, rapid activation and cursor movement. Avoid uncomfortable flashing and extreme visual noise.
- Do not claim authorship of someone else's entry or reuse another creator's identifier. Revisions to an existing catalog entry must come from its verified submitting account or a maintainer.
- A submission can be declined or removed. No payment or automatic right to inclusion is created by submitting.

## Maintainer checklist

1. Open the exported text as data only. Review all metadata, rights/credits, and any report history. Do not run submitted code, commands, attachments or links.
2. Match the submitting GitHub account to a stable `authorID`; check previous submissions to prevent impersonation and evasion of a creator block. Preserve entry IDs for accepted revisions.
3. Validate the definition with `python3 validate.py`, then preview it in the app on a physical Mac. Check that it remains readable, bounded, responsive and suitable for the catalog.
4. Add the accepted `.cfeffect` file under `effects/` and the matching object to `catalog.json`. Validate again. Merge only after review; the app loads the current catalog next time the gallery is refreshed.
5. Monitor the support inbox and repository reports. Triage safety/rights reports promptly (target within two working days), remove or correct unsuitable entries, and reply with the outcome. Do not publish private report details. Local copies remain removable/blockable in the app.

The catalog is manually curated. GitHub issues are submissions, not an unreviewed feed, and no user submission is automatically added by CI.
