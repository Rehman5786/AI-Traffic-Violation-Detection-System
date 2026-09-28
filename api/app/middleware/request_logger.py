import logging
import time

from fastapi import Request


logger = logging.getLogger("smart_traffic_ai.request")


async def request_logger(request: Request, call_next):
    """
    Log incoming HTTP requests and their response time.
    """
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    logger.info(
        "%s %s | status=%s | duration=%.4fs",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response