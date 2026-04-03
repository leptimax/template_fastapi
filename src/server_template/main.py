"""Main module."""

from server_template.core.server import Server


def main():
    """Main process."""
    server = Server()
    server()


if __name__ == "__main__":
    main()
