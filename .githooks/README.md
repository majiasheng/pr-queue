# Add hooks for version control

- Write hook and name it appropriately

  - e.g. `pre-push`

- (At project root, where `.git` is located) run `ln -s ../../.githooks/NAME-OF-HOOK-YOU-JUST-ADDED .git/hooks` to create a symlink in `.git/hooks` to point to version controlled hooks
  - e.g. `ln -s ../../.githooks/pre-push .githooks`
