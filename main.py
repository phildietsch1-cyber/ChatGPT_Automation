"""
ChatGPT Automation
Version 1.0 Development

Main application entry point.
"""

from pathlib import Path
import sys

from config_loader import ConfigLoader
from logging_manager import setup_logger
from service_registry import ServiceRegistry
from service_initializer import ServiceInitializer
from browser_service import BrowserService
from browser_launch_manager import BrowserLaunchManager
from playwright_checker import PlaywrightChecker
from playwright_installer_check import PlaywrightInstallerCheck

VERSION = "1.0.0-dev"


def verify_environment():
    """Verify Python installation and create required folders."""

    print(f"ChatGPT Automation {VERSION}")
    print("Checking environment...")

    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10 or newer is required.")

    cfg = ConfigLoader().load()
    print(f"Configuration loaded: {cfg}")

    Path(cfg["download_dir"]).mkdir(exist_ok=True)
    Path(cfg["upload_dir"]).mkdir(exist_ok=True)
    Path(cfg["archive_dir"]).mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)

    return cfg


def initialize_services(cfg):
    """Build every shared service used by the application."""

    logger = setup_logger(cfg["log_level"])
    logger.info("Environment verification complete.")

    registry = ServiceRegistry()
    registry.register("config", cfg)
    registry.register("logger", logger)

    logger.info("Registered services: %s", registry.list_services())

    initializer = ServiceInitializer(registry, logger)
    initializer.initialize()

    return registry, logger


def initialize_browser(logger):
    """Initialize browser services."""

    browser_service = BrowserService(logger)

    launcher = BrowserLaunchManager(browser_service, logger)
    launcher.launch()

    status = PlaywrightChecker.check()
    logger.info("Playwright installed: %s", status["installed"])

    binaries = PlaywrightInstallerCheck.browser_binary_found()
    logger.info("Playwright browser binaries: %s", binaries)

    if not status["installed"]:
        print("Playwright package is NOT installed.")

    if not binaries:
        print(PlaywrightInstallerCheck.install_hint())

    print("Browser service initialized.")
    return browser_service


def main():
    cfg = verify_environment()
    registry, logger = initialize_services(cfg)

    print("Environment OK")
    print("Bootstrap complete.")

    browser = initialize_browser(logger)

    print()
    print("===================================")
    print("Startup completed successfully.")
    print("===================================")
    print()
    print("Ready for browser automation.")
    browser.browser.wait()
    browser.stop()


if __name__ == "__main__":
    main()