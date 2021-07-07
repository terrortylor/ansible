%w[terraform].each do |file|
  describe file("/etc/sudoers.d/#{file}") do
    it { should exist }
    its('owner') { should eq 'root' }
    its('group') { should eq 'root' }
  end
end
