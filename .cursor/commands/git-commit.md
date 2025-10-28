# Git Commit Assistant

When I ask you to commit changes, follow these best practices for professional version control.

## Instructions:

1. **Analyze the current state** of the repository
2. **Check for uncommitted changes** and staged files
3. **Create focused, atomic commits** with clear messages
4. **Follow semantic commit conventions**

## Git Workflow:

### 1. Pre-commit Analysis:
```bash
# Fix repository ownership issues (common in containers/workspaces)
git config --global --add safe.directory $(pwd)

# Check status
git status

# Try to pull latest changes (handle SSH/HTTPS gracefully)
git pull origin main || echo "Warning: Could not pull from remote"
```

### 2. Commit Strategy:
- **Atomic commits**: One logical change per commit
- **Separate files**: Commit each file individually when possible
- **Group related changes**: If files are logically related, commit together
- **Clear messages**: Use semantic commit format

### 3. Commit Message Format:
Use semantic commit conventions:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks
- `perf:` - Performance improvements

### 4. Commit Process:
```bash
# Check status
git status

# Pull latest changes
git pull origin main

# Add files (one by one for atomic commits)
git add [filename]

# Commit with clear message
git commit -m "feat: add new feature description"

# Repeat for each logical change
```

## Best Practices:

### Commit Granularity:
- **Prefer multiple small commits** over one large commit
- **Each commit should be reviewable** independently
- **Commit early and often** - don't wait for "perfect" code
- **One logical change per commit**

### Commit Messages:
- **Use imperative mood**: "Add feature" not "Added feature"
- **Keep first line under 50 characters**
- **Add detailed description** if needed (after blank line)
- **Reference issues**: "Fixes #123" or "Closes #456"

### Examples:
```bash
# Good commit messages
git commit -m "feat: add user authentication system"
git commit -m "fix: resolve memory leak in data processing"
git commit -m "docs: update API documentation"
git commit -m "refactor: simplify database connection logic"

# With detailed description
git commit -m "feat: implement user dashboard

- Add dashboard layout with navigation
- Include user statistics widgets
- Implement responsive design
- Add dark mode support"
```

## Decision Making:

### When to Commit Separately:
- **Different file types** (code vs documentation)
- **Unrelated changes** in the same file
- **Different features** or bug fixes
- **Different authors** or contexts

### When to Commit Together:
- **Related files** for the same feature
- **Small changes** that are logically connected
- **Configuration changes** that must be applied together

## Commands to Use:

### Status and Pull:
```bash
# Fix common ownership issues
git config --global --add safe.directory $(pwd)

# Check repository status
git status

# Pull with error handling
git pull origin main || echo "Warning: Could not pull from remote"
```

### Adding Files:
```bash
# Add specific file
git add filename.ext

# Add all changes
git add .

# Add with interactive mode
git add -p
```

### Committing:
```bash
# Simple commit
git commit -m "type: description"

# Commit with detailed message
git commit -m "type: short description

Detailed explanation of changes
- Bullet point 1
- Bullet point 2"
```

## Output Format:

When committing, provide:
1. **Status summary** of what was committed
2. **Commit hash** (if available)
3. **Files changed** and their purposes
4. **Next steps** or recommendations

## Example Usage:

When I say "Commit my changes", you should:
1. Fix repository ownership issues with `git config --global --add safe.directory $(pwd)`
2. Run `git status` to see current state
3. Try `git pull origin main` (with error handling if SSH/network issues)
4. Analyze changes and group them logically
5. Create atomic commits with clear messages
6. Report the commit results and any warnings

The goal is to maintain a clean, professional git history with meaningful commits that tell the story of development.
