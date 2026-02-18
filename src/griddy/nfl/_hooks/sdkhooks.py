from griddy.core.hooks.sdkhooks import SDKHooks as CoreSDKHooks

from .registration import init_hooks


class SDKHooks(CoreSDKHooks):
    """NFL-specific SDK hooks with NFL hook registration."""

    def __init__(self) -> None:
        super().__init__(init_hooks_fn=init_hooks)
