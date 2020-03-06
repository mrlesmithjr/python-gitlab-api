# from gitlab import Gitlab
import gitlab


def auth_user(args):
    """Authorize user."""
    gl = gitlab.Gitlab(args.url, args.token)
    gl.auth()

    return gl
