"""
Functions for getting the author
"""

__all__ = [
    "find_author",
    "find_email",
]


from git import Git, Repo, GitCommandError


def is_git(directory=None):
    "Returns if the directory (None=cwd) is a git repository"
    try:
        Git(directory).status()
        return True
    except GitCommandError:
        return False


def get_git_repo(directory=None):
    "Returns the git repository of the directory (None=cwd)"
    return Repo(Git(directory).rev_parse(show_toplevel=True))


def get_git_author(directory=None):
    "Returns the author of the first git commit"
    return get_git_repo(directory).heads.master.log()[0].actor


def find_author(directory=None):
    "Returns the author name"
    if is_git(directory):
        return get_git_author(directory).name
    return None


def find_email(directory=None):
    "Returns the author email"
    if is_git(directory):
        return get_git_author(directory).email
    return None
