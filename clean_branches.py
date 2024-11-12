import subprocess


def get_branch_list():
    """Get the list of branches from git."""
    try:
        # Run the command 'git branch' to list all local branches
        result = subprocess.run(['git', 'branch'], capture_output=True, text=True)
        branches = result.stdout.splitlines()
        return [branch.strip().replace("* ", "") for branch in branches]
    except subprocess.CalledProcessError as e:
        print(f"Error getting branch list: {e}")
        return []


def delete_branches(branches):
    """Delete the branches provided."""
    try:
        # Run the command 'git branch -D' followed by the branch names
        subprocess.run(['git', 'branch', '-D'] + branches)
        print(f"Deleted branches: {', '.join(branches)}")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting branches: {e}")


def main():
    # Fetch the list of branches
    branches = get_branch_list()

    # Filter out 'master' and any branches that are already deleted
    branches_to_delete = [branch for branch in branches if branch != 'master']

    if input(f"These branches will be deleted: {branches_to_delete}. Type yes to continue:") != 'yes':
        return

    if not branches_to_delete:
        print("No branches to delete.")
    else:
        print(f"Branches to be deleted: {', '.join(branches_to_delete)}")

        # Delete the filtered branches
        delete_branches(branches_to_delete)


if __name__ == '__main__':
    main()
