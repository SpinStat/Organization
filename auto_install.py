import os
import sys
import platform
import subprocess
import shutil

# Platform-independent packages
necessary_packages_common = [
    "git",
    "cmake",
    "gperf",
    "ccache",
    "dfu-util",
    "wget",
    "make",
    "gcc",
]

# Linux-only packages
necessary_packages_linux = [
    "python3-dev",
    "python3-venv",
    "python3-tk",
    "ninja-build",
    "file",
    "libmagic1",
    "libsdl2-dev",
    "g++-multilib",
    "gcc-multilib",
    "xz-utils",
    "device-tree-compiler",
]

# macOS-only packages
necessary_packages_macos = [
    "python3",
    "python-tk",
    "qemu",
    "openocd",
    "ninja",
]

# python packages
python_packags = [
    "west"
]


def center_print(inp: str, buffer: chr = " "):
    console_width = os.get_terminal_size()
    print((" " + inp + " ").center(console_width.columns - 2, buffer))


def run_cmd(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def installer_brew(pkg: str):
    check = run_cmd(["brew", "list", pkg])
    if check.returncode == 0:
        center_print(f"{pkg} already installed")
    else:
        center_print(f"Installing {pkg}")
        subprocess.run(["brew", "install", pkg])


def installer_apt(pkg: str):
    check = run_cmd(["dpkg", "-s", pkg])
    if check.returncode == 0:
        center_print(f"{pkg} already installed")
    else:
        center_print(f"Installing {pkg}")
        subprocess.run(["sudo", "apt", "install", "-y", pkg])


def installer_pacman(pkg: str):
    check = run_cmd(["pacman", "-Qi", pkg])
    if check.returncode == 0:
        center_print(f"{pkg} already installed")
    else:
        center_print(f"Installing {pkg}")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", pkg])


def darwin_install():
    center_print("Checking if Homebrew is installed")
    out = run_cmd(["brew", "--version"])
    if out.returncode != 0:
        center_print(
            "You don't have Homebrew installed, this script relies on Homebrew to work for macOS",
            "#",
        )
        return

    center_print("Installing common packages using Homebrew", "_")
    for pkg in necessary_packages_common:
        installer_brew(pkg)

    center_print("Installing macOS-specific packages", "_")
    for pkg in necessary_packages_macos:
        installer_brew(pkg)


def linux_install():
    center_print("Detecting Linux package manager", "_")
    if shutil.which("apt"):
        pkg_manager = "apt"
    elif shutil.which("pacman"):
        pkg_manager = "pacman"
    else:
        center_print(
            "Unsupported package manager. Please install dependencies manually.", "#"
        )
        return

    center_print(f"Using {pkg_manager} as package manager")

    if pkg_manager == "apt":
        subprocess.run(["sudo", "apt", "update"])
        center_print("Installing common packages using apt", "_")
        for pkg in necessary_packages_common:
            installer_apt(pkg)

        center_print("Installing Linux-specific packages", "_")
        for pkg in necessary_packages_linux:
            installer_apt(pkg)

    elif pkg_manager == "pacman":
        subprocess.run(["sudo", "pacman", "-Sy"])  # sync package databases
        center_print("Installing common packages using pacman", "_")
        for pkg in necessary_packages_common:
            installer_pacman(pkg)

        center_print("Installing Linux-specific packages", "_")
        for pkg in necessary_packages_linux:
            installer_pacman(pkg)


def ensure_venv():
    center_print("Checking Python virtual environment", "_")
    if sys.prefix != sys.base_prefix:
        center_print("Already running inside a virtual environment")
        return

    venv_path = os.path.join(os.getcwd(), ".venv")
    if not os.path.exists(venv_path):
        center_print("Creating new virtual environment in .venv")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
    else:
        center_print(".venv already exists")

    activate_script = venv_path / "bin" / "activate"
    center_print(
        f"To activate the virtual environment, run: source {activate_script}", "#"
    )
def install_python_packages():
    center_print(
        "Installing python packages into venv via pip", "_"
    )
    for package in  python_packags:
        center_print(f"Installing: {package}")
        subprocess.run(["pip", "install", package])


def main():
    center_print("Checking OS", "_")
    os_type = platform.system()
    center_print("Found system: " + os_type)
    if os_type == "Darwin":
        darwin_install()
    elif os_type == "Linux":
        linux_install()
    else:
        center_print("Systems of this type not supported by autoinstaller")
        center_print("Check the 'DEV.md' file for a guide to setting up the project")
        return
    ensure_venv()
    install_python_packages()

    center_print("DONE", "=")


if __name__ == "__main__":
    main()
