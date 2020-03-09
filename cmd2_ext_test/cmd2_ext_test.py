#
# coding=utf-8
"""External test interface plugin"""

from typing import Optional

import cmd2


class ExternalTestMixin:
    """A cmd2 plugin (mixin class) that exposes an interface to execute application commands from python"""

    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2 initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2 initializes
        self._pybridge = cmd2.py_bridge.PyBridge(self)

    def app_cmd(self, command: str, echo: Optional[bool] = None) -> cmd2.CommandResult:
        """
        Run the application command
        :param command: The application command as it would be written on the cmd2 application prompt
        :param echo: Flag whether the command's output should be echoed to stdout/stderr
        :return: A CommandResult object that captures stdout, stderr, and the command's result object
        """
        try:
            self._in_py = True

            return self._pybridge(command, echo)

        finally:
            self._in_py = False
