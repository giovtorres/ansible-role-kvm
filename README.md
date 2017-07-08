Ansible Role: kvm
=================

Installs the KVM hypervisor and additional virtualization packages.  Supported on EL7.

Requirements
------------

The CPU on the server must have support for hardware virtualization extensions. See [here](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Virtualization_Deployment_and_Administration_Guide/sect-System_requirements-KVM_requirements.html) for more information.

Role Variables
--------------

Enable the libvirtd management daemon:

    kvm_enable_libvirtd: yes

Suspend active libvirt guests on host shutdown:

    kvm_enable_libvirt_guests: yes

Enable Kernel same-page merging:

    kvm_enable_ksm: yes

Enable the NUMA, the automatic NUMA affinity management daemon:

    kvm_enable_numad: yes

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - giovtorres.kvm

License
-------

BSD
