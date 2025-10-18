# Copilot instructions for contributors and AI agents

This repository is a tiny Python utility called BookBot that reads plain-text books from the
`books/` directory. The codebase is intentionally small — treat it like a single-module script
project where simplicity and clear examples matter.

What this project is and why
- Single-entry script: the primary code is in `main.py` (function: `get_book_text(file_path)`),
  which reads and returns the contents of a text file.
- Data lives under `books/` (example: `books/frankenstein.txt`). There are no external APIs or
  services.

Immediate goals for an AI assistant
- Preserve the simple, explicit style in `main.py` (avoid heavy frameworks).
- Prefer small, well-scoped changes: add a CLI, small parsing helpers, or unit tests.
- When adding a feature, update `README.md` with usage examples and add at least one test file.

Key files and examples you should reference
- `main.py` — the canonical function is `get_book_text(file_path)`; example usage:
  `get_book_text('books/frankenstein.txt')`.
- `books/` — add or modify plain UTF-8 `.txt` files here. Assume whole-file reads are the current
  convention.
- `README.md` — project summary and the place to add run instructions for new features.

Running and behavior notes
- This project currently has no build step, dependencies, or tests. Running `python main.py`
  executes the module but, as of now, `main.py` contains only a helper function and produces no
  observable CLI output. If you add a CLI or runnable entrypoint, document the command in
  `README.md` (example: `python3 main.py --book frankenstein`).

Project-specific patterns to follow
- Keep interfaces tiny and explicit (e.g., functions that accept a file path and return a string).
- Files in `books/` are treated as immutable content inputs; prefer adding new files instead of
  in-place editing during feature work unless intentionally updating text content.
- No packaging: changes should not introduce heavy dependency lists. If a dependency is necessary,
  add a `requirements.txt` with pinned versions and update README with install/run steps.

Common pitfalls and how to handle them
- File not found: prefer explicit error handling (raise FileNotFoundError with a clear message).
- Encoding assumptions: be explicit (use `open(..., encoding='utf-8')`) when reading/writing.
- Running behavior: since `main.py` is not a full CLI yet, do not assume running it will print
  results — add CLI code or tests when creating runnable behavior.

PR and commit guidance for AI-generated changes
- Keep each PR focused (one feature or fix). If adding a runnable CLI, include:
  - README usage snippet
  - a minimal test (e.g., `tests/test_main.py`) that imports `get_book_text`
  - a short changelog line in the PR description explaining the new entrypoint

If you need clarification
- Ask the repo owner whether new dependencies are acceptable before adding them.
- Ask for preferred Python version if you plan to use newer language features.

If you modify this file
- Merge intelligently: preserve human-written intents and examples. This file is the single source
  of guidance for AI assistants — keep it concise and up-to-date.

---
Please review and tell me if you want more examples, test snippets, or a small CLI added.
