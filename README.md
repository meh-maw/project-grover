# Project Grover
website - https://sites.google.com/view/project-grover/home

<details>
<summary>Repository structure and information on directories</summary>
## Directory Overview
### **`technical/`**
   - **Purpose**: The `technical` directory houses all the technical documentation, codebase, and resources related to the development of the project. This is the core directory where all technical work is organized and managed.
   - **Contents**:
     - **sub-systems**: code and technical documents for each sub-systems
     - **Technical Documentation**: Manuals, API documentation, architecture diagrams, and other technical resources.
</details>

<details>
<summary>Instructions on how to push and pull commits to the repository</summary>
  
## Table of Contents
1. [Getting Started](#getting-started)
2. [Creating a New Branch](#creating-a-new-branch)
3. [Pushing Changes](#pushing-changes)
4. [Pulling Changes](#pulling-changes)
5. [Submitting a Pull Request](#submitting-a-pull-request)
6. [Branching Strategy](#branching-strategy)
7. [Pull Request Review Process](#pull-request-review-process)

## Getting Started

Before you start working on this project, ensure you have cloned the repository to your local machine:
```bash
git clone https://github.com/meh-maw/project-grover.git
cd repository-name
```
Ensure you are working in a branch other than `main` before making any changes.

## Creating a New Branch

To keep the `main` branch stable and clean, all work should be done in separate branches. Follow these steps to create a new branch:

1. **Fetch the latest changes** from the remote repository:

```bash
git fetch origin
```

2. **Create a new branch** and switch to it:

```bash
git checkout -b <your-branch-name>
```
Replace `<your-branch-name>` with a meaningful name related to the feature or bug fix you are working on.

3. **Push your branch to the remote repository**:

```bash
git push -u origin <your-branch-name>
```

## Pushing Changes

Once you have made changes in your branch, follow these steps to commit and push them:

1. **Stage the changes** you want to commit:
```bash
git add .
```

2. **Commit your changes** with a meaningful message:
```bash
git commit -m "Your commit message"
```

3. **Push your changes** to the remote branch:
```bash
git push origin <your-branch-name>
```

## Pulling Changes

Before starting new work or when you want to integrate the latest changes from the `main` branch into your branch, you should pull the latest updates:

1. **Switch to the `main` branch**:

```bash
git checkout main
```

2. **Pull the latest changes** from the remote `main` branch:

```bash
git pull origin main
```

3. **Switch back to your branch**:

```bash
git checkout <your-branch-name>
```

4. **Merge `main` into your branch** to incorporate the latest changes:

```bash
git merge main
```

## Submitting a Pull Request

When you are ready to submit your changes for review, follow these steps:

1. **Push your branch** to the remote repository:

```bash
git push origin <your-branch-name>
```

2. **Create a pull request** on GitHub:

- Go to the repository on GitHub.
- Click on the "Compare & pull request" button.
- Add a title and description for your pull request.
- Ensure the base branch is `main` and the compare branch is your branch.
- Click "Create pull request".

## Branching Strategy

We follow a branching strategy where all development is done on branches other than `main`. This helps keep the `main` branch stable and deployable. Each feature, bug fix, or task should have its own branch.

- **Feature Branches**: Branches for new features (e.g., `feature/new-login-page`).
- **Bug Fixes**: Branches for bug fixes (e.g., `bugfix/fix-login-error`).
- **Hotfixes**: Quick fixes that need to be merged into `main` immediately (e.g., `hotfix/security-patch`).

## Pull Request Review Process

All pull requests will be reviewed by at least one other team member before being merged into the `main` branch. Here's the review process:

1. **Create the pull request** as described above.
2. **Wait for a reviewer** to approve your changes. You may receive feedback or requests for changes.
3. **Make any requested changes** and push them to your branch.
4. **Once approved**, the reviewer will merge the pull request into `main`.

### Important Notes

- **Do not push directly to `main`**. Always work in a branch and submit a pull request.
- **Keep your branch updated** with `main` to avoid conflicts during the merge process.
- **Review other team members' pull requests** to help maintain code quality.
</details>
