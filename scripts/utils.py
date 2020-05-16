from pathlib import Path
import structlog

root = Path(__file__).parents[1]
filesdir = root / "files"
datadir = root / "data"

log = structlog.get_logger()
