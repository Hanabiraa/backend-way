import logging
import os
import sys

# fix relative path issue
sys.path.append("..")
new_path = os.path.abspath(".")
sys.path.insert(1, new_path)

from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
