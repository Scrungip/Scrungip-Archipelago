from __future__ import annotations

import ModuleUpdate
ModuleUpdate.update()

from worlds.am2r.AM2RClient import launch
import Utils

if __name__ == "__main__":
    Utils.init_logging("AM2RClient", exception_logger="Client")
    launch()
