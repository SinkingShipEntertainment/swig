name = "swig"

authors = ["Swig"]

version = "4.0.2"

description = \
    """
    SWIG is an interface compiler that connects programs written in C and C++ with
    scripting languages such as Perl, Python, Ruby, and Tcl.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
    "cmake",
    "gcc",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

tools = [
]

uuid = "repository.swig"

def commands():
    env.PATH.prepend("{root}/bin")
    env.SWIG_ROOT = "{root}"
