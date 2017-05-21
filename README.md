Changes - an Ansible stdout callback plugin
==

In a similar way than the [skippy](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/callback/skippy.py) plugin hides skipped events in the stdout log of an Ansible run, this plugin displays only *changed* events.

It also hides task name if no changes are made.

Example
===

This is an example output using this plugin:
```
PLAY [all] ***********************************************************************************************************

TASK [rabbitmq : Configure RabbitMQ users] ***************************************************************************
changed: [rabbitmq1.example.org] => (item={u'username': u'myuser', u'password': u'mypass'})
changed: [rabbitmq2.example.org] => (item={u'username': u'myuser', u'password': u'mypass'})
changed: [rabbitmq3.example.org] => (item={u'username': u'myuser', u'password': u'mypass'})

PLAY RECAP ***********************************************************************************************************
rabbitmq1.example.org : ok=2    changed=1    unreachable=0    failed=0
rabbitmq2.example.org : ok=2    changed=1    unreachable=0    failed=0
rabbitmq3.example.org : ok=2    changed=1    unreachable=0    failed=0
```

Usage
===

In your `ansible.cfg` file add:

```
stdout_callback = changes
callback_plugins = ./plugins/callback
```

Download this plugin in `./plugins/callback`:
```
mkdir -p plugins/callback
wget https://raw.githubusercontent.com/paulRbr/ansible-changes-stdout-callback/master/changes.py -O plugins/callback/changes.py
```

License
===

GNU see [LICENSE.md](https://github.com/paulRbr/ansible-changes-stdout-callback/blob/master/LICENSE.md) file
