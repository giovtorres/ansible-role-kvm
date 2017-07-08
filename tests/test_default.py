import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("pkg", ["qemu-kvm", "libvirt"])
def test_kvm_main_packages(host, pkg):
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", [
    "libguestfs-tools",
    "libvirt-python",
    "virt-install",
    "virt-manager",
    "virt-top",
    "virt-viewer"
])
def test_kvm_addititonal_packages(host, pkg):
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("svc", [
    "libvirtd",
    "libvirt-guests",
    "ksm",
    "numad"
])
def test_kvm_services_enabled_and_running(host, svc):
    assert host.service(svc).is_enabled
    assert host.service(svc).is_running
