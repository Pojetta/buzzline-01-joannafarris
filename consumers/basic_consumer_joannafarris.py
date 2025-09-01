"""
basic_consumer_joannafarris.py

Read a log file as it is being written and raise simple alerts.
"""

# ======================
# Imports
# ======================
import os
import time

from utils.utils_logger import logger, get_log_file_path


# ======================
# Core: tail the log file
# ======================
def process_message(log_file: str) -> None:
    with open(log_file, "r") as file:
        # Start at end so we only read new lines
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for new log messages...")

        processed = 0
        last_report = time.time()
        REPORT_EVERY = 2.0  # seconds

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.2)
                continue

            message = line.strip()
            processed += 1

            # --- Prevent feedback loop: skip lines that are alerts ---
            if "ALERT:" in message:
                continue

            # --- Real-time alerts: print to console ONLY (do not log to same file) ---
            if "debugged a model" in message:
                print(f"\nALERT: Debug event detected!\n{message}")
                # NOTE: do NOT call logger.warning(...) here, or you'll re-trigger on your own write
            elif "inspiring" in message:
                print(f"\nALERT: Inspiring moment spotted!\n{message}")
                # NOTE: do NOT call logger.warning(...) here

            # --- Lightweight heartbeat on one line (no scroll/flicker) ---
            now = time.time()
            if now - last_report >= REPORT_EVERY:
                print(f"Consumer running… processed {processed} messages", end="\r", flush=True)
                last_report = now
# ======================
# Entrypoint
# ======================
def main() -> None:
    logger.info("START consumer...")
    print(">>> CONSUMER STARTED <<<")

    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
    finally:
        logger.info("END consumer.")


# Run only when executed as a script/module
if __name__ == "__main__":
    main()
