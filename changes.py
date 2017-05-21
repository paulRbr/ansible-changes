# (c) 2017, Paul Bonaud <paul@bonaud.fr>
#

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.skippy import CallbackModule as CallbackModule_skippy

class CallbackModule(CallbackModule_skippy):

    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    However in a similar way than skippy plugin hides skipped events, this plugin
    displays only 'changed' events. It also hides task name if no changes are made.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'changes'

    def __init__(self):
        self._last_task_banner_name = None
        self._task_banner_name = None
        super(CallbackModule, self).__init__()

    def _print_task_banner(self, task):
        self._task_banner_name = task.get_name().strip()

    def _really_print_task_banner(self):
        if self._last_task_banner_name != self._task_banner_name:
            self._display.banner(u"TASK [%s]" % (self._task_banner_name))
            self._last_task_banner_name = self._task_banner_name

    def v2_runner_on_ok(self, result):
        if result._result.get('changed', False):
            self._really_print_task_banner()
            return super(CallbackModule, self).v2_runner_on_ok(result)
        else:
            pass

    def v2_runner_item_on_ok(self, result):
        if result._result.get('changed', False):
            self._really_print_task_banner()
            return super(CallbackModule, self).v2_runner_item_on_ok(result)
        else:
            pass
