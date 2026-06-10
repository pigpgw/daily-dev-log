# Repository Guidelines

## Project Structure & Module Organization

This repository is a Markdown-based TIL and daily development log archive. Daily entries live in month folders named `YYYY-MM`, such as `2026-05/`. Use one Markdown file per day, following the existing date patterns in that month, for example `2026-05.26.md`.

Book study notes live under `books/<book title>/`. Each book folder should include a `README.md` for chapter goals or an overview, plus chapter files such as `챕터1.md`. Keep root-level files limited to repository documentation and configuration.

## Build, Test, and Development Commands

There is no application build step or package manager setup in this repository. Useful maintenance commands:

- `rg --files`: list tracked content quickly and confirm file placement.
- `npx markdownlint "**/*.md"`: lint Markdown files if `markdownlint-cli` is available.
- `git status`: review changed daily logs before committing.

Do not add generated build output, dependency folders, or binary assets unless the repository purpose changes.

## Coding Style & Naming Conventions

Write content in Markdown. Use clear headings, short bullet lists, and task lists (`- [ ]`, `- [x]`) for goals and routines. The README asks that directory and file names be written in English, but this repository already contains Korean book titles and chapter names; preserve existing naming for current book-note folders.

Daily log headings should identify the date, for example `# TIL | 2026.05.26 (화요일)`. Keep month directories zero-padded (`2026-05`). Avoid trailing whitespace and keep formatting consistent with neighboring files. The `.markdownlint.json` intentionally relaxes several rules, including line length and heading style.

## Testing Guidelines

Testing is editorial rather than automated. Before opening a PR, preview changed Markdown files and check that links, headings, and checkboxes render correctly. When adding book notes, verify that chapter numbering is sequential and that the book `README.md` reflects new chapters or goals.

## Commit & Pull Request Guidelines

Recent history uses concise documentation commits, especially `docs: update <date> daily log`, for example `docs: update 2026-05-26 daily log`. Follow that convention for daily updates. For broader changes, use a short conventional prefix such as `docs:` or `chore:`.

Pull requests should summarize the date range or book chapters changed, mention any linked Notion, issue, or reference material, and include screenshots only when visual Markdown rendering needs review.

## Agent-Specific Instructions

Keep edits narrow and preserve the personal log voice. Do not rewrite historical entries unless requested; append or correct only the files relevant to the current task.
