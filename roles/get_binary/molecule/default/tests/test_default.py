import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# replace binary if versions don't match
def test_removes_outdated_version(host):
  f = host.file('/usr/local/bin/lazygit')
  assert f.exists is True
  assert f.user == 'root'
  assert f.group == 'root'

def test_sets_binary_name(host):
  f = host.file('/usr/local/bin/wallace')
  assert f.exists is True
  assert f.user == 'root'
  assert f.group == 'root'

def test_can_define_extracted_to_path(host):
  f = host.file('/usr/local/bin/helm')
  assert f.exists is True
  assert f.user == 'root'
  assert f.group == 'root'

