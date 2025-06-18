import subprocess
import sys

def install_requirements():
    try:
        import pkg_resources
        with open('requirements.txt') as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        installed = {pkg.key for pkg in pkg_resources.working_set}
        to_install = [pkg for pkg in packages if pkg.split('==')[0].lower() not in installed]
        if to_install:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *to_install])
        else:
            print("All requirements already installed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install_requirements()