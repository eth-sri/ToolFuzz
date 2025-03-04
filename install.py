import subprocess


def install_package():
    subprocess.run(["pip", "install", "."], check=True)


if __name__ == "__main__":
    install_package()
