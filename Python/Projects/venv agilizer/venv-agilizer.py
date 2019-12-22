#!/usr/bin/python

import os
import sys
import venv


def environment_available(environment):
    possible_environments = os.listdir(os.environ.get('VENV_DIR', os.getcwd()))
    return environment in possible_environments


def retrieve_arguments():
    output = [None, None]
    if len(sys.argv) == 3:
        output = sys.argv[1:3]
    elif len(sys.argv) == 2:
        output = [sys.argv[1], None]

    return output


def block(action, environment):
    # Prevent continuing program if some data is not provided
    if action is None:
        print("VENV can 'create', 'destroy', list', and 'activate' environments.")
        print("[!] Please select one")
        exit()

    if isinstance(action, str):
        action = action.lower().strip()
    env_required = ["create", "destroy", "activate"]
    if action in env_required and action is None:
        print("[!] Please specify environment's name")
        exit()
    else:
        # Skip head since environment is not required
        return

    if isinstance(environment, str):
        environment = environment.strip()

    if not environment_available(environment) and action != "create":
        print(f"[!] Environment by the name of '{environment}' not found!")
        print("[.] Use 'venv list' to show all environments")
        exit()


def main():
    venv_directory = os.environ.get('VENV_DIR', os.getcwd())

    action, environment = retrieve_arguments()
    block(action, environment)

    if isinstance(action, str):
        action = action.lower().strip()
    if isinstance(environment, str):
        environment = environment.strip()

    if action == "list":
        for n, environment in enumerate(os.listdir(venv_directory)):
            print(f"({n+1}) {environment}")
    elif action == "create":
        new_environment = os.path.join(venv_directory, environment)

        venv.create(new_environment, with_pip=True, prompt=environment)
        print(f"[v] '{environment}' successfully created!")
    elif action == "destroy":
        old_environment = os.path.join(venv_directory, environment)

        def rmdir_recursive(target):
            for d in os.listdir(target):
                try:
                    rmdir_recursive(os.path.join(target, d))
                except OSError:
                    os.remove(os.path.join(target, d))
            os.rmdir(target)

        rmdir_recursive(old_environment)
        print(f"[v] '{environment}' successfully destroyed!")
    elif action == "activate":
        activate_environment = os.path.join(venv_directory, environment,
                "Scripts", "activate.bat")
        os.system(f"doskey activate={activate_environment}")


if __name__ == "__main__":
    main()
# Thank you https://docs.python.org/3/library/venv.html#module-venv
