from pathlib import Path
from utils import write_text
from ghapi.all import GhApi
from ghapi.all import GhDeviceAuth



def initialize_gh_client(env_gh_token, gh_client_id, gh_token_file_name,
                         gh_scope, gh_auth_n_polls):
    if env_gh_token:
        print("GitHub token found. Not authenticating...")
        return GhApi(token=env_gh_token)

    if Path(gh_token_file_name).is_file():
        print("GitHub token found. Not authenticating...")
        with open(gh_token_file_name) as gh_token_file:
            file_gh_token = gh_token_file.read()
        return GhApi(token=file_gh_token)

    gh_auth = GhDeviceAuth(gh_client_id, gh_scope)
    print(f"Visit \x1b[33m{gh_auth.verification_uri}\x1b[m in your browser.\n"
          f"Paste the following code when prompted.\n"
          f"One-time code: \x1b[33m{gh_auth.user_code}\x1b[m")
    print("Waiting for authorization...")
    gh_token = gh_auth.wait(n_polls=gh_auth_n_polls)

    if not gh_token:
        return print("Authentication error")
    print("Authenticated with GitHub")
    write_text(gh_token_file_name, gh_token)
    return GhApi(token=gh_token)
