.. TODO(briancurtin): turn this into a full guide on the Connection class
.. TODO(briancurtin): cover user_agent setting

=====
Usage
=====

To use openstacksdk in a project::

    from openstack import connection
    from openstack import profile

    # First, specify your profile
    prof = profile.Profile()
    prof.set_region('network', 'zion')

    # Second, create a connection
    conn = connection.Connection(profile=prof,
                                 auth_url='http://172.20.1.108:5000/v3',
                                 project_name='hacker',
                                 username='neo',
                                 password='bluepill')

    # Finally, access your desired services
    network = conn.network.find_network("matrix")
    if network is None:
        network = conn.network.create_network(name="matrix")
