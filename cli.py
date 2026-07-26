import argparse

def build_parser():
    p = argparse.ArgumentParser(description="ChatGPT Automation")
    p.add_argument("--once", action="store_true", help="Run one workflow cycle")
    p.add_argument("--watch", action="store_true", help="Watch for incoming batches")
    p.add_argument("--master", default="Current/Master.zip",
                   help="Path to the master ZIP")
    return p
