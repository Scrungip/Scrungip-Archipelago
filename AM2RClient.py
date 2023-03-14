import asyncio
import copy
import json
import time
from asyncio import StreamReader, StreamWriter
from typing import List

import Utils
from Utils import async_start
from CommonClient import CommonContext, server_loop, gui_enabled, ClientCommandProcessor, logger, \
    get_base_parser

CONNECTION_TIMING_OUT_STATUS = "Connection timing out"
CONNECTION_REFUSED_STATUS = "Connection Refused"
CONNECTION_RESET_STATUS = "Connection was reset"
CONNECTION_TENTATIVE_STATUS = "Initial Connection Made"
CONNECTION_CONNECTED_STATUS = "Connected"
CONNECTION_INITIAL_STATUS = "Connection has not been initiated"




class AM2RCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class AM2RContext(CommonContext):
    command_processor = AM2RCommandProcessor
    game = 'AM2R'
    items_handling = 0b001 # full local

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.waiting_for_client = False
        self.am2r_streams: (StreamReader, StreamWriter) = None
        self.am2r_sync_task = None
        self.am2r_status = CONNECTION_INITIAL_STATUS
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        if not self.auth:
            self.waiting_for_client = True
            logger.info('Awaiting connection to AM2R to get Player information')
            return
        
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class AM2RManager(GameManager):
            logging_pairs = [
                ("Client", "Multiworld")
            ]
            base_title = "AM2R Multiworld Client"

        self.ui = AM2RManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

async def am2r_sync_task(ctx: AM2RContext):
    logger.info("Starting AM2R connector")
    while not ctx.exit_event.is_set():
        error_status = None
        try:
            logger.debug("Attempting to connect to AM2R")
            ctx.am2r_streams = await asyncio.wait_for(asyncio.open_connection("localhost", 64197), timeout=10)
            ctx.am2r_status = CONNECTION_TENTATIVE_STATUS
        except TimeoutError:
            logger.debug("Connection Timed Out, Trying Again")
            ctx.am2r_status = CONNECTION_TIMING_OUT_STATUS
            continue
        except ConnectionRefusedError:
            logger.debug("Connection Refused, Trying Again")
            ctx.am2r_status = CONNECTION_REFUSED_STATUS
            continue


if __name__ == '__main__':
    # Text Mode to use !hint and such with games that have no text entry
    Utils.init_logging("AM2RClient")

    options = Utils.get_options()

    async def main(args):
        ctx = AM2RContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        ctx.am2r_sync_task = asyncio.create_task(am2r_sync_task(ctx), name="AM2R Sync")
        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    args = parser.parse_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()